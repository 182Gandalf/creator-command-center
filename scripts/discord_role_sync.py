#!/usr/bin/env python3
"""
FlowCast Discord Role Sync
--------------------------
Runs every 10 minutes via cron. Three jobs:

1. Reaction roles    — reads #get-your-role reactions, assigns Splash / Beta Tester
2. Tier verification — reads #account-setup for "verify: email@..." messages,
                       looks up the email in FlowCast, assigns Creator/Pro/Studio role
3. Splash auto-assign — gives Splash to any member with no custom roles
                        (requires Server Members Intent in Discord Dev Portal)

Config: /home/daz/.openclaw/workspace/scripts/discord_secrets.json
"""

import json, time, re, urllib.request, urllib.error, urllib.parse
from datetime import datetime, timezone

# ── Load config ───────────────────────────────────────────────────────────────
with open("/home/daz/.openclaw/openclaw.json") as f:
    config = json.load(f)

TOKEN = config["channels"]["discord"]["token"]

try:
    with open("/home/daz/.openclaw/workspace/scripts/discord_secrets.json") as f:
        secrets = json.load(f)
    FLOWCAST_ADMIN_KEY = secrets.get("flowcast_admin_key", "")
    FLOWCAST_API_URL   = secrets.get("flowcast_api_url", "https://flowcast.space")
except FileNotFoundError:
    FLOWCAST_ADMIN_KEY = ""
    FLOWCAST_API_URL   = "https://flowcast.space"

GUILD   = "1486337670102913024"
HEADERS = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

# ── Role IDs ──────────────────────────────────────────────────────────────────
ROLE_SPLASH       = "1486359934764322888"
ROLE_CREATOR      = "1486359931996213479"
ROLE_CREATOR_PRO  = "1486359930800967752"
ROLE_STUDIO       = "1486359929798266880"
ROLE_BETA_TESTER  = "1486359933611020489"
ROLE_MODERATOR    = "1486359928275865731"
ROLE_TEAM         = "1486359927399251968"

ALL_CUSTOM_ROLES = {
    ROLE_SPLASH, ROLE_CREATOR, ROLE_CREATOR_PRO,
    ROLE_STUDIO, ROLE_BETA_TESTER, ROLE_MODERATOR, ROLE_TEAM,
}

TIER_TO_ROLE = {
    "creator":     ROLE_CREATOR,
    "creator_pro": ROLE_CREATOR_PRO,
    "studio":      ROLE_STUDIO,
}

# ── Channel IDs ───────────────────────────────────────────────────────────────
CH_ACCOUNT_SETUP  = "1486360096291160195"   # #account-setup
CH_ROLE_MSG       = "1486361342628859904"   # #get-your-role
ROLE_MSG_ID       = "1486361343601934487"   # the reaction message

REACTION_ROLES = {
    "\U0001f193": ROLE_SPLASH,       # 🆓
    "\U0001f9ea": ROLE_BETA_TESTER,  # 🧪
}

# ── State file (tracks last processed message IDs) ────────────────────────────
STATE_FILE = "/home/daz/.openclaw/workspace/logs/discord_sync_state.json"


def load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(state):
    import os
    os.makedirs("/home/daz/.openclaw/workspace/logs", exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ── HTTP helpers ──────────────────────────────────────────────────────────────
def api(method, path, data=None):
    url = f"https://discord.com/api/v10{path}"
    body = json.dumps(data).encode() if data else None
    r = urllib.request.Request(url, data=body, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(r) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode()
        print(f"  {e.code} {method} {path}: {err[:120]}")
        return None
    except Exception as ex:
        print(f"  ERR {method} {path}: {ex}")
        return None


def assign_role(user_id, role_id, reason="Auto-assign"):
    r = urllib.request.Request(
        f"https://discord.com/api/v10/guilds/{GUILD}/members/{user_id}/roles/{role_id}",
        headers={**HEADERS, "X-Audit-Log-Reason": urllib.parse.quote(reason)},
        method="PUT"
    )
    try:
        with urllib.request.urlopen(r):
            return True
    except urllib.error.HTTPError as e:
        print(f"  Failed assign role {role_id} → {user_id}: {e.code}")
        return False


def remove_role(user_id, role_id, reason="Role update"):
    r = urllib.request.Request(
        f"https://discord.com/api/v10/guilds/{GUILD}/members/{user_id}/roles/{role_id}",
        headers={**HEADERS, "X-Audit-Log-Reason": urllib.parse.quote(reason)},
        method="DELETE"
    )
    try:
        with urllib.request.urlopen(r):
            return True
    except urllib.error.HTTPError as e:
        print(f"  Failed remove role {role_id} from {user_id}: {e.code}")
        return False


def send_message(channel_id, content):
    return api("POST", f"/channels/{channel_id}/messages", {"content": content})


def delete_message(channel_id, message_id):
    api("DELETE", f"/channels/{channel_id}/messages/{message_id}")


def get_reactions(emoji):
    encoded = urllib.parse.quote(emoji)
    r = urllib.request.Request(
        f"https://discord.com/api/v10/channels/{CH_ROLE_MSG}/messages/{ROLE_MSG_ID}/reactions/{encoded}?limit=100",
        headers=HEADERS
    )
    try:
        with urllib.request.urlopen(r) as resp:
            return json.loads(resp.read())
    except Exception as ex:
        print(f"  ERR reactions {emoji}: {ex}")
        return []


def get_member(user_id):
    return api("GET", f"/guilds/{GUILD}/members/{user_id}")


def get_channel_messages(channel_id, after=None, limit=50):
    path = f"/channels/{channel_id}/messages?limit={limit}"
    if after:
        path += f"&after={after}"
    return api("GET", path) or []


def lookup_flowcast_tier(email):
    """Call FlowCast API to get subscription tier for this email."""
    if not FLOWCAST_ADMIN_KEY:
        print("  ⚠️  No flowcast_admin_key in discord_secrets.json — skipping tier lookup")
        return None
    encoded_email = urllib.parse.quote(email.strip())
    url = f"{FLOWCAST_API_URL}/api/admin/discord/user-tier?email={encoded_email}&admin_key={FLOWCAST_ADMIN_KEY}"
    r = urllib.request.Request(url, headers={"User-Agent": "FlowCast-Discord-Bot/1.0"})
    try:
        with urllib.request.urlopen(r, timeout=10) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"  FlowCast API error {e.code}: {e.read().decode()[:120]}")
        return None
    except Exception as ex:
        print(f"  FlowCast API error: {ex}")
        return None


# ── Job 1: Reaction roles ─────────────────────────────────────────────────────
def process_reaction_roles():
    print("\n[1] Reaction roles...")
    assigned = 0
    for emoji, role_id in REACTION_ROLES.items():
        reactors = get_reactions(emoji)
        for user in reactors:
            if user.get("bot"):
                continue
            user_id = user["id"]
            member = get_member(user_id)
            if member is None:
                continue
            if role_id not in member.get("roles", []):
                uname = user.get("username", "?")
                print(f"  → {emoji} → {uname}")
                if assign_role(user_id, role_id, f"Reaction role: {emoji}"):
                    assigned += 1
            time.sleep(0.2)
    print(f"  Assigned: {assigned}")


# ── Job 2: Account-setup tier verification ────────────────────────────────────
def process_tier_verifications():
    """
    Watches #account-setup for messages matching:
      verify: email@domain.com
    Looks up tier in FlowCast, assigns role, replies, deletes original.
    """
    print("\n[2] Tier verifications (#account-setup)...")
    state = load_state()
    last_id = state.get("account_setup_last_id")

    messages = get_channel_messages(CH_ACCOUNT_SETUP, after=last_id, limit=50)
    if not messages:
        print("  No new messages.")
        return

    # Discord returns newest-first; process oldest-first
    messages = sorted(messages, key=lambda m: int(m["id"]))

    processed = 0
    for msg in messages:
        state["account_setup_last_id"] = msg["id"]
        content = msg.get("content", "").strip()
        author  = msg.get("author", {})

        if author.get("bot"):
            continue

        # Match "verify: email@..." (case-insensitive, flexible spacing)
        match = re.search(r"verify\s*:\s*([^\s]+@[^\s]+)", content, re.IGNORECASE)
        if not match:
            continue

        email   = match.group(1).strip().lower()
        user_id = author["id"]
        uname   = author.get("username", "?")
        msg_id  = msg["id"]

        print(f"  Verify request from {uname}: {email}")
        result = lookup_flowcast_tier(email)

        if result is None:
            send_message(CH_ACCOUNT_SETUP,
                f"<@{user_id}> ⚠️ Couldn't reach FlowCast to verify your account. Please try again in a few minutes.")
            continue

        if not result.get("found"):
            send_message(CH_ACCOUNT_SETUP,
                f"<@{user_id}> ❌ No FlowCast account found for that email. "
                f"Make sure you're using the email you signed up with at flowcast.space")
            delete_message(CH_ACCOUNT_SETUP, msg_id)
            continue

        tier = result.get("tier", "splash")
        role_id = TIER_TO_ROLE.get(tier)

        if not role_id:
            send_message(CH_ACCOUNT_SETUP,
                f"<@{user_id}> ✅ Account verified — you're on the **Splash** (free) plan. "
                f"Upgrade at flowcast.space/pricing to get a Creator or Studio role.")
            delete_message(CH_ACCOUNT_SETUP, msg_id)
            continue

        # Remove any existing tier roles before assigning new one
        member = get_member(user_id)
        if member:
            for old_role in [ROLE_CREATOR, ROLE_CREATOR_PRO, ROLE_STUDIO]:
                if old_role in member.get("roles", []) and old_role != role_id:
                    remove_role(user_id, old_role, "Tier update")

        if assign_role(user_id, role_id, f"FlowCast tier: {tier}"):
            tier_display = {"creator": "Creator", "creator_pro": "Creator Pro", "studio": "Studio"}.get(tier, tier)
            send_message(CH_ACCOUNT_SETUP,
                f"<@{user_id}> ✅ Verified! You've been given the **{tier_display}** role. "
                f"Welcome to your plan's channels. 🎬")
            print(f"    ✅ {uname} → {tier_display}")
        else:
            send_message(CH_ACCOUNT_SETUP,
                f"<@{user_id}> ⚠️ Verified your account but hit an error assigning the role. Ping a mod.")

        delete_message(CH_ACCOUNT_SETUP, msg_id)
        processed += 1
        time.sleep(0.3)

    save_state(state)
    print(f"  Processed: {processed}")


# ── Job 3: Auto-assign Splash to new members ──────────────────────────────────
def process_new_members():
    """Requires Server Members Intent in Discord Developer Portal."""
    print("\n[3] Splash auto-assign...")
    r = urllib.request.Request(
        f"https://discord.com/api/v10/guilds/{GUILD}/members?limit=1000",
        headers=HEADERS
    )
    try:
        with urllib.request.urlopen(r) as resp:
            members = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("  Server Members Intent not enabled — skipping.")
            print("  Enable at: discord.com/developers/applications → Bot → Privileged Gateway Intents")
        else:
            print(f"  Error {e.code}: {e.read().decode()[:100]}")
        return

    count = 0
    for m in members:
        if m.get("user", {}).get("bot"):
            continue
        if not set(m.get("roles", [])).intersection(ALL_CUSTOM_ROLES):
            uid   = m["user"]["id"]
            uname = m["user"].get("username", "?")
            print(f"  → Splash → {uname}")
            if assign_role(uid, ROLE_SPLASH, "Auto-assign: new member"):
                count += 1
            time.sleep(0.3)
    print(f"  Splash assigned: {count}")


# ── Main ──────────────────────────────────────────────────────────────────────
def run():
    print(f"=== FlowCast Discord Role Sync — {datetime.now(timezone.utc).isoformat()} ===")
    process_reaction_roles()
    process_tier_verifications()
    process_new_members()
    print("\n=== Done ===")


if __name__ == "__main__":
    run()

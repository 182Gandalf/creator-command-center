---
name: skill-builder
description: Auto-detects repeatable tasks from conversation context and turns them into reusable workflows/skills. Use when (1) A task pattern emerges that might repeat, (2) Creating or updating a skill, (3) Codex has written similar code/commands multiple times, (4) User mentions "this comes up a lot" or similar, (5) A workflow has 3+ steps that could be automated. Monitors conversations passively and proactively suggests skill creation when patterns are detected.
---

# Skill Builder

Auto-detects repeatable tasks and converts them into reusable skills to save time and tokens.

## Pattern Detection Triggers

Watch for these signals that a task should become a skill:

1. **Repetition indicators**
   - User says: "I do this often", "this comes up a lot", "I need this regularly"
   - Same type of request 2+ times in recent conversations
   - Similar code/commands being rewritten

2. **Complexity indicators**  
   - Multi-step workflow (3+ steps)
   - Requires specific tool combinations
   - Has domain-specific knowledge or parameters

3. **Fragility indicators**
   - Easy to make mistakes
   - Requires specific sequence
   - Has hard-to-remember flags/options

## When to Auto-Create a Skill

Create a skill when ALL are true:
- Pattern detected 2+ times
- Steps are mostly deterministic
- Would save >50 tokens per use
- Not a one-off exploration

## Auto-Detection Workflow

When skill-builder triggers, follow this process:

### Step 1: Analyze the Pattern
- Identify the core repeatable task
- Note required inputs/outputs
- List tools/commands used
- Estimate complexity (simple/medium/complex)

### Step 2: Check for Existing Skills
- Search workspace/skills/ for similar skills
- Check if task fits an existing skill's scope
- Avoid duplication - extend existing if applicable

### Step 3: Design the Skill
**Choose skill type:**
- **Script skill**: For deterministic, fragile operations
- **Template skill**: For boilerplate generation
- **Reference skill**: For domain knowledge lookup
- **Hybrid**: Combine as needed

**Determine inputs:**
- Required vs optional parameters
- Default values
- Validation rules

### Step 4: Create the Skill
Use the skill-creator skill's workflow:

```bash
# Initialize
scripts/init_skill.py <skill-name> --path skills/ --resources scripts,references

# Edit SKILL.md with detected pattern
# Add scripts for repeatable operations
# Test on sample inputs

# Package
scripts/package_skill.py skills/<skill-name>
```

### Step 5: Document & Notify
After creating skill:
1. Add entry to skill-registry.md (see below)
2. Notify user: "Created [skill-name] skill for [task]. Use it by saying [example trigger]"
3. Show estimated token savings

## Skill Registry

Maintain this file to track auto-created skills:

**File:** `/home/daz/.openclaw/workspace/.claw/skills/skill-registry.md`

Format:
```markdown
# Skill Registry
Auto-detected and created skills. Updated automatically by skill-builder.

## Active Skills

### skill-name
- **Created**: YYYY-MM-DD
- **Pattern**: Brief description of detected pattern
- **Triggers**: When to use this skill
- **Saves**: ~X tokens per use
- **Usage count**: N (auto-updated)

## Retired Skills
Skills no longer needed, kept for reference.
```

## Updating This Skill

As new patterns emerge, update skill-builder itself:

1. **Add new detection patterns** to Pattern Detection Triggers
2. **Refine thresholds** based on false positives/negatives  
3. **Improve skill templates** with better defaults
4. **Log detection decisions** for later analysis

## Example Auto-Creations

**Example 1: Deployment Skill**
- Pattern: User deploys app with Railway 3x this week
- Detected: Same 5-step sequence each time
- Created: `railway-deploy` skill with `scripts/deploy.sh`
- Saves: ~200 tokens per deployment

**Example 2: Landing Page Updates**
- Pattern: User requests landing page tweaks repeatedly
- Detected: Similar CSS/HTML changes
- Created: `lp-updater` skill with common templates
- Saves: ~150 tokens per update

**Example 3: Git Operations**
- Pattern: Same git workflow (add, commit, push, verify)
- Detected: Commands rewritten each time
- Created: `git-flow` skill with parameterized script
- Saves: ~100 tokens per operation

## Implementation Notes

- Run pattern detection silently during conversations
- Only suggest creation when confidence >70%
- Respect user's decision if they decline
- Skills should be lean - don't over-engineer
- Prefer scripts over long explanations
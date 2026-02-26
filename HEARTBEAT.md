# HEARTBEAT.md - Self-Improvement Workflow

## On Wake (Every 30 Minutes)

**Model:** Route to local Llama 3.2 via Ollama

**Tasks:**

1. **Review Past Mistakes**
   - Read recent memory files (today + yesterday)
   - Look for errors, failures, or suboptimal outcomes
   - Identify patterns in mistakes

2. **Spawn Self-Improvement Subagent**
   - Spawn a subagent with task: "Review my recent mistakes and suggest concrete improvements"
   - Let it run in parallel (non-blocking)

3. **Quick System Checks** (rotate through these)
   - Check for any urgent notifications
   - Review any pending tasks
   - File organization if needed

## Execution Notes

- Use parallel processing (spawn subagents) for heavy analysis tasks
- Focus on actionable improvements, not just reflection
- Document lessons learned in memory files

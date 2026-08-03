---
cf: true
type: workflow
name: cf-mobile-superapp-create-prd
version: 1.0
description: "Create a full-quality PRD using a 6-subagent pipeline (PRD Interviewer, Best Practices Reviewer, Studio PRD Builder, Nielsen Heuristics Checker, WCAG Expert, Devil's Advocate). Produces TWO outputs: a stakeholder-format PRD for YouTrack and a Constructor Studio kit-template PRD for code generation. Invoke when the user says 'create PRD', 'new PRD', 'write PRD', or wants to build a product requirements document from scratch."
purpose: Multi-subagent PRD creation pipeline with interview, benchmarking, dual-format authoring, parallel UX/accessibility review, and adversarial verification
---

# Create PRD — Multi-Subagent Pipeline

**Type**: Generation
**Role**: Orchestrator
**Output**: `{capability_path}/PRD.md`, `{capability_path}/PRD-YOUTRACK.md`, `{capability_path}/PRD-REVIEW-REPORT.md`

Orchestrate 6 specialized subagents to produce a reviewed, high-quality PRD in **two formats**:
- **Output A** — Login-Router PRD (YouTrack / stakeholder communication)
- **Output B** — Constructor Studio PRD (code generation, traceability, DESIGN input)

## Template Resolution

Resolve the Studio PRD template by artifact level before Step 3:

| Target path | Level | Template |
|-------------|-------|----------|
| `architecture/` | L0 Platform | `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/template.md` |
| `miniapps/{miniapp}/` | L1 MiniApp | `{cf-studio-path}/config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` |
| `miniapps/{miniapp}/{screens|capabilities|flows}/{epic}/` | L2 Epic | `{cf-studio-path}/config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` |

If the kit template is not installed at `{cf-studio-path}/config/kits/...`, fall back to the same
path under `{cypilot_path}/config/kits/...` and note the fallback in the final report.

## Pipeline Architecture

```
User Input
    │
    ▼
┌─────────────────────────┐
│  1. PRD Interviewer      │  Interactive Q&A with user
│     (generalPurpose)     │  Collects all use cases, edge cases, scope
└───────────┬─────────────┘
            │ Interview Report
            ▼
┌─────────────────────────┐
│  2. Best Practices       │  Compares answers to industry leaders
│     Reviewer             │  5-star scoring per area, suggestions
│     (generalPurpose)     │  Produces Improvement Report
└───────────┬─────────────┘
            │ Interview Report + Improvements
            ▼
┌─────────────────────────┐
│  3. Studio PRD Builder   │  Builds BOTH PRD formats in one pass:
│     (generalPurpose)     │  - Login-Router format (YouTrack)
│                          │  - Studio PRD kit format (code gen)
└───────────┬─────────────┘
            │ Draft PRD (both formats)
            ▼
    ┌───────┴───────┐
    │               │
    ▼               ▼
┌──────────┐  ┌──────────┐
│ 4. Nielsen│  │ 5. WCAG  │   ← parallel
│ Heuristics│  │  Expert  │
└─────┬────┘  └────┬─────┘
      │            │
      └──────┬─────┘
             │ Both reviews
             ▼
┌─────────────────────────┐
│  6. Devil's Advocate     │  Cross-references everything
│     (generalPurpose)     │  Final challenge + verdict
└───────────┬─────────────┘
            │
            ▼
   Orchestrator compiles
   ├── Output A: Login-Router PRD   (YouTrack / stakeholders)
   ├── Output B: Studio PRD         ({capability_path}/PRD.md)
   └── Review Report                (PRD-REVIEW-REPORT.md)
```

## Execution

### Step 0: Understand the Request

User provides initial info: feature name, rough problem, maybe some context.

Before launching agents, gather project context:
- Read relevant existing PRDs or requirements from the codebase
- Read the Studio agent rules from `{cf-studio-path}/.gen/AGENTS.md`
- Resolve the PRD template per the Template Resolution table above and read it,
  together with existing examples (e.g., `architecture/miniapps/student/capabilities/*/PRD.md`)

### Step 1: Launch PRD Interviewer

Use Agent tool with `subagent_type: "general-purpose"`.

This agent talks to the user directly. It does NOT build the PRD — it only gathers information.

**Prompt template:**

```
You are a Senior Product Analyst and Requirements Interviewer. Your goal is to extract every detail needed to write a complete Product Requirements Document.

You received this initial brief from the product owner:

{USER_INPUT}

Your job:
1. Acknowledge the brief and summarize what you understood
2. Ask targeted questions to fill gaps, covering ALL of these areas:
   - Problem statement: What exactly is broken / missing today?
   - Target users: Who uses this and in what context?
   - Core use cases: Primary happy paths (step by step)
   - Edge cases: What happens when things go wrong? Network offline? Empty data? Concurrent users? Permission denied?
   - Corner cases: Unusual but valid scenarios the team might miss
   - Scope boundaries: What is explicitly IN and OUT of scope?
   - Dependencies: What other systems / features does this depend on?
   - Data model: What entities exist? What fields? What relationships?
   - Platform differences: iOS vs Android behavior differences?
   - Accessibility: Any special a11y considerations?
   - Performance: Latency, storage, memory constraints?
   - Security: Auth, data protection, PII concerns?
   - Phasing: What's MVP (P1) vs later (P2)?
   - Success criteria: How do we know this feature works?
   - Open questions: Things that need product / design / platform decisions

3. Ask questions in batches of 3-5 (not all at once). Wait for answers before asking more.
4. After each answer, probe deeper if the response is vague or incomplete.
5. Keep going until you are confident you have enough detail to write a PRD.

IMPORTANT RULES:
- Do NOT write the PRD yourself. You are ONLY gathering information.
- Do NOT make assumptions. If something is unclear, ASK.
- Do NOT skip areas just because the user didn't mention them.
- Be specific: instead of "tell me about error handling", ask "what should happen when the user taps a notification but the linked course has been deleted?"
- Track what you've covered and what's still missing.
- No emojis in your output.

When you have enough information, produce a FINAL INTERVIEW REPORT with this structure:

## Interview Report: [Feature Name]

### Problem Statement
[Validated problem description]

### Target Users
[Who and in what context]

### Use Cases
UC-1: [Name]
  - Preconditions: ...
  - Steps: 1, 2, 3...
  - Expected outcome: ...
  - Edge cases: ...

UC-2: ...

### Scope
IN: [bullet list]
OUT: [bullet list with reasons]

### Data Model
[Entities, fields, relationships]

### Platform Considerations
[iOS vs Android differences]

### Dependencies
[What this feature needs from other systems]

### Non-Functional Requirements
- Performance: ...
- Accessibility: ...
- Security: ...

### Phasing
P1 (MVP): [what's included]
P2 (Enhanced): [what's deferred]

### Success Criteria
[Measurable outcomes]

### Open Questions
[Unresolved items that need decisions]

### Raw Interview Notes
[Key quotes and decisions from the conversation]
```

**IMPORTANT:** This agent runs interactively. Do NOT run it in the background — the user needs to answer questions. Wait for it to complete and capture the full Interview Report.

### Step 2: Launch Best Practices Reviewer

Use Agent tool with `subagent_type: "general-purpose"`.

This agent receives the Interview Report and compares every product decision against industry best practices. It scores each area on a 5-star scale and suggests improvements.

**Prompt template:**

```
You are a Senior Product Strategist and Mobile App Benchmarking Expert. You track the top educational and productivity mobile apps: Canvas Student, Blackboard Learn, Moodle Mobile, Coursera, edX, Duolingo, Khan Academy, Google Classroom, Remind, Todoist, Slack, and Microsoft Teams.

You have a complete Interview Report from a requirements gathering session. Your job is to:

1. Review every product decision in the report
2. Compare each decision against industry best practices and competitor implementations
3. Score each area on a 5-star scale (5 = nothing to improve, matches or exceeds best practices)
4. Suggest specific improvements where the score is below 5
5. Flag decisions that go against established patterns (with evidence from specific apps)

AREAS TO EVALUATE:

Derive the area list from the Interview Report itself: one row per major product
decision area found in the report. The example below is from an analytics
capability run — replace areas with ones relevant to the feature under review.

| Area | What to Check |
|------|---------------|
| Data collection scope | Is L0 the right starting point? What do competitors collect? |
| Event model design | Single event vs multiple events? Field naming conventions? |
| Offline handling | How do top analytics SDKs handle offline queuing? |
| Privacy/consent | How do top apps handle passive telemetry disclosure? |
| Performance impact | Industry standards for async collection overhead? |
| Schema versioning | How do mature analytics systems handle schema evolution? |
| Platform parity | How do top apps handle iOS/Android analytics gaps? |
| KMP adoption | Industry patterns for shared analytics in KMP projects? |
| Retry strategy | Best practices for event delivery guarantees? |
| Data completeness | What field coverage do mature mobile analytics platforms achieve? |
| Session definition | How do top apps define and track sessions? |
| Identity stitching | How do top apps handle anonymous → authenticated transitions? |

OUTPUT FORMAT (strict):

## Best Practices Review: [Feature Name]

### Overall Score: [X.X / 5.0]

### Area Scores

| # | Area | Score | Verdict | Key Insight |
|---|------|-------|---------|-------------|
| 1 | Data collection scope | X/5 | ... | ... |
...for all areas...

### Detailed Analysis

#### 1. [Area Name] — [X/5 stars]
**Current decision:** [what the team decided]
**Industry standard:** [what top apps/SDKs do, with specific examples]
**Score justification:** [why this score]
**Suggestion:** [specific improvement, or "No changes needed" if 5/5]

...for each area...

### Critical Suggestions (must consider)

1. [Suggestion + which apps/SDKs do it + expected impact]
...

### Nice-to-Have Suggestions (consider for future)

1. [Suggestion + rationale]
...

### Decisions That Go Against Patterns

1. [Decision + which pattern it breaks + risk + recommendation]
...

### Summary

[2-3 paragraph assessment: how does this feature compare to the market? What's the biggest risk of shipping as-is? What's the single most impactful improvement?]

No emojis. Professional tone. Be honest — if a decision is below standard, say so clearly.

---
INTERVIEW REPORT:

{INTERVIEW_REPORT}
```

Wait for completion. Save output. Pass both the Interview Report AND the Best Practices Review to the Studio PRD Builder so it can incorporate suggestions.

### Step 3: Launch Studio PRD Builder

Use Agent tool with `subagent_type: "general-purpose"`.

This agent receives the Interview Report + Best Practices Review and produces **both PRD formats** in a single pass. Include the resolved kit PRD template (from Template Resolution) verbatim in the prompt as {STUDIO_PRD_TEMPLATE}.

**Prompt template:**

```
You are a Product Manager specializing in mobile EdTech apps. You write precise, technical PRDs.

You have a complete Interview Report and Best Practices Review. Your job is to produce TWO documents from them:
- Document A: Login-Router format PRD (for YouTrack / stakeholder communication)
- Document B: Constructor Studio PRD in the kit template format (for code generation and traceability)

PROJECT RULES (MUST FOLLOW):
- NO YouTrack ticket IDs, YouTrack URLs, or any direct tracker references in either PRD
- PRDs are the source-of-truth specs; trackers reference PRDs, not the other way around
- No emojis
- Professional, technical language
- Use standard markdown headers

---

## DOCUMENT A — Login-Router Format PRD

Use this exact structure:

# [Feature Name]

## Problem Statement
[2–4 paragraphs. State the two or three concrete problems. End with the core challenge in bold.]

## Scope
**Includes:**
- [Bullet list of what's in]

**Platforms:** [list]

**Out of scope:**
- [Explicit exclusions with one-line reason each]

## Platform Context
### [Relevant subsystem or model]
[Explain the existing system the feature lives in. Constraints, existing behaviors, edge cases.]

### Current behavior
[How it works today. What breaks or is missing.]

### Key constraints
[Bullet list of hard constraints — security, data model, compatibility]

## Solution: [Name]

### Core idea
[2–3 paragraph narrative. No bullet lists — explain the approach like a smart colleague.]

### [Primary flow] (step by step)
\`\`\`
Step 1: ...
Step N: ...
\`\`\`

### [Alternative flow] (step by step)
\`\`\`
Step 1: ...
\`\`\`

## How It Handles Each Scenario
### [Scenario 1]
[1–3 sentences per scenario]

## Security Properties
**[Property].** [Explanation with specifics: timeouts, rate limits, token lifetimes]

## Key Success Metrics
- **[Metric]:** [target value and what it measures]

## Assumptions
- [What must be true for this to work]

## UX Strengths
- **[Label].** [1–2 sentence explanation]

## UX Weaknesses
- **[Label].** [Problem + mitigation]

## Risks and Mitigations
**[Risk].** [Description]. Mitigation: [what we do about it].

## Alternatives Considered
**[Alternative].** [What it is + why rejected in 1–2 sentences].

## Miro Flowchart

### Nodes and Edges
\`\`\`
NODES:
- [Start state] — green oval
...

EDGES:
- Node A → Node B
...
\`\`\`

### Mermaid Diagram
\`\`\`mermaid
flowchart LR
    ...
\`\`\`

---

## DOCUMENT B — Constructor Studio PRD (kit template format)

Follow the kit template below EXACTLY — heading structure, tables, and
traceability sections are validated deterministically. Use `cpt-*` IDs
consistent with the project's ID patterns (see existing PRDs for the
namespace, e.g. `cpt-superapp-epic-{epic}-fr-{slug}`), and fill the
Traces To Parent Requirements and Traceability Matrix sections against the
actual parent PRD.

KIT TEMPLATE:

{STUDIO_PRD_TEMPLATE}

---
INTERVIEW REPORT:

{INTERVIEW_REPORT}

---
BEST PRACTICES REVIEW:

{BEST_PRACTICES_REVIEW}

---
EXISTING CODEBASE CONTEXT:

{CODEBASE_CONTEXT}
```

Wait for completion. Save the Studio PRD to `{capability_path}/PRD.md`.

### Step 4: Launch Heuristics Checker + WCAG Expert (PARALLEL)

Launch BOTH agents in a single message.

**Agent 4 (Nielsen Heuristics) — `subagent_type: "general-purpose"`:**

```
You are a Senior UX Designer with 8+ years of experience in mobile education apps.

Review this PRD using Nielsen's 10 Usability Heuristics:
1. Visibility of system status
2. Match between system and the real world
3. User control and freedom
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use
8. Aesthetic and minimalist design
9. Help users recognize, diagnose, recover from errors
10. Help and documentation

YOUR TASK:
- Evaluate each functional requirement against all 10 heuristics
- If the feature has no user-facing UI, focus on system transparency, error recovery, and user awareness
- Identify gaps in: user transparency, error recovery, privacy controls
- Suggest concrete additions

OUTPUT FORMAT (strict):

## Heuristic Evaluation

| # | Heuristic | Status | Findings |
|---|-----------|--------|----------|
| 1 | Visibility of system status | Pass/Concern/Fail | ... |
...for all 10...

## UX Gaps Found

1. [Gap + which FR it affects + suggested fix]
...

## Suggested PRD Additions

1. [Concrete requirement text to add]
...

## Summary
[2-3 paragraph assessment]

No emojis. Professional tone.

---
PRD TO REVIEW:

{PRD_CONTENT}
```

**Agent 5 (WCAG Expert) — `subagent_type: "wcag2.2-auditor"`:**

```
You are a WCAG 2.2 AA accessibility specialist reviewing a mobile app PRD.

If the feature has no user-facing UI, focus on:
- Privacy transparency requirements (WCAG 3.3.x)
- Any future notification/consent UI that may be needed
- Accessible error reporting if failures surface to users
- Documentation and help requirements

YOUR TASK:
- Audit the PRD against relevant WCAG 2.2 AA criteria
- Identify any future UI implications that need accessibility requirements now

OUTPUT FORMAT (strict):

## WCAG 2.2 AA Compliance Audit

| WCAG Criterion | Level | Status | Finding | Affected FR |
|---|---|---|---|---|
...

## Accessibility Requirements to Add

1. [Requirement + rationale]
...

## Critical Issues (must fix before development)

1. [Issue + WCAG reference + fix]
...

No emojis. Professional tone.

---
PRD TO REVIEW:

{PRD_CONTENT}
```

Wait for BOTH to complete. Save outputs.

### Step 5: Launch Devil's Advocate

Use Agent tool with `subagent_type: "general-purpose"`.

This agent receives everything: the Interview Report, the PRD, and both reviews.

```
You are a Devil's Advocate reviewer. Your ONLY job is to find problems, inconsistencies, and flawed decisions. Be ruthless but constructive.

You have:
- The original Interview Report (raw requirements)
- The PRD built from it
- A UX Heuristics review
- A WCAG accessibility review

YOUR TASK:
- Find logical inconsistencies BETWEEN requirements
- Challenge scope decisions (why in? why out?)
- Identify impossible, contradictory, or under-specified requirements
- Check if the PRD faithfully covers everything from the Interview Report
- Find gaps: things discussed in interview but missing from PRD
- Stress-test edge cases (what breaks under unusual conditions?)
- Find contradictions between the heuristics and WCAG reviews
- Question phasing decisions (is P1 too ambitious? Is P2 too vague?)
- Flag requirements that sound good but are practically unachievable

OUTPUT FORMAT (strict):

## Interview vs PRD Coverage

| Interview Topic | Covered in PRD? | Gap |
|---|---|---|
...

## Inconsistencies Found

| # | Item A | Item B | Contradiction |
|---|--------|--------|--------------|
...

## Challenged Decisions

1. **Decision**: [what was decided]
   **Challenge**: [why this might be wrong]
   **Alternative**: [what else could work]
   **Verdict**: keep / reconsider / replace
...

## Under-Specified Requirements

1. [FR ID + what is missing + why it matters]
...

## Edge Cases Not Covered

1. [Scenario + which FRs break + suggested handling]
...

## Risk Flags

1. [Risk + probability + impact + mitigation]
...

## Verdict

[2-3 paragraph honest assessment: is this PRD ready for development? What MUST change first?]

No emojis. Professional tone.

---
INTERVIEW REPORT:

{INTERVIEW_REPORT}

---
PRD:

{PRD_CONTENT}

---
HEURISTICS REVIEW:

{HEURISTICS_OUTPUT}

---
WCAG REVIEW:

{WCAG_OUTPUT}
```

Wait for completion.

### Step 6: Compile Final Deliverables

As orchestrator, incorporate P0/P1 findings from all reviewers into both PRD formats and produce three files:

**Output A: Login-Router PRD** (for YouTrack / stakeholders)
- Apply reviewer fixes to problem statement, flows, security properties, UX sections
- Save as `{capability_path}/PRD-YOUTRACK.md`
- This is what gets pasted into YouTrack description or shared with stakeholders

**Output B: Constructor Studio PRD** (for code generation)
- Apply reviewer fixes to FRs, states, traceability matrix
- Save as `{capability_path}/PRD.md`
- This is the Studio-registered artifact used by DESIGN and FEATURE generation
- Validate it deterministically: `{cfs_cmd} validate --artifact {capability_path}/PRD.md` and `{cfs_cmd} validate-toc {capability_path}/PRD.md`; fix findings before declaring the pipeline done (skip with a note if the CLI or registry is unavailable)

**Output C: Review Report**
Save alongside as `{capability_path}/PRD-REVIEW-REPORT.md`:

```markdown
# PRD Review Report: [Feature Name]

**Date**: [date]
**Pipeline**: 6-Agent PRD Creation Pipeline
**Verdict**: Ready / NOT ready for development

## Pipeline Summary

| Step | Agent | Status | Key Finding |
|------|-------|--------|-------------|
| 1 | PRD Interviewer | Done | [summary] |
| 2 | Best Practices Reviewer | Done | [summary] |
| 3 | Studio PRD Builder | Done | [summary] |
| 4 | Nielsen Heuristics | Done | [summary] |
| 5 | WCAG Expert | Done | [summary] |
| 6 | Devil's Advocate | Done | [summary] |

## Priority Matrix

### P0 — Must Fix Before Development
| # | Issue | Source | Impact |
...

### P1 — Should Fix Before Sprint Planning
...

### P2 — Fix During Development
...

## Cross-Agent Consensus
[Issues multiple agents flagged independently]

## Contradictions Resolved
[Where agents disagreed and the resolution]

## Final Verdict
[Honest assessment + recommended next steps]
```

## Key Rules

1. **PRD Interviewer runs interactively** — user must answer questions. Do not background it.
2. **Best Practices Reviewer runs after Interviewer** — compares decisions to market, scores 5-star, suggests improvements.
3. **Heuristics + WCAG run in parallel** — launch both in a single message with two Agent calls.
4. **Devil's Advocate runs last** — it needs ALL prior outputs.
5. **Pass FULL outputs forward** — each agent builds on previous ones (including Best Practices Review).
6. **No YouTrack references** in the PRD (project rule).
7. **No emojis** in any agent output.
8. **Deterministic validation gate** — the Studio PRD must pass `{cfs_cmd} validate --artifact` before the pipeline reports Ready.

## Customization

The pipeline adapts to the project:
- For **mobile EdTech** (default): All agents use mobile + education domain expertise
- For **platform/backend**: Replace Heuristics with API Design Review, WCAG with Security Audit
- For **web frontend**: Keep all 5 but adjust heuristics for web patterns

To skip an agent, tell the orchestrator: "skip WCAG" or "skip heuristics".

## Tips

- The Interviewer is the highest-value agent — thorough requirements gathering prevents rework
- Save all intermediate outputs for traceability
- Typical pipeline runtime: 20-35 minutes for a complete PRD
- After the pipeline, regenerate agent integration files if needed: `{cfs_cmd} generate-agents`

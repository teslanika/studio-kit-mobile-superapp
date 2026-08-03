# PRD-MINIAPP Checklist — Layer Delta

**Artifact**: PRD-MINIAPP
**Kit**: mobile-superapp
**Level**: L1 (MiniApp)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/checklist.md` (sdlc PRD Expert Checklist)

This checklist is a **delta over the sdlc PRD Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a PRD-MINIAPP document; this file states how each expertise domain is scoped at the MiniApp layer and adds the criteria that exist only at this layer.

---

## Table of Contents

1. [How To Use This Checklist](#how-to-use-this-checklist)
2. [Expertise Domain Scope At This Layer](#expertise-domain-scope-at-this-layer)
3. [Layer Delta: MUST HAVE](#layer-delta-must-have)
4. [Layer Delta: MUST NOT HAVE](#layer-delta-must-not-have)
5. [Layer Delta: Mobile-Specific Criteria](#layer-delta-mobile-specific-criteria)
6. [Reporting](#reporting)

---

## How To Use This Checklist

1. **LOAD the base checklist first** and apply it in full: Referenced Standards, Prerequisites, Applicability Context, Severity Dictionary, Applicability Determination, Checkpointing, all MUST HAVE domains (BIZ, ARCH, SEC, SAFE, PERF, REL, UX, MAINT, COMPL, DATA, INT, OPS, TEST, DOC), and all MUST NOT HAVE items.
2. **Apply the domain scope table** below. Where a domain is marked *Inherited*, the MiniApp PRD satisfies it by referencing the platform PRD requirement and documenting only deviations — restating the platform text verbatim is a violation of `PRD-MINIAPP-NO-001`, and omitting it without a reference is a violation of base `DOC-PRD-001`.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report containing findings from both the base and this delta, citing base IDs (`BIZ-PRD-001`) and delta IDs (`PRD-MINIAPP-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L1 (MiniApp) | Notes |
|--------|-----------------------|-------|
| BIZ | Full | MiniApp purpose, goals, glossary, assumptions, risks are owned here; platform vision is referenced, not repeated |
| ARCH | Narrowed | MiniApp scope boundary and its dependency on kernel capabilities; module internals stay in DESIGN-MINIAPP |
| SEC | Narrowed | Exact per-actor permissions for this MiniApp's resources; authentication mechanics, session policy, and data classification are inherited from the platform PRD |
| SAFE | Inherited | Applicable only if this MiniApp introduces a hazard the platform does not already constrain |
| PERF | Narrowed | Only targets stricter than platform defaults, stated as `extends` with a Threshold |
| REL | Narrowed | MiniApp-level degraded/offline behavior and error expectations |
| UX | Narrowed | MiniApp-level flows, accessibility deviations, locale-specific content needs; per-screen UX is delegated to PRD-EPIC |
| MAINT | Inherited | Documentation/support expectations come from the platform unless this MiniApp needs more |
| COMPL | Inherited | Regulatory obligations are platform-wide; list only obligations this MiniApp's data or content adds |
| DATA | Narrowed | Which data this MiniApp owns vs consumes, and its freshness/retention expectations |
| INT | Narrowed | Backend capabilities this MiniApp requires, at capability level |
| OPS | Inherited | Release and rollout policy is platform-owned; note only MiniApp-specific gating (e.g., feature flag) |
| TEST | Full | Acceptance criteria and testability of every MiniApp requirement |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

---

## Layer Delta: MUST HAVE

### PRD-MINIAPP-001: Platform Traceability
**Severity**: CRITICAL

- [ ] Section 1.5 lists the platform requirements this MiniApp refines or inherits, with relation (`refines` / `inherits`)
- [ ] Every functional requirement either has a `Traces To` platform FR with relation `refines`, or is tagged `miniapp-specific` with a rationale
- [ ] Every referenced platform ID exists in the platform PRD (verified, not assumed)
- [ ] No orphan requirement: nothing is both untraced and untagged

### PRD-MINIAPP-002: Actor Reference Discipline
**Severity**: CRITICAL

- [ ] Actors are referenced by platform ID `cpt-{platform-prefix}-actor-{slug}`, never redefined
- [ ] Human and system actors are separated
- [ ] Each referenced actor has MiniApp-specific context (how this actor uses this MiniApp)
- [ ] If this MiniApp needs an actor the platform does not define, the finding is raised against the platform PRD instead of defining it here

### PRD-MINIAPP-003: Inherited Baseline Discipline
**Severity**: HIGH

- [ ] The Operational Concept section contains only deviations from platform baselines, or is deleted when there are none
- [ ] Each NFR either `extends` a platform NFR with a stricter Threshold, or is listed in NFR Exclusions with a reason
- [ ] Platform constraints are referenced by ID rather than copied
- [ ] Nothing in the document silently contradicts a platform baseline

### PRD-MINIAPP-004: Requirement ID And Priority Contract
**Severity**: HIGH

- [ ] Every FR, NFR, interface, contract, and use case is a checkbox with a priority marker and ID: `- [ ] \`pN\` - **ID**: \`cpt-...\``
- [ ] Priorities `p1`-`p9` are assigned by business impact
- [ ] All IDs follow `cpt-{hierarchy-prefix}-{kind}-{slug}` with the hierarchy prefix registered in `artifacts.toml`
- [ ] Each FR is a verifiable MUST statement with Rationale, Actors, and Acceptance fields
- [ ] No duplicate IDs within the document (verified with `cfs list-ids`)

### PRD-MINIAPP-005: Public MiniApp Surface
**Severity**: HIGH

- [ ] Every surface this MiniApp exposes — deep link, navigation entry point, host widget, notification channel, result returned to callers — is listed with an ID and a Type
- [ ] Each interface declares Stability and Breaking Change Policy
- [ ] Kernel contracts this MiniApp consumes are listed with Direction and Compatibility expectations
- [ ] Only business-level contracts; endpoints, payloads, and schemas are absent

### PRD-MINIAPP-006: Traceability Matrix Completeness
**Severity**: HIGH

- [ ] Platform FR → MiniApp FR coverage table lists every in-scope platform FR with coverage status (Full / Partial / Not in scope)
- [ ] MiniApp FR → Epic coverage table names the target epics for every MiniApp FR
- [ ] Requirements marked Partial state what is deferred and why
- [ ] Matrix rows are consistent with the requirement bodies (no ID appears in one place only)

### PRD-MINIAPP-007: Dependency Naming At Capability Level
**Severity**: MEDIUM

- [ ] Platform dependencies are named by kernel component ID
- [ ] External dependencies name the capability provided and criticality
- [ ] No endpoint, payload, protocol version, or auth header detail

### PRD-MINIAPP-008: ID Reference Appendix
**Severity**: LOW

- [ ] The appendix documents every ID pattern used with a concrete example
- [ ] The meaning of `{hierarchy-prefix}` is explained and matches this MiniApp's registered prefix

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items (`ARCH-PRD-NO-001/002`, `BIZ-PRD-NO-001/002`, `DATA-PRD-NO-001`, `INT-PRD-NO-001`, `TEST-PRD-NO-001`, `OPS-PRD-NO-001`, `SEC-PRD-NO-001`, `MAINT-PRD-NO-001`), all of which apply here unchanged.

### PRD-MINIAPP-NO-001: No Platform Duplication
**Severity**: HIGH

**What to check**:
- [ ] No platform requirement restated verbatim instead of referenced by ID
- [ ] No redefined actors, OS baselines, device classes, or platform-wide NFR thresholds
- [ ] No re-derivation of platform vision or business context

**Where it belongs**: `PRD-PLATFORM` — reference it by ID and document deviations only

### PRD-MINIAPP-NO-002: No Untraceable Requirements
**Severity**: HIGH

**What to check**:
- [ ] No FR without either a `Traces To` platform FR or a `miniapp-specific` tag plus rationale
- [ ] No dangling reference to a platform ID that does not exist
- [ ] No requirement introduced only inside a traceability table

**Where it belongs**: fix the trace, or raise the gap against `PRD-PLATFORM`

### PRD-MINIAPP-NO-003: No Screen-Level Specifications
**Severity**: MEDIUM

**What to check**:
- [ ] No per-screen layouts, component inventories, or interaction tables
- [ ] No screen state machines
- [ ] No copy or microcopy specifications

**Where it belongs**: `PRD-EPIC` (requirements) and `DESIGN-EPIC` (component design)

### PRD-MINIAPP-NO-004: No Module Implementation Detail
**Severity**: HIGH

**What to check**:
- [ ] No module/package structure, DI wiring, or state-management pattern
- [ ] No storage engine, serialization, or threading decisions
- [ ] No KMP/Swift/Kotlin API signatures

**Where it belongs**: `DESIGN-MINIAPP` (structure), `ADR` (decisions), `IMPL-*` (implementation reference)

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-MINIAPP-001: Offline Requirements
**Severity**: HIGH

- [ ] Which of this MiniApp's flows must work offline is stated, or explicitly deferred to the platform default
- [ ] Cached-data staleness expectations are stated at business level
- [ ] Behavior of user actions attempted while offline is stated (queued, blocked, degraded)

### MOBILE-MINIAPP-002: Cross-Platform Parity
**Severity**: HIGH

- [ ] iOS/Android parity is stated for this MiniApp, or deviations are listed with reasons
- [ ] Any platform-conditional capability names the constraining OS API, hardware, or store policy

### MOBILE-MINIAPP-003: Deep Link Requirements
**Severity**: HIGH

- [ ] Deep link entry points into this MiniApp are enumerated with their scheme segment
- [ ] Behavior for an unauthenticated or unauthorized deep-link open is stated
- [ ] Behavior for a deep link to unavailable content is stated

### MOBILE-MINIAPP-004: Push Notification Requirements
**Severity**: MEDIUM

- [ ] Notification types this MiniApp originates are listed with their trigger and target actor
- [ ] Tap-through destination is stated for each notification type
- [ ] User control over each notification type is stated (opt-in/opt-out granularity)

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/checklist.md` — without modification: the Validation Summary, Explicit Handling Verification, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For every domain marked Inherited or Narrowed in the scope table, confirm the PRD references the platform requirement instead of omitting or restating it

# PRD-EPIC Checklist — Layer Delta

**Artifact**: PRD-EPIC
**Kit**: mobile-superapp
**Level**: L2 (Epic / Screen / Flow)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/checklist.md` (sdlc PRD Expert Checklist)

This checklist is a **delta over the sdlc PRD Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a PRD-EPIC document; this file states how each expertise domain is scoped at the epic layer and adds the criteria that exist only at this layer.

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
2. **Apply the domain scope table** below. Where a domain is marked *Inherited*, the epic PRD satisfies it by referencing the MiniApp or platform requirement and documenting only deviations — restating inherited text verbatim is a violation of `PRD-EPIC-NO-001`, and omitting it without a reference is a violation of base `DOC-PRD-001`. An epic is the narrowest requirements layer: at this scope the UX, REL, and TEST criteria carry the most weight.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report containing findings from both the base and this delta, citing base IDs (`UX-PRD-002`) and delta IDs (`PRD-EPIC-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L2 (Epic) | Notes |
|--------|--------------------|-------|
| BIZ | Narrowed | Epic purpose, goals, and glossary terms new at this scope; the MiniApp's vision is referenced, not repeated |
| ARCH | Inherited | Only this epic's boundary and its dependencies; component design is delegated to DESIGN-EPIC |
| SEC | Narrowed | Exact per-actor permissions for the actions on this screen/flow; auth mechanics are inherited |
| SAFE | Inherited | Applicable only if this epic introduces a hazard not already constrained upstream |
| PERF | Narrowed | Only screen-level targets stricter than inherited defaults (e.g., time to interactive), with a Threshold |
| REL | Full | Error, empty, offline, and retry behavior for this screen/flow are owned here |
| UX | Full | Screen states, interactions, accessibility of this screen, and copy expectations are owned here |
| MAINT | Inherited | No epic-specific documentation obligations unless the epic adds a support surface |
| COMPL | Inherited | Reference the inherited obligation; list only what this epic's data or content adds (e.g., a consent prompt) |
| DATA | Narrowed | Which data this screen reads/writes, its owning capability, and freshness/offline expectations |
| INT | Narrowed | Backend capability this epic requires, at capability level |
| OPS | Inherited | Release and rollout policy is platform-owned; note only epic-specific gating (feature flag, staged exposure) |
| TEST | Full | Every epic requirement must be verifiable, including each state and each error condition |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

---

## Layer Delta: MUST HAVE

### PRD-EPIC-001: Parent Traceability
**Severity**: CRITICAL

- [ ] Section 1.5 lists the MiniApp requirements this epic details, with relation `details`
- [ ] The indirect platform trace is shown (MiniApp FR → platform FR) where one exists
- [ ] Every epic FR either has a `Traces To` MiniApp FR, or is tagged `epic-specific` with a rationale
- [ ] Every referenced parent ID exists in the parent document (verified, not assumed)

### PRD-EPIC-002: Actors, Permissions, And Entry Points
**Severity**: CRITICAL

- [ ] Actors are referenced by platform ID, never redefined, with their role in this epic
- [ ] Exact permissions for this epic's actions are stated per actor and resource
- [ ] Entry points into this epic are enumerated (deep link, in-app navigation, notification tap)
- [ ] Behavior for an unauthorized or unauthenticated entry is stated

### PRD-EPIC-003: State Coverage
**Severity**: CRITICAL

- [ ] All applicable states are defined: loading, content, empty, error, offline
- [ ] Each state states its entry condition and the user-visible behavior
- [ ] States are declared with an ID `cpt-{hierarchy-prefix}-state-{slug}`
- [ ] States not applicable to this epic are explicitly marked not applicable with a reason
- [ ] Transitions between states are unambiguous

### PRD-EPIC-004: Error Handling Completeness
**Severity**: HIGH

- [ ] Each realistic failure is listed as a user-facing condition with the message intent and a recovery action
- [ ] Network failure, permission denial, expired session, and unavailable content are covered or explicitly excluded
- [ ] No HTTP status codes, error response formats, or exception types (those belong in DESIGN-EPIC)

### PRD-EPIC-005: Requirement ID And Priority Contract
**Severity**: HIGH

- [ ] Every FR, NFR, state, widget, interface, and use case is a checkbox with a priority marker and ID: `- [ ] \`pN\` - **ID**: \`cpt-...\``
- [ ] Priorities `p1`-`p9` are assigned by business impact
- [ ] All IDs follow `cpt-{hierarchy-prefix}-{kind}-{slug}` with the hierarchy prefix registered in `artifacts.toml`
- [ ] Each FR is a verifiable MUST statement with Actors, UI Element, and Acceptance fields
- [ ] No duplicate IDs within the document (verified with `cfs list-ids`)

### PRD-EPIC-006: UI/UX Requirements
**Severity**: HIGH

- [ ] A screen layout sketch shows the structural regions of the screen
- [ ] Every component referenced by a requirement appears in the component table with an ID
- [ ] Interactions are listed with trigger and result
- [ ] Requirements describe intent and observable behavior, not styling values or design tokens

### PRD-EPIC-007: Data Requirements
**Severity**: MEDIUM

- [ ] Each data entity this epic reads or writes names its owning capability
- [ ] Freshness and offline expectations are stated per entity
- [ ] No endpoint, payload, schema, or field-level type detail

### PRD-EPIC-008: Traceability Matrices
**Severity**: HIGH

- [ ] MiniApp FR → epic FR coverage table lists coverage status for every parent FR in scope
- [ ] Epic FR → feature mapping names the target features
- [ ] The full traceability chain (platform → MiniApp → epic → design → feature) is shown
- [ ] Matrix rows are consistent with the requirement bodies

### PRD-EPIC-009: ID Reference Appendix
**Severity**: LOW

- [ ] The appendix documents every ID pattern used with a concrete example
- [ ] The meaning of `{hierarchy-prefix}` is explained and matches this epic's registered prefix

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items (`ARCH-PRD-NO-001/002`, `BIZ-PRD-NO-001/002`, `DATA-PRD-NO-001`, `INT-PRD-NO-001`, `TEST-PRD-NO-001`, `OPS-PRD-NO-001`, `SEC-PRD-NO-001`, `MAINT-PRD-NO-001`), all of which apply here unchanged.

### PRD-EPIC-NO-001: No Parent Duplication
**Severity**: HIGH

**What to check**:
- [ ] No MiniApp or platform requirement restated verbatim instead of referenced by ID
- [ ] No redefined actors, OS baselines, or platform-wide NFR thresholds
- [ ] No re-derivation of the MiniApp's business context

**Where it belongs**: `PRD-MINIAPP` / `PRD-PLATFORM` — reference by ID and document deviations only

### PRD-EPIC-NO-002: No Technical Architecture
**Severity**: HIGH

**What to check**:
- [ ] No component class diagrams, state-management pattern, or DI wiring
- [ ] No API endpoints, payloads, or status codes
- [ ] No navigation-graph or route-definition code
- [ ] No caching or persistence strategy

**Where it belongs**: `DESIGN-EPIC` (component design), `ADR` (decisions)

### PRD-EPIC-NO-003: No Feature-Level Detail
**Severity**: MEDIUM

**What to check**:
- [ ] No CDSL flows, algorithms, or pseudocode
- [ ] No per-platform implementation notes (Compose/SwiftUI specifics)
- [ ] No test case definitions

**Where it belongs**: `FEATURE-MOBILE` (spec), `IMPL-*` (implementation reference), code (tests)

### PRD-EPIC-NO-004: No Design-System Specifications
**Severity**: MEDIUM

**What to check**:
- [ ] No color values, spacing scales, font sizes, or design-token names
- [ ] No pixel-level measurements or asset export specs
- [ ] No animation curve or duration values

**Where it belongs**: `DESIGN-EPIC` and the design system

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-EPIC-001: Interaction Patterns
**Severity**: MEDIUM

- [ ] Touch interactions this screen supports are stated (tap, long press, swipe, pull to refresh)
- [ ] Keyboard, focus, and input handling are stated where the screen accepts input
- [ ] Back/dismiss behavior is stated, including unsaved-state handling

### MOBILE-EPIC-002: Deep Link Handling
**Severity**: HIGH

- [ ] The deep link that opens this epic is stated with its parameters at business level
- [ ] Cold-start vs warm-start behavior for the deep link is stated
- [ ] Invalid, expired, or unauthorized deep-link handling is stated

### MOBILE-EPIC-003: Platform-Specific UI
**Severity**: MEDIUM

- [ ] iOS/Android differences for this screen are listed with a reason, or parity is stated
- [ ] Platform navigation conventions relevant to this screen are named (e.g., back gesture, swipe-to-dismiss)

### MOBILE-EPIC-004: Accessibility Of This Screen
**Severity**: HIGH

- [ ] Screen-reader expectations are stated for every interactive element (label intent, grouping, order)
- [ ] Dynamic Type / font-scaling behavior of the layout is stated
- [ ] Contrast and touch-target expectations are stated as requirements, not design values

### MOBILE-EPIC-005: Offline Behavior Of This Screen
**Severity**: HIGH

- [ ] Whether this screen is usable offline is stated, consistent with the MiniApp offline policy
- [ ] What cached content is shown offline, and how staleness is communicated, is stated
- [ ] Behavior of user actions attempted offline is stated (queued, blocked, degraded)

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/checklist.md` — without modification: the Validation Summary, Explicit Handling Verification, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For every domain marked Inherited or Narrowed in the scope table, confirm the PRD references the parent requirement instead of omitting or restating it

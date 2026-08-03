# FEATURE-MOBILE Checklist — Layer Delta

**Artifact**: FEATURE-MOBILE
**Kit**: mobile-superapp
**Level**: L3 (Feature)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/FEATURE/checklist.md` (sdlc FEATURE Expert Checklist)

This checklist is a **delta over the sdlc FEATURE Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a FEATURE-MOBILE document; this file states how each expertise domain is scoped at the feature layer and adds the criteria that exist only at this layer.

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

1. **LOAD the base checklist first** and apply it in full: Referenced Standards, Review Scope Selection, Domain Prioritization by Feature Type, Prerequisites, Applicability Context, Severity Dictionary, all MUST HAVE domains (ARCH, SEM, PERF, SEC, REL, DATA, INT, OPS, MAINT, TEST, COMPL, UX, BIZ, DOC), and all MUST NOT HAVE items.
2. **Apply the domain scope table** below. Where a domain is marked *Inherited*, this feature satisfies it by referencing the epic, MiniApp, or platform element by ID and documenting deviations only.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report citing base IDs (`ARCH-FDESIGN-003`) and delta IDs (`FEATURE-MOBILE-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L3 (Feature) | Notes |
|--------|-----------------------|-------|
| ARCH | Narrowed | Flow, process, and state completeness inside this feature; system architecture is inherited |
| SEM | Full | Every in-scope PRD requirement, state, widget, and error condition must be realized by a flow, process, or transition |
| PERF | Narrowed | Feature-level budgets traced to an NFR; system capacity planning is inherited |
| SEC | Full | Input validation, authorization checks, and sensitive-data handling in these flows are owned here |
| REL | Full | Error handling, retry, offline fallback, and recovery for these flows are owned here |
| DATA | Full | Access patterns, validation, transformation, and lifecycle of the data this feature touches |
| INT | Full | API calls, DB operations, cache use, and bridge calls made by these processes |
| OPS | Narrowed | Observability hooks and feature-flag behavior for this feature only |
| MAINT | Narrowed | Process decomposition and reuse; module organization is inherited |
| TEST | Full | Testability, coverage guidance, and acceptance criteria are owned here |
| COMPL | Inherited | Reference the inherited obligation; add only what this feature's data or consent introduces |
| UX | Full | Flow usability and accessibility realization are owned here |
| BIZ | Inherited | Requirements and value are referenced from PRD-EPIC, never restated |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

*Inherited* domains name their source: COMPL → `PRD-PLATFORM` / `DESIGN-PLATFORM`; BIZ → `PRD-EPIC`.

---

## Layer Delta: MUST HAVE

### FEATURE-MOBILE-001: Parent Scope Consistency
**Severity**: CRITICAL

- [ ] The parent feature entry in the Epic DECOMPOSITION is linked and its ID matches
- [ ] Nothing here exceeds the scope that entry assigned; out-of-scope items are respected
- [ ] The declared dependencies match the DECOMPOSITION dependency graph

### FEATURE-MOBILE-002: Process Target Allocation
**Severity**: CRITICAL

- [ ] Every process is allocated to exactly one target: KMP shared, Android, iOS, or the WebView bridge
- [ ] Business logic lives in a KMP shared process; platform processes only reduce UI and integrate with the OS
- [ ] Each process names its source location, matching the DECOMPOSITION platform implementation table
- [ ] No logic is specified twice, once per platform

### FEATURE-MOBILE-003: Flow And Process Linkage
**Severity**: CRITICAL

- [ ] Every actor flow names its actor, entry point, success scenarios, and error scenarios
- [ ] Every flow step that leaves the UI names the process, API call, or DB operation it invokes
- [ ] Every process is called by at least one flow or another process; orphan processes are removed or justified
- [ ] Referenced API endpoints exist in the MiniApp DESIGN contracts

### FEATURE-MOBILE-004: State Machine Completeness
**Severity**: HIGH

- [ ] Every state named in the Epic DESIGN screen state model has at least one transition here
- [ ] Every transition names its source state, target state, and condition
- [ ] Every state is reachable and no state is a dead end without an exit or a documented terminal reason
- [ ] Restoration after configuration change and process death is specified

### FEATURE-MOBILE-005: Definitions Of Done Quality
**Severity**: HIGH

- [ ] Each DoD is a single MUST statement, testable as written
- [ ] Each DoD lists Implements (flow/process IDs), Constraints, Touches (KMP / Android / iOS / API / DB / entities), and Verification
- [ ] Every flow and process is implemented by at least one DoD
- [ ] No DoD references an ID that does not exist in this document or its parents

### FEATURE-MOBILE-006: Acceptance Criteria Coverage
**Severity**: HIGH

- [ ] Functional criteria cover the happy path and each error scenario
- [ ] Platform-specific criteria exist for Android and iOS, or their absence is justified
- [ ] Performance criteria carry a measurable threshold traced to an NFR
- [ ] Accessibility criteria are present
- [ ] Offline criteria are present or explicitly marked not applicable with a reason

### FEATURE-MOBILE-007: ID Reuse And Code Traceability
**Severity**: HIGH

- [ ] Widget, component, use case, and repository references reuse the IDs from PRD-EPIC and DESIGN-EPIC
- [ ] Only flow, process, state, dod, and featstatus IDs are newly defined here
- [ ] Each CDSL instruction carries an `inst-{slug}` marker, unique within its process
- [ ] `featstatus` is unchecked while any nested tracked ID is unchecked

### FEATURE-MOBILE-008: Traceability Links
**Severity**: MEDIUM

- [ ] Links to Epic PRD, Epic DESIGN, and Epic DECOMPOSITION are present
- [ ] Implementation links for KMP, Android, and iOS are present
- [ ] The requirement coverage table maps each in-scope requirement to a realizing element and a verifying criterion

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### FEATURE-MOBILE-NO-001: No Platform Coding Conventions
**Severity**: LOW

**What to check**:
- [ ] No naming, formatting, or style rules
- [ ] No dependency-injection wiring instructions

**Where it belongs**: `IMPL-IOS` / `IMPL-ANDROID` / `IMPL-KMP`

### FEATURE-MOBILE-NO-002: No Design-System Values
**Severity**: MEDIUM

**What to check**:
- [ ] No colors, spacing, typography, or animation curve values
- [ ] No pixel measurements

**Where it belongs**: the design system

### FEATURE-MOBILE-NO-003: No Parent Design Duplication
**Severity**: HIGH

**What to check**:
- [ ] No redefined domain entities, repository interfaces, or state contracts
- [ ] No restated navigation graph or module structure

**Where it belongs**: `DESIGN-EPIC` / `DESIGN-MINIAPP` — reference by ID

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-FEATURE-001: Cross-Platform Behavioral Parity
**Severity**: HIGH

- [ ] The Android and iOS processes produce the same user-visible outcome for the same intent
- [ ] Any deliberate divergence is stated with its reason and reflected in the acceptance criteria
- [ ] Nothing platform-specific is left implicit ("as native as possible" is not a specification)

### MOBILE-FEATURE-002: Offline And Cache Behavior
**Severity**: HIGH

- [ ] The repository process specifies cache read, staleness, write-through, and offline fallback
- [ ] Queued writes name the queue and the conflict-resolution rule
- [ ] The Offline state transition and its user-visible surface are specified

### MOBILE-FEATURE-003: Lifecycle And Interruption Handling
**Severity**: HIGH

- [ ] Backgrounding, foregrounding, and process death during the flow are handled
- [ ] Android configuration change and iOS scene-phase transitions are both addressed
- [ ] In-flight requests on interruption are cancelled, retried, or resumed by an explicit rule

### MOBILE-FEATURE-004: Accessibility In The Flow
**Severity**: HIGH

- [ ] Screen-reader announcements for state changes (loading, error, success) are specified
- [ ] Focus movement across the flow is specified
- [ ] Font-scaling behavior for the affected screens is specified

### MOBILE-FEATURE-005: WebView Bridge Discipline
**Severity**: MEDIUM

- [ ] If a WebView is involved, every bridge method used is named and its parameters validated
- [ ] Session propagation and its security properties are specified
- [ ] Page-load failure has a native error surface with recovery

### MOBILE-FEATURE-006: Performance Of This Flow
**Severity**: MEDIUM

- [ ] Paging, prefetch, and image-loading behavior are specified where the flow is data-heavy
- [ ] The performance criterion states the device class or network condition it applies to
- [ ] Main-thread work in the platform processes is bounded

### MOBILE-FEATURE-007: Notification And Deep Link Entry
**Severity**: MEDIUM

- [ ] Flows reachable from a deep link or notification specify the cold-start path
- [ ] Authentication requirements on such entry are specified
- [ ] Invalid or expired link parameters have a defined behavior

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/FEATURE/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For every domain marked Narrowed or Inherited in the scope table, confirm the feature references the parent element or names the artifact that carries the content
- [ ] State the parity result explicitly: which processes are shared, which are per-platform, and which divergences are deliberate

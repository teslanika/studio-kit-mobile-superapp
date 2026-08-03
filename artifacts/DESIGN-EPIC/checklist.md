# DESIGN-EPIC Checklist — Layer Delta

**Artifact**: DESIGN-EPIC
**Kit**: mobile-superapp
**Level**: L2 (Epic)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/DESIGN/checklist.md` (sdlc DESIGN Expert Checklist)

This checklist is a **delta over the sdlc DESIGN Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a DESIGN-EPIC document; this file states how each expertise domain is scoped at the epic layer and adds the criteria that exist only at this layer.

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

1. **LOAD the base checklist first** and apply it in full: Referenced Standards, Review Scope Selection, Prerequisites, Evidence Requirements (STRICT mode), Applicability Context, Severity Dictionary, all MUST HAVE domains (ARCH, SEM, PERF, SEC, REL, DATA, INT, OPS, MAINT, TEST, COMPL, UX, BIZ, DOC), and all MUST NOT HAVE items.
2. **Apply the domain scope table** below. Where a domain is marked *Inherited*, the epic design satisfies it by referencing the MiniApp or platform element by ID and documenting deviations only — restating it violates `DESIGN-EPIC-NO-001`, omitting it without a reference violates base `DOC-DESIGN-001`.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report citing base IDs (`ARCH-DESIGN-002`) and delta IDs (`DESIGN-EPIC-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L2 (Epic) | Notes |
|--------|--------------------|-------|
| ARCH | Narrowed | Screen/flow component structure only; module and platform architecture are inherited |
| SEM | Full | Every epic PRD requirement, state, widget, and error condition must map to a design element |
| PERF | Narrowed | Screen-level budgets (time to interactive, list rendering, payload size) |
| SEC | Narrowed | Authorization checks for this screen's actions and handling of sensitive fields shown here |
| REL | Full | Error detection, retry, offline behavior, and state restoration for this screen are owned here |
| DATA | Narrowed | Which MiniApp entities and operations this epic uses, plus epic-local caching |
| INT | Narrowed | Endpoints this epic calls, via MiniApp contracts |
| OPS | Narrowed | Feature gating and rollout of this epic only |
| MAINT | Narrowed | Component boundaries and reuse of design-system components |
| TEST | Narrowed | Verification approach per NFR and per state; test cases are deferred to FEATURE/code |
| COMPL | Inherited | Reference the inherited obligation; add only what this screen's data or consent introduces |
| UX | Full | Screen composition, states, interactions, and accessibility realization are owned here |
| BIZ | Inherited | Business goals are referenced from the PRD, never restated |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

*Deferred* domains name their target artifact: TEST → `FEATURE-MOBILE`.

---

## Layer Delta: MUST HAVE

### DESIGN-EPIC-001: Parent Design Inheritance
**Severity**: CRITICAL

- [ ] Parent MiniApp design is linked; inherited module structure, entities, repositories, and navigation graph are referenced by MiniApp ID
- [ ] Inherited NFRs are listed, deviations documented and justified
- [ ] Every referenced parent ID exists in the parent document (verified, not assumed)

### DESIGN-EPIC-002: PRD Realization Completeness
**Severity**: CRITICAL

- [ ] Every PRD FR appears in the functional drivers table with a design response
- [ ] Every PRD state requirement maps to a modelled state value with its entry condition
- [ ] Every PRD widget ID appears as a component here, reusing the same ID
- [ ] Every PRD error condition has a detection mechanism and a UI response
- [ ] Every PRD entry point (navigation, deep link, notification) is realized

### DESIGN-EPIC-003: Component Contract
**Severity**: CRITICAL

- [ ] Each screen and widget component is documented with the base component contract (why it exists, responsibility scope, responsibility boundaries, technology and location, related components by ID)
- [ ] All three targets (shared, Android, iOS) are named with source locations, or divergence is justified
- [ ] UI components never access repositories directly

### DESIGN-EPIC-004: State Contracts
**Severity**: CRITICAL

- [ ] State, intent, and effect types are given as signatures
- [ ] Every state value is reachable and every intent has a defined reduction
- [ ] State restoration across configuration change and process death is specified
- [ ] The state model is consistent with the MiniApp state pattern

### DESIGN-EPIC-005: Data Flow
**Severity**: HIGH

- [ ] Use cases list input, output, and the repository operations they invoke
- [ ] Repository operations state source and caching behavior
- [ ] Endpoints used are traced to the owning MiniApp contract
- [ ] At least one sequence diagram covers the primary flow including its failure branch

### DESIGN-EPIC-006: Navigation Realization
**Severity**: HIGH

- [ ] Entry and exit points are enumerated with their triggers
- [ ] Navigation parameters state type, requiredness, validation, and invalid-input behavior
- [ ] Back/dismiss behavior including unsaved state is specified

### DESIGN-EPIC-007: Error And Offline Design
**Severity**: HIGH

- [ ] Each error condition maps detection → state → recovery action
- [ ] Offline capability is stated and consistent with the MiniApp offline policy
- [ ] Queued writes name the queue and the conflict-resolution behavior

### DESIGN-EPIC-008: Traceability And Coverage
**Severity**: HIGH

- [ ] Links to the epic PRD, MiniApp DESIGN, ADR folder, DECOMPOSITION, and features folder are present
- [ ] The requirement coverage table maps FRs, states, widgets, and NFRs to design elements by ID
- [ ] Matrix rows are consistent with the section bodies

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### DESIGN-EPIC-NO-001: No Parent Design Duplication
**Severity**: HIGH

**What to check**:
- [ ] No redefined MiniApp module structure, domain entities, or repository interfaces
- [ ] No restated platform layers, kernel internals, or navigation graph
- [ ] No re-derivation of inherited NFR thresholds beyond a reference

**Where it belongs**: `DESIGN-MINIAPP` / `DESIGN-PLATFORM` — reference by ID

### DESIGN-EPIC-NO-002: No Implementation Bodies
**Severity**: HIGH

**What to check**:
- [ ] Code blocks are signatures, state contracts, or schemas only
- [ ] No reducer bodies, algorithms, or copy-pasted production code

**Where it belongs**: code, `FEATURE-MOBILE` (flow specification)

### DESIGN-EPIC-NO-003: No Design-System Values
**Severity**: MEDIUM

**What to check**:
- [ ] No color, spacing, font, or token values
- [ ] No pixel measurements or animation curve values

**Where it belongs**: the design system

### DESIGN-EPIC-NO-004: No Product Requirements
**Severity**: HIGH

**What to check**:
- [ ] No business requirements, user stories, or acceptance criteria
- [ ] No requirement priorities re-litigated here

**Where it belongs**: `PRD-EPIC`

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-DESIGN-EPIC-001: Platform Divergence
**Severity**: MEDIUM

- [ ] Android and iOS implementations are named per component, with divergence justified
- [ ] Lifecycle handling is specified per platform (configuration change, scene phases, back gesture)

### MOBILE-DESIGN-EPIC-002: WebView Integration
**Severity**: MEDIUM

- [ ] If WebView is used, URL, bridge methods, and both event directions are specified
- [ ] Session propagation into the page and its security properties are specified

### MOBILE-DESIGN-EPIC-003: Accessibility Realization
**Severity**: HIGH

- [ ] Screen-reader semantics are specified per interactive component
- [ ] Font-scaling and layout-reflow behavior is specified
- [ ] Focus order and touch-target compliance are specified

### MOBILE-DESIGN-EPIC-004: Performance Of This Screen
**Severity**: MEDIUM

- [ ] Eager vs lazy loading and paging strategy for lists are specified
- [ ] Image/media loading and caching strategy is specified
- [ ] Recomposition / view-update concerns are addressed where the screen is data-heavy

### MOBILE-DESIGN-EPIC-005: Feature Gating
**Severity**: LOW

- [ ] Feature flags for this epic are named with default and removal condition
- [ ] The gated-off fallback experience is specified

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/DESIGN/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, Evidence Requirements, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For every domain marked Narrowed, Deferred, or Inherited in the scope table, confirm the design references the parent element or names the artifact that carries the deferred content

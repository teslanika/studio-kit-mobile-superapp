# DECOMPOSITION-EPIC Checklist — Layer Delta

**Artifact**: DECOMPOSITION-EPIC
**Kit**: mobile-superapp
**Level**: L2 (Epic)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md` (sdlc DECOMPOSITION Expert Checklist)

This checklist is a **delta over the sdlc DECOMPOSITION Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a DECOMPOSITION-EPIC document; this file states how each expertise domain is scoped at the epic layer and adds the criteria that exist only at this layer.

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

1. **LOAD the base checklist first** and apply it in full: Referenced Standards, Prerequisites, Applicability Context, Severity Dictionary, Checkpointing, all MUST HAVE domains (COV, EXC, ATTR, LEV, CFG, TRC, DEP, CHK, DOC, FMT), and all MUST NOT HAVE items.
2. **Apply the domain scope table** below. This is the layer where the base checklist's "feature" vocabulary applies literally.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report citing base IDs (`COV-001`) and delta IDs (`DECOMP-EPIC-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L2 (Epic) | Notes |
|--------|--------------------|-------|
| COV | Full | Every epic design component, widget, use case, sequence, and cache must be assigned to a feature |
| EXC | Full | Feature scopes must be mutually exclusive at widget and use-case granularity |
| ATTR | Full | Each feature entry needs ID, purpose, scope, dependencies, and its platform implementation targets |
| LEV | Full | Decomposition stops at the feature; FEATURE-MOBILE specifies the inside of a feature |
| CFG | Narrowed | A feature is a change-control unit inside the epic, not a release unit |
| TRC | Full | Forward to FEATURE-MOBILE and code, backward to epic PRD/DESIGN and up to the MiniApp DECOMPOSITION entry |
| DEP | Full | Feature dependency graph must be a DAG; the foundation feature has no dependencies |
| CHK | Full | `status-overall` cascades from all `feature` entries |
| DOC | Full | Explicit non-applicability is mandatory at every layer |
| FMT | Full | Entry format, required fields, and checkbox syntax as in the base |

*Narrowed* domains inherit the platform disposition: CFG release-unit criteria are satisfied at L0 by `DECOMPOSITION-PLATFORM`.

---

## Layer Delta: MUST HAVE

### DECOMP-EPIC-001: Parent Scope Consistency
**Severity**: CRITICAL

- [ ] The parent MiniApp DECOMPOSITION entry for this epic is linked
- [ ] No feature here extends beyond the scope the MiniApp decomposition assigned to this epic
- [ ] Anything that exceeds that scope is raised as a change to the parent, not silently added

### DECOMP-EPIC-002: Design Element Assignment Completeness
**Severity**: CRITICAL

- [ ] Every DESIGN-EPIC component, widget, use case, sequence, and cache appears in the Coverage Matrix with an owning feature
- [ ] Epic principles and constraints are assigned to the features that must honour them
- [ ] Unassigned elements are listed with a reason (screen-shell, deferred, out of scope)

### DECOMP-EPIC-003: Requirement And State Coverage
**Severity**: CRITICAL

- [ ] Every epic PRD FR is covered by at least one feature
- [ ] Every PRD state requirement (loading, empty, error, offline) is covered by a feature, not left implicit
- [ ] Every PRD widget ID appears under a feature's Design Components, reusing the same ID

### DECOMP-EPIC-004: ID Reuse, Not Re-Minting
**Severity**: HIGH

- [ ] Component, widget, and use case references reuse the IDs minted in PRD-EPIC and DESIGN-EPIC
- [ ] No element is given a second ID in this document
- [ ] Only `feature` and `status` IDs are newly defined here

### DECOMP-EPIC-005: Feature Independence
**Severity**: HIGH

- [ ] Each feature can be implemented and verified on its own once its dependencies are met
- [ ] No feature requires a later feature to be demonstrable
- [ ] Features that cannot stand alone are merged or their dependency is made explicit

### DECOMP-EPIC-006: Platform Implementation Map
**Severity**: HIGH

- [ ] Each feature names its shared, Android, and iOS targets with source locations, or justifies the divergence
- [ ] The Platform Implementation Matrix agrees with the per-entry tables
- [ ] Shared logic is not duplicated across the Android and iOS rows

### DECOMP-EPIC-007: Implementation Order
**Severity**: MEDIUM

- [ ] Implementation Order agrees with the dependency graph
- [ ] Phase 1 contains at least one feature with no dependencies
- [ ] Features that can run in parallel are identified as such

### DECOMP-EPIC-008: Traceability Links
**Severity**: HIGH

- [ ] Links to epic PRD, epic DESIGN, and the MiniApp DECOMPOSITION are present
- [ ] Each entry links to its feature folder path
- [ ] Coverage Matrix rows are consistent with the entry bodies
- [ ] The Acceptance Criteria Summary references criteria that exist in the epic PRD

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### DECOMP-EPIC-NO-001: No Feature Internals
**Severity**: HIGH

**What to check**:
- [ ] No CDSL flows, step-by-step business logic, or algorithms
- [ ] No Definition of Done, test cases, or QA scripts per feature

**Where it belongs**: `FEATURE-MOBILE`

### DECOMP-EPIC-NO-002: No Epic Design Restatement
**Severity**: MEDIUM

**What to check**:
- [ ] No restated state contracts, intents, or effects
- [ ] No re-derived navigation parameters or error tables

**Where it belongs**: `DESIGN-EPIC` — reference by ID

### DECOMP-EPIC-NO-003: No Requirements Definition
**Severity**: HIGH

**What to check**:
- [ ] No new FRs, state requirements, or acceptance criteria authored here
- [ ] Requirement priorities are not re-litigated

**Where it belongs**: `PRD-EPIC`

### DECOMP-EPIC-NO-004: No Visual Or Token Detail
**Severity**: LOW

**What to check**:
- [ ] No colors, spacing, typography, or animation values
- [ ] No pixel measurements

**Where it belongs**: the design system

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-DECOMP-EPIC-001: Per-Platform Delivery Sequencing
**Severity**: MEDIUM

- [ ] The order states whether shared logic lands before, with, or after each platform UI
- [ ] Any deliberate Android-first or iOS-first sequencing is stated with the reason

### MOBILE-DECOMP-EPIC-002: Offline And Cache Features
**Severity**: MEDIUM

- [ ] Features that introduce local caching or offline behavior are identified and list their data stores
- [ ] Cache invalidation ownership is assigned to a feature, not left unassigned

### MOBILE-DECOMP-EPIC-003: Accessibility As Feature Scope
**Severity**: HIGH

- [ ] Accessibility realization is inside feature scope, not deferred to a separate cleanup feature
- [ ] Any accessibility work that genuinely needs its own feature is justified

### MOBILE-DECOMP-EPIC-004: Feature Gating Assignment
**Severity**: LOW

- [ ] Features behind a flag name the flag and its default
- [ ] The gated-off behavior is assigned to a feature's scope

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] State the coverage result explicitly: number of epic design elements, number assigned, number documented as excluded
- [ ] Confirm the parent MiniApp DECOMPOSITION scope was checked, and report any feature that exceeds it

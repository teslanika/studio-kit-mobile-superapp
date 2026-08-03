# DECOMPOSITION-MINIAPP Checklist — Layer Delta

**Artifact**: DECOMPOSITION-MINIAPP
**Kit**: mobile-superapp
**Level**: L1 (MiniApp)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md` (sdlc DECOMPOSITION Expert Checklist)

This checklist is a **delta over the sdlc DECOMPOSITION Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a DECOMPOSITION-MINIAPP document; this file states how each expertise domain is scoped at the MiniApp layer and adds the criteria that exist only at this layer.

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
2. **Apply the domain scope table** below. The decomposition entity at this layer is an **epic** (screen, capability, or flow), not a feature — read every base criterion that says "feature" as applying to an epic entry.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report citing base IDs (`EXC-001`) and delta IDs (`DECOMP-MINIAPP-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L1 (MiniApp) | Notes |
|--------|-----------------------|-------|
| COV | Full | Every MiniApp design component, entity, repository operation, sequence, and data store must be assigned to an epic |
| EXC | Full | Epic scopes must be mutually exclusive; a shared widget belongs to one owning epic and is referenced by the others |
| ATTR | Full | Each entry needs ID, category (Screen/Capability/Flow), purpose, actors, scope, and subordinates |
| LEV | Full | Decomposition stops at the epic; features are the next level down |
| CFG | Narrowed | An epic is a change-control unit inside the MiniApp, not an independently releasable binary |
| TRC | Full | Forward to epic PRD/DESIGN, backward to MiniApp PRD/DESIGN and up to the Platform DECOMPOSITION entry |
| DEP | Full | Epic dependency graph must be a DAG; entry-point epics have no epic dependencies |
| CHK | Full | `status-overall` cascades from all `epic` entries |
| DOC | Full | Explicit non-applicability is mandatory at every layer |
| FMT | Full | Entry format, required fields, and checkbox syntax as in the base |

*Narrowed* domains inherit the platform disposition: CFG release-unit criteria are satisfied at L0 by `DECOMPOSITION-PLATFORM`.

---

## Layer Delta: MUST HAVE

### DECOMP-MINIAPP-001: Parent Scope Consistency
**Severity**: CRITICAL

- [ ] The parent Platform DECOMPOSITION entry for this MiniApp is linked
- [ ] No epic here extends beyond the scope the platform decomposition assigned to this MiniApp
- [ ] Anything that exceeds that scope is raised as a change to the parent, not silently added

### DECOMP-MINIAPP-002: Entry Category Assignment
**Severity**: HIGH

- [ ] Each entry is classified as exactly one of Screen, Capability, or Flow
- [ ] Screen entries correspond to destinations in the MiniApp navigation graph
- [ ] Capability entries are cross-cutting and name the screens that consume them
- [ ] Flow entries name their entry and exit points

### DECOMP-MINIAPP-003: Navigation Graph Coverage
**Severity**: CRITICAL

- [ ] Every destination in the MiniApp navigation graph is covered by exactly one Screen epic
- [ ] Every epic states its Entry Points (navigation, deep link, or notification)
- [ ] Deep links referenced here exist in the MiniApp DESIGN deep-link table

### DECOMP-MINIAPP-004: Actors From The Platform
**Severity**: HIGH

- [ ] Each entry names its actors as `cpt-superapp-actor-{slug}`
- [ ] No actor is defined or renamed in this document
- [ ] Every actor served by this MiniApp appears in at least one entry

### DECOMP-MINIAPP-005: Design Element Assignment Completeness
**Severity**: CRITICAL

- [ ] Every DESIGN-MINIAPP component, domain entity, sequence, and data store appears in the Coverage Matrix with an owning epic
- [ ] MiniApp principles and constraints are assigned to the epics that must honour them
- [ ] Unassigned elements are listed with a reason (module-internal, deferred, out of scope)

### DECOMP-MINIAPP-006: Platform Coverage Declared
**Severity**: HIGH

- [ ] Every entry declares Platform Coverage (shared / Android / iOS)
- [ ] An entry planned for only one platform states the reason and the parity plan
- [ ] Shared-only coverage with no UI target is challenged

### DECOMP-MINIAPP-007: Implementation Order
**Severity**: MEDIUM

- [ ] Implementation Order agrees with the dependency graph
- [ ] Phase 1 contains at least one entry-point epic with no dependencies
- [ ] Target releases per entry are consistent with the phase table

### DECOMP-MINIAPP-008: Traceability Links
**Severity**: HIGH

- [ ] Links to MiniApp PRD, MiniApp DESIGN, and the Platform DECOMPOSITION are present
- [ ] Each entry links to its epic folder path
- [ ] Coverage Matrix rows are consistent with the entry bodies

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### DECOMP-MINIAPP-NO-001: No Feature-Level Decomposition
**Severity**: HIGH

**What to check**:
- [ ] No feature entries, task lists, or per-widget breakdown inside an epic entry
- [ ] No Definition of Done or acceptance criteria per feature

**Where it belongs**: `DECOMPOSITION-EPIC`

### DECOMP-MINIAPP-NO-002: No MiniApp Design Restatement
**Severity**: MEDIUM

**What to check**:
- [ ] No redefined module structure, domain entities, repositories, or navigation graph
- [ ] No re-derived NFR thresholds beyond a reference

**Where it belongs**: `DESIGN-MINIAPP` — reference by ID

### DECOMP-MINIAPP-NO-003: No Screen Composition Or Visual Detail
**Severity**: MEDIUM

**What to check**:
- [ ] No widget layouts, states, or interaction specification
- [ ] No colors, spacing, or design tokens

**Where it belongs**: `PRD-EPIC` / `DESIGN-EPIC` and the design system

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-DECOMP-MINIAPP-001: Offline Scope Per Epic
**Severity**: MEDIUM

- [ ] Epics that must work offline are identified and consistent with the MiniApp offline policy
- [ ] Their local data stores are listed in the entry's Data field

### MOBILE-DECOMP-MINIAPP-002: Notification-Triggered Epics
**Severity**: MEDIUM

- [ ] Epics reachable from a push notification declare it as an entry point
- [ ] The cold-start path into such an epic is acknowledged as in scope

### MOBILE-DECOMP-MINIAPP-003: WebView Epics Flagged
**Severity**: MEDIUM

- [ ] Epics realized wholly or partly in WebView are flagged
- [ ] Their native-shell responsibilities (navigation, session, error surface) are stated as in scope

### MOBILE-DECOMP-MINIAPP-004: Delivery Sequencing Across Platforms
**Severity**: LOW

- [ ] The implementation order states whether shared logic lands before, with, or after each platform UI
- [ ] Any deliberate Android-first or iOS-first sequencing is stated with the reason

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] State the coverage result explicitly: number of MiniApp design elements, number assigned, number documented as excluded
- [ ] Confirm the parent Platform DECOMPOSITION scope was checked, and report any epic that exceeds it

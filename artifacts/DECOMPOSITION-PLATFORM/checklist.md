# DECOMPOSITION-PLATFORM Checklist — Layer Delta

**Artifact**: DECOMPOSITION-PLATFORM
**Kit**: mobile-superapp
**Level**: L0 (Platform / Host App)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md` (sdlc DECOMPOSITION Expert Checklist)

This checklist is a **delta over the sdlc DECOMPOSITION Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a DECOMPOSITION-PLATFORM document; this file states how each expertise domain is scoped at the platform layer and adds the criteria that exist only at this layer.

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
2. **Apply the domain scope table** below. The decomposition entity at this layer is a **MiniApp**, not a feature — read every base criterion that says "feature" as applying to a MiniApp entry.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report citing base IDs (`COV-001`) and delta IDs (`DECOMP-PLATFORM-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L0 (Platform) | Notes |
|--------|------------------------|-------|
| COV | Full | Every platform design component, kernel contract, integration, sequence, and data store must be assigned to a MiniApp or to the shared kernel |
| EXC | Full | MiniApp scopes must be mutually exclusive; shared capability belongs to the kernel |
| ATTR | Full | Each MiniApp entry needs ID, type, purpose, scope, and subordinates (its epics, named or planned) |
| LEV | Full | Decomposition stops at the MiniApp; epics are the next level down |
| CFG | Full | Each MiniApp is a configuration item — independently versioned and releasable |
| TRC | Full | Forward to MiniApp PRD/DESIGN, backward to Platform PRD/DESIGN |
| DEP | Full | MiniApp dependency graph must be a DAG; kernel-only dependencies are the baseline |
| CHK | Full | `status-overall` cascades from all `miniapp` entries |
| DOC | Full | Explicit non-applicability is mandatory at every layer |
| FMT | Full | Entry format, required fields, and checkbox syntax as in the base |

No domain is deferred at this layer: the platform decomposition is the only artifact that assigns platform-level design elements to owners.

---

## Layer Delta: MUST HAVE

### DECOMP-PLATFORM-001: MiniApp Boundary Justification
**Severity**: CRITICAL

- [ ] Each MiniApp boundary is justified by user role, domain cohesion, or release independence — not by team structure
- [ ] Two MiniApps that always ship together and share the same users are challenged as a single MiniApp
- [ ] Each MiniApp can be developed, released, and activated independently, or the coupling is documented

### DECOMP-PLATFORM-002: Kernel vs MiniApp Allocation
**Severity**: CRITICAL

- [ ] Every capability used by more than one MiniApp is allocated to the kernel, not duplicated per MiniApp
- [ ] The Shared Kernel Coverage table lists each kernel component and the MiniApps that consume it
- [ ] Each entry lists the kernel contracts it consumes by `cpt-{prefix}-contract-{slug}`
- [ ] No MiniApp is listed as owning a kernel component

### DECOMP-PLATFORM-003: Deep Link Namespace Uniqueness
**Severity**: HIGH

- [ ] Each MiniApp declares a deep link namespace `{scheme}://{miniapp}/*`
- [ ] Namespaces are unique across all MiniApps and match the platform routing design
- [ ] The scheme matches the one registered in DESIGN-PLATFORM

### DECOMP-PLATFORM-004: Target Users Per MiniApp
**Severity**: HIGH

- [ ] Each MiniApp names its target users by `cpt-{prefix}-actor-{slug}` from the Platform PRD
- [ ] Every platform actor is served by at least one MiniApp, or the gap is documented
- [ ] No actor is invented here

### DECOMP-PLATFORM-005: Design Element Assignment Completeness
**Severity**: CRITICAL

- [ ] Every DESIGN-PLATFORM component, integration, sequence, and data store appears in the Coverage Matrix with an owner
- [ ] Platform principles and constraints are assigned to the MiniApps that must honour them
- [ ] Unassigned elements are listed with a reason (kernel-internal, deferred, out of scope)

### DECOMP-PLATFORM-006: Release Roadmap Consistency
**Severity**: MEDIUM

- [ ] Each MiniApp has a target release and the roadmap table agrees with the per-entry values
- [ ] Roadmap ordering does not violate the dependency graph
- [ ] The MVP release is identified and is self-sufficient (its MiniApps depend only on the kernel and on each other)

### DECOMP-PLATFORM-007: Traceability Links
**Severity**: HIGH

- [ ] Links to Platform PRD and Platform DESIGN are present
- [ ] Each entry links to its MiniApp folder path
- [ ] Coverage Matrix rows are consistent with the entry bodies

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### DECOMP-PLATFORM-NO-001: No Epic-Level Decomposition
**Severity**: HIGH

**What to check**:
- [ ] No screens, flows, or capabilities enumerated inside a MiniApp entry beyond a scope statement
- [ ] No navigation graphs or screen inventories

**Where it belongs**: `DECOMPOSITION-MINIAPP`

### DECOMP-PLATFORM-NO-002: No Platform Design Restatement
**Severity**: MEDIUM

**What to check**:
- [ ] No redefined platform layers, kernel internals, or container model
- [ ] No re-derived NFR thresholds beyond a reference

**Where it belongs**: `DESIGN-PLATFORM` — reference by ID

### DECOMP-PLATFORM-NO-003: No Team Or Estimate Planning
**Severity**: MEDIUM

**What to check**:
- [ ] No story points, sprint assignments, or team names
- [ ] No developer-level task breakdown

**Where it belongs**: the project plan / issue tracker

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-DECOMP-PLATFORM-001: Store Release Unit Awareness
**Severity**: MEDIUM

- [ ] The roadmap states whether each MiniApp ships inside the host app binary or is remotely activated
- [ ] MiniApps that require a store submission are distinguished from those gated by a feature flag

### MOBILE-DECOMP-PLATFORM-002: Platform Parity Of The Decomposition
**Severity**: MEDIUM

- [ ] Any MiniApp planned for only one of Android/iOS is flagged with the reason and the parity plan
- [ ] The roadmap does not silently assume simultaneous delivery on both platforms

### MOBILE-DECOMP-PLATFORM-003: Offline And Notification Ownership
**Severity**: MEDIUM

- [ ] MiniApps that require offline capability or push notifications are identified
- [ ] The supporting kernel contracts are listed among their consumed contracts

### MOBILE-DECOMP-PLATFORM-004: Binary Footprint Consideration
**Severity**: LOW

- [ ] MiniApps that materially affect app size or startup time are flagged
- [ ] Any resulting modularization or on-demand delivery need is stated as a dependency on DESIGN-PLATFORM

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] State the coverage result explicitly: number of platform design elements, number assigned, number documented as excluded

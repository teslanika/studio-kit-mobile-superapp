# IMPL-KMP Checklist — Layer Delta

**Artifact**: IMPL-KMP
**Kit**: mobile-superapp
**Target**: KMP shared (`constructor-sdk/feature/{miniapp}/`)
**Base Checklist**: `{cf-studio-path}/config/kits/mobile-superapp/codebase/checklist.md`

This checklist is a **delta over the mobile SuperApp code checklist**, not a replacement. The base itself layers over `{cf-studio-path}/.core/requirements/code-checklist.md` (generic code quality) and `{cf-studio-path}/config/kits/sdlc/codebase/checklist.md` (semantic alignment, SEM-CODE-001..007), so loading the base loads the whole chain.

This file adds the criteria that apply to the **implementation-reference document** itself and narrows the base's code criteria to the shared target.

---

## Table of Contents

1. [How To Use This Checklist](#how-to-use-this-checklist)
2. [Code Criteria Scope At This Target](#code-criteria-scope-at-this-target)
3. [Layer Delta: MUST HAVE](#layer-delta-must-have)
4. [Layer Delta: MUST NOT HAVE](#layer-delta-must-not-have)
5. [Layer Delta: KMP-Specific Criteria](#layer-delta-kmp-specific-criteria)
6. [Reporting](#reporting)

---

## How To Use This Checklist

1. **LOAD the base checklist first** — `config/kits/mobile-superapp/codebase/checklist.md` — and apply it in full, including the generic and semantic bases it loads.
2. **Apply the scope table** below: which base delta sections are in force for shared code, and which belong to the platform IMPL artifacts.
3. **Apply the delta criteria** in this file to the IMPL-KMP document.
4. **Report once**, in the base report format, citing generic, SEM-CODE, base-delta (`KMP-001`), and this file's IDs (`IMPL-KMP-001`) in the same finding field.

Severity values are the base checklists': CRITICAL, HIGH, MEDIUM, LOW.

---

## Code Criteria Scope At This Target

| Base delta section | Scope for IMPL-KMP |
|--------------------|--------------------|
| Delta: KMP Shared Code (`KMP-001..006`) | Full — this is the owning target |
| Delta: Android Code (`ANDROID-*`) | Out of scope — see `IMPL-ANDROID` |
| Delta: iOS Code (`IOS-*`) | Out of scope — see `IMPL-IOS` |
| Delta: WebView Bridge Code (`WEBVIEW-*`) | Out of scope unless a shared process owns bridge payload construction |
| Delta: Mobile Performance (`MOBILE-PERF-*`) | Full for network and memory; UI thread criteria apply at the platform targets |
| Delta: Mobile Security (`MOBILE-SEC-*`) | Full — token handling, storage, and input validation in shared code |
| Semantic Alignment (`SEM-CODE-001..007`) | Full, restricted to processes whose Target is KMP shared |

---

## Layer Delta: MUST HAVE

### IMPL-KMP-001: Overview And Module Identity
**Severity**: MEDIUM

- [ ] The module path is stated and matches the DECOMPOSITION platform implementation table
- [ ] The document states that it is a reference map, not a design or coding guide
- [ ] Version and status are present

### IMPL-KMP-002: References Resolve
**Severity**: CRITICAL

- [ ] FEATURE-MOBILE, Epic DESIGN, MiniApp DESIGN, and Platform DESIGN rows are present
- [ ] Every path resolves and every ID exists (`cfs list-ids`)
- [ ] IDs use the `cpt-{hierarchy-prefix}-{kind}-{slug}` scheme

### IMPL-KMP-003: Scope Declares Target Ownership
**Severity**: HIGH

- [ ] Scope lists what this module implements in terms of shared-target processes and shared components
- [ ] Out-of-scope names `IMPL-ANDROID`, `IMPL-IOS`, and the kernel contracts consumed
- [ ] No Android- or iOS-target process appears in scope

### IMPL-KMP-004: Traceability Table Completeness
**Severity**: CRITICAL

- [ ] Every process whose Target is KMP shared has at least one row
- [ ] Every row's design ID exists and every code file path exists
- [ ] Every row's marker is present in that code file, in the format from the traceability spec
- [ ] No code file in the module implements a design element without a row

### IMPL-KMP-005: Directory Structure Accuracy
**Severity**: MEDIUM

- [ ] The tree matches the module on disk, including the `commonMain` / `androidMain` / `iosMain` / `commonTest` split
- [ ] Planned-but-absent directories are marked as planned

### IMPL-KMP-006: Marker Format Correctness
**Severity**: HIGH

- [ ] FULL mode examples use `@cpt-{kind}:{cpt-id}:p{N}` scope markers and paired `@cpt-begin` / `@cpt-end` block markers
- [ ] DOCS-ONLY mode is stated to use `@cpt-impl {cpt-id}`
- [ ] The mode this module operates in is stated

### IMPL-KMP-007: Dependencies And Kernel Contracts
**Severity**: HIGH

- [ ] Every kernel service the module consumes is listed with its purpose
- [ ] No kernel capability is reimplemented inside the feature module
- [ ] No dependency on `android-app/` or `ios-app/` appears

### IMPL-KMP-008: Validation Commands Present
**Severity**: MEDIUM

- [ ] `cfs validate --artifact` for this module path is stated
- [ ] The build and test commands for `:constructor-sdk` are stated
- [ ] Lint commands are stated

### IMPL-KMP-009: Implementation Notes Substance
**Severity**: MEDIUM

- [ ] Every deviation from the design is stated with its reason
- [ ] Every `expect`/`actual` boundary is named with why it is platform-specific
- [ ] The section is not left as a placeholder

---

## Layer Delta: MUST NOT HAVE

### IMPL-KMP-NO-001: No Full Implementation Code
**Severity**: HIGH

- [ ] No complete class or function bodies beyond short marker illustrations

**Where it belongs**: the source files

### IMPL-KMP-NO-002: No Unresolvable References
**Severity**: CRITICAL

- [ ] No design ID that `cfs list-ids` cannot find
- [ ] No file path that does not exist

**Where it belongs**: fix the reference, or add the design element first

### IMPL-KMP-NO-003: No Architecture Definitions
**Severity**: HIGH

- [ ] No module boundary, layering, or API contract definitions

**Where it belongs**: `DESIGN-MINIAPP` / `DESIGN-PLATFORM`

### IMPL-KMP-NO-004: No Platform-Target Content
**Severity**: MEDIUM

- [ ] No Compose or SwiftUI content, no per-platform UI mapping

**Where it belongs**: `IMPL-ANDROID` / `IMPL-IOS`

### IMPL-KMP-NO-005: No Coding Conventions
**Severity**: LOW

- [ ] No naming, formatting, or DI wiring instructions

**Where it belongs**: the project `AGENTS.md`

---

## Layer Delta: KMP-Specific Criteria

### MOBILE-IMPL-KMP-001: Module Structure Conformance
**Severity**: HIGH

- [ ] `domain/`, `data/`, and `presentation/` are separated as designed
- [ ] `domain/` has no dependency on `data/` implementations
- [ ] Test sources exist under `commonTest/`

### MOBILE-IMPL-KMP-002: Use Case Mapping
**Severity**: HIGH

- [ ] Every use case in the Epic DESIGN has exactly one shared implementation row
- [ ] No use case is implemented twice, once per platform

### MOBILE-IMPL-KMP-003: ViewModel And State Mapping
**Severity**: HIGH

- [ ] The ViewModel, State, Intent, and Effect files are mapped to the design component and state IDs
- [ ] The state file implements the state machine from FEATURE-MOBILE section 4

### MOBILE-IMPL-KMP-004: Repository And Cache Mapping
**Severity**: HIGH

- [ ] Every repository operation in the Epic DESIGN has a row
- [ ] Cache, staleness, and offline-fallback behavior is mapped to the repository process, not to platform code

### MOBILE-IMPL-KMP-005: Entity Mapping
**Severity**: MEDIUM

- [ ] Every domain entity this feature touches has a row referencing the MiniApp DESIGN entity ID
- [ ] No entity is redefined here

### MOBILE-IMPL-KMP-006: Platform Actual Coverage
**Severity**: MEDIUM

- [ ] Every `expect` declaration has an `actual` for both Android and iOS, or the missing target is documented as planned
- [ ] No `if (platform)` branching substitutes for an `expect`/`actual` boundary

---

## Reporting

Use the **base checklist's Reporting section** — `config/kits/mobile-superapp/codebase/checklist.md` — without modification.

Additional reporting requirements for this artifact:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the traceability mode and the shared-target marker coverage percentage
- [ ] List unmapped shared-target processes and unmapped code files explicitly as coverage gaps

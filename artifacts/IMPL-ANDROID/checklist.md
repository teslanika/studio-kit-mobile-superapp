# IMPL-ANDROID Checklist — Layer Delta

**Artifact**: IMPL-ANDROID
**Kit**: mobile-superapp
**Target**: Android (`android-app/feature/{miniapp}/`)
**Base Checklist**: `{cf-studio-path}/config/kits/mobile-superapp/codebase/checklist.md`

This checklist is a **delta over the mobile SuperApp code checklist**, not a replacement. The base itself layers over `{cf-studio-path}/.core/requirements/code-checklist.md` (generic code quality) and `{cf-studio-path}/config/kits/sdlc/codebase/checklist.md` (semantic alignment, SEM-CODE-001..007), so loading the base loads the whole chain.

This file adds the criteria that apply to the **implementation-reference document** itself and narrows the base's code criteria to the Android target.

---

## Table of Contents

1. [How To Use This Checklist](#how-to-use-this-checklist)
2. [Code Criteria Scope At This Target](#code-criteria-scope-at-this-target)
3. [Layer Delta: MUST HAVE](#layer-delta-must-have)
4. [Layer Delta: MUST NOT HAVE](#layer-delta-must-not-have)
5. [Layer Delta: Android-Specific Criteria](#layer-delta-android-specific-criteria)
6. [Reporting](#reporting)

---

## How To Use This Checklist

1. **LOAD the base checklist first** — `config/kits/mobile-superapp/codebase/checklist.md` — and apply it in full, including the generic and semantic bases it loads.
2. **Apply the scope table** below.
3. **Apply the delta criteria** in this file to the IMPL-ANDROID document.
4. **Report once**, in the base report format, citing generic, SEM-CODE, base-delta (`ANDROID-001`), and this file's IDs (`IMPL-ANDROID-001`) in the same finding field.

Severity values are the base checklists': CRITICAL, HIGH, MEDIUM, LOW.

---

## Code Criteria Scope At This Target

| Base delta section | Scope for IMPL-ANDROID |
|--------------------|------------------------|
| Delta: Android Code (`ANDROID-001..005`) | Full — this is the owning target |
| Delta: KMP Shared Code (`KMP-*`) | Out of scope — see `IMPL-KMP`; verify only that shared code is consumed, not duplicated |
| Delta: iOS Code (`IOS-*`) | Out of scope — see `IMPL-IOS`; used only for the parity check |
| Delta: WebView Bridge Code (`WEBVIEW-*`) | Full when this module hosts a WebView |
| Delta: Mobile Performance (`MOBILE-PERF-*`) | Full for UI and rendering; network criteria belong to the shared repository |
| Delta: Mobile Security (`MOBILE-SEC-*`) | Full for deep-link input validation, debug affordances, and logging |
| Semantic Alignment (`SEM-CODE-001..007`) | Full, restricted to processes whose Target is Android |

---

## Layer Delta: MUST HAVE

### IMPL-ANDROID-001: Overview And Module Identity
**Severity**: MEDIUM

- [ ] The module path is stated and matches the DECOMPOSITION platform implementation table
- [ ] The document states that it is a reference map, not a design or coding guide
- [ ] Version and status are present

### IMPL-ANDROID-002: References Resolve
**Severity**: CRITICAL

- [ ] FEATURE-MOBILE, Epic DESIGN, MiniApp DESIGN, and IMPL-KMP rows are present
- [ ] Every path resolves and every ID exists (`cfs list-ids`)
- [ ] IDs use the `cpt-{hierarchy-prefix}-{kind}-{slug}` scheme

### IMPL-ANDROID-003: Scope Declares Target Ownership
**Severity**: HIGH

- [ ] Scope lists the Android-target processes, screens, widgets, and navigation this module implements
- [ ] Out-of-scope names `IMPL-KMP` for business logic, `IMPL-IOS`, and the design system
- [ ] No shared-target process appears in scope

### IMPL-ANDROID-004: Traceability Table Completeness
**Severity**: CRITICAL

- [ ] Every process whose Target is Android has at least one row
- [ ] Every screen and widget assigned to Android in the Epic DESIGN has a row
- [ ] Every row's design ID exists, code file exists, and the marker is present in that file
- [ ] No composable implementing a design element is missing from the table

### IMPL-ANDROID-005: Navigation And Deep Links Mapped
**Severity**: HIGH

- [ ] Every navigation destination in the Epic DESIGN has a row pointing at the nav graph
- [ ] Every declared deep link is listed with its destination and its parameter validation
- [ ] The deep-link scheme matches the namespace assigned in DECOMPOSITION-PLATFORM

### IMPL-ANDROID-006: Directory Structure Accuracy
**Severity**: MEDIUM

- [ ] The tree matches the module on disk, including `ui/`, `navigation/`, `di/`, resources, and both test source sets
- [ ] Planned-but-absent directories are marked as planned

### IMPL-ANDROID-007: Marker Format Correctness
**Severity**: HIGH

- [ ] FULL mode examples use `@cpt-{kind}:{cpt-id}:p{N}` scope markers and paired `@cpt-begin` / `@cpt-end` block markers
- [ ] DOCS-ONLY mode is stated to use `@cpt-impl {cpt-id}`
- [ ] The mode this module operates in is stated

### IMPL-ANDROID-008: Dependencies Declared
**Severity**: HIGH

- [ ] The shared module dependency is listed and is the source of the ViewModel and use cases
- [ ] Design-system and navigation commons are listed
- [ ] No direct dependency on `ios-app/` and no feature-to-feature dependency that the design did not sanction

### IMPL-ANDROID-009: Validation Commands Present
**Severity**: MEDIUM

- [ ] `cfs validate --artifact` for this module path is stated
- [ ] `assembleDebug`, unit test, and UI test commands are stated
- [ ] `ktlintCheck` and `detekt` are stated

### IMPL-ANDROID-010: Implementation Notes Substance
**Severity**: MEDIUM

- [ ] Every deviation from the design is stated with its reason
- [ ] Compose and navigation decisions that a reader could not infer from the code layout are recorded
- [ ] The section is not left as a placeholder

---

## Layer Delta: MUST NOT HAVE

### IMPL-ANDROID-NO-001: No Full Implementation Code
**Severity**: HIGH

- [ ] No complete composable or class bodies beyond short marker illustrations

**Where it belongs**: the source files

### IMPL-ANDROID-NO-002: No Unresolvable References
**Severity**: CRITICAL

- [ ] No design ID that `cfs list-ids` cannot find
- [ ] No file path that does not exist

**Where it belongs**: fix the reference, or add the design element first

### IMPL-ANDROID-NO-003: No Architecture Definitions
**Severity**: HIGH

- [ ] No module boundary, layering, or API contract definitions

**Where it belongs**: `DESIGN-MINIAPP` / `DESIGN-PLATFORM`

### IMPL-ANDROID-NO-004: No Business Logic Mapping
**Severity**: HIGH

- [ ] No use case, repository, or domain rule documented as Android code

**Where it belongs**: `IMPL-KMP`

### IMPL-ANDROID-NO-005: No Design-System Values
**Severity**: MEDIUM

- [ ] No colors, spacing, typography, or animation values

**Where it belongs**: the design system

### IMPL-ANDROID-NO-006: No Coding Conventions
**Severity**: LOW

- [ ] No naming, formatting, or DI wiring instructions

**Where it belongs**: the project `AGENTS.md`

---

## Layer Delta: Android-Specific Criteria

### MOBILE-IMPL-ANDROID-001: Screen And Widget Mapping
**Severity**: HIGH

- [ ] Each screen composable maps to exactly one Epic DESIGN screen ID
- [ ] Each reusable widget maps to a widget ID, or is documented as feature-local and not a design element

### MOBILE-IMPL-ANDROID-002: Shared ViewModel Consumption
**Severity**: CRITICAL

- [ ] The screen consumes the shared ViewModel from `constructor-sdk/feature/{miniapp}`
- [ ] No Android-local ViewModel duplicates shared state or logic
- [ ] State collection is documented as lifecycle-aware

### MOBILE-IMPL-ANDROID-003: State Restoration Mapping
**Severity**: HIGH

- [ ] Configuration-change and process-death restoration is mapped to the state row
- [ ] The behavior matches FEATURE-MOBILE section 4

### MOBILE-IMPL-ANDROID-004: Accessibility Mapping
**Severity**: HIGH

- [ ] The file that carries semantics and content descriptions for the screen is identified
- [ ] Font-scaling and touch-target handling are noted where they required a decision

### MOBILE-IMPL-ANDROID-005: Resource And String Ownership
**Severity**: MEDIUM

- [ ] Feature strings live in the feature module, not in the app module
- [ ] No hardcoded user-visible string is documented as intentional

### MOBILE-IMPL-ANDROID-006: Parity With iOS
**Severity**: HIGH

- [ ] Every element mapped here has an `IMPL-IOS` counterpart, or the divergence is documented in both
- [ ] Deliberate divergences cite the FEATURE-MOBILE statement that authorizes them

---

## Reporting

Use the **base checklist's Reporting section** — `config/kits/mobile-superapp/codebase/checklist.md` — without modification.

Additional reporting requirements for this artifact:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the traceability mode and the Android-target marker coverage percentage
- [ ] State the parity result against `IMPL-IOS`: matched elements, gaps, and documented divergences

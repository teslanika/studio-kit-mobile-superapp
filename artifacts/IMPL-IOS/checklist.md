# IMPL-IOS Checklist — Layer Delta

**Artifact**: IMPL-IOS
**Kit**: mobile-superapp
**Target**: iOS (`ios-app/Features/{Module}/`)
**Base Checklist**: `{cf-studio-path}/config/kits/mobile-superapp/codebase/checklist.md`

This checklist is a **delta over the mobile SuperApp code checklist**, not a replacement. The base itself layers over `{cf-studio-path}/.core/requirements/code-checklist.md` (generic code quality) and `{cf-studio-path}/config/kits/sdlc/codebase/checklist.md` (semantic alignment, SEM-CODE-001..007), so loading the base loads the whole chain.

This file adds the criteria that apply to the **implementation-reference document** itself and narrows the base's code criteria to the iOS target.

---

## Table of Contents

1. [How To Use This Checklist](#how-to-use-this-checklist)
2. [Code Criteria Scope At This Target](#code-criteria-scope-at-this-target)
3. [Layer Delta: MUST HAVE](#layer-delta-must-have)
4. [Layer Delta: MUST NOT HAVE](#layer-delta-must-not-have)
5. [Layer Delta: iOS-Specific Criteria](#layer-delta-ios-specific-criteria)
6. [Reporting](#reporting)

---

## How To Use This Checklist

1. **LOAD the base checklist first** — `config/kits/mobile-superapp/codebase/checklist.md` — and apply it in full, including the generic and semantic bases it loads.
2. **Apply the scope table** below.
3. **Apply the delta criteria** in this file to the IMPL-IOS document.
4. **Report once**, in the base report format, citing generic, SEM-CODE, base-delta (`IOS-001`), and this file's IDs (`IMPL-IOS-001`) in the same finding field.

Severity values are the base checklists': CRITICAL, HIGH, MEDIUM, LOW.

---

## Code Criteria Scope At This Target

| Base delta section | Scope for IMPL-IOS |
|--------------------|--------------------|
| Delta: iOS Code (`IOS-001..005`) | Full — this is the owning target |
| Delta: KMP Shared Code (`KMP-*`) | Out of scope — see `IMPL-KMP`; verify only that shared code is bridged, not duplicated |
| Delta: Android Code (`ANDROID-*`) | Out of scope — see `IMPL-ANDROID`; used only for the parity check |
| Delta: WebView Bridge Code (`WEBVIEW-*`) | Full when this module hosts a WebView |
| Delta: Mobile Performance (`MOBILE-PERF-*`) | Full for UI and rendering; network criteria belong to the shared repository |
| Delta: Mobile Security (`MOBILE-SEC-*`) | Full for universal-link input validation, debug affordances, and logging |
| Semantic Alignment (`SEM-CODE-001..007`) | Full, restricted to processes whose Target is iOS |

---

## Layer Delta: MUST HAVE

### IMPL-IOS-001: Overview And Module Identity
**Severity**: MEDIUM

- [ ] The module path is stated and matches the DECOMPOSITION platform implementation table
- [ ] The document states that it is a reference map, not a design or coding guide
- [ ] Version and status are present

### IMPL-IOS-002: References Resolve
**Severity**: CRITICAL

- [ ] FEATURE-MOBILE, Epic DESIGN, MiniApp DESIGN, and IMPL-KMP rows are present
- [ ] Every path resolves and every ID exists (`cfs list-ids`)
- [ ] IDs use the `cpt-{hierarchy-prefix}-{kind}-{slug}` scheme

### IMPL-IOS-003: Scope Declares Target Ownership
**Severity**: HIGH

- [ ] Scope lists the iOS-target processes, screens, widgets, and navigation this module implements
- [ ] Out-of-scope names `IMPL-KMP` for business logic, `IMPL-ANDROID`, and the design system
- [ ] No shared-target process appears in scope

### IMPL-IOS-004: Traceability Table Completeness
**Severity**: CRITICAL

- [ ] Every process whose Target is iOS has at least one row
- [ ] Every screen and widget assigned to iOS in the Epic DESIGN has a row
- [ ] Every row's design ID exists, code file exists, and the marker is present in that file
- [ ] No view implementing a design element is missing from the table

### IMPL-IOS-005: Navigation And Universal Links Mapped
**Severity**: HIGH

- [ ] Every navigation destination in the Epic DESIGN has a row pointing at the coordinator
- [ ] Every universal link and custom scheme is listed with its destination and parameter validation
- [ ] The scheme matches the namespace assigned in DECOMPOSITION-PLATFORM

### IMPL-IOS-006: KMP Integration Documented
**Severity**: CRITICAL

- [ ] The bridge type is named and mapped to the shared ViewModel it wraps
- [ ] How Kotlin state reaches SwiftUI, and where cancellation propagates, is stated
- [ ] Where Kotlin result and error types are mapped is stated, and it is a single boundary

### IMPL-IOS-007: Directory Structure Accuracy
**Severity**: MEDIUM

- [ ] The tree matches the module on disk, including `Views/`, `Navigation/`, `ViewModels/`, `Resources/`, and tests
- [ ] Planned-but-absent directories are marked as planned

### IMPL-IOS-008: Marker Format Correctness
**Severity**: HIGH

- [ ] FULL mode examples use `@cpt-{kind}:{cpt-id}:p{N}` scope markers and paired `@cpt-begin` / `@cpt-end` block markers
- [ ] DOCS-ONLY mode is stated to use `@cpt-impl {cpt-id}`
- [ ] The mode this module operates in is stated

### IMPL-IOS-009: Dependencies Declared
**Severity**: HIGH

- [ ] The shared framework dependency is listed and is the source of the ViewModel and use cases
- [ ] Design-system and navigation commons are listed
- [ ] No direct dependency on `android-app/` and no feature-to-feature dependency the design did not sanction

### IMPL-IOS-010: Validation Commands Present
**Severity**: MEDIUM

- [ ] `cfs validate --artifact` for this module path is stated
- [ ] `xcodebuild` build and test commands with a concrete scheme and destination are stated
- [ ] `swiftlint` is stated

### IMPL-IOS-011: Implementation Notes Substance
**Severity**: MEDIUM

- [ ] Every deviation from the design is stated with its reason
- [ ] SwiftUI, coordinator, and bridging decisions a reader could not infer from the code layout are recorded
- [ ] The section is not left as a placeholder

---

## Layer Delta: MUST NOT HAVE

### IMPL-IOS-NO-001: No Full Implementation Code
**Severity**: HIGH

- [ ] No complete view or class bodies beyond short marker illustrations

**Where it belongs**: the source files

### IMPL-IOS-NO-002: No Unresolvable References
**Severity**: CRITICAL

- [ ] No design ID that `cfs list-ids` cannot find
- [ ] No file path that does not exist

**Where it belongs**: fix the reference, or add the design element first

### IMPL-IOS-NO-003: No Architecture Definitions
**Severity**: HIGH

- [ ] No module boundary, layering, or API contract definitions

**Where it belongs**: `DESIGN-MINIAPP` / `DESIGN-PLATFORM`

### IMPL-IOS-NO-004: No Business Logic Mapping
**Severity**: HIGH

- [ ] No use case, repository, or domain rule documented as Swift code
- [ ] No shared ViewModel reimplemented in Swift

**Where it belongs**: `IMPL-KMP`

### IMPL-IOS-NO-005: No Design-System Values
**Severity**: MEDIUM

- [ ] No colors, spacing, typography, or animation values

**Where it belongs**: the design system

### IMPL-IOS-NO-006: No Coding Conventions
**Severity**: LOW

- [ ] No naming, formatting, or dependency-wiring instructions

**Where it belongs**: the project `AGENTS.md`

---

## Layer Delta: iOS-Specific Criteria

### MOBILE-IMPL-IOS-001: View And Widget Mapping
**Severity**: HIGH

- [ ] Each screen view maps to exactly one Epic DESIGN screen ID
- [ ] Each reusable component maps to a widget ID, or is documented as feature-local and not a design element

### MOBILE-IMPL-IOS-002: Bridge Discipline
**Severity**: CRITICAL

- [ ] Exactly one bridge type per shared ViewModel; no parallel Swift state store
- [ ] Published state is derived from the shared state, not maintained independently
- [ ] Intents are forwarded to the shared ViewModel rather than handled locally

### MOBILE-IMPL-IOS-003: Scene Lifecycle Mapping
**Severity**: HIGH

- [ ] Scene-phase transitions and state restoration are mapped to the state row
- [ ] The behavior matches FEATURE-MOBILE section 4 and the Android counterpart

### MOBILE-IMPL-IOS-004: Accessibility Mapping
**Severity**: HIGH

- [ ] The file that carries accessibility labels, traits, and values for the screen is identified
- [ ] Dynamic Type and touch-target handling are noted where they required a decision

### MOBILE-IMPL-IOS-005: Resource And String Ownership
**Severity**: MEDIUM

- [ ] Feature strings live in the feature module's `Resources/`, not in the app target
- [ ] No hardcoded user-visible string is documented as intentional

### MOBILE-IMPL-IOS-006: Parity With Android
**Severity**: HIGH

- [ ] Every element mapped in `IMPL-ANDROID` has a counterpart here, or the divergence is documented in both
- [ ] Deliberate divergences cite the FEATURE-MOBILE statement that authorizes them

---

## Reporting

Use the **base checklist's Reporting section** — `config/kits/mobile-superapp/codebase/checklist.md` — without modification.

Additional reporting requirements for this artifact:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the traceability mode and the iOS-target marker coverage percentage
- [ ] State the parity result against `IMPL-ANDROID`: matched elements, gaps, and documented divergences

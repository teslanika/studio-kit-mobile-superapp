# IMPL-IOS Rules

**Artifact**: IMPL-IOS  
**Kit**: mobile-superapp  
**Level**: Implementation (iOS UI)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/IMPL-IOS/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/IMPL-IOS/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md` — parent FEATURE reference
- `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` — Epic DESIGN reference
- `config/kits/mobile-superapp/artifacts/IMPL-KMP/template.md` — KMP shared logic reference

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Requirements](#requirements)
3. [Tasks](#tasks)
4. [Validation](#validation)
5. [Error Handling](#error-handling)
6. [Next Steps](#next-steps)

---

## Prerequisites

### Load Dependencies

- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-IOS/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-IOS/checklist.md` for semantic guidance
- [ ] Read parent FEATURE-MOBILE for CDSL specifications
- [ ] Read Epic DESIGN for component definitions
- [ ] Read IMPL-KMP for shared logic reference
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] IMPL-IOS follows `config/kits/mobile-superapp/artifacts/IMPL-IOS/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (module path)
  - References (Feature, Epic DESIGN, MiniApp DESIGN)
  - Scope (what iOS module implements)
  - Implementation Notes
  - Traceability Table
  - Directory Structure
  - Code Markers
  - KMP Integration
  - Dependencies
  - Validation
- [ ] Module path is correct: `ios-app/Features/{Module}/`
- [ ] All references have valid paths and IDs
- [ ] No placeholder content (TODO, TBD, FIXME)

### Code Traceability

- [ ] Traceability Table maps:
  - Design Component ID → Code File → Implementation ID
- [ ] Implementation IDs follow format: `@cpt-impl cpt-ios-{module}-{kind}-{slug}`
- [ ] All FEATURE CDSL steps (Section 3.3) have corresponding code markers
- [ ] All Epic DESIGN iOS components (views, widgets) have markers
- [ ] Code markers are in `@cpt-impl` comment format (Swift)

### Mobile-Specific (iOS)

- [ ] Directory structure follows iOS conventions:
  - `ios-app/Features/{Module}/`
  - `Views/` — SwiftUI views
  - `Views/Components/` — Reusable UI components
  - `Navigation/` — Navigation coordinators
  - `ViewModels/` — KMP ViewModel wrappers (if needed)
  - `Resources/` — Localizable.strings, Assets
- [ ] SwiftUI components documented:
  - `{Feature}View.swift` — Main SwiftUI view
  - Widget components in `Components/`
  - Coordinator in `Navigation/`
- [ ] KMP Integration section documents:
  - ViewModel wrapper pattern
  - State observation from KMP
  - Intent sending to KMP
- [ ] Dependencies section includes:
  - ConstructorSDK framework reference
  - Common UI module reference
  - Common Navigation module reference
- [ ] Swift code markers are valid comment syntax

### Versioning

- [ ] When editing existing IMPL: update traceability table
- [ ] When adding new components: add to traceability table
- [ ] When code moves: update file paths in table

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-IOS/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-IOS/checklist.md` for semantic guidance
- [ ] Read FEATURE-MOBILE Section 3.3 (iOS UI)
- [ ] Read Epic DESIGN for iOS component definitions
- [ ] Read IMPL-KMP for shared ViewModel reference
- [ ] Identify all iOS components to implement

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Document module path |
| References | Link to FEATURE, Epic DESIGN, MiniApp DESIGN |
| Scope | Describe what this iOS module implements |
| Implementation Notes | Document SwiftUI patterns, coordinators |
| Traceability Table | Map design IDs → code files → impl IDs |
| Directory Structure | Document module file organization |
| Code Markers | Show `@cpt-impl` marker examples |
| KMP Integration | Document ViewModel wrapper pattern |
| Dependencies | List ConstructorSDK and common module dependencies |

**Traceability Table Format**:

| Design Component ID | Code File | Implementation ID |
|---------------------|-----------|-------------------|
| `cpt-{miniapp}-{epic}-screen-{slug}` | `Views/{Feature}/{Feature}View.swift` | `@cpt-impl cpt-ios-{module}-view-{slug}` |
| `cpt-{miniapp}-{epic}-widget-{slug}` | `Views/{Feature}/Components/{Widget}.swift` | `@cpt-impl cpt-ios-{module}-widget-{slug}` |
| `cpt-{miniapp}-{epic}-nav` | `Navigation/{Feature}Coordinator.swift` | `@cpt-impl cpt-ios-{module}-nav-{slug}` |

**KMP Integration Pattern**:

```swift
// Wrapper to bridge KMP ViewModel to SwiftUI
class {Feature}ViewModelWrapper: ObservableObject {
    private let kmpViewModel: {Feature}ViewModel
    
    @Published var state: {Feature}State
    
    init() {
        self.kmpViewModel = {Feature}ViewModel()
        // Observe KMP state flow
    }
    
    func send(_ intent: {Feature}Intent) {
        kmpViewModel.processIntent(intent)
    }
}
```

**Partial Completion Handling**:

If IMPL-IOS cannot be completed in a single session:
1. Checkpoint progress with documented components
2. Mark incomplete mappings with `PENDING: {reason}`
3. Document resumption point

### Phase 3: IDs and References

- [ ] Link to FEATURE ID: `cpt-{miniapp}-feature-{slug}`
- [ ] Link to Epic DESIGN ID: `cpt-{miniapp}-epic-{epic}`
- [ ] Link to MiniApp DESIGN ID: `cpt-{miniapp}-design`
- [ ] Generate implementation IDs:
  - Views: `@cpt-impl cpt-ios-{module}-view-{slug}`
  - Widgets: `@cpt-impl cpt-ios-{module}-widget-{slug}`
  - Navigation: `@cpt-impl cpt-ios-{module}-nav-{slug}`
  - UI logic: `@cpt-impl cpt-ios-{module}-ui-{slug}`
- [ ] Verify implementation IDs match FEATURE CDSL `inst-ios-` markers

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/IMPL-IOS/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify all FEATURE Section 3.3 steps have impl markers
- [ ] Verify all Epic DESIGN iOS components are mapped
- [ ] Verify directory structure matches actual code
- [ ] Verify KMP integration pattern is documented
- [ ] Verify ConstructorSDK dependency is correctly referenced

### Phase 5: Validation Commands

- [ ] Document `cfs validate` command for this module
- [ ] Verify validation checks are appropriate

---

## Validation

### Phase 1: Structural Validation

- [ ] Run `cfs validate --artifact ios-app/Features/{Module}/` for:
  - Template structure compliance
  - ID format validation
  - Cross-reference validity

### Phase 2: Code Marker Validation

- [ ] All design components have `@cpt-impl` markers in code
- [ ] All code markers reference valid design IDs
- [ ] No orphan markers (markers without design IDs)
- [ ] No missing markers (design IDs without code markers)

### Phase 3: Coverage Validation

- [ ] All FEATURE CDSL steps (Section 3.3) are implemented
- [ ] All Epic DESIGN iOS components have implementations
- [ ] Coverage meets minimum threshold (e.g., 100% for P1 items)

### Phase 4: iOS-Specific Validation

- [ ] SwiftUI views use `@StateObject` for ViewModel wrappers
- [ ] State observation uses proper Combine patterns
- [ ] Navigation uses coordinator pattern or SwiftUI navigation
- [ ] KMP ViewModel wrapper correctly bridges state and intents
- [ ] Scene phase handling is implemented where needed

### Validation Report Format

```
IMPL-IOS Validation Report
══════════════════════════

Module: ios-app/Features/{Module}/

Structural: PASS/FAIL
Code Markers: PASS/FAIL (N markers found)
Coverage: X/Y components (Z%)

Issues:
- [SEVERITY] Description
```

---

## Error Handling

### Missing FEATURE-MOBILE

- [ ] If parent FEATURE-MOBILE not found:
  - Option 1: Run `/cf-generate FEATURE-MOBILE` first (recommended)
  - Option 2: Continue without FEATURE (traceability will be incomplete)
  - Document "FEATURE pending" in IMPL header

### Missing IMPL-KMP

- [ ] If IMPL-KMP not found:
  - Option 1: Run `/cf-generate IMPL-KMP` first (recommended)
  - Option 2: Continue without KMP reference
  - Document KMP dependency assumptions

### KMP Integration Issues

- [ ] If KMP ViewModel not accessible in Swift:
  - Check ConstructorSDK framework export
  - Verify KMP module is properly configured for iOS
  - Document integration constraints

### Code Marker Mismatches

- [ ] If code markers don't match design IDs:
  - Review FEATURE CDSL `inst-ios-` markers
  - Update code markers to match
  - Or update IMPL traceability table to reflect actual code

### Escalation

- [ ] Ask user when SwiftUI patterns deviate from FEATURE spec
- [ ] Ask user when code organization differs from template
- [ ] Ask user when iOS-specific constraints arise
- [ ] Ask user when KMP integration has limitations

---

## Next Steps

### Options

- [ ] IMPL-IOS complete → Implement actual Swift/SwiftUI code with `@cpt-impl` markers
- [ ] IMPL-IOS complete → All platforms implemented → run full validation
- [ ] IMPL-KMP missing → `/cf-generate IMPL-KMP` — create KMP reference first
- [ ] IMPL-ANDROID missing → `/cf-generate IMPL-ANDROID` — create Android reference
- [ ] FEATURE missing → `/cf-generate FEATURE-MOBILE` — create FEATURE first
- [ ] IMPL needs revision → continue editing IMPL-IOS
- [ ] Ready for code review → validate markers with `cfs validate`

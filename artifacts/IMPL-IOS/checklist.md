# IMPL-IOS Checklist

**Artifact**: IMPL-IOS  
**Kit**: mobile-superapp  
**Level**: Implementation (iOS)

This checklist provides semantic quality criteria for iOS Implementation Reference documents in mobile SuperApp projects.

---

## Table of Contents

1. [MUST HAVE Requirements](#must-have-requirements)
2. [SHOULD HAVE Requirements](#should-have-requirements)
3. [MUST NOT HAVE (Violations)](#must-not-have-violations)
4. [Mobile-Specific Criteria](#mobile-specific-criteria)
5. [Reporting](#reporting)

---

## MUST HAVE Requirements

### IMPL-IOS-001: Overview Section

**Priority**: CRITICAL

The IMPL MUST include overview:

- [ ] Module path (`ios-app/Features/{Module}/`)
- [ ] Clear statement linking implementation to product documentation

**Why it matters**: Overview establishes module context.

### IMPL-IOS-002: References Table

**Priority**: CRITICAL

The IMPL MUST include references:

- [ ] Feature reference with path and ID
- [ ] Epic DESIGN reference with path and ID
- [ ] MiniApp DESIGN reference with path and ID

**Why it matters**: References enable navigation to specifications.

### IMPL-IOS-003: Scope Definition

**Priority**: HIGH

The IMPL MUST define scope:

- [ ] What FEATURE sections this module implements (e.g., Section 3.3)
- [ ] iOS-specific components from DESIGN
- [ ] SwiftUI views, navigation, platform integration

**Why it matters**: Scope prevents ambiguity about module responsibility.

### IMPL-IOS-004: Traceability Table

**Priority**: CRITICAL

The IMPL MUST include traceability table:

- [ ] Design Component ID column
- [ ] Code File column (relative path)
- [ ] Implementation ID column (`@cpt-impl cpt-ios-{module}-{type}-{slug}`)
- [ ] View components mapped
- [ ] Widget components mapped
- [ ] Navigation components mapped
- [ ] UI algorithm mapped

**Why it matters**: Traceability enables validation of code markers.

### IMPL-IOS-005: Directory Structure

**Priority**: HIGH

The IMPL MUST include directory structure:

- [ ] Tree diagram of module structure
- [ ] IMPL.md location marked
- [ ] Views/ folder with feature views and Components/
- [ ] Navigation/ folder with Coordinators
- [ ] ViewModels/ folder (for KMP wrappers if needed)
- [ ] Resources/ for Localizable.strings and Assets

**Why it matters**: Structure guides code organization.

### IMPL-IOS-006: Code Markers Format

**Priority**: CRITICAL

The IMPL MUST document code marker format:

- [ ] Example showing `@cpt-impl` marker
- [ ] Format: `// @cpt-impl cpt-ios-{module}-{type}-{slug}`
- [ ] Placement guidance (before struct declaration)

**Why it matters**: Markers enable automated traceability validation.

### IMPL-IOS-007: KMP Integration Section

**Priority**: CRITICAL

The IMPL MUST include KMP integration:

- [ ] ViewModel wrapper pattern explained
- [ ] ObservableObject wrapper example
- [ ] KMP state flow observation pattern
- [ ] Intent sending pattern

**Why it matters**: iOS must properly bridge to KMP ViewModels.

### IMPL-IOS-008: Dependencies Section

**Priority**: HIGH

The IMPL MUST include dependencies:

- [ ] Dependencies table (dependency, purpose)
- [ ] ConstructorSDK dependency (KMP framework)
- [ ] Common/UI dependency
- [ ] Common/Navigation dependency

**Why it matters**: Dependencies document module relationships.

### IMPL-IOS-009: Validation Command

**Priority**: HIGH

The IMPL MUST include validation:

- [ ] Validation command (`cfs validate --artifact {path}`)
- [ ] What validation checks
- [ ] Coverage threshold mention

**Why it matters**: Validation ensures traceability completeness.

---

## SHOULD HAVE Requirements

### IMPL-IOS-010: Implementation Notes

**Priority**: MEDIUM

The IMPL SHOULD include:

- [ ] iOS-specific decisions
- [ ] SwiftUI patterns used
- [ ] Navigation coordinator details

### IMPL-IOS-011: Component Type Markers

**Priority**: MEDIUM

Traceability table SHOULD cover all types:

- [ ] `view` type markers
- [ ] `widget` type markers
- [ ] `nav` type markers
- [ ] `ui` type markers (for algorithms)

### IMPL-IOS-012: Code Examples

**Priority**: LOW

The IMPL SHOULD include:

- [ ] SwiftUI View example with marker
- [ ] @StateObject usage demonstrated
- [ ] ObservableObject wrapper pattern

---

## MUST NOT HAVE (Violations)

### IMPL-IOS-NO-001: No Full Implementation Code

**Priority**: HIGH

The IMPL MUST NOT contain:

- [ ] Complete SwiftUI View implementations
- [ ] Full UI code
- [ ] Production code beyond examples

**Why it matters**: Implementation belongs in code files, not IMPL.md.

### IMPL-IOS-NO-002: No Missing Design References

**Priority**: CRITICAL

The IMPL MUST NOT have:

- [ ] Traceability entries without design component IDs
- [ ] Implementation IDs without corresponding design IDs
- [ ] Orphaned code markers

**Why it matters**: Every implementation must trace to design.

### IMPL-IOS-NO-003: No Incorrect Paths

**Priority**: HIGH

The IMPL MUST NOT have:

- [ ] Code file paths that don't match actual structure
- [ ] Module paths inconsistent with directory structure
- [ ] Broken relative links

**Why it matters**: Paths must be accurate for navigation and validation.

### IMPL-IOS-NO-004: No KMP Business Logic

**Priority**: HIGH

The IMPL MUST NOT contain:

- [ ] Use Case implementations (belongs in KMP IMPL)
- [ ] Repository implementations (belongs in KMP IMPL)
- [ ] Domain logic (belongs in KMP IMPL)

**Why it matters**: iOS IMPL covers UI only; shared logic is in KMP.

---

## Mobile-Specific Criteria

### MOBILE-IMPL-IOS-001: SwiftUI Module Structure

**Priority**: CRITICAL

Directory structure MUST follow iOS conventions:

- [ ] `ios-app/Features/{Module}/`
- [ ] Views/ for SwiftUI views
- [ ] Components/ for reusable widgets
- [ ] Navigation/ for Coordinators

### MOBILE-IMPL-IOS-002: View Pattern

**Priority**: HIGH

View markers MUST follow pattern:

- [ ] `@cpt-impl cpt-ios-{module}-view-{slug}`
- [ ] `struct` declaration
- [ ] `View` suffix on struct names
- [ ] `View` protocol conformance

### MOBILE-IMPL-IOS-003: Widget Pattern

**Priority**: HIGH

Widget markers MUST follow pattern:

- [ ] `@cpt-impl cpt-ios-{module}-widget-{slug}`
- [ ] Located in Components/ folder
- [ ] Reusable across views

### MOBILE-IMPL-IOS-004: Navigation Pattern

**Priority**: HIGH

Navigation markers MUST follow pattern:

- [ ] `@cpt-impl cpt-ios-{module}-nav-{slug}`
- [ ] Coordinator suffix on class names
- [ ] Located in Navigation/ folder

### MOBILE-IMPL-IOS-005: KMP ViewModel Wrapper

**Priority**: CRITICAL

ViewModel wrapper MUST include:

- [ ] `class` declaration with `ObservableObject`
- [ ] Private KMP ViewModel instance
- [ ] `@Published var state` property
- [ ] `send(_ intent:)` method

**Example pattern:**
```swift
class {Feature}ViewModelWrapper: ObservableObject {
    private let kmpViewModel: {Feature}ViewModel
    @Published var state: {Feature}State
    
    func send(_ intent: {Feature}Intent) {
        kmpViewModel.processIntent(intent)
    }
}
```

### MOBILE-IMPL-IOS-006: State Observation

**Priority**: CRITICAL

View code examples MUST show:

- [ ] `@StateObject` for ViewModel wrapper
- [ ] State-based rendering in body
- [ ] Intent sending on user actions

---

## Reporting

### Report Format

For each issue found, report:

```markdown
## Issue: {CHECKLIST-ID}

**Severity**: CRITICAL | HIGH | MEDIUM | LOW

**Why Applicable**: {Why this requirement applies}

**Issue**: {What is wrong}

**Evidence**: {Quote from document or "Not found"}

**Impact**: {Why this matters}

**Proposal**: {How to fix}
```

### Reporting Commitment

- [ ] I reported all issues I found
- [ ] I used the exact report format
- [ ] I included evidence for each issue
- [ ] I proposed concrete fixes
- [ ] I did not hide or omit known problems

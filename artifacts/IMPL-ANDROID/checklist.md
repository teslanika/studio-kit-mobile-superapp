# IMPL-ANDROID Checklist

**Artifact**: IMPL-ANDROID  
**Kit**: mobile-superapp  
**Level**: Implementation (Android)

This checklist provides semantic quality criteria for Android Implementation Reference documents in mobile SuperApp projects.

---

## Table of Contents

1. [MUST HAVE Requirements](#must-have-requirements)
2. [SHOULD HAVE Requirements](#should-have-requirements)
3. [MUST NOT HAVE (Violations)](#must-not-have-violations)
4. [Mobile-Specific Criteria](#mobile-specific-criteria)
5. [Reporting](#reporting)

---

## MUST HAVE Requirements

### IMPL-ANDROID-001: Overview Section

**Priority**: CRITICAL

The IMPL MUST include overview:

- [ ] Module path (`android-app/feature/{module}/`)
- [ ] Clear statement linking implementation to product documentation

**Why it matters**: Overview establishes module context.

### IMPL-ANDROID-002: References Table

**Priority**: CRITICAL

The IMPL MUST include references:

- [ ] Feature reference with path and ID
- [ ] Epic DESIGN reference with path and ID
- [ ] MiniApp DESIGN reference with path and ID

**Why it matters**: References enable navigation to specifications.

### IMPL-ANDROID-003: Scope Definition

**Priority**: HIGH

The IMPL MUST define scope:

- [ ] What FEATURE sections this module implements (e.g., Section 3.2)
- [ ] Android-specific components from DESIGN
- [ ] Jetpack Compose UI, navigation, platform integration

**Why it matters**: Scope prevents ambiguity about module responsibility.

### IMPL-ANDROID-004: Traceability Table

**Priority**: CRITICAL

The IMPL MUST include traceability table:

- [ ] Design Component ID column
- [ ] Code File column (relative path)
- [ ] Implementation ID column (`@cpt-impl cpt-android-{module}-{type}-{slug}`)
- [ ] Screen components mapped
- [ ] Widget components mapped
- [ ] Navigation components mapped
- [ ] UI algorithm mapped

**Why it matters**: Traceability enables validation of code markers.

### IMPL-ANDROID-005: Directory Structure

**Priority**: HIGH

The IMPL MUST include directory structure:

- [ ] Tree diagram of module structure
- [ ] IMPL.md location marked
- [ ] ui/ folder with screens and components/
- [ ] navigation/ folder
- [ ] di/ folder (Hilt modules)
- [ ] src/main/res/ for resources
- [ ] build.gradle.kts location

**Why it matters**: Structure guides code organization.

### IMPL-ANDROID-006: Code Markers Format

**Priority**: CRITICAL

The IMPL MUST document code marker format:

- [ ] Example showing `@cpt-impl` marker
- [ ] Format: `// @cpt-impl cpt-android-{module}-{type}-{slug}`
- [ ] Placement guidance (before @Composable function)

**Why it matters**: Markers enable automated traceability validation.

### IMPL-ANDROID-007: Dependencies Section

**Priority**: HIGH

The IMPL MUST include dependencies:

- [ ] Dependencies table (dependency, purpose)
- [ ] KMP shared module dependency (`constructor-sdk/feature/{module}`)
- [ ] Common UI dependency (`android-app/common/ui`)
- [ ] Common Navigation dependency (`android-app/common/navigation`)

**Why it matters**: Dependencies document module relationships.

### IMPL-ANDROID-008: Validation Command

**Priority**: HIGH

The IMPL MUST include validation:

- [ ] Validation command (`cfs validate --artifact {path}`)
- [ ] What validation checks
- [ ] Coverage threshold mention

**Why it matters**: Validation ensures traceability completeness.

---

## SHOULD HAVE Requirements

### IMPL-ANDROID-009: Implementation Notes

**Priority**: MEDIUM

The IMPL SHOULD include:

- [ ] Android-specific decisions
- [ ] Compose patterns used
- [ ] Navigation setup details

### IMPL-ANDROID-010: Component Type Markers

**Priority**: MEDIUM

Traceability table SHOULD cover all types:

- [ ] `screen` type markers
- [ ] `widget` type markers
- [ ] `nav` type markers
- [ ] `ui` type markers (for algorithms)

### IMPL-ANDROID-011: Code Examples

**Priority**: LOW

The IMPL SHOULD include:

- [ ] Composable screen example with marker
- [ ] Proper state collection pattern shown
- [ ] hiltViewModel() usage demonstrated

---

## MUST NOT HAVE (Violations)

### IMPL-ANDROID-NO-001: No Full Implementation Code

**Priority**: HIGH

The IMPL MUST NOT contain:

- [ ] Complete Composable implementations
- [ ] Full UI code
- [ ] Production code beyond examples

**Why it matters**: Implementation belongs in code files, not IMPL.md.

### IMPL-ANDROID-NO-002: No Missing Design References

**Priority**: CRITICAL

The IMPL MUST NOT have:

- [ ] Traceability entries without design component IDs
- [ ] Implementation IDs without corresponding design IDs
- [ ] Orphaned code markers

**Why it matters**: Every implementation must trace to design.

### IMPL-ANDROID-NO-003: No Incorrect Paths

**Priority**: HIGH

The IMPL MUST NOT have:

- [ ] Code file paths that don't match actual structure
- [ ] Module paths inconsistent with directory structure
- [ ] Broken relative links

**Why it matters**: Paths must be accurate for navigation and validation.

### IMPL-ANDROID-NO-004: No KMP Code

**Priority**: HIGH

The IMPL MUST NOT contain:

- [ ] ViewModel implementations (belongs in KMP IMPL)
- [ ] Use Case implementations (belongs in KMP IMPL)
- [ ] Repository implementations (belongs in KMP IMPL)

**Why it matters**: Android IMPL covers UI only; shared logic is in KMP.

---

## Mobile-Specific Criteria

### MOBILE-IMPL-ANDROID-001: Compose Module Structure

**Priority**: CRITICAL

Directory structure MUST follow Android conventions:

- [ ] `src/main/kotlin/com/constructor/android/feature/{module}/`
- [ ] ui/ for Composables
- [ ] components/ for reusable widgets
- [ ] navigation/ for NavGraph

### MOBILE-IMPL-ANDROID-002: Screen Pattern

**Priority**: HIGH

Screen markers MUST follow pattern:

- [ ] `@cpt-impl cpt-android-{module}-screen-{slug}`
- [ ] @Composable annotation
- [ ] Screen suffix on function names
- [ ] ViewModel parameter with hiltViewModel()

### MOBILE-IMPL-ANDROID-003: Widget Pattern

**Priority**: HIGH

Widget markers MUST follow pattern:

- [ ] `@cpt-impl cpt-android-{module}-widget-{slug}`
- [ ] @Composable annotation
- [ ] Located in components/ folder

### MOBILE-IMPL-ANDROID-004: Navigation Pattern

**Priority**: HIGH

Navigation markers MUST follow pattern:

- [ ] `@cpt-impl cpt-android-{module}-nav-{slug}`
- [ ] NavGraph suffix on function names
- [ ] Located in navigation/ folder

### MOBILE-IMPL-ANDROID-005: State Collection

**Priority**: CRITICAL

Screen code examples MUST show:

- [ ] `collectAsStateWithLifecycle()` usage
- [ ] State-based rendering pattern
- [ ] Intent sending on user actions

### MOBILE-IMPL-ANDROID-006: Hilt Integration

**Priority**: HIGH

DI structure MUST include:

- [ ] di/ folder for Hilt modules
- [ ] {Feature}Module.kt pattern
- [ ] hiltViewModel() for ViewModel injection

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

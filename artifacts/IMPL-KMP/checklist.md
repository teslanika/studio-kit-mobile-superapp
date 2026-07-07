# IMPL-KMP Checklist

**Artifact**: IMPL-KMP  
**Kit**: mobile-superapp  
**Level**: Implementation (KMP)

This checklist provides semantic quality criteria for KMP (Kotlin Multiplatform) Implementation Reference documents in mobile SuperApp projects.

---

## Table of Contents

1. [MUST HAVE Requirements](#must-have-requirements)
2. [SHOULD HAVE Requirements](#should-have-requirements)
3. [MUST NOT HAVE (Violations)](#must-not-have-violations)
4. [Mobile-Specific Criteria](#mobile-specific-criteria)
5. [Reporting](#reporting)

---

## MUST HAVE Requirements

### IMPL-KMP-001: Overview Section

**Priority**: CRITICAL

The IMPL MUST include overview:

- [ ] Module path (`constructor-sdk/feature/{module}/`)
- [ ] Clear statement linking implementation to product documentation

**Why it matters**: Overview establishes module context.

### IMPL-KMP-002: References Table

**Priority**: CRITICAL

The IMPL MUST include references:

- [ ] Feature reference with path and ID
- [ ] Epic DESIGN reference with path and ID
- [ ] MiniApp DESIGN reference with path and ID

**Why it matters**: References enable navigation to specifications.

### IMPL-KMP-003: Scope Definition

**Priority**: HIGH

The IMPL MUST define scope:

- [ ] What FEATURE sections this module implements (e.g., Section 3.1)
- [ ] What DESIGN components this module implements

**Why it matters**: Scope prevents ambiguity about module responsibility.

### IMPL-KMP-004: Traceability Table

**Priority**: CRITICAL

The IMPL MUST include traceability table:

- [ ] Design Component ID column
- [ ] Code File column (relative path)
- [ ] Implementation ID column (`@cpt-impl cpt-kmp-{module}-{type}-{slug}`)
- [ ] All design components mapped

**Why it matters**: Traceability enables validation of code markers.

### IMPL-KMP-005: Directory Structure

**Priority**: HIGH

The IMPL MUST include directory structure:

- [ ] Tree diagram of module structure
- [ ] IMPL.md location marked
- [ ] `src/commonMain/kotlin/` path
- [ ] domain/ folder (model/, usecase/)
- [ ] data/ folder (repository/, remote/, local/)
- [ ] presentation/ folder (ViewModel, State, Intent, Effect)
- [ ] build.gradle.kts location

**Why it matters**: Structure guides code organization.

### IMPL-KMP-006: Code Markers Format

**Priority**: CRITICAL

The IMPL MUST document code marker format:

- [ ] Example showing `@cpt-impl` marker
- [ ] Format: `// @cpt-impl cpt-kmp-{module}-{type}-{slug}`
- [ ] Placement guidance (before class/function)

**Why it matters**: Markers enable automated traceability validation.

### IMPL-KMP-007: Validation Command

**Priority**: HIGH

The IMPL MUST include validation:

- [ ] Validation command (`cfs validate --artifact {path}`)
- [ ] What validation checks (design components have markers)
- [ ] What validation verifies (markers reference valid IDs)
- [ ] Coverage threshold mention

**Why it matters**: Validation ensures traceability completeness.

---

## SHOULD HAVE Requirements

### IMPL-KMP-008: Implementation Notes

**Priority**: MEDIUM

The IMPL SHOULD include:

- [ ] Platform-specific decisions
- [ ] Deviations from design
- [ ] Implementation constraints

### IMPL-KMP-009: Component Type Markers

**Priority**: MEDIUM

Traceability table SHOULD cover all types:

- [ ] `usecase` type markers
- [ ] `state` type markers
- [ ] `vm` (ViewModel) type markers
- [ ] `repo` (Repository) type markers
- [ ] `entity` type markers

### IMPL-KMP-010: Code Examples

**Priority**: LOW

The IMPL SHOULD include:

- [ ] UseCase code example with marker
- [ ] Proper marker placement demonstrated

---

## MUST NOT HAVE (Violations)

### IMPL-KMP-NO-001: No Full Implementation Code

**Priority**: HIGH

The IMPL MUST NOT contain:

- [ ] Complete class implementations
- [ ] Full method bodies
- [ ] Production code beyond examples

**Why it matters**: Implementation belongs in code files, not IMPL.md.

### IMPL-KMP-NO-002: No Missing Design References

**Priority**: CRITICAL

The IMPL MUST NOT have:

- [ ] Traceability entries without design component IDs
- [ ] Implementation IDs without corresponding design IDs
- [ ] Orphaned code markers

**Why it matters**: Every implementation must trace to design.

### IMPL-KMP-NO-003: No Incorrect Paths

**Priority**: HIGH

The IMPL MUST NOT have:

- [ ] Code file paths that don't match actual structure
- [ ] Module paths inconsistent with directory structure
- [ ] Broken relative links

**Why it matters**: Paths must be accurate for navigation and validation.

### IMPL-KMP-NO-004: No Architecture Definitions

**Priority**: MEDIUM

The IMPL MUST NOT contain:

- [ ] Architecture decisions (belongs in DESIGN)
- [ ] Component interfaces (belongs in DESIGN)
- [ ] State definitions (belongs in DESIGN)

**Why it matters**: IMPL references architecture, doesn't define it.

---

## Mobile-Specific Criteria

### MOBILE-IMPL-KMP-001: KMP Module Structure

**Priority**: CRITICAL

Directory structure MUST follow KMP conventions:

- [ ] `src/commonMain/kotlin/` for shared code
- [ ] Package path: `com/constructor/sdk/feature/{module}/`
- [ ] domain/, data/, presentation/ separation

### MOBILE-IMPL-KMP-002: Use Case Pattern

**Priority**: HIGH

UseCase markers MUST follow pattern:

- [ ] `@cpt-impl cpt-kmp-{module}-usecase-{slug}`
- [ ] UseCase suffix on class names
- [ ] Result<T> return type

### MOBILE-IMPL-KMP-003: ViewModel Pattern

**Priority**: HIGH

ViewModel markers MUST follow pattern:

- [ ] `@cpt-impl cpt-kmp-{module}-vm-{slug}`
- [ ] ViewModel suffix on class names
- [ ] State, Intent, Effect references

### MOBILE-IMPL-KMP-004: Repository Pattern

**Priority**: HIGH

Repository markers MUST follow pattern:

- [ ] `@cpt-impl cpt-kmp-{module}-repo-{slug}`
- [ ] RepositoryImpl suffix on implementation
- [ ] Interface in domain, impl in data

### MOBILE-IMPL-KMP-005: Entity Pattern

**Priority**: HIGH

Entity markers MUST follow pattern:

- [ ] `@cpt-impl cpt-kmp-{module}-entity-{slug}`
- [ ] Located in domain/model/
- [ ] Data class structure

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

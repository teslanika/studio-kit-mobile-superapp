# IMPL-KMP Rules

**Artifact**: IMPL-KMP  
**Kit**: mobile-superapp  
**Level**: Implementation (KMP Shared Logic)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/IMPL-KMP/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/IMPL-KMP/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md` — parent FEATURE reference
- `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` — Epic DESIGN reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-KMP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-KMP/checklist.md` for semantic guidance
- [ ] Read parent FEATURE-MOBILE for CDSL specifications
- [ ] Read Epic DESIGN for component definitions
- [ ] Read MiniApp DESIGN for shared patterns
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] IMPL-KMP follows `config/kits/mobile-superapp/artifacts/IMPL-KMP/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (module path)
  - References (Feature, Epic DESIGN, MiniApp DESIGN)
  - Scope (what KMP module implements)
  - Implementation Notes
  - Traceability Table
  - Directory Structure
  - Code Markers
  - Validation
- [ ] Module path is correct: `constructor-sdk/feature/{module}/`
- [ ] All references have valid paths and IDs
- [ ] No placeholder content (TODO, TBD, FIXME)

### Code Traceability

- [ ] Traceability Table maps:
  - Design Component ID → Code File → Implementation ID
- [ ] Implementation IDs follow format: `@cpt-impl cpt-kmp-{module}-{kind}-{slug}`
- [ ] All FEATURE CDSL steps (Section 3.1) have corresponding code markers
- [ ] All Epic DESIGN components (ViewModel, UseCase, Repository) have markers
- [ ] Code markers are in `@cpt-impl` comment format

### Mobile-Specific

- [ ] Directory structure follows KMP conventions:
  - `src/commonMain/kotlin/com/constructor/sdk/feature/{module}/`
  - `domain/model/` — Domain entities
  - `domain/usecase/` — Use cases
  - `data/repository/` — Repository implementations
  - `data/remote/` — API clients, DTOs
  - `data/local/` — Local data sources
  - `presentation/` — ViewModel, State, Intent, Effect
- [ ] MVI pattern components documented:
  - `{Feature}ViewModel.kt`
  - `{Feature}State.kt`
  - `{Feature}Intent.kt`
  - `{Feature}Effect.kt`
- [ ] Kotlin code markers are valid comment syntax

### Versioning

- [ ] When editing existing IMPL: update traceability table
- [ ] When adding new components: add to traceability table
- [ ] When code moves: update file paths in table

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-KMP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/IMPL-KMP/checklist.md` for semantic guidance
- [ ] Read FEATURE-MOBILE Section 3.1 (KMP Shared Logic)
- [ ] Read Epic DESIGN for component definitions
- [ ] Identify all KMP components to implement

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Document module path |
| References | Link to FEATURE, Epic DESIGN, MiniApp DESIGN |
| Scope | Describe what this KMP module implements |
| Implementation Notes | Document KMP-specific decisions, constraints |
| Traceability Table | Map design IDs → code files → impl IDs |
| Directory Structure | Document module file organization |
| Code Markers | Show `@cpt-impl` marker examples |

**Traceability Table Format**:

| Design Component ID | Code File | Implementation ID |
|---------------------|-----------|-------------------|
| `cpt-{miniapp}-{epic}-usecase-{slug}` | `src/commonMain/kotlin/.../usecase/{UseCase}.kt` | `@cpt-impl cpt-kmp-{module}-usecase-{slug}` |
| `cpt-{miniapp}-{epic}-state` | `src/commonMain/kotlin/.../presentation/{State}.kt` | `@cpt-impl cpt-kmp-{module}-state-{slug}` |

**Partial Completion Handling**:

If IMPL-KMP cannot be completed in a single session:
1. Checkpoint progress with documented components
2. Mark incomplete mappings with `PENDING: {reason}`
3. Document resumption point

### Phase 3: IDs and References

- [ ] Link to FEATURE ID: `cpt-{miniapp}-feature-{slug}`
- [ ] Link to Epic DESIGN ID: `cpt-{miniapp}-epic-{epic}`
- [ ] Link to MiniApp DESIGN ID: `cpt-{miniapp}-design`
- [ ] Generate implementation IDs:
  - Use cases: `@cpt-impl cpt-kmp-{module}-usecase-{slug}`
  - State: `@cpt-impl cpt-kmp-{module}-state-{slug}`
  - ViewModel: `@cpt-impl cpt-kmp-{module}-vm-{slug}`
  - Repository: `@cpt-impl cpt-kmp-{module}-repo-{slug}`
  - Entity: `@cpt-impl cpt-kmp-{module}-entity-{slug}`
- [ ] Verify implementation IDs match FEATURE CDSL `inst-` markers

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/IMPL-KMP/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify all FEATURE Section 3.1 steps have impl markers
- [ ] Verify all Epic DESIGN KMP components are mapped
- [ ] Verify directory structure matches actual code

### Phase 5: Validation Commands

- [ ] Document `cfs validate` command for this module
- [ ] Verify validation checks are appropriate

---

## Validation

### Phase 1: Structural Validation

- [ ] Run `cfs validate --artifact constructor-sdk/feature/{module}/` for:
  - Template structure compliance
  - ID format validation
  - Cross-reference validity

### Phase 2: Code Marker Validation

- [ ] All design components have `@cpt-impl` markers in code
- [ ] All code markers reference valid design IDs
- [ ] No orphan markers (markers without design IDs)
- [ ] No missing markers (design IDs without code markers)

### Phase 3: Coverage Validation

- [ ] All FEATURE CDSL steps (Section 3.1) are implemented
- [ ] All Epic DESIGN KMP components have implementations
- [ ] Coverage meets minimum threshold (e.g., 100% for P1 items)

### Validation Report Format

```
IMPL-KMP Validation Report
══════════════════════════

Module: constructor-sdk/feature/{module}/

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

### Missing Epic DESIGN

- [ ] If Epic DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-EPIC` first
  - Option 2: Continue with assumptions documented
  - Document component assumptions made

### Code Marker Mismatches

- [ ] If code markers don't match design IDs:
  - Review FEATURE CDSL `inst-` markers
  - Update code markers to match
  - Or update IMPL traceability table to reflect actual code

### Escalation

- [ ] Ask user when KMP patterns deviate from FEATURE spec
- [ ] Ask user when code organization differs from template
- [ ] Ask user when implementation constraints arise

---

## Next Steps

### Options

- [ ] IMPL-KMP complete → Implement actual Kotlin code with `@cpt-impl` markers
- [ ] IMPL-KMP complete → `/cf-generate IMPL-ANDROID` — create Android implementation reference
- [ ] IMPL-KMP complete → `/cf-generate IMPL-IOS` — create iOS implementation reference
- [ ] FEATURE missing → `/cf-generate FEATURE-MOBILE` — create FEATURE first
- [ ] IMPL needs revision → continue editing IMPL-KMP
- [ ] Ready for code review → validate markers with `cfs validate`

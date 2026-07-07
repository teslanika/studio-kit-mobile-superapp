# DECOMPOSITION-EPIC Rules

**Artifact**: DECOMPOSITION-EPIC  
**Kit**: mobile-superapp  
**Level**: L2 (Epic)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` — parent Epic DESIGN reference
- `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` — Epic PRD reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md` for semantic guidance
- [ ] Read Epic PRD for requirements context
- [ ] Read Epic DESIGN for architectural context
- [ ] Read MiniApp DECOMPOSITION for Epic boundaries
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] DECOMPOSITION-EPIC follows `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (parent documents reference)
  - Feature Entries (all features with full details)
  - Feature Dependencies
  - Coverage Matrix (Requirements → Features, Design Components → Features)
  - Platform Implementation Matrix
  - Implementation Order
  - Acceptance Criteria Summary
- [ ] All IDs follow `cpt-{miniapp}-feature-{slug}` convention
- [ ] Each Feature entry has complete metadata:
  - Purpose, Depends On, Scope (in/out)
  - Requirements Covered, Design Components
  - Screen/Widget, Use Cases, API Endpoints
  - Platform Implementation table
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Each Feature specifies platform implementation:
  - KMP module and location
  - Android component and location
  - iOS component and location
- [ ] Platform Implementation Matrix shows KMP/Android/iOS status per feature
- [ ] Features reference screens, widgets, use cases from Epic DESIGN
- [ ] API endpoints are documented for each feature
- [ ] Features are independently testable

### Traceability

- [ ] Every Feature traces to Epic FRs it covers
- [ ] Design components from Epic DESIGN are allocated to Features
- [ ] Requirements → Features coverage matrix complete
- [ ] Design Components → Features coverage matrix complete
- [ ] Links to parent documents (Epic PRD, Epic DESIGN, MiniApp DECOMPOSITION)

### Versioning

- [ ] When editing existing DECOMPOSITION: increment version in document header
- [ ] When adding/removing Feature: document rationale

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md` for semantic guidance
- [ ] Read Epic PRD for requirements
- [ ] Read Epic DESIGN for components
- [ ] Identify natural Feature boundaries from use cases and widgets

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Link to parent PRD, DESIGN, MiniApp DECOMPOSITION |
| Feature Entries | Create entry for each feature with full metadata |
| Dependencies | Create dependency diagram with rationale |
| Coverage Matrix | Map FRs and components to Features |
| Platform Matrix | Track KMP/Android/iOS implementation status |
| Implementation Order | Plan phased implementation |
| Acceptance Criteria | Summarize key criteria per feature |

**Feature Entry Checklist**:

For each Feature, document:
- [ ] Purpose (few sentences)
- [ ] Depends On (other Features or "None")
- [ ] Scope (in-scope and out-of-scope items)
- [ ] Requirements Covered (Epic FRs with priority)
- [ ] Design Components (IDs from Epic DESIGN)
- [ ] Screen/Widget (component IDs)
- [ ] Use Cases (use case IDs)
- [ ] API Endpoints (methods and paths)
- [ ] Platform Implementation (KMP, Android, iOS locations)

**Partial Completion Handling**:

If DECOMPOSITION-EPIC cannot be completed in a single session:
1. Checkpoint progress with completed Feature entries
2. Add `status: DRAFT` to document header
3. Mark incomplete Features with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate overall status ID: `cpt-{miniapp}-{epic}-status-overall`
- [ ] Generate Feature IDs: `cpt-{miniapp}-feature-{slug}`
- [ ] Link to Epic FR IDs
- [ ] Link to Epic component IDs (screens, widgets, use cases)
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify all Epic FRs are covered by at least one Feature
- [ ] Verify all DESIGN components are allocated
- [ ] Verify Features are independently implementable
- [ ] Verify Platform Implementation Matrix is complete

### Phase 5: Table of Contents

- [ ] Run `cfs toc <path>` to generate/update Table of Contents
- [ ] Verify TOC is present and complete

---

## Validation

### Phase 1: Structural Validation

- [ ] Run `cfs validate --artifact <path>` for:
  - Template structure compliance
  - ID format validation
  - Cross-reference validity
  - No placeholders

### Phase 2: Semantic Validation

- [ ] Read `config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Decomposition-Specific Validation

- [ ] All Epic FRs have Feature coverage
- [ ] All DESIGN components are allocated to Features
- [ ] Features are right-sized (not too big, not too small)
- [ ] Dependencies are minimal and justified
- [ ] Implementation order respects dependencies
- [ ] Platform Implementation Matrix is consistent

### Validation Report Format

```
DECOMPOSITION-EPIC Validation Report
════════════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Decomposition-Specific: PASS/FAIL (N issues)

Coverage:
- Epic FRs covered: N/M (X%)
- DESIGN components allocated: N/M (X%)
- Platform coverage: KMP: N/M, Android: N/M, iOS: N/M

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing Epic DESIGN

- [ ] If Epic DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-EPIC` first (recommended)
  - Option 2: Continue without DESIGN (component allocation will be incomplete)
  - Document "DESIGN pending" in DECOMPOSITION header

### Missing Epic PRD

- [ ] If Epic PRD not found:
  - Option 1: Run `/cf-generate PRD-EPIC` first
  - Option 2: Continue without PRD (requirements coverage will be incomplete)
  - Document requirements assumptions made

### Feature Boundary Uncertainty

- [ ] If uncertain about Feature boundaries:
  - Ask user for guidance
  - Consider use case boundaries (one use case = one Feature)
  - Consider widget boundaries (complex widget = one Feature)
  - Consider API boundaries (related endpoints = one Feature)
  - Document decision rationale

### Escalation

- [ ] Ask user when Feature scope is unclear
- [ ] Ask user when platform implementation varies significantly
- [ ] Ask user when API contracts are unavailable

---

## Next Steps

### Options

- [ ] DECOMPOSITION-EPIC complete → `/cf-generate FEATURE-MOBILE` — create Feature specification
- [ ] DESIGN missing → `/cf-generate DESIGN-EPIC` — create Epic DESIGN first
- [ ] PRD missing → `/cf-generate PRD-EPIC` — create Epic PRD first
- [ ] DECOMPOSITION needs revision → continue editing DECOMPOSITION-EPIC
- [ ] Ready for implementation → `/cf-generate IMPL-KMP` — create KMP implementation reference

# DECOMPOSITION-MINIAPP Rules

**Artifact**: DECOMPOSITION-MINIAPP  
**Kit**: mobile-superapp  
**Level**: L1 (MiniApp)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md` — parent MiniApp DESIGN reference
- `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` — MiniApp PRD reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md` for semantic guidance
- [ ] Read MiniApp PRD for requirements context
- [ ] Read MiniApp DESIGN for architectural context
- [ ] Read Platform DECOMPOSITION for MiniApp boundaries
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] DECOMPOSITION-MINIAPP follows `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (parent documents reference)
  - Epic Entries (organized by category: Screens, Capabilities, Flows)
  - Epic Dependencies
  - Coverage Matrix (Requirements, Design Components)
  - Implementation Order
- [ ] All IDs follow `cpt-{miniapp}-epic-{slug}` convention
- [ ] Each Epic entry has complete metadata:
  - Category, Purpose, Actors
  - Depends On, Scope (in/out)
  - Requirements Covered, Design Components
  - KMP Modules (if applicable), Target Release
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Epics are categorized:
  - **Screens**: Individual screens/views
  - **Capabilities**: Cross-cutting features (offline, notifications)
  - **Flows**: Multi-screen user journeys
- [ ] Each Epic specifies KMP module dependencies
- [ ] Screen Epics specify entry points (navigation, deep link)
- [ ] Capability Epics specify Kernel integration
- [ ] Flow Epics list screens involved

### Traceability

- [ ] Every Epic traces to MiniApp FRs it covers
- [ ] Design components from MiniApp DESIGN are allocated to Epics
- [ ] Requirements coverage matrix shows FR → Epic mapping
- [ ] Design component coverage matrix shows component → Epic mapping
- [ ] Links to parent documents (MiniApp PRD, MiniApp DESIGN, Platform DECOMPOSITION)

### Versioning

- [ ] When editing existing DECOMPOSITION: increment version in document header
- [ ] When adding/removing Epic: document rationale

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md` for semantic guidance
- [ ] Read MiniApp PRD for requirements
- [ ] Read MiniApp DESIGN for components
- [ ] Identify natural Epic boundaries from screens, capabilities, and flows

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Link to parent PRD, DESIGN, Platform DECOMPOSITION |
| Screens | Create Epic entry for each screen |
| Capabilities | Create Epic entry for cross-cutting capabilities |
| Flows | Create Epic entry for multi-screen journeys |
| Dependencies | Create dependency diagram with rationale |
| Coverage Matrix | Map FRs and components to Epics |
| Implementation Order | Plan phased implementation |

**Epic Entry Checklist**:

For each Epic, document:
- [ ] Category (Screen / Capability / Flow)
- [ ] Purpose (few sentences)
- [ ] Actors (actor IDs)
- [ ] Depends On (other Epics or "None")
- [ ] Scope (in-scope and out-of-scope items)
- [ ] Requirements Covered (MiniApp FRs with priority)
- [ ] Design Components (IDs from MiniApp DESIGN)
- [ ] KMP Modules (if applicable)
- [ ] Target Release (quarter)

**Partial Completion Handling**:

If DECOMPOSITION-MINIAPP cannot be completed in a single session:
1. Checkpoint progress with completed Epic entries
2. Add `status: DRAFT` to document header
3. Mark incomplete Epics with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate overall status ID: `cpt-{miniapp}-status-overall`
- [ ] Generate Epic IDs: `cpt-{miniapp}-epic-{slug}`
- [ ] Link to MiniApp FR IDs
- [ ] Link to MiniApp component IDs
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify all MiniApp FRs are covered by at least one Epic
- [ ] Verify all DESIGN components are allocated
- [ ] Verify Epic boundaries don't overlap significantly
- [ ] Verify dependency graph supports parallel development where possible

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

- [ ] Read `config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Decomposition-Specific Validation

- [ ] All MiniApp FRs have Epic coverage
- [ ] All DESIGN components are allocated to Epics
- [ ] Epic categories are appropriate (Screen vs Capability vs Flow)
- [ ] Dependencies are justified and minimal
- [ ] Implementation order respects dependencies
- [ ] Parallel development opportunities identified

### Validation Report Format

```
DECOMPOSITION-MINIAPP Validation Report
══════════════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Decomposition-Specific: PASS/FAIL (N issues)

Coverage:
- MiniApp FRs covered: N/M (X%)
- DESIGN components allocated: N/M (X%)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing MiniApp DESIGN

- [ ] If MiniApp DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-MINIAPP` first (recommended)
  - Option 2: Continue without DESIGN (component allocation will be incomplete)
  - Document "DESIGN pending" in DECOMPOSITION header

### Missing MiniApp PRD

- [ ] If MiniApp PRD not found:
  - Option 1: Run `/cf-generate PRD-MINIAPP` first
  - Option 2: Continue without PRD (requirements coverage will be incomplete)
  - Document requirements assumptions made

### Epic Boundary Uncertainty

- [ ] If uncertain about Epic boundaries:
  - Ask user for guidance
  - Consider screen boundaries (one screen = one Epic)
  - Consider user flow boundaries (complete journey = one Flow Epic)
  - Consider capability scope (single capability = one Capability Epic)
  - Document decision rationale

### Escalation

- [ ] Ask user when Epic scope is unclear
- [ ] Ask user when dependencies are complex
- [ ] Ask user when implementation priorities conflict

---

## Next Steps

### Options

- [ ] DECOMPOSITION-MINIAPP complete → `/cf-generate PRD-EPIC` — create Epic PRD
- [ ] DECOMPOSITION-MINIAPP complete → `/cf-generate DESIGN-EPIC` — create Epic DESIGN
- [ ] DESIGN missing → `/cf-generate DESIGN-MINIAPP` — create MiniApp DESIGN first
- [ ] PRD missing → `/cf-generate PRD-MINIAPP` — create MiniApp PRD first
- [ ] DECOMPOSITION needs revision → continue editing DECOMPOSITION-MINIAPP
- [ ] Ready for Epic work → create Epic folder structure

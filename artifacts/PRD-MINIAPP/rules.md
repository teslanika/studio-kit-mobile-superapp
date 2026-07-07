# PRD-MINIAPP Rules

**Artifact**: PRD-MINIAPP  
**Kit**: mobile-superapp  
**Level**: L1 (MiniApp)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md` — semantic quality criteria
- `{platform_prd}` — parent Platform PRD reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md` for semantic guidance
- [ ] Read parent Platform PRD for context
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] PRD-MINIAPP follows `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (purpose, scope, traces to platform)
  - Actors (primary actors with MiniApp-specific context)
  - Functional Requirements (core capabilities, MiniApp-level NFRs)
  - Use Cases (key user scenarios)
  - Dependencies (platform, external)
  - Traceability Matrix
  - Acceptance Criteria
- [ ] All IDs follow `cpt-{miniapp}-{kind}-{slug}` convention
- [ ] References to Platform PRD are valid
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Requirements address mobile context:
  - Offline capabilities where needed
  - Push notification scenarios
  - Deep link entry points
  - Platform-specific UX considerations
- [ ] Actors reference platform-level actor IDs (`cpt-superapp-actor-{slug}`)
- [ ] Dependencies specify required Kernel services (Auth, Storage, Network)
- [ ] Integration points clearly identify backend APIs

### Traceability

- [ ] Every MiniApp FR traces to Platform PRD FR (refines relationship)
- [ ] Platform NFRs applicable to MiniApp are inherited with `inherits` relation
- [ ] MiniApp-specific FRs are tagged `miniapp-specific` with rationale
- [ ] Use cases trace to MiniApp FRs
- [ ] Traceability matrix documents:
  - Platform FR → MiniApp FR coverage
  - MiniApp FR → Epic coverage (planned)

### Versioning

- [ ] When editing existing PRD: increment version in document header
- [ ] When changing requirement: update version field in requirement table

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md` for semantic guidance
- [ ] Read Platform PRD for parent requirements
- [ ] Identify which Platform FRs this MiniApp refines

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Document purpose, scope (in/out), platform traces |
| Actors | List primary actors with MiniApp-specific context |
| Functional Requirements | Define FRs with priority, actor, description, acceptance |
| NFRs | Extend/specialize Platform NFRs for MiniApp context |
| Use Cases | Document key user scenarios with flows |
| Dependencies | List Kernel services and external integrations |
| Traceability | Build coverage matrix for Platform → MiniApp |

**Partial Completion Handling**:

If PRD-MINIAPP cannot be completed in a single session:
1. Checkpoint progress with completed sections
2. Add `status: DRAFT` to document header
3. Mark incomplete sections with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate MiniApp PRD anchor: `cpt-{miniapp}-prd`
- [ ] Generate FR IDs: `cpt-{miniapp}-fr-{slug}`
- [ ] Generate NFR IDs: `cpt-{miniapp}-nfr-{slug}`
- [ ] Generate use case IDs: `cpt-{miniapp}-usecase-{slug}`
- [ ] Link to Platform PRD requirements
- [ ] Reference platform actor IDs
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify every FR is testable (measurable acceptance criteria)
- [ ] Verify Platform traceability is complete

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

- [ ] Read `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Requirements Quality Validation

- [ ] All FRs have measurable acceptance criteria
- [ ] All FRs have assigned priority (P1/P2/P3)
- [ ] All FRs have associated actor
- [ ] No ambiguous requirements (avoid "should", "might", "usually")
- [ ] No implementation details in requirements

### Validation Report Format

```
PRD-MINIAPP Validation Report
════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Requirements Quality: PASS/FAIL (N issues)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing Platform PRD

- [ ] If parent Platform PRD not found:
  - Option 1: Run `/cf-generate PRD-PLATFORM` first (recommended)
  - Option 2: Continue without Platform PRD (document assumptions)
  - Document "Platform PRD pending" in MiniApp PRD header

### Unclear Scope

- [ ] If uncertain about MiniApp scope:
  - Ask user for scope clarification
  - Document assumptions made
  - Mark scope section for review

### Escalation

- [ ] Ask user when uncertain about requirement priority
- [ ] Ask user when Platform FR mapping is unclear
- [ ] Ask user when actors/personas need clarification

---

## Next Steps

### Options

- [ ] PRD-MINIAPP complete → `/cf-generate DESIGN-MINIAPP` — create technical design
- [ ] Need Platform context → `/cf-generate PRD-PLATFORM` — create Platform PRD first
- [ ] PRD needs revision → continue editing PRD-MINIAPP
- [ ] Ready for Epic → `/cf-generate PRD-EPIC` — create Epic-level PRD
- [ ] Ready for decomposition → `/cf-generate DECOMPOSITION-MINIAPP` — break into epics

# DECOMPOSITION-PLATFORM Rules

**Artifact**: DECOMPOSITION-PLATFORM  
**Kit**: mobile-superapp  
**Level**: L0 (Platform)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/template.md` — parent Platform DESIGN reference
- `{platform_prd}` — Platform PRD reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md` for semantic guidance
- [ ] Read Platform PRD for requirements context
- [ ] Read Platform DESIGN for architectural context
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] DECOMPOSITION-PLATFORM follows `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (parent documents reference)
  - MiniApp Entries (all MiniApps with full details)
  - Shared Kernel Components
  - MiniApp Dependencies
  - Release Roadmap
- [ ] All IDs follow `cpt-{platform}-miniapp-{slug}` convention
- [ ] Each MiniApp entry has complete metadata:
  - Purpose, Target Users, Depends On
  - Scope (in/out), Requirements Covered
  - Platform Components, Integration Points
  - Target Release
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Each MiniApp documents Kernel dependencies (Auth, Storage, Network)
- [ ] Platform components reference DESIGN-PLATFORM IDs
- [ ] Integration points match DESIGN-PLATFORM integrations
- [ ] MiniApps are self-contained (loosely coupled)
- [ ] Communication between MiniApps via deep links and events only

### Traceability

- [ ] Every MiniApp traces to Platform FRs it covers
- [ ] Platform components from DESIGN are allocated to MiniApps
- [ ] Shared Kernel components table shows which MiniApps use each
- [ ] Requirements coverage is explicit (with priority)
- [ ] Links to parent documents (PRD, DESIGN)

### Versioning

- [ ] When editing existing DECOMPOSITION: increment version in document header
- [ ] When adding/removing MiniApp: document rationale

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md` for semantic guidance
- [ ] Read Platform PRD for requirements
- [ ] Read Platform DESIGN for components and integrations
- [ ] Identify natural MiniApp boundaries from user actors and capabilities

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Link to parent PRD and DESIGN |
| MiniApp Entries | Create entry for each MiniApp with full metadata |
| Shared Kernel | Document Kernel components and which MiniApps use them |
| Dependencies | Create dependency diagram, document rationale |
| Release Roadmap | Plan quarterly releases with milestones |

**MiniApp Entry Checklist**:

For each MiniApp, document:
- [ ] Purpose (few sentences)
- [ ] Target Users (actor ID)
- [ ] Depends On (Kernel + other MiniApps if any)
- [ ] Scope (in-scope and out-of-scope items)
- [ ] Requirements Covered (Platform FRs with priority)
- [ ] Platform Components (IDs from DESIGN)
- [ ] Integration Points (external integrations)
- [ ] Target Release (quarter)

**Partial Completion Handling**:

If DECOMPOSITION-PLATFORM cannot be completed in a single session:
1. Checkpoint progress with completed MiniApp entries
2. Add `status: DRAFT` to document header
3. Mark incomplete MiniApps with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate overall status ID: `cpt-{platform}-status-overall`
- [ ] Generate MiniApp IDs: `cpt-{platform}-miniapp-{slug}`
- [ ] Link to Platform FR IDs
- [ ] Link to Platform component IDs
- [ ] Link to Platform integration IDs
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify all Platform FRs are covered by at least one MiniApp
- [ ] Verify all DESIGN components are allocated
- [ ] Verify MiniApp boundaries don't overlap
- [ ] Verify dependency graph is acyclic (except Kernel)

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

- [ ] Read `config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Decomposition-Specific Validation

- [ ] All Platform FRs have MiniApp coverage
- [ ] All DESIGN components are allocated to MiniApps or Kernel
- [ ] MiniApp dependencies are justified
- [ ] No circular dependencies (except through Kernel)
- [ ] Release roadmap is realistic
- [ ] Kernel components are shared correctly

### Validation Report Format

```
DECOMPOSITION-PLATFORM Validation Report
════════════════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Decomposition-Specific: PASS/FAIL (N issues)

Coverage:
- Platform FRs covered: N/M (X%)
- DESIGN components allocated: N/M (X%)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing Platform DESIGN

- [ ] If Platform DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-PLATFORM` first (recommended)
  - Option 2: Continue without DESIGN (component allocation will be incomplete)
  - Document "DESIGN pending" in DECOMPOSITION header

### Missing Platform PRD

- [ ] If Platform PRD not found:
  - Option 1: Run `/cf-generate PRD-PLATFORM` first
  - Option 2: Continue without PRD (requirements coverage will be incomplete)
  - Document requirements assumptions made

### MiniApp Boundary Uncertainty

- [ ] If uncertain about MiniApp boundaries:
  - Ask user for guidance
  - Consider user actor boundaries (Student, Instructor, Admin)
  - Consider capability groupings (Learn, Assess, Communicate)
  - Document decision rationale

### Escalation

- [ ] Ask user when MiniApp scope is unclear
- [ ] Ask user when release priorities conflict
- [ ] Ask user when dependency decisions need business input

---

## Next Steps

### Options

- [ ] DECOMPOSITION-PLATFORM complete → `/cf-generate PRD-MINIAPP` — create MiniApp PRD
- [ ] DECOMPOSITION-PLATFORM complete → `/cf-generate DESIGN-MINIAPP` — create MiniApp DESIGN
- [ ] DESIGN missing → `/cf-generate DESIGN-PLATFORM` — create Platform DESIGN first
- [ ] PRD missing → `/cf-generate PRD-PLATFORM` — create Platform PRD first
- [ ] DECOMPOSITION needs revision → continue editing DECOMPOSITION-PLATFORM
- [ ] Ready for MiniApp work → create MiniApp folder structure

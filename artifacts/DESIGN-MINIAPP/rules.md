# DESIGN-MINIAPP Rules

**Artifact**: DESIGN-MINIAPP  
**Kit**: mobile-superapp  
**Level**: L1 (MiniApp)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` — parent PRD reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md` for semantic guidance
- [ ] Read parent MiniApp PRD for context
- [ ] Read Platform DESIGN for architectural context
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] DESIGN-MINIAPP follows `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md` structure
- [ ] All required sections present and non-empty:
  - MiniApp Overview (purpose, capabilities, architecture drivers)
  - Module Structure (KMP, Android, iOS modules)
  - Navigation Architecture
  - State Management (MVI pattern)
  - Domain Model
  - API Layer
  - Kernel Integration
  - Traceability
- [ ] All IDs follow `cpt-{miniapp}-{kind}-{slug}` convention
- [ ] References to MiniApp PRD are valid
- [ ] References to Platform DESIGN are valid
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Module structure covers all three platforms:
  - KMP shared logic (`constructor-sdk/feature/{miniapp}/`)
  - Android UI (`android-app/feature/{miniapp}/`)
  - iOS UI (`ios-app/Features/{MiniApp}/`)
- [ ] MVI pattern documented with State, Intent, Effect classes
- [ ] Navigation graph includes deep link support
- [ ] Kernel integration specifies required services (Auth, Storage, Network)
- [ ] MiniApp contract interface implementation documented

### Traceability

- [ ] Every MiniApp capability traces to a MiniApp PRD FR
- [ ] NFR allocation traces to MiniApp PRD NFRs
- [ ] Module components trace to Platform DESIGN patterns
- [ ] ADR references provided for key decisions

### Versioning

- [ ] When editing existing DESIGN: increment version in document header
- [ ] When changing component definition: add `-v{N}` suffix to ID or increment

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md` for semantic guidance
- [ ] Read MiniApp PRD for requirements
- [ ] Read Platform DESIGN for architectural context

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| MiniApp Overview | Document purpose, capabilities mapping, NFR allocation |
| Module Structure | Define KMP/Android/iOS module organization |
| Navigation | Design navigation graph, deep links, screen inventory |
| State Management | Define MVI pattern with State/Intent/Effect |
| Domain Model | Define entities, repository interfaces |
| API Layer | Document BFF endpoints, WebSocket connections |
| Kernel Integration | Specify kernel services usage, MiniApp contract |

**Partial Completion Handling**:

If DESIGN-MINIAPP cannot be completed in a single session:
1. Checkpoint progress with completed sections
2. Add `status: DRAFT` to document header
3. Mark incomplete sections with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate component IDs: `cpt-{miniapp}-component-{slug}`
- [ ] Generate entity IDs: `cpt-{miniapp}-entity-{slug}`
- [ ] Generate repo IDs: `cpt-{miniapp}-repo-{slug}`
- [ ] Generate navigation IDs: `cpt-{miniapp}-component-navigation`
- [ ] Link to MiniApp PRD capabilities
- [ ] Reference Platform DESIGN principles
- [ ] Reference relevant ADRs
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify PRD traceability
- [ ] Verify Platform DESIGN alignment

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

- [ ] Read `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Mobile-Specific Validation

- [ ] All three platforms (KMP, Android, iOS) have module definitions
- [ ] MVI pattern is consistently applied
- [ ] Navigation includes deep link handling
- [ ] Kernel integration is complete
- [ ] MiniApp contract interface is implemented

### Validation Report Format

```
DESIGN-MINIAPP Validation Report
═══════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Mobile-Specific: PASS/FAIL (N issues)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing MiniApp PRD

- [ ] If parent MiniApp PRD not found:
  - Option 1: Run `/cf-generate PRD-MINIAPP` first (recommended)
  - Option 2: Continue without PRD (DESIGN will lack traceability)
  - Document "PRD pending" in DESIGN header

### Missing Platform DESIGN

- [ ] If Platform DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-PLATFORM` first
  - Option 2: Continue with assumptions documented
  - Document architectural assumptions made

### Escalation

- [ ] Ask user when uncertain about module boundaries
- [ ] Ask user when Kernel integration requires undocumented services
- [ ] Ask user when navigation patterns need clarification

---

## Next Steps

### Options

- [ ] DESIGN-MINIAPP complete → `/cf-generate DECOMPOSITION-MINIAPP` — create epics manifest
- [ ] Need architecture decision → `/cf-generate ADR` — document key decision
- [ ] PRD missing/incomplete → `/cf-generate PRD-MINIAPP` — create/update PRD first
- [ ] DESIGN needs revision → continue editing DESIGN-MINIAPP
- [ ] Ready for Epic → `/cf-generate PRD-EPIC` — create Epic-level PRD

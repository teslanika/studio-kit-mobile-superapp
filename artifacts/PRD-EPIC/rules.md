# PRD-EPIC Rules

**Artifact**: PRD-EPIC  
**Kit**: mobile-superapp  
**Level**: L2 (Epic)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md` — parent MiniApp PRD reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md` for semantic guidance
- [ ] Read parent MiniApp PRD for context
- [ ] Read MiniApp DESIGN for architectural context
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] PRD-EPIC follows `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` structure
- [ ] All required sections present and non-empty:
  - Overview (purpose, scope, epic type, traces to parent)
  - Actors & Context (actors, entry points)
  - Functional Requirements (core, state, error handling)
  - UI/UX Requirements (layout, components, interactions)
  - Data Requirements (required data, API contracts)
  - Traceability Matrix
  - Acceptance Criteria
- [ ] All IDs follow `cpt-{miniapp}-epic-{epic}-{kind}-{slug}` convention
- [ ] References to MiniApp PRD are valid
- [ ] Epic type is specified: Screen | Capability | Flow | Widget
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Screen states defined (Loading, Content, Empty, Error, Offline)
- [ ] Entry points include:
  - Navigation (tab bar, menu, parent screen)
  - Deep links with format `constructor://{miniapp}/{epic}?{params}`
  - Push notifications (if applicable)
- [ ] UI layout uses platform-appropriate patterns
- [ ] Interactions are touch-optimized (tap, swipe, long press)
- [ ] Error handling includes recovery actions

### Traceability

- [ ] Every Epic FR traces to MiniApp PRD FR (details relationship)
- [ ] Epic-specific FRs are tagged `epic-specific` with rationale
- [ ] Widget IDs use `cpt-{miniapp}-{epic}-widget-{slug}` format
- [ ] Indirect Platform trace documented
- [ ] Traceability matrix documents:
  - MiniApp FR → Epic FR coverage
  - Epic FR → Feature mapping (planned)
- [ ] Full traceability chain shown (Platform → MiniApp → Epic)

### Versioning

- [ ] When editing existing PRD: increment version in document header
- [ ] When changing requirement: update version field in requirement table

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md` for semantic guidance
- [ ] Read MiniApp PRD for parent requirements
- [ ] Read MiniApp DESIGN for architectural patterns
- [ ] Identify which MiniApp FRs this Epic details

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Overview | Document purpose, scope, epic type, parent traces |
| Actors & Context | Define actors' roles in epic, entry points |
| Core Requirements | Detail FRs with UI elements, acceptance criteria |
| State Requirements | Define all screen states and conditions |
| Error Handling | Document error types, messages, recovery actions |
| UI/UX | Design screen layout, components, interactions |
| Data | Specify required data, sources, caching, API contracts |
| Traceability | Build coverage matrix for MiniApp → Epic |

**Partial Completion Handling**:

If PRD-EPIC cannot be completed in a single session:
1. Checkpoint progress with completed sections
2. Add `status: DRAFT` to document header
3. Mark incomplete sections with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate Epic PRD anchor: `cpt-{miniapp}-epic-{epic}-prd`
- [ ] Generate Epic FR IDs: `cpt-{miniapp}-epic-{epic}-fr-{slug}`
- [ ] Generate state ID: `cpt-{miniapp}-epic-{epic}-state`
- [ ] Generate widget IDs: `cpt-{miniapp}-{epic}-widget-{slug}`
- [ ] Link to MiniApp PRD requirements
- [ ] Document indirect Platform trace
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify every FR is implementable at Epic scope
- [ ] Verify all states have UI behavior defined
- [ ] Verify MiniApp traceability is complete

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

- [ ] Read `config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Epic-Specific Validation

- [ ] Epic type is appropriate for content
- [ ] All screen states are defined and have UI behavior
- [ ] All entry points have deep link format
- [ ] All error scenarios have recovery actions
- [ ] All API contracts are specified
- [ ] Component list is complete for screen layout

### Validation Report Format

```
PRD-EPIC Validation Report
══════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Epic-Specific: PASS/FAIL (N issues)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing MiniApp PRD

- [ ] If parent MiniApp PRD not found:
  - Option 1: Run `/cf-generate PRD-MINIAPP` first (recommended)
  - Option 2: Continue without MiniApp PRD (Epic will lack traceability)
  - Document "MiniApp PRD pending" in Epic PRD header

### Missing MiniApp DESIGN

- [ ] If MiniApp DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-MINIAPP` first
  - Option 2: Continue with assumptions documented
  - Document architectural assumptions made

### Unclear Epic Scope

- [ ] If uncertain about what belongs in this Epic:
  - Ask user for scope clarification
  - Reference MiniApp DECOMPOSITION for epic boundaries
  - Mark scope section for review

### Escalation

- [ ] Ask user when uncertain about screen states
- [ ] Ask user when API contracts are unclear
- [ ] Ask user when UI/UX decisions need stakeholder input

---

## Next Steps

### Options

- [ ] PRD-EPIC complete → `/cf-generate DESIGN-EPIC` — create Epic technical design
- [ ] Need MiniApp context → `/cf-generate PRD-MINIAPP` — create MiniApp PRD first
- [ ] PRD needs revision → continue editing PRD-EPIC
- [ ] Ready for features → `/cf-generate DECOMPOSITION-EPIC` — decompose into features
- [ ] Ready for implementation → `/cf-generate FEATURE-MOBILE` — create feature spec

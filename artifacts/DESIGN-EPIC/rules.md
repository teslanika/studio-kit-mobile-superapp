# DESIGN-EPIC Rules

**Artifact**: DESIGN-EPIC  
**Kit**: mobile-superapp  
**Level**: L2 (Epic)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` — parent Epic PRD reference
- `config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md` — parent MiniApp DESIGN reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md` for semantic guidance
- [ ] Read parent Epic PRD for requirements
- [ ] Read parent MiniApp DESIGN for architectural context
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] DESIGN-EPIC follows `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` structure
- [ ] All required sections present and non-empty:
  - Epic Overview (purpose, requirements coverage, drivers)
  - Component Architecture (diagram, screens, widgets)
  - State Management (state, intents, effects)
  - Data Flow (use cases, repositories, API contracts)
  - Navigation (entry/exit points, parameters)
  - Platform-Specific Considerations (Android, iOS, WebView)
  - Error Handling (error states, offline behavior)
  - Traceability
- [ ] All IDs follow `cpt-{miniapp}-{epic}-{kind}-{slug}` convention
- [ ] References to Epic PRD are valid
- [ ] References to MiniApp DESIGN are valid
- [ ] Component diagram present (Mermaid flowchart)
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Platform implementation table for each component:
  - KMP module location
  - Android component location
  - iOS component location
- [ ] MVI pattern documented with State, Intent, Effect classes
- [ ] Use cases have Input/Output types and step documentation
- [ ] Repository operations specify caching strategy
- [ ] Navigation includes deep link format
- [ ] Platform-specific sections for Android (Compose) and iOS (SwiftUI)
- [ ] WebView integration documented (if applicable)

### Traceability

- [ ] Requirements coverage table maps Epic PRD FRs to design responses
- [ ] ADR references provided for key decisions
- [ ] Screen/widget IDs link to Epic PRD components
- [ ] Use case IDs link to Epic PRD requirements
- [ ] Links to parent documents (Epic PRD, MiniApp DESIGN)

### Versioning

- [ ] When editing existing DESIGN: increment version in document header
- [ ] When changing component definition: add `-v{N}` suffix to ID or increment

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md` for semantic guidance
- [ ] Read Epic PRD for requirements
- [ ] Read MiniApp DESIGN for architectural patterns
- [ ] Identify which Epic FRs this DESIGN addresses

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Epic Overview | Document purpose, requirements coverage, ADRs |
| Component Architecture | Create component diagram, document screens/widgets |
| State Management | Define MVI State/Intent/Effect classes |
| Data Flow | Document use cases, repositories, API contracts |
| Navigation | Define entry/exit points, deep links, parameters |
| Platform-Specific | Document Android Compose, iOS SwiftUI specifics |
| Error Handling | Define error states, offline behavior |

**Partial Completion Handling**:

If DESIGN-EPIC cannot be completed in a single session:
1. Checkpoint progress with completed sections
2. Add `status: DRAFT` to document header
3. Mark incomplete sections with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate component overview ID: `cpt-{miniapp}-epic-{epic}-component-overview`
- [ ] Generate screen IDs: `cpt-{miniapp}-{epic}-screen-{slug}`
- [ ] Generate widget IDs: `cpt-{miniapp}-{epic}-widget-{slug}`
- [ ] Generate state ID: `cpt-{miniapp}-{epic}-state`
- [ ] Generate use case IDs: `cpt-{miniapp}-{epic}-usecase-{slug}`
- [ ] Generate repo IDs: `cpt-{miniapp}-{epic}-repo-{slug}`
- [ ] Generate API IDs: `cpt-{miniapp}-{epic}-api-{slug}`
- [ ] Generate nav ID: `cpt-{miniapp}-{epic}-nav`
- [ ] Generate platform IDs: `cpt-{miniapp}-{epic}-android`, `cpt-{miniapp}-{epic}-ios`
- [ ] Generate offline ID: `cpt-{miniapp}-{epic}-offline`
- [ ] Link to Epic PRD requirements
- [ ] Reference MiniApp DESIGN patterns
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify Epic PRD traceability
- [ ] Verify MiniApp DESIGN alignment
- [ ] Verify MVI pattern is consistent

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

- [ ] Read `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Epic-Specific Validation

- [ ] Component diagram accurately represents architecture
- [ ] All screens have platform implementation table
- [ ] All widgets have states and props documented
- [ ] MVI State/Intent/Effect are complete
- [ ] All use cases have steps documented
- [ ] Navigation includes deep link handling
- [ ] Error handling covers all error types
- [ ] Offline behavior is defined (if applicable)

### Validation Report Format

```
DESIGN-EPIC Validation Report
═════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Epic-Specific: PASS/FAIL (N issues)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing Epic PRD

- [ ] If parent Epic PRD not found:
  - Option 1: Run `/cf-generate PRD-EPIC` first (recommended)
  - Option 2: Continue without PRD (DESIGN will lack traceability)
  - Document "PRD pending" in DESIGN header

### Missing MiniApp DESIGN

- [ ] If parent MiniApp DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-MINIAPP` first
  - Option 2: Continue with assumptions documented
  - Document architectural assumptions made

### Escalation

- [ ] Ask user when uncertain about component boundaries
- [ ] Ask user when API contracts are unavailable
- [ ] Ask user when platform-specific behavior needs clarification

---

## Next Steps

### Options

- [ ] DESIGN-EPIC complete → `/cf-generate DECOMPOSITION-EPIC` — create features manifest
- [ ] Need architecture decision → `/cf-generate ADR` — document key decision
- [ ] PRD missing/incomplete → `/cf-generate PRD-EPIC` — create/update PRD first
- [ ] DESIGN needs revision → continue editing DESIGN-EPIC
- [ ] Ready for Feature → `/cf-generate FEATURE-MOBILE` — create feature specification
- [ ] MiniApp DESIGN missing → `/cf-generate DESIGN-MINIAPP` — create MiniApp DESIGN first

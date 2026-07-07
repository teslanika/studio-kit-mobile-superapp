# FEATURE-MOBILE Rules

**Artifact**: FEATURE-MOBILE  
**Kit**: mobile-superapp  
**Level**: L3 (Feature)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md` — semantic quality criteria
- `config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md` — parent Epic PRD reference
- `config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md` — parent Epic DESIGN reference

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

- [ ] Load `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md` for semantic guidance
- [ ] Read Epic PRD for requirements context
- [ ] Read Epic DESIGN for architectural context
- [ ] Read Epic DECOMPOSITION for feature boundaries
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats
- [ ] Load `{cf-studio-path}/.core/architecture/specs/cdsl.md` for CDSL syntax

---

## Requirements

### Structural

- [ ] FEATURE-MOBILE follows `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md` structure
- [ ] All required sections present and non-empty:
  - Feature Context (overview, purpose, actors, references)
  - Actor Flows (CDSL) — user-facing interactions
  - Platform Implementation (CDSL) — KMP, Android, iOS, WebView
  - States (CDSL) — state machine definition
  - Definitions of Done
  - Acceptance Criteria
  - Traceability
- [ ] All IDs follow appropriate conventions:
  - Feature ID: `cpt-{miniapp}-feature-{slug}`
  - Flow ID: `cpt-{miniapp}-flow-{feature-slug}-{slug}`
  - Algo ID: `cpt-{miniapp}-algo-{feature-slug}-{platform}`
  - State ID: `cpt-{miniapp}-state-{feature-slug}`
  - DoD ID: `cpt-{miniapp}-dod-{feature-slug}-{slug}`
- [ ] All CDSL steps have `inst-{id}` markers for implementation tracking
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific (CDSL Flows)

- [ ] Actor Flows use CDSL syntax:
  - Steps with priority: `[ ] - p{N} - {description} - inst-{id}`
  - Conditionals: `**IF** {condition}`, `**ELSE**`
  - API calls: `API: {METHOD} /path (summary)`
  - DB operations: `DB: {OPERATION} {table} ({key columns})`
  - Returns: `**RETURN** {result}`
- [ ] Platform Implementation uses CDSL for each platform:
  - KMP Shared Logic (ViewModel, UseCase, Repository steps)
  - Android UI (Compose screen steps)
  - iOS UI (SwiftUI view steps)
  - WebView Integration (if applicable)
- [ ] State machine uses CDSL format:
  - States, Initial State, Transitions
  - `**FROM** {state} **TO** {state} **WHEN** {trigger}`
- [ ] Each flow has Success and Error scenarios

### Traceability

- [ ] Feature traces to Epic PRD requirements
- [ ] Actor Flows implement use cases from Epic DESIGN
- [ ] Platform Implementation traces to Epic DESIGN components
- [ ] Definitions of Done specify:
  - Implements (flow IDs)
  - Touches (KMP, Android, iOS, API)
  - Verification (tests)
- [ ] Links to parent documents and implementation references

### Versioning

- [ ] When editing existing FEATURE: increment version in document header
- [ ] When changing flow steps: preserve `inst-{id}` markers for continuity

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md` for semantic guidance
- [ ] Load CDSL syntax reference
- [ ] Read Epic PRD for requirements
- [ ] Read Epic DESIGN for components and use cases
- [ ] Read Epic DECOMPOSITION for feature scope

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Feature Context | Document overview, purpose, actors, references |
| Actor Flows | Write CDSL flows for user interactions |
| KMP Implementation | Document ViewModel, UseCase, Repository steps |
| Android Implementation | Document Compose screen steps |
| iOS Implementation | Document SwiftUI view steps |
| WebView Integration | Document JS bridge (if applicable) |
| States | Define state machine with transitions |
| Definitions of Done | Specify implementable work items |
| Acceptance Criteria | Write testable criteria |

**CDSL Writing Guidelines**:

For Actor Flows:
```markdown
1. [ ] - `p1` - Actor opens {screen} - `inst-{id}`
2. [ ] - `p1` - **IF** {condition} - `inst-{id}`
   1. [ ] - `p1` - System {action} - `inst-{id}`
3. [ ] - `p1` - API: `GET /api/v1/mobile/{path}` (response summary) - `inst-{id}`
4. [ ] - `p1` - **RETURN** {result} - `inst-{id}`
```

For Platform Implementation:
```markdown
1. [ ] - `p1` - Receive intent from UI - `inst-kmp-1`
2. [ ] - `p1` - **TRY** - `inst-kmp-2`
   1. [ ] - `p1` - Call repository - `inst-kmp-2a`
3. [ ] - `p1` - **CATCH** {error} - `inst-kmp-3`
   1. [ ] - `p1` - Map to domain error - `inst-kmp-3a`
```

**Partial Completion Handling**:

If FEATURE-MOBILE cannot be completed in a single session:
1. Checkpoint progress with completed sections
2. Add `status: DRAFT` to document header
3. Mark incomplete flows with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate feature status ID: `cpt-{miniapp}-featstatus-{feature-slug}`
- [ ] Generate feature ID: `cpt-{miniapp}-feature-{slug}`
- [ ] Generate flow IDs: `cpt-{miniapp}-flow-{feature-slug}-{slug}`
- [ ] Generate algo IDs: `cpt-{miniapp}-algo-{feature-slug}-{platform}`
- [ ] Generate state ID: `cpt-{miniapp}-state-{feature-slug}`
- [ ] Generate DoD IDs: `cpt-{miniapp}-dod-{feature-slug}-{slug}`
- [ ] Generate unique `inst-{id}` for each CDSL step
- [ ] Link to Epic PRD requirements
- [ ] Link to Epic DESIGN components
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify CDSL syntax is correct
- [ ] Verify all flows have success and error scenarios
- [ ] Verify all platforms have implementation steps
- [ ] Verify DoDs are implementable

### Phase 5: Table of Contents

- [ ] Run `cfs toc <path>` to generate/update Table of Contents
- [ ] Verify TOC is present and complete

---

## Validation

### Phase 1: Structural Validation

- [ ] Run `cfs validate --artifact <path>` for:
  - Template structure compliance
  - ID format validation
  - CDSL syntax validation
  - Cross-reference validity
  - No placeholders

### Phase 2: Semantic Validation

- [ ] Read `config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: CDSL-Specific Validation

- [ ] All CDSL steps have `inst-{id}` markers
- [ ] All steps have priority (`p1`, `p2`, `p3`)
- [ ] Conditionals (`IF/ELSE`, `TRY/CATCH`, `WHEN`) are properly nested
- [ ] API calls specify method, path, and summary
- [ ] State transitions are complete (all states reachable)
- [ ] Platform implementations cover KMP, Android, iOS

### Phase 4: Implementation Readiness Validation

- [ ] Definitions of Done are specific and implementable
- [ ] Each DoD specifies which flows it implements
- [ ] Each DoD lists modules/components touched
- [ ] Each DoD has verification criteria (tests)
- [ ] Acceptance criteria are testable

### Validation Report Format

```
FEATURE-MOBILE Validation Report
════════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
CDSL: PASS/FAIL (N issues)
Implementation Readiness: PASS/FAIL (N issues)

Coverage:
- Actor Flows: N defined
- Platform Implementations: KMP: ✓/✗, Android: ✓/✗, iOS: ✓/✗
- States: N states, M transitions
- DoDs: N defined

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing Epic DESIGN

- [ ] If Epic DESIGN not found:
  - Option 1: Run `/cf-generate DESIGN-EPIC` first (recommended)
  - Option 2: Continue without DESIGN (implementation details will be assumptions)
  - Document "DESIGN pending" in FEATURE header

### Missing Epic PRD

- [ ] If Epic PRD not found:
  - Option 1: Run `/cf-generate PRD-EPIC` first
  - Option 2: Continue without PRD (requirements traceability will be incomplete)
  - Document requirements assumptions made

### CDSL Syntax Errors

- [ ] If CDSL validation fails:
  - Check step format: `[ ] - p{N} - {description} - inst-{id}`
  - Check conditional keywords: `**IF**`, `**ELSE**`, `**TRY**`, `**CATCH**`, `**WHEN**`
  - Check nesting (indentation with numbers: 1., 1.1., etc.)
  - Refer to CDSL syntax reference

### Escalation

- [ ] Ask user when flow scenarios are unclear
- [ ] Ask user when API contracts are unavailable
- [ ] Ask user when platform-specific behavior needs clarification

---

## Next Steps

### Options

- [ ] FEATURE-MOBILE complete → `/cf-generate IMPL-KMP` — create KMP implementation reference
- [ ] FEATURE-MOBILE complete → `/cf-generate IMPL-ANDROID` — create Android implementation reference
- [ ] FEATURE-MOBILE complete → `/cf-generate IMPL-IOS` — create iOS implementation reference
- [ ] DESIGN missing → `/cf-generate DESIGN-EPIC` — create Epic DESIGN first
- [ ] PRD missing → `/cf-generate PRD-EPIC` — create Epic PRD first
- [ ] FEATURE needs revision → continue editing FEATURE-MOBILE
- [ ] Ready for implementation → start coding with FEATURE as spec

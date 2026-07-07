# DESIGN-PLATFORM Rules

**Artifact**: DESIGN-PLATFORM  
**Kit**: mobile-superapp  
**Level**: L0 (Platform)

**Dependencies**:
- `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/template.md` — structural reference
- `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md` — semantic quality criteria
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

- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md` for semantic guidance
- [ ] Read Platform PRD for requirements
- [ ] Load `config/kits/mobile-superapp/constraints.toml` for kit-level constraints
- [ ] Load `{cf-studio-path}/.core/architecture/specs/traceability.md` for ID formats

---

## Requirements

### Structural

- [ ] DESIGN-PLATFORM follows `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/template.md` structure
- [ ] All required sections present and non-empty:
  - Platform Architecture Overview (vision, drivers, layers)
  - Cross-Platform Strategy (native vs WebView, KMP scope, code sharing)
  - MiniApp Architecture (container model, lifecycle, communication)
  - Shared Kernel (auth, storage, network, notifications)
  - External Integrations
  - Traceability
- [ ] All IDs follow `cpt-{platform}-{kind}-{slug}` convention
- [ ] References to Platform PRD are valid
- [ ] Architecture diagrams are present (ASCII or Mermaid)
- [ ] No placeholder content (TODO, TBD, FIXME)
- [ ] No duplicate IDs within document

### Mobile-Specific

- [ ] Platform layers are clearly defined:
  - Presentation (iOS Native, Android Native, WebView Container)
  - Application (KMP SDK, ViewModels, Use Cases)
  - Domain (Entities, Business Rules)
  - Infrastructure (Network, Storage, Platform APIs)
- [ ] Native vs WebView decision matrix provided for all content types
- [ ] KMP SDK scope clearly defined (included/not included)
- [ ] Code sharing matrix shows platform coverage
- [ ] MiniApp container model with Kernel integration
- [ ] MiniApp interface contract (Kotlin) documented

### Traceability

- [ ] Architecture drivers trace to Platform PRD FRs
- [ ] NFR allocation traces to Platform PRD NFRs with:
  - Allocated component/mechanism
  - Design response
  - Verification approach
- [ ] ADR references provided for key architectural decisions
- [ ] Component IDs link to implementation modules

### Versioning

- [ ] When editing existing DESIGN: increment version in document header
- [ ] When changing architecture principle: add `-v{N}` suffix to ID or increment
- [ ] Document ADR for significant architectural changes

---

## Tasks

### Phase 1: Setup

- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/template.md` for structure
- [ ] Load `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md` for semantic guidance
- [ ] Read Platform PRD for requirements
- [ ] Identify key architecture drivers from PRD

### Phase 2: Content Creation

Apply checklist semantics during creation:

| Checklist Category | Generation Task |
|-------------------|-----------------|
| Architecture Overview | Document vision, drivers, layer diagram |
| Cross-Platform Strategy | Define native/WebView decisions, KMP scope |
| MiniApp Architecture | Design container model, lifecycle, communication |
| Shared Kernel | Document Auth, Storage, Network, Notifications modules |
| External Integrations | Define integration points with direction, protocol |
| Traceability | Link to PRD, ADRs, decomposition |

**Partial Completion Handling**:

If DESIGN-PLATFORM cannot be completed in a single session:
1. Checkpoint progress with completed sections
2. Add `status: DRAFT` to document header
3. Mark incomplete sections with `INCOMPLETE: {reason}`
4. Document resumption point

### Phase 3: IDs and References

- [ ] Generate layer IDs: `cpt-{platform}-layer-{slug}`
- [ ] Generate principle IDs: `cpt-{platform}-principle-{slug}`
- [ ] Generate component IDs: `cpt-{platform}-component-{slug}`
- [ ] Generate state IDs: `cpt-{platform}-state-{slug}`
- [ ] Generate integration IDs: `cpt-{platform}-integration-{slug}`
- [ ] Link to Platform PRD requirements
- [ ] Reference relevant ADRs
- [ ] Verify uniqueness with `cfs list-ids`

### Phase 4: Quality Check

- [ ] Self-review against `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md` MUST HAVE items
- [ ] Ensure no MUST NOT HAVE violations
- [ ] Verify PRD traceability complete
- [ ] Verify all layers have clear responsibility
- [ ] Verify Kernel modules have technology specified

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

- [ ] Read `config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md` in full
- [ ] For each MUST HAVE item: check if requirement is met
- [ ] For each MUST NOT HAVE item: scan document for violations

### Phase 3: Architecture Validation

- [ ] All platform layers are documented
- [ ] Native vs WebView decision matrix is complete
- [ ] KMP SDK scope is clearly bounded
- [ ] MiniApp interface contract is implementable
- [ ] All Kernel modules have clear responsibilities
- [ ] All external integrations have protocol specified

### Validation Report Format

```
DESIGN-PLATFORM Validation Report
═════════════════════════════════

Structural: PASS/FAIL
Semantic: PASS/FAIL (N issues)
Architecture: PASS/FAIL (N issues)

Issues:
- [SEVERITY] CHECKLIST-ID: Description
```

---

## Error Handling

### Missing Platform PRD

- [ ] If Platform PRD not found:
  - Option 1: Run `/cf-generate PRD-PLATFORM` first (recommended)
  - Option 2: Continue without PRD (DESIGN will lack requirements traceability)
  - Document "PRD pending" in DESIGN header

### Technology Decision Uncertainty

- [ ] If uncertain about technology choices:
  - Document decision as ADR with options analysis
  - Mark decision as PENDING REVIEW
  - Ask user for stakeholder input

### Escalation

- [ ] Ask user when architecture trade-offs need business input
- [ ] Ask user when external integration contracts are unavailable
- [ ] Ask user when performance/security NFRs need specific targets

---

## Next Steps

### Options

- [ ] DESIGN-PLATFORM complete → `/cf-generate DECOMPOSITION-PLATFORM` — create MiniApp manifest
- [ ] Need architecture decision → `/cf-generate ADR` — document key decision
- [ ] PRD missing/incomplete → `/cf-generate PRD-PLATFORM` — create/update PRD first
- [ ] DESIGN needs revision → continue editing DESIGN-PLATFORM
- [ ] Ready for MiniApp → `/cf-generate PRD-MINIAPP` — create MiniApp-level PRD
- [ ] Ready for MiniApp DESIGN → `/cf-generate DESIGN-MINIAPP` — create MiniApp technical design

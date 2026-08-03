# DECOMPOSITION-MINIAPP Rules

**Artifact**: DECOMPOSITION-MINIAPP
**Kit**: mobile-superapp
**Level**: L1 (MiniApp)

```pdsl
UNIT DecompositionMiniappAuthoring

PURPOSE:
  Author or revise a MiniApp-level decomposition that breaks the MiniApp DESIGN
  into epics (screens, capabilities, flows) with full coverage.

WHEN:
  - REQUIRE authoring or revising a DECOMPOSITION-MINIAPP

DO:
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/template.md for structure
  - LOAD config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md for the MiniApp-layer delta over that base
  - RUN read MiniApp PRD and extract FRs, NFRs, actors, and user journeys to cover
  - RUN read MiniApp DESIGN and extract components, domain entities, repositories, navigation graph, sequences, and data stores to assign
  - RUN read the parent Platform DECOMPOSITION to confirm this MiniApp's scope and dependencies
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN classify each entry as Screen, Capability, or Flow and group design elements by cohesion
  - RUN author each entry with Category, Purpose, Actors, Depends On, Scope, Out of scope, Requirements Covered, Design Principles Covered, Design Constraints Covered, Domain Model Entities, Design Components, API, Sequences, Data, Entry Points, Platform Coverage, Target Release
  - RUN author Entry Dependencies as an acyclic graph with a rationale per edge
  - RUN author the Coverage Matrix and Implementation Order
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS give each entry a unique ID cpt-{hierarchy-prefix}-epic-{slug}, a priority marker p1-p9, and a checkbox
  - ALWAYS define checkbox IDs per constraints: kind `status` (cpt-{hierarchy-prefix}-status-overall, checked when ALL entries checked) and kind `epic` (checked when that epic's PRD/DESIGN/DECOMPOSITION set is complete)
  - ALWAYS treat cpt-... occurrences outside an **ID** definition line as references (kinds: fr, nfr, principle, constraint, component, actor, seq, db, dbtable)
  - ALWAYS classify every entry as exactly one of Screen, Capability, or Flow
  - ALWAYS achieve 100% coverage: every MiniApp design component, entity, sequence, and data store is assigned to at least one epic, and every MiniApp FR/NFR is covered transitively
  - ALWAYS reference platform actors as cpt-superapp-actor-{slug}; NEVER redefine actors here
  - ALWAYS state Entry Points for each epic (navigation, deep link, or notification) consistent with the MiniApp navigation graph
  - ALWAYS state Platform Coverage (shared / Android / iOS) for each entry
  - ALWAYS make dependencies explicit and acyclic; a foundation epic is an entry point with no epic dependencies
  - ALWAYS apply ID versioning per the traceability spec; IDs stay stable through implementation
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT DecompositionMiniappOmissions

PURPOSE:
  Enforce DECOMPOSITION scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include implementation details — code, algorithms, state machines, API request/response schemas (DECOMP-NO-001, CRITICAL) — they belong in FEATURE-MOBILE
  - NEVER define requirements — FRs, NFRs, use cases, actors (DECOMP-NO-002, HIGH) — they belong in PRD-MINIAPP
  - NEVER include architecture decisions or technology rationale (DECOMP-NO-003, HIGH) — they belong in ADR and DESIGN-MINIAPP
  - NEVER leave silent omissions — an uncovered design element or a deliberate overlap must be stated with reasoning (DOC-001, CRITICAL)
  - NEVER decompose an epic into features (MINIAPP-DECOMP-NO-001, HIGH) — that belongs in DECOMPOSITION-EPIC
  - NEVER restate MiniApp module structure, domain entities, or the navigation graph (MINIAPP-DECOMP-NO-002, MEDIUM) — reference DESIGN-MINIAPP elements by ID
  - NEVER include screen layout, widget composition, or visual specification (MINIAPP-DECOMP-NO-003, MEDIUM) — they belong in PRD-EPIC and DESIGN-EPIC
```

```pdsl
UNIT DecompositionMiniappValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the DECOMPOSITION-MINIAPP.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, valid status, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md and RUN the full base semantic pass (COV, EXC, ATTR, LEV, CFG, TRC, DEP, CHK, DOC, FMT, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-MINIAPP/checklist.md and RUN the MiniApp-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every MiniApp design component and navigation destination is assigned, and every MiniApp FR/NFR is covered
  - ALWAYS maintain cascade rules — an `epic` ID is not checked until that epic's document set is complete; `status-overall` is not checked until ALL entries are checked
  - NEVER consider the DECOMPOSITION done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT DecompositionMiniappErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the DECOMPOSITION-MINIAPP template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_miniapp_design ->
    EMIT "MiniApp DESIGN not found. Recommended: run /cf-generate DESIGN-MINIAPP first — components and the navigation graph are assigned from it. Or continue with the design elements documented as assumptions."
    WAIT user.reply
  missing_platform_decomposition ->
    EMIT warning
    CONTINUE with this MiniApp's scope taken from its own PRD and the gap listed as an open dependency
  coverage_gap ->
    RUN assign the design element to an epic or document the exclusion with reasoning
  scope_overlap ->
    RUN assign to a single epic, or document the sharing with reasoning

RULES:
  - ALWAYS escalate to the user when epic granularity is unclear, when a capability spans several screens, or when release ordering needs a product decision
```

```pdsl
UNIT DecompositionMiniappNextSteps

PURPOSE:
  Offer next actions after the DECOMPOSITION-MINIAPP is complete.

DO:
  - EMIT_MENU DecompositionMiniappNextStepsMenu

MENU DecompositionMiniappNextStepsMenu:
  TITLE: DECOMPOSITION-MINIAPP next steps
  OPTIONS:
    1 -> RUN /cf-generate PRD-EPIC (start the first epic)
    2 -> RUN /cf-generate DESIGN-EPIC (design an epic)
    3 -> RUN update epic status in this decomposition
    4 -> CONTINUE DecompositionMiniappAuthoring (add or revise an entry)
    5 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

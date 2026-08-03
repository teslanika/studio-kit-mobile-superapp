# DECOMPOSITION-EPIC Rules

**Artifact**: DECOMPOSITION-EPIC
**Kit**: mobile-superapp
**Level**: L2 (Epic)

```pdsl
UNIT DecompositionEpicAuthoring

PURPOSE:
  Author or revise an Epic-level decomposition that breaks the Epic DESIGN into
  implementable features with full coverage and a per-platform implementation map.

WHEN:
  - REQUIRE authoring or revising a DECOMPOSITION-EPIC

DO:
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/template.md for structure
  - LOAD config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md for the Epic-layer delta over that base
  - RUN read Epic PRD and extract FRs, state requirements, widgets, error conditions, and acceptance criteria to cover
  - RUN read Epic DESIGN and extract components, widgets, use cases, state contracts, sequences, and caches to assign
  - RUN read the parent MiniApp DECOMPOSITION to confirm this epic's scope and dependencies
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN group design elements into features that are independently implementable, testable, and deliverable
  - RUN author each entry with Purpose, Depends On, Scope, Out of scope, Requirements Covered, Design Principles Covered, Design Constraints Covered, Domain Model Entities, Design Components, Use Cases, API, Sequences, Data, Platform Implementation
  - RUN author Feature Dependencies as an acyclic graph with a rationale per edge
  - RUN author the Coverage Matrix including the Platform Implementation Matrix, then Implementation Order and Acceptance Criteria Summary
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS give each entry a unique ID cpt-{hierarchy-prefix}-feature-{slug}, a priority marker p1-p9, and a checkbox
  - ALWAYS define checkbox IDs per constraints: kind `status` (cpt-{hierarchy-prefix}-status-overall, checked when ALL entries checked) and kind `feature` (checked when that feature's FEATURE-MOBILE spec is complete)
  - ALWAYS treat cpt-... occurrences outside an **ID** definition line as references (kinds: fr, state, principle, constraint, component, widget, usecase, seq, db)
  - ALWAYS reuse the Epic PRD widget IDs and the Epic DESIGN component IDs when listing what a feature covers; NEVER mint a new ID for an existing element
  - ALWAYS achieve 100% coverage: every epic design component, widget, use case, sequence, and cache is assigned to at least one feature, and every epic FR and state requirement is covered transitively
  - ALWAYS keep feature scopes mutually exclusive with clear boundaries
  - ALWAYS name the shared, Android, and iOS implementation targets with source locations for each feature, or justify the divergence
  - ALWAYS make dependencies explicit and acyclic; a foundation feature has no dependencies
  - ALWAYS size features so that each can be implemented and verified independently
  - ALWAYS apply ID versioning per the traceability spec; IDs stay stable through implementation
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT DecompositionEpicOmissions

PURPOSE:
  Enforce DECOMPOSITION scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include implementation details — code, algorithms, state machines, API request/response schemas (DECOMP-NO-001, CRITICAL) — they belong in FEATURE-MOBILE
  - NEVER define requirements — FRs, state requirements, use cases, actors (DECOMP-NO-002, HIGH) — they belong in PRD-EPIC
  - NEVER include architecture decisions or technology rationale (DECOMP-NO-003, HIGH) — they belong in ADR and DESIGN-EPIC
  - NEVER leave silent omissions — an uncovered design element or a deliberate overlap must be stated with reasoning (DOC-001, CRITICAL)
  - NEVER include CDSL flows, step-by-step business logic, or a Definition of Done (EPIC-DECOMP-NO-001, HIGH) — they belong in FEATURE-MOBILE
  - NEVER restate epic state contracts, intents, or effects (EPIC-DECOMP-NO-002, MEDIUM) — reference DESIGN-EPIC elements by ID
  - NEVER include test case definitions or QA scripts (EPIC-DECOMP-NO-003, MEDIUM) — they belong in FEATURE-MOBILE and code
  - NEVER include design-system token values, colors, or spacing (EPIC-DECOMP-NO-004, LOW) — visual specification belongs in the design system
```

```pdsl
UNIT DecompositionEpicValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the DECOMPOSITION-EPIC.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, valid status, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md and RUN the full base semantic pass (COV, EXC, ATTR, LEV, CFG, TRC, DEP, CHK, DOC, FMT, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-EPIC/checklist.md and RUN the Epic-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every epic design component, widget, and use case is assigned, and every epic FR and state requirement is covered
  - ALWAYS maintain cascade rules — a `feature` ID is not checked until that feature is fully implemented; `status-overall` is not checked until ALL entries are checked
  - NEVER consider the DECOMPOSITION done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT DecompositionEpicErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the DECOMPOSITION-EPIC template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_epic_design ->
    EMIT "Epic DESIGN not found. Recommended: run /cf-generate DESIGN-EPIC first — components, widgets, and use cases are assigned from it. Or continue with the design elements documented as assumptions."
    WAIT user.reply
  missing_miniapp_decomposition ->
    EMIT warning
    CONTINUE with this epic's scope taken from its own PRD and the gap listed as an open dependency
  coverage_gap ->
    RUN assign the design element to a feature or document the exclusion with reasoning
  scope_overlap ->
    RUN assign to a single feature, or document the sharing with reasoning

RULES:
  - ALWAYS escalate to the user when feature granularity is unclear, when a widget spans several features, or when platform sequencing (Android before iOS or in parallel) needs a delivery decision
```

```pdsl
UNIT DecompositionEpicNextSteps

PURPOSE:
  Offer next actions after the DECOMPOSITION-EPIC is complete.

DO:
  - EMIT_MENU DecompositionEpicNextStepsMenu

MENU DecompositionEpicNextStepsMenu:
  TITLE: DECOMPOSITION-EPIC next steps
  OPTIONS:
    1 -> RUN /cf-generate FEATURE-MOBILE (specify the first feature)
    2 -> RUN update feature status in this decomposition
    3 -> RUN /cf-analyze DESIGN-EPIC (all features implemented — validate design completion)
    4 -> CONTINUE DecompositionEpicAuthoring (add or revise an entry)
    5 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

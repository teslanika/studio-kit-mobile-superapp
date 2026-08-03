# DESIGN-EPIC Rules

**Artifact**: DESIGN-EPIC
**Kit**: mobile-superapp
**Level**: L2 (Epic)

```pdsl
UNIT DesignEpicAuthoring

PURPOSE:
  Author or revise an Epic-level technical design (screen/flow components, state
  contracts, data flow, navigation, error and offline behavior) that follows the
  template, conventions, and authoring boundaries.

WHEN:
  - REQUIRE authoring or revising a DESIGN-EPIC

DO:
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-EPIC/template.md for structure
  - LOAD config/kits/sdlc/artifacts/DESIGN/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md for the Epic-layer delta over that base
  - RUN read parent Epic PRD and extract FRs, state requirements, widgets, error conditions, entry points, and data needs
  - RUN read MiniApp DESIGN for module structure, domain model, repositories, navigation graph, and state pattern to inherit
  - RUN read existing ADRs to reuse recorded decisions instead of re-deciding them
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section guided by template prompts (Architecture Overview, Principles & Constraints, Technical Architecture, State Management, Navigation, Platform-Specific Considerations, Error Handling & Offline, Additional Context, Traceability)
  - SET design anchor = cpt-{hierarchy-prefix}-design-epic; component IDs = cpt-{hierarchy-prefix}-component-{slug}; widget IDs = cpt-{hierarchy-prefix}-widget-{slug} reusing the PRD widget IDs; state ID = cpt-{hierarchy-prefix}-state-screen; use case IDs = cpt-{hierarchy-prefix}-usecase-{slug}; repository IDs = cpt-{hierarchy-prefix}-repo-{slug}; interface IDs = cpt-{hierarchy-prefix}-interface-{slug}; contract IDs = cpt-{hierarchy-prefix}-contract-{slug}; sequence IDs = cpt-{hierarchy-prefix}-seq-{slug}; store IDs = cpt-{hierarchy-prefix}-db-{slug} and cpt-{hierarchy-prefix}-dbtable-{slug}; platform tech IDs = cpt-{hierarchy-prefix}-tech-{slug}; gating IDs = cpt-{hierarchy-prefix}-topology-{slug}
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS mark every design element as a checkbox with a priority marker: - [ ] `pN` - **ID**: `cpt-...`
  - ALWAYS map every PRD state requirement to a modelled state value, and every PRD error condition to a detection and a UI response
  - ALWAYS reuse the PRD widget IDs for the components that realize them; NEVER mint a second ID for the same widget
  - ALWAYS document each component with why it exists, its responsibility scope, its responsibility boundaries, its technology and location, and its related components by ID
  - ALWAYS reference MiniApp entities, repositories, and the navigation graph by MiniApp ID; NEVER redefine them
  - ALWAYS specify all three platform implementations (shared, Android, iOS) with source locations, or justify the divergence
  - ALWAYS specify state restoration across configuration change and process death
  - ALWAYS keep the design decision-level: state contracts, intents, effects, and signatures are in scope, method bodies are not
  - ALWAYS record a decision that has alternatives as an ADR and reference it, rather than arguing it inline
  - ALWAYS version on change: increment the header version when editing; add `-v{N}` to an ID whose meaning changed and record an ADR
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT DesignEpicOmissions

PURPOSE:
  Enforce DESIGN scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include product requirements, user stories, or acceptance criteria (BIZ-DESIGN-NO-001, HIGH) — they belong in PRD-EPIC
  - NEVER include decision rationale that supersedes an ADR (ARCH-DESIGN-NO-001, HIGH) — decisions with alternatives belong in ADR and are referenced here
  - NEVER include implementation bodies beyond illustrative signatures, state contracts, and schemas (MAINT-DESIGN-NO-001, HIGH) — method bodies belong in code
  - NEVER include implementation tasks, estimates, or sequencing (BIZ-DESIGN-NO-002, HIGH) — they belong in DECOMPOSITION-EPIC
  - NEVER include CDSL flows, step-by-step algorithms, or Definition of Done (BIZ-DESIGN-NO-003, MEDIUM) — they belong in FEATURE-MOBILE
  - NEVER include test case definitions (TEST-DESIGN-NO-001, MEDIUM) — tests belong in FEATURE/code
  - NEVER redefine MiniApp module structure, domain entities, repositories, or the navigation graph (EPIC-DESIGN-NO-001, HIGH) — they belong in DESIGN-MINIAPP and are referenced by ID
  - NEVER redefine platform layers, kernel internals, or the MiniApp container model (EPIC-DESIGN-NO-002, HIGH) — they belong in DESIGN-PLATFORM
  - NEVER include design-system token values, colors, spacing, or animation curves (EPIC-DESIGN-NO-003, MEDIUM) — visual specification belongs in the design system
  - NEVER include platform-specific coding conventions (EPIC-DESIGN-NO-004, LOW) — conventions belong in IMPL-IOS / IMPL-ANDROID / IMPL-KMP
```

```pdsl
UNIT DesignEpicValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the DESIGN-EPIC.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/DESIGN/checklist.md and RUN the full base semantic pass (Review Scope Selection, Evidence Requirements, all expertise domains, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-EPIC/checklist.md and RUN the Epic-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every PRD state requirement, widget, and error condition is realized in this design
  - NEVER consider the DESIGN done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT DesignEpicErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the DESIGN-EPIC template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_epic_prd ->
    EMIT "Parent Epic PRD not found. Recommended: run /cf-generate PRD-EPIC first — states, widgets, and error conditions are derived from it. Or continue with documented assumptions and 'PRD pending' in the header."
    WAIT user.reply
  missing_miniapp_design ->
    EMIT "MiniApp DESIGN not found. Recommended: run /cf-generate DESIGN-MINIAPP first — module structure, entities, and repositories are inherited from it. Or continue with the inherited elements documented as assumptions."
    WAIT user.reply
  backend_contract_unavailable ->
    EMIT warning
    CONTINUE with the data need stated at capability level and the missing contract listed as an open dependency

RULES:
  - ALWAYS escalate to the user when a required repository operation does not exist yet, when a state's behavior is undefined in the PRD, or when a platform divergence needs a product decision
```

```pdsl
UNIT DesignEpicNextSteps

PURPOSE:
  Offer next actions after the DESIGN-EPIC is complete.

DO:
  - EMIT_MENU DesignEpicNextStepsMenu

MENU DesignEpicNextStepsMenu:
  TITLE: DESIGN-EPIC next steps
  OPTIONS:
    1 -> RUN /cf-generate DECOMPOSITION-EPIC (break the Epic into features)
    2 -> RUN /cf-generate FEATURE-MOBILE (create a feature spec)
    3 -> RUN /cf-generate ADR (record an Epic-level decision)
    4 -> CONTINUE DesignEpicAuthoring (revise DESIGN)
    5 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

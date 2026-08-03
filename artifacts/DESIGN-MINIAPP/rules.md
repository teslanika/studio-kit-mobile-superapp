# DESIGN-MINIAPP Rules

**Artifact**: DESIGN-MINIAPP
**Kit**: mobile-superapp
**Level**: L1 (MiniApp)

```pdsl
UNIT DesignMiniappAuthoring

PURPOSE:
  Author or revise a MiniApp-level technical design (module structure, domain model,
  navigation, state management, kernel integration) that follows the template,
  conventions, and authoring boundaries.

WHEN:
  - REQUIRE authoring or revising a DESIGN-MINIAPP

DO:
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/template.md for structure
  - LOAD config/kits/sdlc/artifacts/DESIGN/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md for the MiniApp-layer delta over that base
  - RUN read parent MiniApp PRD and extract functional drivers, NFRs, and public interface declarations
  - RUN read Platform DESIGN for layers, kernel contracts, MiniApp lifecycle, and dependency rules to inherit
  - RUN read existing ADRs to reuse recorded decisions instead of re-deciding them
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section guided by template prompts (Architecture Overview, Principles & Constraints, Technical Architecture, Navigation Architecture, State Management, Additional Context, Traceability)
  - SET design anchor = cpt-{hierarchy-prefix}-design-miniapp; tech IDs = cpt-{hierarchy-prefix}-tech-{slug}; principle IDs = cpt-{hierarchy-prefix}-principle-{slug}; constraint IDs = cpt-{hierarchy-prefix}-constraint-{slug}; component IDs = cpt-{hierarchy-prefix}-component-{slug}; entity IDs = cpt-{hierarchy-prefix}-entity-{slug}; repository IDs = cpt-{hierarchy-prefix}-repo-{slug}; interface IDs = cpt-{hierarchy-prefix}-interface-{slug}; contract IDs = cpt-{hierarchy-prefix}-contract-{slug}; sequence IDs = cpt-{hierarchy-prefix}-seq-{slug}; store IDs = cpt-{hierarchy-prefix}-db-{slug} and cpt-{hierarchy-prefix}-dbtable-{slug}; topology IDs = cpt-{hierarchy-prefix}-topology-{slug}
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS mark every design element as a checkbox with a priority marker: - [ ] `pN` - **ID**: `cpt-...`
  - ALWAYS allocate every MiniApp NFR to a module, component, or mechanism with a design response and a verification approach; list inherited platform NFRs and document deviations only
  - ALWAYS document each component with why it exists, its responsibility scope, its responsibility boundaries, its technology and location, and its related components by ID
  - ALWAYS reference platform layers, kernel contracts, and the MiniApp lifecycle by platform ID; NEVER redefine them
  - ALWAYS define the module structure across shared, Android, and iOS with source locations
  - ALWAYS state the kernel services this MiniApp consumes with the contract ID and criticality
  - ALWAYS state dependency rules: kernel contracts only, no MiniApp-to-MiniApp dependency, domain depends on nothing outward
  - ALWAYS specify navigation graph, screen inventory with owning epic, and deep links with parameters and auth expectation
  - ALWAYS keep the design decision-level: interface signatures, state contracts, and schemas are in scope, method bodies are not
  - ALWAYS record a decision that has alternatives as an ADR and reference it, rather than arguing it inline
  - ALWAYS version on change: increment the header version when editing; add `-v{N}` to an ID whose meaning changed and record an ADR
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT DesignMiniappOmissions

PURPOSE:
  Enforce DESIGN scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include product requirements, user stories, or acceptance criteria (BIZ-DESIGN-NO-001, HIGH) — they belong in PRD-MINIAPP
  - NEVER include decision rationale that supersedes an ADR (ARCH-DESIGN-NO-001, HIGH) — decisions with alternatives belong in ADR and are referenced here
  - NEVER include implementation code beyond illustrative interfaces, state contracts, and schemas (MAINT-DESIGN-NO-001, HIGH) — method bodies belong in code
  - NEVER include implementation tasks, estimates, or sequencing (BIZ-DESIGN-NO-002, HIGH) — they belong in DECOMPOSITION-MINIAPP
  - NEVER include feature-level specs or CDSL flows (BIZ-DESIGN-NO-003, MEDIUM) — they belong in FEATURE-MOBILE
  - NEVER include test case definitions (TEST-DESIGN-NO-001, MEDIUM) — tests belong in FEATURE/code
  - NEVER redefine platform layers, kernel internals, or the MiniApp container model (MINIAPP-DESIGN-NO-001, HIGH) — they belong in DESIGN-PLATFORM and are referenced by ID
  - NEVER include per-screen component composition, screen state, or widget design (MINIAPP-DESIGN-NO-002, HIGH) — screen design belongs in DESIGN-EPIC
  - NEVER include platform-specific coding conventions (MINIAPP-DESIGN-NO-003, LOW) — conventions belong in IMPL-IOS / IMPL-ANDROID / IMPL-KMP
```

```pdsl
UNIT DesignMiniappValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the DESIGN-MINIAPP.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/DESIGN/checklist.md and RUN the full base semantic pass (Review Scope Selection, Evidence Requirements, all expertise domains, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-MINIAPP/checklist.md and RUN the MiniApp-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every PRD NFR is either allocated here or listed as inherited from the platform
  - ALWAYS verify every screen in the inventory names its owning epic
  - NEVER consider the DESIGN done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT DesignMiniappErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the DESIGN-MINIAPP template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_miniapp_prd ->
    EMIT "Parent MiniApp PRD not found. Recommended: run /cf-generate PRD-MINIAPP first. Or continue with documented assumptions and 'PRD pending' in the header."
    WAIT user.reply
  missing_platform_design ->
    EMIT "Platform DESIGN not found. Recommended: run /cf-generate DESIGN-PLATFORM first — layers, kernel contracts, and the MiniApp lifecycle are inherited from it. Or continue with the inherited elements documented as assumptions."
    WAIT user.reply
  kernel_contract_unavailable ->
    EMIT warning
    CONTINUE with the required kernel service named at capability level and the missing contract listed as an open dependency

RULES:
  - ALWAYS escalate to the user when a module boundary is ambiguous, when a required kernel capability does not exist yet, or when an NFR lacks a specific target to design against
```

```pdsl
UNIT DesignMiniappNextSteps

PURPOSE:
  Offer next actions after the DESIGN-MINIAPP is complete.

DO:
  - EMIT_MENU DesignMiniappNextStepsMenu

MENU DesignMiniappNextStepsMenu:
  TITLE: DESIGN-MINIAPP next steps
  OPTIONS:
    1 -> RUN /cf-generate DECOMPOSITION-MINIAPP (break the MiniApp into epics)
    2 -> RUN /cf-generate ADR (record a MiniApp architecture decision)
    3 -> RUN /cf-generate DESIGN-EPIC (create an Epic technical design)
    4 -> RUN /cf-generate PRD-EPIC (create an Epic-level PRD)
    5 -> CONTINUE DesignMiniappAuthoring (revise DESIGN)
    6 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, 5, or 6."
    WAIT user.reply
    STOP_TURN
```

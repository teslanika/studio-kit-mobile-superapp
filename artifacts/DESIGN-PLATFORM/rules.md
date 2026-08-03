# DESIGN-PLATFORM Rules

**Artifact**: DESIGN-PLATFORM
**Kit**: mobile-superapp
**Level**: L0 (Platform / Host App)

```pdsl
UNIT DesignPlatformAuthoring

PURPOSE:
  Author or revise the platform-level technical design (host app, shared kernel,
  MiniApp container model, external integrations) that follows the template,
  conventions, and authoring boundaries.

WHEN:
  - REQUIRE authoring or revising a DESIGN-PLATFORM

DO:
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/template.md for structure
  - LOAD config/kits/sdlc/artifacts/DESIGN/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md for the platform-layer delta over that base
  - RUN read parent Platform PRD and extract functional drivers, NFRs, actors, and public interface declarations
  - RUN read existing ADRs to reuse recorded decisions instead of re-deciding them
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section guided by template prompts (Architecture Overview, Principles & Constraints, Technical Architecture, Cross-Platform Strategy, MiniApp Platform Model, Additional Context, Traceability)
  - SET design anchor = cpt-{hierarchy-prefix}-design-platform; tech IDs = cpt-{hierarchy-prefix}-tech-{slug}; principle IDs = cpt-{hierarchy-prefix}-principle-{slug}; constraint IDs = cpt-{hierarchy-prefix}-constraint-{slug}; component IDs = cpt-{hierarchy-prefix}-component-{slug}; interface IDs = cpt-{hierarchy-prefix}-interface-{slug}; contract IDs = cpt-{hierarchy-prefix}-contract-{slug}; sequence IDs = cpt-{hierarchy-prefix}-seq-{slug}; store IDs = cpt-{hierarchy-prefix}-db-{slug} and cpt-{hierarchy-prefix}-dbtable-{slug}; topology IDs = cpt-{hierarchy-prefix}-topology-{slug}; integration IDs = cpt-{hierarchy-prefix}-integration-{slug}; state IDs = cpt-{hierarchy-prefix}-state-{slug}
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS mark every design element as a checkbox with a priority marker: - [ ] `pN` - **ID**: `cpt-...`
  - ALWAYS allocate every platform NFR from the PRD to a layer, component, or mechanism with a design response and a verification approach
  - ALWAYS document each component with why it exists, its responsibility scope, its responsibility boundaries, its technology and location, and its related components by ID
  - ALWAYS declare stability for every contract MiniApps consume (kernel service, navigation entry, deep link, WebView bridge)
  - ALWAYS state dependency rules explicitly: no circular kernel dependencies, MiniApps depend on kernel contracts only, platform-specific modules depend on KMP and never the reverse
  - ALWAYS keep the design decision-level: interface signatures and schemas are in scope, method bodies and production code are not
  - ALWAYS record a decision that has alternatives as an ADR and reference it, rather than arguing it inline
  - ALWAYS define the platform layers, the native/WebView split, the KMP scope, and the MiniApp lifecycle here — MiniApp designs inherit them
  - ALWAYS version on change: increment the header version when editing; add `-v{N}` to an ID whose meaning changed and record an ADR
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT DesignPlatformOmissions

PURPOSE:
  Enforce DESIGN scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include product requirements, user stories, or acceptance criteria (BIZ-DESIGN-NO-001, HIGH) — they belong in PRD-PLATFORM
  - NEVER include decision rationale that supersedes an ADR (ARCH-DESIGN-NO-001, HIGH) — decisions with alternatives belong in ADR and are referenced here
  - NEVER include implementation code beyond illustrative interfaces and schemas (MAINT-DESIGN-NO-001, HIGH) — method bodies belong in code
  - NEVER include implementation tasks, estimates, or sequencing (BIZ-DESIGN-NO-002, HIGH) — they belong in DECOMPOSITION-PLATFORM
  - NEVER include feature-level specs or CDSL flows (BIZ-DESIGN-NO-003, MEDIUM) — they belong in FEATURE-MOBILE
  - NEVER include test case definitions (TEST-DESIGN-NO-001, MEDIUM) — tests belong in FEATURE/code
  - NEVER include MiniApp-internal module structure, navigation graphs, or MiniApp state management (PLATFORM-DESIGN-NO-001, HIGH) — they belong in DESIGN-MINIAPP
  - NEVER include screen-level component or widget design (PLATFORM-DESIGN-NO-002, MEDIUM) — screen design belongs in DESIGN-EPIC
  - NEVER include platform-specific coding conventions (PLATFORM-DESIGN-NO-003, LOW) — conventions belong in IMPL-IOS / IMPL-ANDROID / IMPL-KMP
```

```pdsl
UNIT DesignPlatformValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the DESIGN-PLATFORM.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/DESIGN/checklist.md and RUN the full base semantic pass (Review Scope Selection, Evidence Requirements, all expertise domains, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/DESIGN-PLATFORM/checklist.md and RUN the platform-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every PRD NFR appears in the NFR allocation table before declaring the design complete
  - NEVER consider the DESIGN done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT DesignPlatformErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the DESIGN-PLATFORM template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_platform_prd ->
    EMIT "Parent Platform PRD not found. Recommended: run /cf-generate PRD-PLATFORM first. Or continue with documented assumptions and 'PRD pending' in the header."
    WAIT user.reply
  technology_decision_uncertain ->
    EMIT "Technology choice for {area} has viable alternatives. Recommended: record an ADR with the options analysis and reference it here."
    WAIT user.reply
  external_contract_unavailable ->
    EMIT warning
    CONTINUE with the integration documented at capability level and the missing contract listed as an open dependency

RULES:
  - ALWAYS escalate to the user when an architecture trade-off needs business input, when an external integration contract is unavailable, or when an NFR lacks a specific target to design against
```

```pdsl
UNIT DesignPlatformNextSteps

PURPOSE:
  Offer next actions after the DESIGN-PLATFORM is complete.

DO:
  - EMIT_MENU DesignPlatformNextStepsMenu

MENU DesignPlatformNextStepsMenu:
  TITLE: DESIGN-PLATFORM next steps
  OPTIONS:
    1 -> RUN /cf-generate DECOMPOSITION-PLATFORM (create the MiniApp manifest)
    2 -> RUN /cf-generate ADR (record a platform architecture decision)
    3 -> RUN /cf-generate DESIGN-MINIAPP (create a MiniApp technical design)
    4 -> RUN /cf-generate PRD-MINIAPP (create a MiniApp-level PRD)
    5 -> CONTINUE DesignPlatformAuthoring (revise DESIGN)
    6 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, 5, or 6."
    WAIT user.reply
    STOP_TURN
```

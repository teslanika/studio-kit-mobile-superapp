# PRD-MINIAPP Rules

**Artifact**: PRD-MINIAPP
**Kit**: mobile-superapp
**Level**: L1 (MiniApp)

```pdsl
UNIT PrdMiniappAuthoring

PURPOSE:
  Author or revise a MiniApp-level PRD that follows the template, conventions, and authoring boundaries.

WHEN:
  - REQUIRE authoring or revising a PRD-MINIAPP

DO:
  - LOAD config/kits/mobile-superapp/artifacts/PRD-MINIAPP/template.md for structure
  - LOAD config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md for semantic criteria
  - RUN read parent Platform PRD (architecture/PRD.md) and identify which Platform FRs this MiniApp refines
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section guided by template prompts (Overview, Actors, Functional Requirements, MiniApp NFRs, Use Cases, Dependencies, Assumptions, Risks, Traceability Matrix, Acceptance Criteria)
  - SET PRD anchor = cpt-{miniapp}-prd; FR IDs = cpt-{miniapp}-fr-{slug}; NFR IDs = cpt-{miniapp}-nfr-{slug}; use case IDs = cpt-{miniapp}-usecase-{slug}; assign priorities p1-p9 by business impact
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS mark every FR/NFR/use case as a checkbox with a priority marker: - [ ] `pN` - **ID**: `cpt-...`
  - ALWAYS state each FR as a verifiable MUST statement with Rationale and Actors fields
  - ALWAYS trace every MiniApp FR to a Platform FR (refines) or tag it `miniapp-specific` with rationale
  - ALWAYS reference platform actor IDs (cpt-superapp-actor-{slug}); NEVER redefine actors — only add MiniApp-specific context
  - ALWAYS address mobile context: offline capabilities, push notification scenarios, deep link entry points, iOS/Android parity
  - ALWAYS keep the PRD requirements-only (WHAT not HOW); express every NFR as a business-level quality requirement (user/business outcome, SLA, measurable Threshold), not a technical implementation spec
  - ALWAYS state authorization as exact per-actor/operation permissions (which actor may perform which action on which resource); NEVER restate the generic "every operation requires authentication/authorization", which is assumed
  - ALWAYS name backend dependencies at capability level (which service provides what data or operation); NEVER specify endpoints, payloads, or API contracts
  - ALWAYS version on change: increment the header version when editing; keep a changelog of significant changes
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT PrdMiniappOmissions

PURPOSE:
  Enforce PRD scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include technical implementation details (ARCH-PRD-NO-001, CRITICAL) — PRD captures what, not how
  - NEVER include architectural decisions (ARCH-PRD-NO-002, CRITICAL) — they belong in ADR
  - NEVER include implementation tasks (BIZ-PRD-NO-001, HIGH) — they belong in DECOMPOSITION-MINIAPP
  - NEVER include spec-level design (BIZ-PRD-NO-002, HIGH) — specs belong in FEATURE-MOBILE
  - NEVER include data schema definitions (DATA-PRD-NO-001, HIGH) — schemas belong in DESIGN-MINIAPP
  - NEVER include API specifications (INT-PRD-NO-001, HIGH) — no API contracts/OpenAPI, REST endpoints, HTTP methods, HTTP/REST status codes, authentication header specifications, or standardized error response formats; API contracts belong in DESIGN-MINIAPP, API design decisions in ADR
  - NEVER include test cases (TEST-PRD-NO-001, MEDIUM) — tests belong in FEATURE/code
  - NEVER include infrastructure specifications (OPS-PRD-NO-001, MEDIUM) — infra belongs in DESIGN
  - NEVER include security implementation details (SEC-PRD-NO-001, HIGH) — implementation belongs in DESIGN/code
  - NEVER include code-level documentation (MAINT-PRD-NO-001, MEDIUM) — code docs belong in code
  - NEVER redefine Platform-level requirements or duplicate Platform constraints verbatim — refine with traces instead
```

```pdsl
UNIT PrdMiniappValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the PRD-MINIAPP.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, no placeholders, no duplicate IDs)
  - LOAD config/kits/mobile-superapp/artifacts/PRD-MINIAPP/checklist.md and RUN semantic validation + report using it (MUST HAVE items, MUST NOT HAVE scan, mobile-specific criteria)
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - NEVER consider the PRD done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT PrdMiniappErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the PRD-MINIAPP template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_platform_prd ->
    EMIT "Parent Platform PRD not found. Recommended: run /cf-generate PRD-PLATFORM first. Or continue with documented assumptions and 'Platform PRD pending' in the header."
    WAIT user.reply
  unclear_scope ->
    EMIT "MiniApp scope is unclear — please clarify what is in/out of scope."
    WAIT user.reply

RULES:
  - ALWAYS escalate to the user when requirement priority is uncertain, when Platform FR mapping is unclear, when actors/personas need clarification, or when uncertain whether a checklist category is truly N/A vs missing
```

```pdsl
UNIT PrdMiniappNextSteps

PURPOSE:
  Offer next actions after the PRD-MINIAPP is complete.

DO:
  - EMIT_MENU PrdMiniappNextStepsMenu

MENU PrdMiniappNextStepsMenu:
  TITLE: PRD-MINIAPP next steps
  OPTIONS:
    1 -> RUN /cf-generate DESIGN-MINIAPP (create MiniApp technical design)
    2 -> RUN /cf-generate DECOMPOSITION-MINIAPP (break MiniApp into epics)
    3 -> RUN /cf-generate PRD-EPIC (create Epic-level PRD)
    4 -> CONTINUE PrdMiniappAuthoring (revise PRD)
    5 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

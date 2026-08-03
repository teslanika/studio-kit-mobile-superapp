# PRD-PLATFORM Rules

**Artifact**: PRD-PLATFORM
**Kit**: mobile-superapp
**Level**: L0 (Platform / Host App)

```pdsl
UNIT PrdPlatformAuthoring

PURPOSE:
  Author or revise the platform-level PRD (host app, shared kernel, cross-MiniApp
  capabilities) that follows the template, conventions, and authoring boundaries.

WHEN:
  - REQUIRE authoring or revising a PRD-PLATFORM

DO:
  - LOAD config/kits/mobile-superapp/artifacts/PRD-PLATFORM/template.md for structure
  - LOAD config/kits/sdlc/artifacts/PRD/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/PRD-PLATFORM/checklist.md for the platform-layer delta over that base
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section guided by template prompts (Overview, Actors, Operational Concept & Environment, Scope, Functional Requirements, NFRs, Public Platform Interfaces, Use Cases, Acceptance Criteria, Dependencies, Assumptions, Risks, MiniApp Map)
  - SET PRD anchor = cpt-{hierarchy-prefix}-prd; actor IDs = cpt-{hierarchy-prefix}-actor-{slug}; FR IDs = cpt-{hierarchy-prefix}-fr-{slug}; NFR IDs = cpt-{hierarchy-prefix}-nfr-{slug}; interface IDs = cpt-{hierarchy-prefix}-interface-{slug}; contract IDs = cpt-{hierarchy-prefix}-contract-{slug}; use case IDs = cpt-{hierarchy-prefix}-usecase-{slug}; assign priorities p1-p9 by business impact
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS mark every actor/FR/NFR/interface/contract/use case as a checkbox with a priority marker: - [ ] `pN` - **ID**: `cpt-...`
  - ALWAYS state each FR as a verifiable MUST statement with Rationale and Actors fields
  - ALWAYS define actors ONCE here — this is the single source of actor IDs for every MiniApp and Epic PRD
  - ALWAYS set project-wide runtime baselines here (OS minimums, device classes, connectivity and lifecycle policy) so MiniApps only document deviations
  - ALWAYS keep platform FRs to host-app and shared-kernel capabilities; delegate MiniApp-owned capabilities to the MiniApp PRD
  - ALWAYS keep the PRD requirements-only (WHAT not HOW); express every NFR as a business-level quality requirement (user/business outcome, SLA, measurable Threshold), not a technical implementation spec
  - ALWAYS state authorization as exact per-actor/operation permissions (which actor may perform which action on which resource); NEVER restate the generic "every operation requires authentication/authorization", which is assumed
  - ALWAYS declare stability and breaking-change policy for every public kernel, navigation, or deep-link contract MiniApps consume
  - ALWAYS name backend, OS, and vendor dependencies at capability level; NEVER specify endpoints, payloads, or API contracts
  - ALWAYS version on change: increment the header version when editing; keep a changelog of significant changes
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT PrdPlatformOmissions

PURPOSE:
  Enforce PRD scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include technical implementation details (ARCH-PRD-NO-001, CRITICAL) — PRD captures what, not how
  - NEVER include architectural decisions (ARCH-PRD-NO-002, CRITICAL) — they belong in ADR
  - NEVER include implementation tasks (BIZ-PRD-NO-001, HIGH) — they belong in DECOMPOSITION-PLATFORM
  - NEVER include spec-level design (BIZ-PRD-NO-002, HIGH) — specs belong in FEATURE-MOBILE
  - NEVER include data schema definitions (DATA-PRD-NO-001, HIGH) — schemas belong in DESIGN-PLATFORM
  - NEVER include API specifications (INT-PRD-NO-001, HIGH) — no API contracts/OpenAPI, REST endpoints, HTTP methods, HTTP/REST status codes, authentication header specifications, or standardized error response formats; API contracts belong in DESIGN-PLATFORM, API design decisions in ADR
  - NEVER include test cases (TEST-PRD-NO-001, MEDIUM) — tests belong in FEATURE/code
  - NEVER include infrastructure specifications (OPS-PRD-NO-001, MEDIUM) — infra belongs in DESIGN
  - NEVER include security implementation details (SEC-PRD-NO-001, HIGH) — implementation belongs in DESIGN/code
  - NEVER include code-level documentation (MAINT-PRD-NO-001, MEDIUM) — code docs belong in code
  - NEVER include MiniApp-internal requirements (PLATFORM-PRD-NO-001, HIGH) — capabilities owned by a single MiniApp belong in that MiniApp's PRD
  - NEVER include per-screen UI specifications (PLATFORM-PRD-NO-002, MEDIUM) — screen-level requirements belong in PRD-EPIC
```

```pdsl
UNIT PrdPlatformValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the PRD-PLATFORM.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/PRD/checklist.md and RUN the full base semantic pass (all expertise domains, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/PRD-PLATFORM/checklist.md and RUN the platform-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - NEVER consider the PRD done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT PrdPlatformErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the PRD-PLATFORM template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  unclear_platform_boundary ->
    EMIT "Platform vs MiniApp boundary is unclear for {capability} — should it be a platform capability consumed by several MiniApps, or owned by one MiniApp?"
    WAIT user.reply
  missing_miniapp_inventory ->
    EMIT "MiniApp inventory unknown. Recommended: run /cf-generate DECOMPOSITION-PLATFORM after this PRD. Or continue with the MiniApp Map marked as provisional."
    WAIT user.reply

RULES:
  - ALWAYS escalate to the user when requirement priority is uncertain, when the platform/MiniApp ownership boundary is unclear, when actors/personas need clarification, or when uncertain whether a checklist category is truly N/A vs missing
```

```pdsl
UNIT PrdPlatformNextSteps

PURPOSE:
  Offer next actions after the PRD-PLATFORM is complete.

DO:
  - EMIT_MENU PrdPlatformNextStepsMenu

MENU PrdPlatformNextStepsMenu:
  TITLE: PRD-PLATFORM next steps
  OPTIONS:
    1 -> RUN /cf-generate DESIGN-PLATFORM (create platform technical design)
    2 -> RUN /cf-generate DECOMPOSITION-PLATFORM (break platform into MiniApps)
    3 -> RUN /cf-generate PRD-MINIAPP (create MiniApp-level PRD)
    4 -> RUN /cf-generate ADR (record a platform-level decision)
    5 -> CONTINUE PrdPlatformAuthoring (revise PRD)
    6 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, 5, or 6."
    WAIT user.reply
    STOP_TURN
```

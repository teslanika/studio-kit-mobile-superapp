# PRD-EPIC Rules

**Artifact**: PRD-EPIC
**Kit**: mobile-superapp
**Level**: L2 (Epic)

```pdsl
UNIT PrdEpicAuthoring

PURPOSE:
  Author or revise an Epic-level PRD that follows the template, conventions, and authoring boundaries.

WHEN:
  - REQUIRE authoring or revising a PRD-EPIC

DO:
  - LOAD config/kits/mobile-superapp/artifacts/PRD-EPIC/template.md for structure
  - LOAD config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md for semantic criteria
  - RUN read parent MiniApp PRD and identify which MiniApp FRs this Epic details
  - RUN read MiniApp DESIGN for architectural context (if present)
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section guided by template prompts (Overview, Actors & Context, Functional Requirements, State Requirements, Error Handling, UI/UX Requirements, Data Requirements, Traceability Matrix, Acceptance Criteria)
  - SET Epic PRD anchor = cpt-{miniapp}-epic-{epic}-prd; FR IDs = cpt-{miniapp}-epic-{epic}-fr-{slug}; state ID = cpt-{miniapp}-epic-{epic}-state; widget IDs = cpt-{miniapp}-{epic}-widget-{slug}; assign priorities p1-p9 by business impact
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS specify the Epic type: Screen | Capability | Flow | Widget
  - ALWAYS mark every FR as a checkbox with a priority marker: - [ ] `pN` - **ID**: `cpt-...`
  - ALWAYS state each FR as a verifiable MUST statement with Actors, UI Element, and Acceptance fields
  - ALWAYS trace every Epic FR to a MiniApp FR (details) or tag it `epic-specific` with rationale; document the indirect Platform trace
  - ALWAYS define all screen states (Loading, Content, Empty, Error, Offline) with condition and UI behavior
  - ALWAYS define entry points (navigation, deep link constructor://{miniapp}/{epic}?{params}, push notification where applicable)
  - ALWAYS define error handling with user message and recovery action per error type; keep interactions touch-optimized
  - ALWAYS keep the PRD requirements-only (WHAT not HOW); express any quality expectation as a business-level outcome with a measurable Threshold, not a technical implementation spec
  - ALWAYS state authorization as exact per-actor/operation permissions (which actor may perform which action on which resource); NEVER restate the generic "every operation requires authentication/authorization", which is assumed
  - ALWAYS state data needs at business level (what data, owning backend capability, freshness/offline expectation); NEVER specify endpoints, payloads, or API contracts
  - ALWAYS version on change: increment the header version when editing; keep a changelog of significant changes
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT PrdEpicOmissions

PURPOSE:
  Enforce PRD scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include technical implementation details (ARCH-PRD-NO-001, CRITICAL) — PRD captures what, not how
  - NEVER include architectural decisions (ARCH-PRD-NO-002, CRITICAL) — they belong in ADR
  - NEVER include component architecture or state management implementation — they belong in DESIGN-EPIC
  - NEVER include implementation tasks (BIZ-PRD-NO-001, HIGH) — they belong in DECOMPOSITION-EPIC
  - NEVER include spec-level design, CDSL flows, step-by-step implementation, or Definition of Done (BIZ-PRD-NO-002, HIGH) — they belong in FEATURE-MOBILE
  - NEVER include data schema definitions (DATA-PRD-NO-001, HIGH) — schemas belong in DESIGN-EPIC
  - NEVER include API specifications (INT-PRD-NO-001, HIGH) — no API contracts/OpenAPI, REST endpoints, HTTP methods, HTTP/REST status codes, authentication header specifications, or standardized error response formats; API contracts belong in DESIGN-EPIC, API design decisions in ADR
  - NEVER include test cases (TEST-PRD-NO-001, MEDIUM) — tests belong in FEATURE/code
  - NEVER include infrastructure specifications (OPS-PRD-NO-001, MEDIUM) — infra belongs in DESIGN
  - NEVER include security implementation details (SEC-PRD-NO-001, HIGH) — implementation belongs in DESIGN/code
  - NEVER redefine MiniApp-level requirements, duplicate MiniApp constraints verbatim, or redefine actors — detail with traces and add Epic context instead
```

```pdsl
UNIT PrdEpicValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the PRD-EPIC.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, no placeholders, no duplicate IDs)
  - LOAD config/kits/mobile-superapp/artifacts/PRD-EPIC/checklist.md and RUN semantic validation + report using it (MUST HAVE items, MUST NOT HAVE scan, mobile-specific criteria)
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - NEVER consider the PRD done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT PrdEpicErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the PRD-EPIC template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_miniapp_prd ->
    EMIT "Parent MiniApp PRD not found. Recommended: run /cf-generate PRD-MINIAPP first. Or continue without it (Epic will lack traceability) and note 'MiniApp PRD pending' in the header."
    WAIT user.reply
  missing_miniapp_design ->
    EMIT warning
    CONTINUE with documented architectural assumptions
  unclear_scope ->
    EMIT "Epic scope is unclear — please clarify; MiniApp DECOMPOSITION defines epic boundaries."
    WAIT user.reply

RULES:
  - ALWAYS escalate to the user when screen states are uncertain, when data needs are unclear, or when UI/UX decisions need stakeholder input
```

```pdsl
UNIT PrdEpicNextSteps

PURPOSE:
  Offer next actions after the PRD-EPIC is complete.

DO:
  - EMIT_MENU PrdEpicNextStepsMenu

MENU PrdEpicNextStepsMenu:
  TITLE: PRD-EPIC next steps
  OPTIONS:
    1 -> RUN /cf-generate DESIGN-EPIC (create Epic technical design)
    2 -> RUN /cf-generate DECOMPOSITION-EPIC (decompose Epic into features)
    3 -> RUN /cf-generate FEATURE-MOBILE (create feature spec)
    4 -> CONTINUE PrdEpicAuthoring (revise PRD)
    5 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

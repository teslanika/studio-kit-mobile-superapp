# FEATURE-MOBILE Rules

**Artifact**: FEATURE-MOBILE
**Kit**: mobile-superapp
**Level**: L3 (Feature)

```pdsl
UNIT FeatureMobileAuthoring

PURPOSE:
  Author or revise a mobile feature specification: CDSL actor flows, processes /
  business logic allocated across KMP / Android / iOS / WebView, state machines,
  Definitions of Done, and acceptance criteria for one implementable unit.

WHEN:
  - REQUIRE authoring or revising a FEATURE-MOBILE

DO:
  - LOAD config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/template.md for structure
  - LOAD config/kits/sdlc/artifacts/FEATURE/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md for the feature-layer delta over that base
  - RUN read the Epic DECOMPOSITION to get this feature's ID, scope, out-of-scope, dependencies, and platform implementation targets
  - RUN read Epic PRD for FRs, state requirements, widgets, error conditions, and acceptance criteria
  - RUN read Epic DESIGN for components, widgets, use cases, repository operations, state contracts, and sequences
  - RUN read the MiniApp DESIGN for the module structure, domain entities, and API contracts this feature consumes
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats and code-marker syntax
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN author each required section (Feature Context, Actor Flows, Processes / Business Logic, States, Definitions of Done, Acceptance Criteria, Traceability)
  - SET featstatus ID under the H1 = cpt-{hierarchy-prefix}-featstatus-{feature-slug}; feature ref = cpt-{hierarchy-prefix}-feature-{feature-slug}; flow IDs = cpt-{hierarchy-prefix}-flow-{feature-slug}-{slug}; process IDs = cpt-{hierarchy-prefix}-algo-{feature-slug}-{slug}; state IDs = cpt-{hierarchy-prefix}-state-{feature-slug}; dod IDs = cpt-{hierarchy-prefix}-dod-{feature-slug}-{slug}
  - RUN author CDSL instructions in the form `N. [ ] - \`pN\` - Description - \`inst-{slug}\`` using IF / ELSE / FOR EACH / TRY / CATCH / RETURN / FROM-TO-WHEN, nesting conditional branches
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS reference the parent feature entry from the Epic DECOMPOSITION
  - ALWAYS describe what happens, not how it is coded; CDSL steps are decision-level, not source lines
  - ALWAYS allocate every process to exactly one target: KMP shared, Android, iOS, or the WebView bridge
  - ALWAYS place business logic in a KMP shared process; platform processes are UI reduction and platform integration only
  - ALWAYS name the shared, Android, and iOS locations for each process, matching the DECOMPOSITION platform implementation table
  - ALWAYS reference platform actors as cpt-superapp-actor-{slug}; NEVER redefine actors here
  - ALWAYS reuse the Epic PRD widget IDs and the Epic DESIGN component, use case, and repository IDs; NEVER mint a second ID for an existing element
  - ALWAYS cover every state named in the Epic DESIGN screen state model with a transition here
  - ALWAYS give every DoD item its Implements, Constraints, Touches, and Verification fields
  - ALWAYS keep featstatus consistent: `[x]` iff ALL nested task-tracked ID definitions and task-checkbox references in scope are `[x]`
  - ALWAYS check an element only when all its code markers exist and the implementation is verified; a dod is checked when implementation is complete AND tests pass
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document

INVARIANTS:
  - ALWAYS increment the version on edit and keep a changelog of significant changes
  - ALWAYS add a `-v{N}` suffix to an ID whose flow, process, state, or DoD meaning changed; the matching code marker becomes @cpt-{kind}:cpt-{hierarchy-prefix}-{kind}-{slug}-v{N}:p{N}
  - ALWAYS when all flows, processes, states, and DoD items are `[x]`, mark the feature `[x]` in the Epic DECOMPOSITION so status cascades to DESIGN and PRD
```

```pdsl
UNIT FeatureMobileOmissions

PURPOSE:
  Enforce FEATURE scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER redefine system-level types or domain entities (ARCH-FDESIGN-NO-001, CRITICAL) — they belong in DESIGN-MINIAPP
  - NEVER introduce new API endpoints (ARCH-FDESIGN-NO-002, CRITICAL) — the API surface belongs in DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER include architectural decisions or technology rationale (ARCH-FDESIGN-NO-003, HIGH) — they belong in ADR
  - NEVER define product requirements or user stories (BIZ-FDESIGN-NO-001, HIGH) — they belong in PRD-EPIC
  - NEVER include sprint or task breakdowns (BIZ-FDESIGN-NO-002, HIGH) — sequencing belongs in DECOMPOSITION-EPIC
  - NEVER include code snippets (MAINT-FDESIGN-NO-001, HIGH) — code belongs in the implementation
  - NEVER include test implementations (TEST-FDESIGN-NO-001, MEDIUM) — test code belongs in the implementation
  - NEVER include secrets, tokens, or credentials (SEC-FDESIGN-NO-001, CRITICAL) — they must never appear in documentation
  - NEVER include infrastructure or build configuration (OPS-FDESIGN-NO-001, MEDIUM) — it belongs in the implementation and IMPL-* guides
  - NEVER include platform coding conventions or style rules (FEATURE-MOBILE-NO-001, LOW) — they belong in IMPL-IOS / IMPL-ANDROID / IMPL-KMP
  - NEVER include design-system token values, colors, spacing, or animation curves (FEATURE-MOBILE-NO-002, MEDIUM) — visual specification belongs in the design system
```

```pdsl
UNIT FeatureMobileValidate

PURPOSE:
  Run deterministic, semantic, coverage, and TOC validation on the FEATURE-MOBILE.

DO:
  - RUN cfs validate --artifact <path> (template compliance, ID format, priority markers, CDSL format, no placeholders, parent reference, reference rules, heading scoping, checked-ref-implies-checked-def)
  - LOAD config/kits/sdlc/artifacts/FEATURE/checklist.md and RUN the full base semantic pass (Review Scope Selection, all expertise domains, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/FEATURE-MOBILE/checklist.md and RUN the feature-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs spec-coverage when code exists — percentage of CDSL instructions carrying code markers, plus missing/orphaned markers
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every Epic PRD FR, state requirement, and error condition in this feature's scope is realized by a flow, process, or state transition
  - ALWAYS trace to code: IDs with to_code="true" map to markers @cpt-{kind}:{cpt-id}:p{N}, and each CDSL instruction maps to a code marker
  - NEVER leave a to_code="true" ID untraced to code
  - NEVER consider the FEATURE done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT FeatureMobileErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the FEATURE-MOBILE template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_decomposition ->
    EMIT "Epic DECOMPOSITION not found. Recommended: run /cf-generate DECOMPOSITION-EPIC first — this feature's ID, scope, and platform targets come from it. Or continue without the manifest, accepting that traceability is incomplete."
    WAIT user.reply
  missing_epic_design ->
    EMIT "Epic DESIGN not found. Recommended: run /cf-generate DESIGN-EPIC first — components, state contracts, and use cases are referenced from it. Or continue with 'DESIGN pending' in the header and the referenced elements documented as assumptions."
    WAIT user.reply
  missing_parent_feature ->
    EMIT "Feature ID cpt-{hierarchy-prefix}-feature-{slug} not found in the Epic DECOMPOSITION. If the feature is new, add the entry there first; if it is a typo, correct the reference."
    WAIT user.reply
  platform_divergence_undecided ->
    EMIT warning
    CONTINUE with the shared behavior specified and the divergence listed as an open decision

RULES:
  - ALWAYS escalate to the user when flow correctness needs domain expertise, when a state transition is ambiguous in the PRD, when a repository operation does not exist yet, or when Android and iOS must behave differently and the product choice is unmade
```

```pdsl
UNIT FeatureMobileNextSteps

PURPOSE:
  Offer next actions after the FEATURE-MOBILE is complete.

DO:
  - EMIT_MENU FeatureMobileNextStepsMenu

MENU FeatureMobileNextStepsMenu:
  TITLE: FEATURE-MOBILE next steps
  OPTIONS:
    1 -> RUN /cf-generate CODE (implement this feature)
    2 -> RUN /cf-analyze CODE (validate the implementation against this spec)
    3 -> RUN update feature status in DECOMPOSITION-EPIC (feature implemented)
    4 -> CONTINUE FeatureMobileAuthoring (revise this feature spec)
    5 -> RUN /cf-generate FEATURE-MOBILE (specify the next feature)
    6 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, 5, or 6."
    WAIT user.reply
    STOP_TURN
```

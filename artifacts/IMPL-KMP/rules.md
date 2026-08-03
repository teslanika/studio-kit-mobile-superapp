# IMPL-KMP Rules

**Artifact**: IMPL-KMP
**Kit**: mobile-superapp
**Target**: KMP shared (`constructor-sdk/feature/{miniapp}/`)

```pdsl
UNIT ImplKmpAuthoring

PURPOSE:
  Author or revise the implementation reference that maps the KMP shared module
  to the FEATURE-MOBILE processes and DESIGN components it realizes.

WHEN:
  - REQUIRE authoring or revising an IMPL-KMP

DO:
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-KMP/template.md for structure
  - LOAD config/kits/mobile-superapp/codebase/checklist.md — the base checklist for code at this layer, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-KMP/checklist.md for the KMP-target delta over that base
  - RUN read the FEATURE-MOBILE documents this module implements; collect every process whose Target is KMP shared
  - RUN read the Epic DESIGN for the component, use case, repository, and state contracts assigned to shared code
  - RUN read the MiniApp DESIGN for domain entities and API contracts, and the Platform DESIGN for kernel contracts consumed
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for marker syntax
  - RUN scan the module tree for existing @cpt markers so the traceability table reflects actual code
  - RUN author each required section (Overview, References, Scope, Implementation Notes, Traceability Table, Directory Structure, Code Markers, Dependencies, Validation)
  - RUN cfs list-ids to confirm every referenced design ID exists

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS reference design IDs that already exist; NEVER mint a design ID here
  - ALWAYS list only processes whose declared Target is KMP shared
  - ALWAYS give every traceability row a code file path that exists in the repository
  - ALWAYS state deviations from the design in Implementation Notes, with their reason
  - ALWAYS keep the directory structure section in sync with the module on disk
  - NEVER define architecture, module boundaries, or API contracts here — reference DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER include full implementation code; short illustrative marker snippets only
  - NEVER restate project coding conventions from AGENTS.md
  - ALWAYS treat the checklist as the single source of semantic quality criteria
```

```pdsl
UNIT ImplKmpOmissions

PURPOSE:
  Enforce IMPL-KMP scope boundaries — content that MUST NOT appear and where it belongs.

RULES:
  - NEVER include full implementation code (IMPL-KMP-NO-001, HIGH) — code belongs in the source files
  - NEVER reference a design ID that does not exist (IMPL-KMP-NO-002, CRITICAL) — fix the reference or add the design element first
  - NEVER use file paths that do not exist in the repository (IMPL-KMP-NO-003, HIGH)
  - NEVER define architecture or module boundaries (IMPL-KMP-NO-004, HIGH) — they belong in DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER document Android- or iOS-target processes here (IMPL-KMP-NO-005, MEDIUM) — they belong in IMPL-ANDROID / IMPL-IOS
  - NEVER include secrets, tokens, or credentials (SEC-IMPL-NO-001, CRITICAL)
```

```pdsl
UNIT ImplKmpValidate

PURPOSE:
  Run deterministic, semantic, and coverage validation on the IMPL-KMP.

DO:
  - RUN cfs validate --artifact <path> (template compliance, reference resolution, no placeholders)
  - LOAD config/kits/mobile-superapp/codebase/checklist.md and RUN the full base pass — it loads {cf-studio-path}/.core/requirements/code-checklist.md and config/kits/sdlc/codebase/checklist.md as its own bases
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-KMP/checklist.md and RUN the KMP-target delta pass
  - RETURN one merged report in the base report format, citing base and delta checklist IDs
  - RUN cfs spec-coverage — percentage of shared-target CDSL instructions carrying code markers, plus missing/orphaned markers
  - RUN ./gradlew :constructor-sdk:build and ./gradlew :constructor-sdk:allTests -> REQUIRE success
  - RUN ktlintCheck and detekt -> REQUIRE pass
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS verify every traceability row resolves: design ID exists, code file exists, marker present in that file
  - ALWAYS report unmapped shared-target processes as coverage gaps
  - NEVER consider the IMPL-KMP done while validation reports fail/error or cfs validate-toc does not PASS
  - NEVER restate semantic criteria here
```

```pdsl
UNIT ImplKmpErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies and mismatches.

ON_ERROR:
  missing_feature_spec ->
    EMIT "FEATURE-MOBILE not found. Recommended: run /cf-generate FEATURE-MOBILE first — the shared-target process list comes from it. Or continue documenting only what the code shows, marking coverage as unverified."
    WAIT user.reply
  missing_epic_design ->
    EMIT "Epic DESIGN not found. Recommended: run /cf-generate DESIGN-EPIC first — component and state contracts are referenced from it. Or continue with the referenced elements documented as assumptions."
    WAIT user.reply
  marker_mismatch ->
    EMIT "A traceability row names a marker absent from the code file, or a marker in code has no row. List both directions and ask which side to correct."
    WAIT user.reply
  module_missing ->
    EMIT warning
    CONTINUE with the directory structure marked as planned, not as existing

RULES:
  - ALWAYS escalate when the code implements behavior that no design element specifies
  - NEVER invent a design ID to make a marker resolve
```

```pdsl
UNIT ImplKmpNextSteps

PURPOSE:
  Offer next actions after the IMPL-KMP is complete.

DO:
  - EMIT_MENU ImplKmpNextStepsMenu

MENU ImplKmpNextStepsMenu:
  TITLE: IMPL-KMP next steps
  OPTIONS:
    1 -> RUN /cf-generate IMPL-ANDROID (map the Android module)
    2 -> RUN /cf-generate IMPL-IOS (map the iOS module)
    3 -> RUN /cf-analyze CODE (review the shared implementation against FEATURE-MOBILE)
    4 -> CONTINUE ImplKmpAuthoring (revise this reference)
    5 -> RUN update feature status in DECOMPOSITION-EPIC
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

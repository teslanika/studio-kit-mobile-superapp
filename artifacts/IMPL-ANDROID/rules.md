# IMPL-ANDROID Rules

**Artifact**: IMPL-ANDROID
**Kit**: mobile-superapp
**Target**: Android (`android-app/feature/{miniapp}/`)

```pdsl
UNIT ImplAndroidAuthoring

PURPOSE:
  Author or revise the implementation reference that maps the Android module to
  the FEATURE-MOBILE processes, screens, widgets, and navigation it realizes.

WHEN:
  - REQUIRE authoring or revising an IMPL-ANDROID

DO:
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-ANDROID/template.md for structure
  - LOAD config/kits/mobile-superapp/codebase/checklist.md — the base checklist for code at this layer, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-ANDROID/checklist.md for the Android-target delta over that base
  - RUN read the FEATURE-MOBILE documents this module implements; collect every process whose Target is Android
  - RUN read the Epic DESIGN for screens, widgets, navigation destinations, deep links, and state contracts
  - RUN read the IMPL-KMP reference for the shared surface this module consumes
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for marker syntax
  - RUN scan the module tree for existing @cpt markers so the traceability table reflects actual code
  - RUN author each required section (Overview, References, Scope, Implementation Notes, Traceability Table, Directory Structure, Code Markers, Dependencies, Validation)
  - RUN cfs list-ids to confirm every referenced design ID exists

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS reference design IDs that already exist; NEVER mint a design ID here
  - ALWAYS list only processes whose declared Target is Android
  - ALWAYS name the shared component this UI consumes rather than describing reimplemented logic
  - ALWAYS give every traceability row a code file path that exists in the repository
  - ALWAYS state deviations from the design in Implementation Notes, with their reason
  - ALWAYS document declared deep links and their destination alongside the navigation row
  - NEVER define architecture, module boundaries, or API contracts here — reference DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER include full implementation code; short illustrative marker snippets only
  - NEVER document business logic here — it belongs to IMPL-KMP
  - NEVER restate Compose style rules or design-system token values
  - ALWAYS treat the checklist as the single source of semantic quality criteria
```

```pdsl
UNIT ImplAndroidOmissions

PURPOSE:
  Enforce IMPL-ANDROID scope boundaries — content that MUST NOT appear and where it belongs.

RULES:
  - NEVER include full implementation code (IMPL-ANDROID-NO-001, HIGH) — code belongs in the source files
  - NEVER reference a design ID that does not exist (IMPL-ANDROID-NO-002, CRITICAL)
  - NEVER use file paths that do not exist in the repository (IMPL-ANDROID-NO-003, HIGH)
  - NEVER define architecture or module boundaries (IMPL-ANDROID-NO-004, HIGH) — they belong in DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER document business logic or shared processes (IMPL-ANDROID-NO-005, HIGH) — they belong in IMPL-KMP
  - NEVER include design-system token values, colors, spacing, or typography (IMPL-ANDROID-NO-006, MEDIUM) — they belong in the design system
  - NEVER include secrets, tokens, or credentials (SEC-IMPL-NO-001, CRITICAL)
```

```pdsl
UNIT ImplAndroidValidate

PURPOSE:
  Run deterministic, semantic, and coverage validation on the IMPL-ANDROID.

DO:
  - RUN cfs validate --artifact <path> (template compliance, reference resolution, no placeholders)
  - LOAD config/kits/mobile-superapp/codebase/checklist.md and RUN the full base pass — it loads {cf-studio-path}/.core/requirements/code-checklist.md and config/kits/sdlc/codebase/checklist.md as its own bases
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-ANDROID/checklist.md and RUN the Android-target delta pass
  - RETURN one merged report in the base report format, citing base and delta checklist IDs
  - RUN cfs spec-coverage — percentage of Android-target CDSL instructions carrying code markers, plus missing/orphaned markers
  - RUN ./gradlew :android-app:assembleDebug and ./gradlew :android-app:testDebugUnitTest -> REQUIRE success
  - RUN ktlintCheck and detekt -> REQUIRE pass
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS verify every traceability row resolves: design ID exists, code file exists, marker present in that file
  - ALWAYS verify every Epic DESIGN screen and widget assigned to Android has a row
  - ALWAYS report unmapped Android-target processes as coverage gaps
  - NEVER consider the IMPL-ANDROID done while validation reports fail/error or cfs validate-toc does not PASS
  - NEVER restate semantic criteria here
```

```pdsl
UNIT ImplAndroidErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies and mismatches.

ON_ERROR:
  missing_feature_spec ->
    EMIT "FEATURE-MOBILE not found. Recommended: run /cf-generate FEATURE-MOBILE first — the Android-target process list comes from it. Or continue documenting only what the code shows, marking coverage as unverified."
    WAIT user.reply
  missing_epic_design ->
    EMIT "Epic DESIGN not found. Recommended: run /cf-generate DESIGN-EPIC first — screens, widgets, and navigation are referenced from it. Or continue with the referenced elements documented as assumptions."
    WAIT user.reply
  missing_impl_kmp ->
    EMIT warning
    CONTINUE with the consumed shared surface documented from the code
  marker_mismatch ->
    EMIT "A traceability row names a marker absent from the code file, or a marker in code has no row. List both directions and ask which side to correct."
    WAIT user.reply

RULES:
  - ALWAYS escalate when the Android code implements logic that the design allocated to shared code
  - NEVER invent a design ID to make a marker resolve
```

```pdsl
UNIT ImplAndroidNextSteps

PURPOSE:
  Offer next actions after the IMPL-ANDROID is complete.

DO:
  - EMIT_MENU ImplAndroidNextStepsMenu

MENU ImplAndroidNextStepsMenu:
  TITLE: IMPL-ANDROID next steps
  OPTIONS:
    1 -> RUN /cf-generate IMPL-IOS (map the iOS module for parity)
    2 -> RUN /cf-analyze CODE (review the Android implementation against FEATURE-MOBILE)
    3 -> RUN /cf-generate IMPL-KMP (map the shared module)
    4 -> CONTINUE ImplAndroidAuthoring (revise this reference)
    5 -> RUN update feature status in DECOMPOSITION-EPIC
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

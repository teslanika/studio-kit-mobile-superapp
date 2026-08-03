# IMPL-IOS Rules

**Artifact**: IMPL-IOS
**Kit**: mobile-superapp
**Target**: iOS (`ios-app/Features/{Module}/`)

```pdsl
UNIT ImplIosAuthoring

PURPOSE:
  Author or revise the implementation reference that maps the iOS module to the
  FEATURE-MOBILE processes, screens, widgets, and navigation it realizes.

WHEN:
  - REQUIRE authoring or revising an IMPL-IOS

DO:
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-IOS/template.md for structure
  - LOAD config/kits/mobile-superapp/codebase/checklist.md — the base checklist for code at this layer, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-IOS/checklist.md for the iOS-target delta over that base
  - RUN read the FEATURE-MOBILE documents this module implements; collect every process whose Target is iOS
  - RUN read the Epic DESIGN for screens, widgets, navigation, universal links, and state contracts
  - RUN read the IMPL-KMP reference for the shared surface this module bridges to
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for marker syntax
  - RUN scan the module tree for existing @cpt markers so the traceability table reflects actual code
  - RUN author each required section (Overview, References, Scope, Implementation Notes, Traceability Table, Directory Structure, Code Markers, KMP Integration, Dependencies, Validation)
  - RUN cfs list-ids to confirm every referenced design ID exists

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS reference design IDs that already exist; NEVER mint a design ID here
  - ALWAYS list only processes whose declared Target is iOS
  - ALWAYS document the KMP bridge: which shared ViewModel is consumed and how state and errors cross the boundary
  - ALWAYS give every traceability row a code file path that exists in the repository
  - ALWAYS state deviations from the design in Implementation Notes, with their reason
  - ALWAYS document declared universal links and custom schemes alongside the navigation row
  - ALWAYS name the Android counterpart when iOS behavior deliberately differs
  - NEVER define architecture, module boundaries, or API contracts here — reference DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER include full implementation code; short illustrative marker snippets only
  - NEVER document business logic here — it belongs to IMPL-KMP
  - NEVER restate SwiftUI style rules or design-system token values
  - ALWAYS treat the checklist as the single source of semantic quality criteria
```

```pdsl
UNIT ImplIosOmissions

PURPOSE:
  Enforce IMPL-IOS scope boundaries — content that MUST NOT appear and where it belongs.

RULES:
  - NEVER include full implementation code (IMPL-IOS-NO-001, HIGH) — code belongs in the source files
  - NEVER reference a design ID that does not exist (IMPL-IOS-NO-002, CRITICAL)
  - NEVER use file paths that do not exist in the repository (IMPL-IOS-NO-003, HIGH)
  - NEVER define architecture or module boundaries (IMPL-IOS-NO-004, HIGH) — they belong in DESIGN-MINIAPP / DESIGN-PLATFORM
  - NEVER document business logic or shared processes (IMPL-IOS-NO-005, HIGH) — they belong in IMPL-KMP
  - NEVER reimplement a shared ViewModel in Swift (IMPL-IOS-NO-006, CRITICAL) — bridge it
  - NEVER include design-system token values, colors, spacing, or typography (IMPL-IOS-NO-007, MEDIUM)
  - NEVER include secrets, tokens, or credentials (SEC-IMPL-NO-001, CRITICAL)
```

```pdsl
UNIT ImplIosValidate

PURPOSE:
  Run deterministic, semantic, and coverage validation on the IMPL-IOS.

DO:
  - RUN cfs validate --artifact <path> (template compliance, reference resolution, no placeholders)
  - LOAD config/kits/mobile-superapp/codebase/checklist.md and RUN the full base pass — it loads {cf-studio-path}/.core/requirements/code-checklist.md and config/kits/sdlc/codebase/checklist.md as its own bases
  - LOAD config/kits/mobile-superapp/artifacts/IMPL-IOS/checklist.md and RUN the iOS-target delta pass
  - RETURN one merged report in the base report format, citing base and delta checklist IDs
  - RUN cfs spec-coverage — percentage of iOS-target CDSL instructions carrying code markers, plus missing/orphaned markers
  - RUN xcodebuild build and xcodebuild test for the app scheme -> REQUIRE success
  - RUN swiftlint -> REQUIRE pass
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS verify every traceability row resolves: design ID exists, code file exists, marker present in that file
  - ALWAYS verify every Epic DESIGN screen and widget assigned to iOS has a row
  - ALWAYS verify the iOS row set matches the Android row set element for element, except where a divergence is documented
  - ALWAYS report unmapped iOS-target processes as coverage gaps
  - NEVER consider the IMPL-IOS done while validation reports fail/error or cfs validate-toc does not PASS
  - NEVER restate semantic criteria here
```

```pdsl
UNIT ImplIosErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies and mismatches.

ON_ERROR:
  missing_feature_spec ->
    EMIT "FEATURE-MOBILE not found. Recommended: run /cf-generate FEATURE-MOBILE first — the iOS-target process list comes from it. Or continue documenting only what the code shows, marking coverage as unverified."
    WAIT user.reply
  missing_epic_design ->
    EMIT "Epic DESIGN not found. Recommended: run /cf-generate DESIGN-EPIC first — screens, widgets, and navigation are referenced from it. Or continue with the referenced elements documented as assumptions."
    WAIT user.reply
  missing_impl_kmp ->
    EMIT warning
    CONTINUE with the bridged shared surface documented from the code
  parity_gap ->
    EMIT "An element mapped in IMPL-ANDROID has no iOS counterpart and no documented divergence. Add the row or document the divergence."
    WAIT user.reply
  marker_mismatch ->
    EMIT "A traceability row names a marker absent from the code file, or a marker in code has no row. List both directions and ask which side to correct."
    WAIT user.reply

RULES:
  - ALWAYS escalate when the iOS code implements logic that the design allocated to shared code
  - NEVER invent a design ID to make a marker resolve
```

```pdsl
UNIT ImplIosNextSteps

PURPOSE:
  Offer next actions after the IMPL-IOS is complete.

DO:
  - EMIT_MENU ImplIosNextStepsMenu

MENU ImplIosNextStepsMenu:
  TITLE: IMPL-IOS next steps
  OPTIONS:
    1 -> RUN /cf-analyze CODE (review the iOS implementation against FEATURE-MOBILE)
    2 -> RUN /cf-generate IMPL-ANDROID (map the Android module for parity)
    3 -> RUN /cf-generate IMPL-KMP (map the shared module)
    4 -> CONTINUE ImplIosAuthoring (revise this reference)
    5 -> RUN update feature status in DECOMPOSITION-EPIC
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

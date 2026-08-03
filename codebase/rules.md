# CODEBASE Rules

**Artifact**: CODEBASE (mobile SuperApp implementation)
**Kit**: mobile-superapp
**Targets**: KMP shared (`constructor-sdk/`), Android (`android-app/`), iOS (`ios-app/`)

**Dependencies** (lazy-loaded): `config/kits/mobile-superapp/codebase/checklist.md` (mobile delta), `config/kits/sdlc/codebase/checklist.md` (SDLC semantic alignment), `{cf-studio-path}/.core/requirements/code-checklist.md` (generic code quality).

---

```pdsl
UNIT CodebaseImplementation

PURPOSE:
  Implement mobile code from a resolved design source, in work packages, across
  the KMP / Android / iOS targets, under the correct traceability mode.

STATE:
  - SET TRACEABILITY_MODE: FULL | DOCS-ONLY
    default: DOCS-ONLY

DO:
  - RUN resolve source in priority order:
      1 FEATURE-MOBILE design (registered, has `to_code="true"` IDs) -> FULL possible
      2 Other Constructor Studio artifact (DESIGN-EPIC / DESIGN-MINIAPP / DESIGN-PLATFORM / PRD-* / DECOMPOSITION-*) -> DOCS-ONLY
      3 User-provided description / requirements -> DOCS-ONLY
      4 Prompt only -> DOCS-ONLY
  - REQUIRE if no source -> suggest /cf-generate FEATURE-MOBILE first
  - LOAD project AGENTS.md for code conventions
  - LOAD the FEATURE-MOBILE artifact being implemented (flows, processes, states, definitions of done)
  - LOAD DESIGN-EPIC for component boundaries, state contracts, and navigation; DESIGN-MINIAPP for entities, repositories, and API contracts; DESIGN-PLATFORM for kernel contracts and platform constraints
  - LOAD {cf-studio-path}/.core/requirements/code-checklist.md for generic code quality
  - SET TRACEABILITY_MODE: FULL when the source is FEATURE-MOBILE with `to_code="true"` IDs; else DOCS-ONLY
  - RUN plan the work packages in target order: KMP shared -> Android -> iOS -> WebView bridge
  - RUN per work package:
      1 identify the exact design items to code (flows / processes / states / DoD / tests)
      2 implement per project conventions in the target the process declares
      3 WHEN Mode FULL: add @cpt-begin/@cpt-end markers per CDSL instruction (see CodebaseMarkers)
      4 run work-package validation (build, lint, tests per platform)
      5 WHEN Mode FULL: sync FEATURE-MOBILE and DECOMPOSITION checkboxes (see CodebaseCascade)
      6 continue to the next work package
  - CONTINUE CodebaseValidate

RULES:
  - ALWAYS apply TDD (failing test first, minimal code, then refactor), SOLID, DRY, KISS, YAGNI, explicit error handling, and testability
  - ALWAYS implement a process in the target it declares: business logic in constructor-sdk/, UI reduction in android-app/ or ios-app/, bridge handling in the native shell
  - NEVER duplicate a shared process per platform
  - ALWAYS consume kernel services through the contracts named in DESIGN-PLATFORM; NEVER reimplement auth, storage, network, or notifications inside a feature
  - ALWAYS implement Android and iOS to the same user-visible behavior, except where FEATURE-MOBILE states a deliberate divergence
  - ALWAYS refactor only after tests pass; keep behavior unchanged
  - ALWAYS load {cf-studio-path}/.core/requirements/code-checklist.md for the full generic code-quality criteria; do not restate them here
  - NEVER leave placeholder or stub code (no TODO / FIXME / XXX / HACK in domain or presentation layers; no bare `!!` in Kotlin, no force unwrap in Swift production code)

NOTES:
  Mode FULL requires the traceability spec {cf-studio-path}/.core/architecture/specs/traceability.md.
  Mode determination also follows the Traceability Preconditions in config/kits/mobile-superapp/codebase/checklist.md.
```

```pdsl
UNIT CodebaseMarkers

PURPOSE:
  Define @cpt marker syntax and granularity for mobile code (Traceability Mode FULL only).

WHEN:
  - REQUIRE TRACEABILITY_MODE == FULL

DO:
  - EMIT scope markers: @cpt-{kind}:{cpt-id}:p{N} — single-line, at the function or class entry point (kind: flow | algo | state | dod)
  - EMIT paired block markers: @cpt-begin:{cpt-id}:p{N}:inst-{local} / @cpt-end:{cpt-id}:p{N}:inst-{local}
  - EMIT in DOCS-ONLY mode simplified markers only: @cpt-impl {cpt-id}

RULES:
  - ALWAYS wrap the SMALLEST code fragment implementing one CDSL instruction in each begin/end pair
  - ALWAYS place a separate begin/end pair per instruction when a function implements multiple instructions
  - ALWAYS place markers as close to the implementing code as possible
  - ALWAYS ensure every `to_code="true"` ID has markers and every implemented CDSL instruction ([x] ... inst-*) has a paired begin/end block wrapping non-empty code
  - ALWAYS use the same comment syntax as the host language (// in Kotlin and Swift)
  - NEVER wrap a whole multi-instruction function body in a single begin/end pair
  - NEVER leave orphaned or stale markers
```

Correct — each instruction wrapped individually, in shared KMP code:

```kotlin
// @cpt-algo:cpt-superapp-student-home-algo-home-viewmodel:p1
class HomeViewModel(private val loadHome: LoadHomeUseCase) : ViewModel() {

    fun processIntent(intent: HomeIntent) {
        // @cpt-begin:cpt-superapp-student-home-algo-home-viewmodel:p1:inst-vm-1
        when (intent) {
            is HomeIntent.Load -> loadData()
        }
        // @cpt-end:cpt-superapp-student-home-algo-home-viewmodel:p1:inst-vm-1
    }

    private fun loadData() = viewModelScope.launch {
        // @cpt-begin:cpt-superapp-student-home-algo-home-viewmodel:p1:inst-vm-2
        val result = loadHome()
        // @cpt-end:cpt-superapp-student-home-algo-home-viewmodel:p1:inst-vm-2

        // @cpt-begin:cpt-superapp-student-home-algo-home-viewmodel:p1:inst-vm-3
        _state.value = when (result) {
            is Result.Success -> HomeState.Content(result.data)
            is Result.Error -> HomeState.Error(result.reason)
        }
        // @cpt-end:cpt-superapp-student-home-algo-home-viewmodel:p1:inst-vm-3
    }
}
```

Anti-pattern: a single `@cpt-begin/.../@cpt-end` pair wrapping the entire multi-instruction function body.

```pdsl
UNIT CodebaseCascade

PURPOSE:
  Cascade code markers up through FEATURE-MOBILE / DECOMPOSITION-EPIC / DECOMPOSITION-MINIAPP / DECOMPOSITION-PLATFORM / PRD-DESIGN checkboxes, consistently and versioned.

WHEN:
  - REQUIRE TRACEABILITY_MODE == FULL

DO:
  - RUN cascade chain:
      CODE markers exist
        -> FEATURE-MOBILE: flow/algo/state/dod IDs [x] (dod also requires verification evidence complete)
        -> DECOMPOSITION-EPIC: feature entry [x]
        -> DECOMPOSITION-MINIAPP: epic entry [x]
        -> DECOMPOSITION-PLATFORM: miniapp entry [x]
        -> PRD-* / DESIGN-*: referenced IDs [x] when ALL downstream refs [x]
  - RUN update order:
      1 after implementing a CDSL instruction: add block markers, mark the step [x] in FEATURE-MOBILE
      2 after all steps of a flow/process/state/dod are [x]: mark that ID [x] in FEATURE-MOBILE
      3 after all FEATURE-MOBILE IDs are [x]: mark the feature entry [x] in DECOMPOSITION-EPIC and advance its status
      4 after the epic's features are all [x]: mark the epic entry [x] in DECOMPOSITION-MINIAPP; likewise the miniapp entry in DECOMPOSITION-PLATFORM
      5 mark referenced IDs [x] in PRD-* / DESIGN-* only when all downstream refs are [x]
  - RUN marker versioning on a design ID bump:
      WHEN a design ID is versioned (-v2) -> update markers to @cpt-{kind}:{cpt-id}-v2:p{N}; migrate ALL markers; old markers may stay commented during the transition

RULES:
  - ALWAYS require all three target implementations (shared, Android, iOS) before checking a feature entry, unless FEATURE-MOBILE documents single-platform scope
  - NEVER mark a CDSL instruction [x] unless code block markers exist and wrap non-empty implementation code
  - NEVER add a code block marker pair unless the CDSL instruction exists in the design (add it there first)
  - ALWAYS keep a parent ID checkbox consistent with all nested task-tracked items in its scope: parent [x] IFF all nested task-tracked items [x]
  - NEVER mark a reference [x] while its definition is still [ ]

NOTES:
  `cfs validate` warns if a code marker exists but the FEATURE checkbox is [ ],
  warns if a FEATURE checkbox is [x] but the code marker is missing,
  and reports coverage: N% of FEATURE IDs have code markers.
```

```pdsl
UNIT CodebaseValidate

PURPOSE:
  Deterministic gates per platform, then one delegated semantic review; decide PASS/FAIL.

DO:
  - REQUIRE no placeholder/stub code in domain or presentation layers
  - RUN cfs validate (Mode FULL): valid marker format, all begin/end pairs matched, no empty blocks, all `to_code="true"` IDs have markers, no orphaned/stale markers, design checkboxes synced, coverage %
  - REQUIRE test scenarios exist and are traceable: a test per design scenario, the scenario ID in a comment, not ignored without justification, actually validating behavior
  - RUN build per target -> REQUIRE success: KMP (`./gradlew :constructor-sdk:build`), Android (`./gradlew :android-app:assembleDebug`), iOS (`xcodebuild`)
  - RUN lint per target -> REQUIRE pass: ktlint, detekt, swiftlint
  - RUN tests -> REQUIRE KMP unit, Android unit + UI, iOS unit + UI pass AND coverage meets the project requirement
  - RUN semantic expert review per config/kits/mobile-superapp/codebase/checklist.md (which loads {cf-studio-path}/.core/requirements/code-checklist.md and config/kits/sdlc/codebase/checklist.md SEM-CODE-001..007 as its bases)
  - RETURN PASS only if: all builds, lint, and tests pass; coverage met; no CRITICAL design divergences; AND (Mode FULL) required markers present and properly paired

RULES:
  - ALWAYS delegate generic code-quality criteria to {cf-studio-path}/.core/requirements/code-checklist.md
  - ALWAYS delegate semantic alignment to config/kits/sdlc/codebase/checklist.md and platform criteria to the mobile delta checklist
  - ALWAYS report each platform build and test result separately; a green KMP build is not a green feature
  - NEVER restate the generic or semantic checklists inline

NOTES:
  Report shape: Build KMP/Android/iOS PASS/FAIL, Lint PASS/FAIL, Tests X/Y,
  Coverage N%, Checklist PASS/FAIL (issues), Logic Consistency PASS/FAIL
  (CRITICAL/MINOR divergences), Marker Coverage N% (Mode FULL).
```

```pdsl
UNIT CodebaseErrorHandling

PURPOSE:
  Recover deterministically from missing sources and platform blockers.

ON_ERROR:
  missing_feature_spec ->
    EMIT "FEATURE-MOBILE not found. Recommended: run /cf-generate FEATURE-MOBILE first so the implementation is traceable. Or continue in DOCS-ONLY mode with the design source you have."
    WAIT user.reply
  missing_design ->
    EMIT warning
    CONTINUE in DOCS-ONLY mode with the referenced design elements listed as assumptions
  platform_toolchain_unavailable ->
    EMIT warning
    CONTINUE with the available targets and report the skipped target explicitly as NOT VERIFIED
  api_contract_mismatch ->
    EMIT "The endpoint used does not match the DESIGN-MINIAPP contract."
    WAIT user.reply

RULES:
  - ALWAYS escalate when the design and the backend disagree, when a shared process cannot be expressed in shared code, or when Android and iOS cannot behave identically
  - NEVER silently skip a platform target; an unbuilt target is reported as NOT VERIFIED, never as PASS
```

```pdsl
UNIT CodebaseNextSteps

PURPOSE:
  Offer next actions after validation.

DO:
  - EMIT_MENU CodebaseNextStepsMenu

MENU CodebaseNextStepsMenu:
  TITLE: CODE — next steps
  OPTIONS:
    1 -> RUN update the feature entry to implemented in DECOMPOSITION-EPIC
    2 -> RUN /cf-analyze CODE (validate the implementation against FEATURE-MOBILE)
    3 -> RUN /cf-generate FEATURE-MOBILE (specify the next feature)
    4 -> RUN /cf-analyze semantic (checklist-only review)
    5 -> CONTINUE CodebaseImplementation (finish the remaining platform target)
    6 -> RUN /cf-generate DESIGN-EPIC (design mismatch found — revise the design first)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, 5, or 6."
    WAIT user.reply
    STOP_TURN
```

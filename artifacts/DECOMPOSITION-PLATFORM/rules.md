# DECOMPOSITION-PLATFORM Rules

**Artifact**: DECOMPOSITION-PLATFORM
**Kit**: mobile-superapp
**Level**: L0 (Platform / Host App)

```pdsl
UNIT DecompositionPlatformAuthoring

PURPOSE:
  Author or revise a Platform-level decomposition that breaks the Platform DESIGN
  into MiniApps with full coverage of platform requirements and design elements.

WHEN:
  - REQUIRE authoring or revising a DECOMPOSITION-PLATFORM

DO:
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/template.md for structure
  - LOAD config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md — the base checklist, applied in full
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md for the platform-layer delta over that base
  - RUN read Platform PRD and extract FRs, NFRs, actors, and scope boundaries to cover
  - RUN read Platform DESIGN and extract components, kernel contracts, integrations, sequences, and data stores to assign
  - LOAD config/kits/mobile-superapp/constraints.toml for kit-level constraints
  - LOAD {cf-studio-path}/.core/architecture/specs/traceability.md for ID formats
  - RUN read project config for ID prefix and resolve output path from {cf-studio-path}/config/artifacts.toml
  - RUN group platform capabilities into MiniApps by user role and domain cohesion (high cohesion, loose coupling)
  - RUN author each entry with Purpose, Target Users, Depends On, Scope, Out of scope, Requirements Covered, Design Principles Covered, Design Constraints Covered, Domain Model Entities, Design Components, Kernel Contracts Consumed, Deep Link Namespace, Sequences, Data, Integration Points, Target Release
  - RUN author Entry Dependencies as an acyclic graph with a rationale per edge
  - RUN author Shared Kernel Coverage, Coverage Matrix, and Release Roadmap
  - RUN cfs list-ids to verify ID uniqueness

RULES:
  - ALWAYS follow the template structure; all required sections present and non-empty
  - ALWAYS give each entry a unique ID cpt-{hierarchy-prefix}-miniapp-{slug}, a priority marker p1-p9, and a checkbox
  - ALWAYS define checkbox IDs per constraints: kind `status` (cpt-{hierarchy-prefix}-status-overall, checked when ALL entries checked) and kind `miniapp` (checked when that MiniApp's PRD/DESIGN/DECOMPOSITION set is complete)
  - ALWAYS treat cpt-... occurrences outside an **ID** definition line as references (kinds: fr, nfr, principle, constraint, component, contract, actor, seq, db, integration)
  - ALWAYS achieve 100% coverage: every platform design component, kernel contract, integration, sequence, and data store is assigned to at least one MiniApp or to the shared kernel, and every platform FR/NFR is covered transitively
  - ALWAYS keep MiniApp scopes mutually exclusive with clear boundaries; shared platform capability belongs to the kernel, not duplicated into MiniApps
  - ALWAYS give each MiniApp a unique deep link namespace {scheme}://{miniapp}/*
  - ALWAYS make dependencies explicit and acyclic; a foundation MiniApp depends on the kernel only
  - ALWAYS apply ID versioning per the traceability spec; IDs stay stable through implementation
  - ALWAYS treat the checklist as the single source of semantic quality criteria
  - NEVER duplicate semantic criteria here; NEVER leave placeholders (TODO, TBD, FIXME); NEVER create duplicate IDs within the document
```

```pdsl
UNIT DecompositionPlatformOmissions

PURPOSE:
  Enforce DECOMPOSITION scope boundaries — content that MUST NOT appear and the artifact where it belongs. Report as a violation if found.

RULES:
  - NEVER include implementation details — code, algorithms, state machines, API request/response schemas (DECOMP-NO-001, CRITICAL) — they belong in FEATURE-MOBILE
  - NEVER define requirements — FRs, NFRs, use cases, actors (DECOMP-NO-002, HIGH) — they belong in PRD-PLATFORM
  - NEVER include architecture decisions or technology rationale (DECOMP-NO-003, HIGH) — they belong in ADR and DESIGN-PLATFORM
  - NEVER leave silent omissions — an uncovered design element or a deliberate overlap must be stated with reasoning (DOC-001, CRITICAL)
  - NEVER decompose a MiniApp into epics, screens, or flows (PLATFORM-DECOMP-NO-001, HIGH) — that belongs in DECOMPOSITION-MINIAPP
  - NEVER restate platform layer or kernel internals (PLATFORM-DECOMP-NO-002, MEDIUM) — reference DESIGN-PLATFORM components by ID
```

```pdsl
UNIT DecompositionPlatformValidate

PURPOSE:
  Run deterministic, semantic, and TOC validation on the DECOMPOSITION-PLATFORM.

DO:
  - RUN cfs validate --artifact <path> (template structure, ID format, priority markers, valid status, no placeholders, no duplicate IDs)
  - LOAD config/kits/sdlc/artifacts/DECOMPOSITION/checklist.md and RUN the full base semantic pass (COV, EXC, ATTR, LEV, CFG, TRC, DEP, CHK, DOC, FMT, MUST NOT HAVE scan)
  - LOAD config/kits/mobile-superapp/artifacts/DECOMPOSITION-PLATFORM/checklist.md and RUN the platform-layer delta pass (domain scope table, delta MUST HAVE, delta MUST NOT HAVE, mobile-specific criteria)
  - RETURN one merged report in the base checklist's report format, citing base and delta checklist IDs
  - RUN cfs toc <path> then cfs validate-toc <path>

RULES:
  - ALWAYS run cfs validate --artifact <path>
  - ALWAYS verify every platform design component and kernel contract is assigned, and every platform FR/NFR is covered
  - ALWAYS maintain cascade rules — a `miniapp` ID is not checked until that MiniApp's document set is complete; `status-overall` is not checked until ALL entries are checked
  - NEVER consider the DECOMPOSITION done while validation reports fail/error or cfs validate-toc does not PASS
  - ALWAYS use the checklist for semantic criteria, applicability handling, and report format — do not restate them here
```

```pdsl
UNIT DecompositionPlatformErrorHandling

PURPOSE:
  Recover deterministically from missing dependencies, config, and ambiguity.

ON_ERROR:
  missing_template ->
    STOP — cannot proceed without the DECOMPOSITION-PLATFORM template
  missing_checklist ->
    EMIT warning
    SET skip semantic validation
  missing_platform_design ->
    EMIT "Platform DESIGN not found. Recommended: run /cf-generate DESIGN-PLATFORM first — components and kernel contracts are assigned from it. Or continue with the design elements documented as assumptions."
    WAIT user.reply
  coverage_gap ->
    RUN assign the design element to a MiniApp or to the shared kernel, or document the exclusion with reasoning
  scope_overlap ->
    RUN assign to a single MiniApp, or document the sharing with reasoning

RULES:
  - ALWAYS escalate to the user when MiniApp boundaries are ambiguous, when a capability could belong to the kernel or to a MiniApp, or when release ordering needs a product decision
```

```pdsl
UNIT DecompositionPlatformNextSteps

PURPOSE:
  Offer next actions after the DECOMPOSITION-PLATFORM is complete.

DO:
  - EMIT_MENU DecompositionPlatformNextStepsMenu

MENU DecompositionPlatformNextStepsMenu:
  TITLE: DECOMPOSITION-PLATFORM next steps
  OPTIONS:
    1 -> RUN /cf-generate PRD-MINIAPP (start the first MiniApp)
    2 -> RUN /cf-generate DESIGN-MINIAPP (design a MiniApp)
    3 -> RUN update MiniApp status in this decomposition
    4 -> CONTINUE DecompositionPlatformAuthoring (add or revise an entry)
    5 -> RUN /cf-analyze semantic (checklist-only review)
  INVALID:
    EMIT "Reply with 1, 2, 3, 4, or 5."
    WAIT user.reply
    STOP_TURN
```

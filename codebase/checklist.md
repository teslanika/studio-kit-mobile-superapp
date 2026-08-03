# Mobile SuperApp Code Checklist — Kit Delta

ALWAYS open and follow `{cf-studio-path}/.core/requirements/code-checklist.md` FIRST

**Artifact**: Code Implementation (mobile-superapp)
**Kit**: mobile-superapp
**Scope**: KMP shared, Android (Compose), iOS (SwiftUI), WebView bridge
**Base Checklists**:
1. `{cf-studio-path}/.core/requirements/code-checklist.md` — all generic code-quality criteria
2. `{cf-studio-path}/config/kits/sdlc/codebase/checklist.md` — SDLC semantic alignment (SEM-CODE-001..007)

This file is a **delta over those two base checklists**, not a replacement. It adds the mobile-specific criteria that a KMP + Compose + SwiftUI implementation introduces, and maps the SDLC semantic-alignment checks onto the mobile artifact set.

---

## Table of Contents

1. [How To Use This Checklist](#how-to-use-this-checklist)
2. [Traceability Preconditions](#traceability-preconditions)
3. [Semantic Alignment At This Layer](#semantic-alignment-at-this-layer)
4. [Delta: KMP Shared Code](#delta-kmp-shared-code)
5. [Delta: Android Code](#delta-android-code)
6. [Delta: iOS Code](#delta-ios-code)
7. [Delta: WebView Bridge Code](#delta-webview-bridge-code)
8. [Delta: Mobile Performance](#delta-mobile-performance)
9. [Delta: Mobile Security](#delta-mobile-security)
10. [Reporting](#reporting)

---

## How To Use This Checklist

1. **LOAD `{cf-studio-path}/.core/requirements/code-checklist.md`** and apply it in full — organization, naming, error handling, testing, documentation, and all other generic quality criteria live there and are not restated here.
2. **LOAD `{cf-studio-path}/config/kits/sdlc/codebase/checklist.md`** and apply SEM-CODE-001..007, reading its artifact names through the mapping table in [Semantic Alignment At This Layer](#semantic-alignment-at-this-layer).
3. **Apply the delta sections** in this file for the platform-specific criteria.
4. **Report once**, in the base report format, citing generic IDs, SEM-CODE IDs, and delta IDs (`KMP-001`, `ANDROID-002`, `MOBILE-PERF-001`) in the same finding field.

Severity values are the base checklists': CRITICAL, HIGH, MEDIUM, LOW.

---

## Traceability Preconditions

- [ ] Determine the traceability mode from `artifacts.toml` for the relevant system/artifact: `FULL` vs `DOCS-ONLY`
- [ ] If `FULL`: resolve the FEATURE-MOBILE design source to trace against
- [ ] If `DOCS-ONLY`: skip marker requirements and validate semantics against the provided design sources
- [ ] Confirm markers use the mobile ID prefix scheme `cpt-{hierarchy-prefix}-{kind}-{slug}`

---

## Semantic Alignment At This Layer

Apply the sdlc `SEM-CODE-001..007` checks with these artifact substitutions:

| Base check | Reads as, in this kit |
|------------|-----------------------|
| SEM-CODE-001 Resolve Design Sources | Resolve `FEATURE-MOBILE` via `@cpt-*` markers; fall back to `DESIGN-EPIC` |
| SEM-CODE-002 Spec Context Semantics | Feature Context of `FEATURE-MOBILE`; actors are `cpt-superapp-actor-*` |
| SEM-CODE-003 Spec Flows Semantics | Section 2 Actor Flows (CDSL) |
| SEM-CODE-004 Algorithms Semantics | Section 3 Processes / Business Logic (CDSL), per target (KMP / Android / iOS / WebView) |
| SEM-CODE-005 State Semantics | Section 4 States (CDSL) plus the `DESIGN-EPIC` screen state model |
| SEM-CODE-006 Definition of Done Semantics | Section 5 Definitions of Done and section 6 Acceptance Criteria |
| SEM-CODE-007 Overall Design Consistency | `DESIGN-EPIC` → `DESIGN-MINIAPP` → `DESIGN-PLATFORM`, in that order of locality |

Additional alignment requirements at this layer:

- [ ] Code placed in `constructor-sdk/` implements only processes whose target is KMP shared
- [ ] Code placed in `android-app/` or `ios-app/` implements only processes whose target is that platform
- [ ] A process specified as shared is not reimplemented per platform
- [ ] Kernel services are consumed through the contracts named in `DESIGN-PLATFORM`, not reimplemented

---

## Delta: KMP Shared Code

### KMP-001: State Immutability
**Severity**: HIGH

- [ ] State classes are immutable data classes; updates create a new instance
- [ ] No mutable collections or `var` fields exposed in state
- [ ] State is exposed as an observable stream, never as a mutable holder

### KMP-002: Intent Pattern
**Severity**: HIGH

- [ ] Every user action arrives as a declared intent type
- [ ] The intent set is exhaustive and each intent has a defined reduction
- [ ] UI never mutates state directly

### KMP-003: Effect Pattern
**Severity**: MEDIUM

- [ ] One-shot outcomes (navigation, toasts, dialogs) are effects, not state
- [ ] Effects are consumed once and are not replayed on recomposition or reattachment

### KMP-004: Use Case Design
**Severity**: HIGH

- [ ] Each use case has a single responsibility and returns a result type rather than throwing across the boundary
- [ ] Business rules live in use cases, not in ViewModels or UI
- [ ] Input validation happens before any repository call

### KMP-005: Repository Pattern
**Severity**: HIGH

- [ ] Repositories are the only source of remote and local data for the feature
- [ ] Cache read, staleness, write-through, and offline fallback match the FEATURE-MOBILE repository process
- [ ] Platform-specific behavior is behind an expect/actual boundary, not an `if (platform)` branch

### KMP-006: Concurrency Discipline
**Severity**: HIGH

- [ ] Long-running work runs off the main dispatcher, with the dispatcher injected rather than hardcoded
- [ ] Coroutine scopes are cancelled with their owner; no leaked scopes
- [ ] Shared mutable state across coroutines is protected or eliminated

---

## Delta: Android Code

### ANDROID-001: Compose Correctness
**Severity**: HIGH

- [ ] Composables are side-effect free apart from declared effect APIs
- [ ] State is hoisted; no business logic inside composables
- [ ] Lists use stable keys; expensive work is remembered rather than recomputed per recomposition

### ANDROID-002: State Handling
**Severity**: HIGH

- [ ] State is collected in a lifecycle-aware way
- [ ] Configuration change and process death restore the state described in FEATURE-MOBILE
- [ ] No state is duplicated between the ViewModel and composable-local state

### ANDROID-003: Navigation
**Severity**: MEDIUM

- [ ] Navigation destinations and arguments match the DESIGN-EPIC navigation section
- [ ] Deep links are registered as designed and validate their parameters
- [ ] Back behavior including unsaved state matches the design

### ANDROID-004: Lifecycle Awareness
**Severity**: HIGH

- [ ] Work started for the screen is cancelled when the screen leaves
- [ ] Background/foreground transitions behave as specified
- [ ] No leaked listeners, receivers, or observers

### ANDROID-005: Accessibility
**Severity**: HIGH

- [ ] Interactive elements have content descriptions or semantics
- [ ] Touch targets meet the platform minimum
- [ ] Layout survives large font scales; state changes are announced

---

## Delta: iOS Code

### IOS-001: SwiftUI Correctness
**Severity**: HIGH

- [ ] View bodies are pure; no side effects outside declared task/onChange APIs
- [ ] Property wrappers match ownership semantics (`@State` local, `@ObservedObject`/`@StateObject` correctly chosen)
- [ ] Lists provide stable identity

### IOS-002: KMP Integration
**Severity**: HIGH

- [ ] Shared ViewModels are consumed through the generated interface, not reimplemented
- [ ] Kotlin flows are bridged with cancellation propagated
- [ ] Kotlin result and error types are mapped once, at the boundary

### IOS-003: State Handling
**Severity**: HIGH

- [ ] State observation matches scene lifecycle
- [ ] Scene-phase transitions restore state as specified in FEATURE-MOBILE
- [ ] No state duplicated between the shared ViewModel and view-local state

### IOS-004: Navigation
**Severity**: MEDIUM

- [ ] Navigation matches the DESIGN-EPIC navigation section
- [ ] Universal links / custom scheme handling validates parameters
- [ ] Dismiss behavior including unsaved state matches the design

### IOS-005: Accessibility
**Severity**: HIGH

- [ ] Accessibility labels, traits, and values are set on interactive elements
- [ ] Touch targets meet the platform minimum
- [ ] Dynamic Type is supported; state changes are announced

---

## Delta: WebView Bridge Code

### WEBVIEW-001: Bridge Surface
**Severity**: HIGH

- [ ] Only the bridge methods declared in DESIGN-PLATFORM / DESIGN-EPIC are exposed
- [ ] Every inbound call validates its parameters before acting
- [ ] Bridge errors return a defined response rather than failing silently

### WEBVIEW-002: Session Propagation
**Severity**: CRITICAL

- [ ] The session is propagated by the mechanism the design specifies
- [ ] No token appears in a URL, query string, or log
- [ ] Only allowed origins may call the bridge

### WEBVIEW-003: Failure Surface
**Severity**: MEDIUM

- [ ] Page-load failure shows the native error surface with retry
- [ ] Offline entry into a WebView screen behaves as designed

---

## Delta: Mobile Performance

### MOBILE-PERF-001: Network
**Severity**: HIGH

- [ ] Requests are batched or paged as designed; no N+1 request patterns per list item
- [ ] Responses are cached per the repository process; conditional requests are used where designed
- [ ] Timeouts and retry/backoff are configured, not left at library defaults where the design states otherwise

### MOBILE-PERF-002: UI
**Severity**: HIGH

- [ ] No blocking work on the main thread or main actor
- [ ] Images are downsampled and cached; large media is loaded lazily
- [ ] Long lists page rather than materializing the whole set

### MOBILE-PERF-003: Memory And Startup
**Severity**: MEDIUM

- [ ] No retained references to destroyed screens
- [ ] Feature initialization does not run at app launch unless the design requires it
- [ ] Any measurable app-size or startup impact is within the platform budget stated in DESIGN-PLATFORM

---

## Delta: Mobile Security

### MOBILE-SEC-001: Data Protection
**Severity**: CRITICAL

- [ ] Tokens and credentials are stored in Keychain / Keystore, never in plain preferences or files
- [ ] Sensitive fields are not written to logs, crash reports, or analytics
- [ ] Local databases holding personal data are encrypted where the design requires it

### MOBILE-SEC-002: Authentication And Session
**Severity**: HIGH

- [ ] Session refresh and expiry follow the kernel auth contract
- [ ] Logout clears local state, caches, and queued writes for the feature
- [ ] Authenticated screens reached by deep link enforce the auth requirement

### MOBILE-SEC-003: Input And Transport
**Severity**: HIGH

- [ ] All external input, including deep link and bridge parameters, is validated
- [ ] TLS is enforced; certificate handling is not weakened for convenience
- [ ] Debug-only affordances are compiled out of release builds

---

## Reporting

Use the report format from `{cf-studio-path}/.core/requirements/code-checklist.md` without modification.

Additional reporting requirements for this kit:

- [ ] Report generic, semantic-alignment, and mobile-delta findings in one merged report, ordered by severity
- [ ] State the traceability mode used (FULL or DOCS-ONLY) and, in FULL mode, the marker coverage percentage
- [ ] State the platform allocation result: which reviewed code is shared, which is Android, which is iOS, and whether any shared process was duplicated per platform

# DESIGN-MINIAPP Checklist — Layer Delta

**Artifact**: DESIGN-MINIAPP
**Kit**: mobile-superapp
**Level**: L1 (MiniApp)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/DESIGN/checklist.md` (sdlc DESIGN Expert Checklist)

This checklist is a **delta over the sdlc DESIGN Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a DESIGN-MINIAPP document; this file states how each expertise domain is scoped at the MiniApp layer and adds the criteria that exist only at this layer.

---

## Table of Contents

1. [How To Use This Checklist](#how-to-use-this-checklist)
2. [Expertise Domain Scope At This Layer](#expertise-domain-scope-at-this-layer)
3. [Layer Delta: MUST HAVE](#layer-delta-must-have)
4. [Layer Delta: MUST NOT HAVE](#layer-delta-must-not-have)
5. [Layer Delta: Mobile-Specific Criteria](#layer-delta-mobile-specific-criteria)
6. [Reporting](#reporting)

---

## How To Use This Checklist

1. **LOAD the base checklist first** and apply it in full: Referenced Standards, Review Scope Selection, Prerequisites, Evidence Requirements (STRICT mode), Applicability Context, Severity Dictionary, all MUST HAVE domains (ARCH, SEM, PERF, SEC, REL, DATA, INT, OPS, MAINT, TEST, COMPL, UX, BIZ, DOC), and all MUST NOT HAVE items.
2. **Apply the domain scope table** below. Where a domain is marked *Inherited*, the MiniApp design satisfies it by referencing the platform design element by ID and documenting deviations only — restating it is a violation of `DESIGN-MINIAPP-NO-001`, and omitting it without a reference is a violation of base `DOC-DESIGN-001`.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report containing findings from both the base and this delta, citing base IDs (`ARCH-DESIGN-002`) and delta IDs (`DESIGN-MINIAPP-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L1 (MiniApp) | Notes |
|--------|-----------------------|-------|
| ARCH | Full | Module structure, component model, navigation, and internal dependency direction are owned here |
| SEM | Full | Every MiniApp PRD requirement and public interface must map to a design element |
| PERF | Narrowed | MiniApp-specific budgets (screen load, list rendering, payload size); platform budgets are inherited |
| SEC | Narrowed | Data sensitivity of this MiniApp's storage and its authorization checks; auth mechanics are inherited |
| REL | Narrowed | This MiniApp's offline behavior, retry, and cache policy within the platform's offline architecture |
| DATA | Full | MiniApp domain model, repositories, and local stores are owned here |
| INT | Full | Backend endpoints and real-time channels this MiniApp consumes are owned here |
| OPS | Inherited | Build, release, and observability are platform-owned; note only MiniApp-specific flags or rollout gating |
| MAINT | Full | Module boundaries, module dependency rules, and public-surface versioning are owned here |
| TEST | Narrowed | Verification approach per NFR and per contract; test cases are deferred to FEATURE/code |
| COMPL | Inherited | Reference the platform obligation; list only what this MiniApp's data or content adds |
| UX | Narrowed | Navigation graph and native/WebView allocation per screen; screen design is deferred |
| BIZ | Inherited | Business goals are referenced from the PRD, never restated |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

*Deferred* domains name their target artifact: TEST → `FEATURE-MOBILE`, UX screen design → `DESIGN-EPIC`.

---

## Layer Delta: MUST HAVE

### DESIGN-MINIAPP-001: Platform Design Inheritance
**Severity**: CRITICAL

- [ ] The parent platform design is linked, and inherited layers, kernel contracts, and the MiniApp lifecycle are referenced by platform ID
- [ ] Inherited platform NFRs are listed, with deviations documented and justified
- [ ] No inherited element is redefined or contradicted
- [ ] Every referenced platform ID exists in the platform design (verified, not assumed)

### DESIGN-MINIAPP-002: Module Structure Across Targets
**Severity**: CRITICAL

- [ ] Shared, Android, and iOS modules are all defined with source locations
- [ ] The module table states responsibility and technology per module
- [ ] Module dependencies are listed with the interface used
- [ ] The structure is consistent with the platform layer model

### DESIGN-MINIAPP-003: Component Contract Per Module
**Severity**: CRITICAL

- [ ] Each module and cross-cutting component is documented with the base component contract (why it exists, responsibility scope, responsibility boundaries, technology and location, related components by ID)
- [ ] Responsibility boundaries state what is delegated to the kernel and what is delegated to epics
- [ ] No two components claim the same responsibility

### DESIGN-MINIAPP-004: Domain Model And Repositories
**Severity**: CRITICAL

- [ ] Core entities are listed with IDs and locations
- [ ] Entity relationships are shown
- [ ] Repository interfaces are given as signatures with their result/error type
- [ ] The domain layer has no outward dependency on data or presentation

### DESIGN-MINIAPP-005: Navigation And Deep Links
**Severity**: HIGH

- [ ] A navigation graph shows entry point and internal routes
- [ ] The screen inventory names the owning epic and the implementation type (native / WebView) per screen
- [ ] Deep links are listed with parameters and auth expectation
- [ ] Unknown, unauthorized, and cold-start link handling is specified

### DESIGN-MINIAPP-006: State Management Contracts
**Severity**: HIGH

- [ ] The state, intent, and effect contracts are given as type signatures
- [ ] The unidirectional flow is stated, consistent with the platform principle
- [ ] Persisted vs transient state is separated, with the store named
- [ ] Restore behavior after process death is stated

### DESIGN-MINIAPP-007: Kernel Integration
**Severity**: CRITICAL

- [ ] Every kernel service this MiniApp consumes is listed with the kernel contract ID, usage, and criticality
- [ ] The host contract implementation covers every lifecycle callback
- [ ] Behavior when a consumed kernel service is unavailable is stated
- [ ] No kernel internal is reached around the published contract

### DESIGN-MINIAPP-008: API Contracts And External Dependencies
**Severity**: HIGH

- [ ] Backend endpoints are listed with method, path, request, and response shape
- [ ] Real-time channels, where used, list their events
- [ ] Each external dependency states protocol, contract ID, and failure mode
- [ ] Every interface declared in the PRD's Public MiniApp Interfaces section has a realizing contract with stability

### DESIGN-MINIAPP-009: Local Stores And Schemas
**Severity**: HIGH

- [ ] Each local store is declared with technology and an ID
- [ ] Tables list columns, types, primary key, and constraints
- [ ] Migration, retention, and encryption are stated where the data warrants it
- [ ] Cached data has a staleness policy consistent with the platform offline architecture

### DESIGN-MINIAPP-010: Dependency Rules Stated
**Severity**: HIGH

- [ ] Rules forbid dependency on another MiniApp and require kernel contracts only
- [ ] Platform UI modules depend on the shared module and never the reverse
- [ ] Cross-MiniApp navigation goes through the platform router
- [ ] No circular dependency between this MiniApp's modules

### DESIGN-MINIAPP-011: Traceability And Requirement Coverage
**Severity**: HIGH

- [ ] Links to the MiniApp PRD, platform DESIGN, ADR folder, DECOMPOSITION, and epic folders are present
- [ ] The requirement coverage table maps PRD FRs, NFRs, and interfaces to design elements by ID
- [ ] Every referenced PRD ID exists in the PRD (verified, not assumed)

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### DESIGN-MINIAPP-NO-001: No Platform Design Duplication
**Severity**: HIGH

**What to check**:
- [ ] No redefined platform layers, kernel internals, or MiniApp container model
- [ ] No restated platform-wide dependency rules or NFR thresholds beyond a reference
- [ ] No re-derivation of the native/WebView strategy or KMP scope

**Where it belongs**: `DESIGN-PLATFORM` — reference by ID and document deviations only

### DESIGN-MINIAPP-NO-002: No Screen-Level Design
**Severity**: HIGH

**What to check**:
- [ ] No screen composition, widget hierarchy, or per-screen component inventory
- [ ] No per-screen state, intents, or effects
- [ ] No screen-level error state catalogue

**Where it belongs**: `DESIGN-EPIC`

### DESIGN-MINIAPP-NO-003: No Implementation Bodies
**Severity**: HIGH

**What to check**:
- [ ] Code blocks are interface signatures, state contracts, or schemas only
- [ ] No method bodies, algorithms, or copy-pasted production code
- [ ] No DI wiring code beyond naming the mechanism

**Where it belongs**: code, `IMPL-KMP` / `IMPL-ANDROID` / `IMPL-IOS` (conventions)

### DESIGN-MINIAPP-NO-004: No Product Requirements
**Severity**: HIGH

**What to check**:
- [ ] No business requirements, user stories, or acceptance criteria
- [ ] No requirement priorities re-litigated here

**Where it belongs**: `PRD-MINIAPP`

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-DESIGN-MINIAPP-001: Cross-Platform Parity
**Severity**: HIGH

- [ ] Android and iOS module responsibilities are symmetric, or divergence is justified
- [ ] Shared logic is placed in the shared module rather than duplicated per platform
- [ ] Platform-specific behavior is named explicitly, not left implicit

### MOBILE-DESIGN-MINIAPP-002: Offline And Cache Design
**Severity**: HIGH

- [ ] Which operations work offline is specified, consistent with the PRD offline policy
- [ ] Cache scope, invalidation, and staleness signalling are specified
- [ ] Write operations attempted offline are specified as queued, blocked, or degraded
- [ ] Conflict resolution on sync is specified where writes can queue

### MOBILE-DESIGN-MINIAPP-003: WebView Allocation
**Severity**: MEDIUM

- [ ] Screens implemented as WebView are identified with a reason
- [ ] The data and session passed into the WebView is specified
- [ ] Native/WebView navigation hand-back is specified

### MOBILE-DESIGN-MINIAPP-004: Notifications And Background Work
**Severity**: MEDIUM

- [ ] Notification categories this MiniApp publishes or consumes are named with their routing target
- [ ] Background work (sync, prefetch, upload) is specified with its trigger and OS constraints
- [ ] Behavior when background execution is denied by the OS is specified

### MOBILE-DESIGN-MINIAPP-005: Resource Footprint
**Severity**: MEDIUM

- [ ] Eager vs lazy initialization at MiniApp start is specified
- [ ] Memory-heavy resources (media, large lists) have a bounded strategy
- [ ] Disposal behavior on `dispose()` releases every resource this MiniApp acquired

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/DESIGN/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, Evidence Requirements, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For every domain marked Narrowed, Deferred, or Inherited in the scope table, confirm the design references the platform element or names the artifact that carries the deferred content

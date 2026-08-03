# DESIGN-PLATFORM Checklist — Layer Delta

**Artifact**: DESIGN-PLATFORM
**Kit**: mobile-superapp
**Level**: L0 (Platform / Host App)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/DESIGN/checklist.md` (sdlc DESIGN Expert Checklist)

This checklist is a **delta over the sdlc DESIGN Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a DESIGN-PLATFORM document; this file states how each expertise domain is scoped at the platform layer and adds the criteria that exist only at this layer.

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
2. **Apply the domain scope table** below. Where a domain is marked *Deferred*, the platform design satisfies it by defining the pattern and naming the artifact that instantiates it — silently dropping the domain is a violation of base `DOC-DESIGN-001`. The platform layer is the widest design scope: ARCH, SEC, INT, and OPS criteria carry the most weight here.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section for a single merged report containing findings from both the base and this delta, citing base IDs (`ARCH-DESIGN-002`) and delta IDs (`DESIGN-PLATFORM-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L0 (Platform) | Notes |
|--------|------------------------|-------|
| ARCH | Full | Layers, component model, dependency rules, and the MiniApp container model are owned here |
| SEM | Full | Every platform PRD requirement, actor, and public interface must map to a design element |
| PERF | Full | Cold start, memory, and battery budgets are allocated here; MiniApps inherit them |
| SEC | Full | Auth kernel, token lifecycle, secure storage, and transport security are owned here |
| REL | Full | Offline queue, retry, sync, and kernel failure modes are owned here |
| DATA | Narrowed | Platform-owned stores and shared domain entities only; per-MiniApp persistence is deferred |
| INT | Full | Every external system the platform talks to is documented here with protocol and failure mode |
| OPS | Full | Build targets, distribution channels, release and update policy, observability are owned here |
| MAINT | Full | Module boundaries, versioning of kernel contracts, and deprecation policy are owned here |
| TEST | Narrowed | Verification approach per NFR and per contract; test cases are deferred to FEATURE/code |
| COMPL | Narrowed | Platform-wide obligations (store policy, privacy manifest, data residency); feature-level consent is deferred |
| UX | Narrowed | Navigation shell, native/WebView split, and platform UX conventions; screen design is deferred |
| BIZ | Inherited | Business goals are referenced from the PRD, never restated |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

*Deferred* domains name their target artifact: DATA → `DESIGN-MINIAPP`, TEST → `FEATURE-MOBILE`, UX → `DESIGN-EPIC`, COMPL feature-level → `PRD-EPIC`.

---

## Layer Delta: MUST HAVE

### DESIGN-PLATFORM-001: Platform Layers Defined Once
**Severity**: CRITICAL

- [ ] A layer diagram shows presentation, application, domain, and infrastructure layers
- [ ] The layer table states responsibility, technology, and source location per layer
- [ ] Layers carry an ID (`cpt-{hierarchy-prefix}-tech-layers` or per-layer IDs)
- [ ] Every layer's allowed dependency direction is stated
- [ ] MiniApp and epic designs can inherit these layers without redefining them

### DESIGN-PLATFORM-002: Cross-Platform Strategy
**Severity**: CRITICAL

- [ ] A native vs WebView decision matrix covers every content type with a rationale
- [ ] The KMP SDK scope lists what is shared and what stays platform-specific
- [ ] A code sharing matrix shows Android / iOS / shared coverage per module
- [ ] The hybrid decision references an ADR

### DESIGN-PLATFORM-003: MiniApp Container Model
**Severity**: CRITICAL

- [ ] The container diagram shows host, kernel, registry, and MiniApp slots
- [ ] The MiniApp registration contract is given as an interface signature
- [ ] Isolation between MiniApps is stated (what a MiniApp can and cannot reach)
- [ ] The container is declared with ID `cpt-{hierarchy-prefix}-component-miniapp-container`

### DESIGN-PLATFORM-004: MiniApp Lifecycle
**Severity**: HIGH

- [ ] All lifecycle states are named with an initial state
- [ ] Every transition states its trigger
- [ ] Failure handling for initialization and disposal is stated
- [ ] The lifecycle is declared with ID `cpt-{hierarchy-prefix}-state-miniapp-lifecycle`

### DESIGN-PLATFORM-005: Shared Kernel Component Contract
**Severity**: CRITICAL

- [ ] Auth, storage, networking, and notification kernel modules are each documented with the base component contract (why it exists, responsibility scope, responsibility boundaries, technology and location, related components by ID)
- [ ] Each kernel module declares which MiniApp-facing contract it exposes and that contract's stability
- [ ] Responsibility boundaries state what the kernel delegates to MiniApps
- [ ] No two kernel modules claim the same responsibility

### DESIGN-PLATFORM-006: NFR Allocation Completeness
**Severity**: CRITICAL

- [ ] Every NFR in the platform PRD appears in the NFR allocation table
- [ ] Each row names the layer/component/mechanism, the design response, and the verification approach
- [ ] NFRs that MiniApps inherit are marked as such, so MiniApp designs know what they are bound by

### DESIGN-PLATFORM-007: Public Platform Surface Realized
**Severity**: HIGH

- [ ] Every interface declared in the PRD's Public Platform Interfaces section has a realizing contract here
- [ ] Each contract states technology, location, and stability
- [ ] The deep link scheme and its segment ownership are specified
- [ ] Breaking-change handling for a consumed contract is stated

### DESIGN-PLATFORM-008: Dependency Rules Stated
**Severity**: HIGH

- [ ] Internal dependencies are listed with the interface used, not the internal types
- [ ] Explicit rules forbid circular kernel dependencies and MiniApp-to-MiniApp dependencies
- [ ] Platform-specific modules depend on the shared module and never the reverse
- [ ] Only adapter/integration modules talk to external systems

### DESIGN-PLATFORM-009: External Integrations
**Severity**: HIGH

- [ ] Every external system is declared with ID `cpt-{hierarchy-prefix}-integration-{slug}`
- [ ] Direction, protocol, authentication, and key contracts are stated per integration
- [ ] A failure mode is stated per integration (what the platform does when it is unavailable)
- [ ] Vendor/OS services (push, store, biometrics) are included, not only backends

### DESIGN-PLATFORM-010: Build And Distribution Topology
**Severity**: MEDIUM

- [ ] Build targets and their artifacts are listed per platform
- [ ] Distribution channels are named
- [ ] The shared-module packaging form per platform is stated
- [ ] Declared with ID `cpt-{hierarchy-prefix}-topology-{slug}`

### DESIGN-PLATFORM-011: Traceability And Requirement Coverage
**Severity**: HIGH

- [ ] Links to the platform PRD, ADR folder, DECOMPOSITION, and MiniApps folder are present
- [ ] The requirement coverage table maps PRD FRs and NFRs to design elements by ID
- [ ] Every referenced PRD ID exists in the PRD (verified, not assumed)

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items, all of which apply here unchanged.

### DESIGN-PLATFORM-NO-001: No MiniApp-Internal Design
**Severity**: HIGH

**What to check**:
- [ ] No MiniApp module structure or package layout
- [ ] No MiniApp navigation graph or route table
- [ ] No MiniApp state-management specifics
- [ ] No per-MiniApp repository or use-case inventory

**Where it belongs**: `DESIGN-MINIAPP`

### DESIGN-PLATFORM-NO-002: No Screen-Level Design
**Severity**: MEDIUM

**What to check**:
- [ ] No screen composition, widget hierarchy, or per-screen state
- [ ] No per-screen intents, effects, or view models

**Where it belongs**: `DESIGN-EPIC`

### DESIGN-PLATFORM-NO-003: No Implementation Bodies
**Severity**: HIGH

**What to check**:
- [ ] Code blocks are interface signatures, schemas, or diagrams only
- [ ] No method bodies, algorithms, or copy-pasted production code
- [ ] No build script contents beyond the target/artifact table

**Where it belongs**: code, `IMPL-KMP` / `IMPL-ANDROID` / `IMPL-IOS` (conventions)

### DESIGN-PLATFORM-NO-004: No Product Requirements
**Severity**: HIGH

**What to check**:
- [ ] No business requirements, user stories, or acceptance criteria
- [ ] No requirement priorities re-litigated here

**Where it belongs**: `PRD-PLATFORM`

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-DESIGN-PLATFORM-001: Native Shell And WebView Bridge
**Severity**: CRITICAL

- [ ] The native shell is specified per platform (UI toolkit, navigation implementation)
- [ ] The WebView container design is specified, including the JS bridge surface
- [ ] Session/token propagation into the WebView is specified with its security properties
- [ ] WebView → native communication and its allowed operations are bounded

### MOBILE-DESIGN-PLATFORM-002: Offline Architecture
**Severity**: HIGH

- [ ] The offline queue mechanism and its durability guarantees are specified
- [ ] Cache scope, eviction, and staleness signalling are specified
- [ ] The sync/conflict-resolution approach is specified
- [ ] Network-state detection and the transition behavior are specified

### MOBILE-DESIGN-PLATFORM-003: Push Notification Architecture
**Severity**: HIGH

- [ ] Android and iOS transport integrations are both specified
- [ ] Token registration, refresh, and revocation flows are specified
- [ ] Routing from a notification tap to the owning MiniApp is specified
- [ ] Behavior when notification permission is absent or revoked is specified

### MOBILE-DESIGN-PLATFORM-004: Deep Link Architecture
**Severity**: HIGH

- [ ] The deep link format is specified with segment ownership per MiniApp
- [ ] Routing, parameter parsing, and validation are specified
- [ ] Cold-start queueing and replay after kernel readiness are specified
- [ ] Unknown, unauthorized, and malformed link handling is specified

### MOBILE-DESIGN-PLATFORM-005: Startup And Resource Budget
**Severity**: HIGH

- [ ] Cold-start sequence is documented with what is initialized eagerly vs lazily
- [ ] Per-MiniApp resource expectations (memory, background work) are bounded
- [ ] Background/foreground transition handling is specified for the kernel

### MOBILE-DESIGN-PLATFORM-006: Store And OS Constraints
**Severity**: MEDIUM

- [ ] Store policy constraints that shape the architecture are recorded as constraints with IDs
- [ ] The OS baseline from the PRD is reflected in technology choices
- [ ] Forced-update / minimum-supported-version enforcement is specified

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/DESIGN/checklist.md` — without modification: the Validation Summary, Reporting Readiness Checklist, Full/Compact report formats, Evidence Requirements, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For every domain marked Narrowed, Deferred, or Inherited in the scope table, confirm the design names the artifact that carries the deferred content instead of dropping it

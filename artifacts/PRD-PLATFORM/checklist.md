# PRD-PLATFORM Checklist — Layer Delta

**Artifact**: PRD-PLATFORM
**Kit**: mobile-superapp
**Level**: L0 (Platform / Host App)
**Base Checklist**: `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/checklist.md` (sdlc PRD Expert Checklist)

This checklist is a **delta over the sdlc PRD Expert Checklist**, not a replacement. Every criterion in the base checklist applies to a PRD-PLATFORM document; this file states how each expertise domain is scoped at the platform layer and adds the criteria that exist only at this layer.

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

1. **LOAD the base checklist first** and apply it in full: Referenced Standards, Prerequisites, Applicability Context, Severity Dictionary, Applicability Determination, Checkpointing, all MUST HAVE domains (BIZ, ARCH, SEC, SAFE, PERF, REL, UX, MAINT, COMPL, DATA, INT, OPS, TEST, DOC), and all MUST NOT HAVE items.
2. **Apply the domain scope table** below. For each expertise domain it states whether the domain applies in full at this layer, applies with a narrowed scope, or is delegated downward to another artifact. A delegated domain is not a free pass: verify the PRD delegates it explicitly (per base `DOC-PRD-001`), rather than silently omitting it.
3. **Apply the delta criteria** in this file after the base pass.
4. **Report once.** Use the base checklist's Reporting section — its report format, Reporting Readiness Checklist, and Reporting Commitment — for a single merged report containing findings from both the base and this delta. Cite base IDs (`BIZ-PRD-001`) and delta IDs (`PRD-PLATFORM-001`) in the same `Checklist Item` field.

Severity values are the base checklist's: CRITICAL, HIGH, MEDIUM, LOW.

---

## Expertise Domain Scope At This Layer

| Domain | Scope at L0 (Platform) | Notes |
|--------|------------------------|-------|
| BIZ | Full | Platform vision, goals, glossary, assumptions, risks, non-goals are owned here |
| ARCH | Full | Scope boundaries and the platform/MiniApp split are owned here; component decomposition stays in DESIGN-PLATFORM |
| SEC | Full | Authentication, authorization, data classification, audit, privacy are platform-wide and set once here |
| SAFE | Narrowed | Applicable only if the platform can cause physical/behavioral harm (e.g., proctoring lockdown, driving-mode restrictions); otherwise delegate explicitly |
| PERF | Full | Cold start, navigation responsiveness, and capacity expectations set as project-wide defaults |
| REL | Full | Availability, degraded/offline behavior, crash-free-session targets set as project-wide defaults |
| UX | Full | Accessibility, i18n, device/platform support, inclusivity apply platform-wide; per-screen UX is delegated to PRD-EPIC |
| MAINT | Full | Documentation and support expectations for the platform and its MiniApp authors |
| COMPL | Full | Regulatory, industry, legal, and app-store obligations apply to the whole app binary and are owned here |
| DATA | Full | Data ownership, quality, and lifecycle across MiniApps are owned here |
| INT | Full | External systems and platform-consumed contracts are owned here; contract schemas stay in DESIGN-PLATFORM |
| OPS | Narrowed | Release channels, staged rollout, minimum-version enforcement, and monitoring expectations at business level; infrastructure is out of scope for any PRD |
| TEST | Full | Acceptance criteria and testability of platform requirements |
| DOC | Full | Explicit non-applicability is mandatory at every layer |

---

## Layer Delta: MUST HAVE

### PRD-PLATFORM-001: Actor Single Source Of Truth
**Severity**: CRITICAL

- [ ] Every actor used anywhere in the project is defined in this document with an ID `cpt-{hierarchy-prefix}-actor-{slug}`
- [ ] Human and system actors are separated
- [ ] Each actor has description, goals/interaction, and usage context
- [ ] No actor is introduced for the first time in a MiniApp or Epic PRD
- [ ] Actor IDs are stable — renaming an actor is treated as a breaking change to every referencing artifact

### PRD-PLATFORM-002: Platform / MiniApp Boundary
**Severity**: CRITICAL

- [ ] Section 1.1 states which responsibilities belong to the platform and which to MiniApps
- [ ] Every platform FR is a host-app or shared-kernel capability, not a capability owned by exactly one MiniApp
- [ ] Each platform FR names its consumers (`Consumed By`: all MiniApps, or a specific list)
- [ ] Capabilities deliberately left to MiniApps appear in Out of Scope

### PRD-PLATFORM-003: Runtime Baselines Declared Once
**Severity**: HIGH

- [ ] Supported OS minimum and target versions are stated for both iOS and Android with rationale
- [ ] Device classes and their support level (full / degraded / unsupported) are stated
- [ ] Connectivity assumptions and app lifecycle expectations are stated at business level
- [ ] Update policy (forced update, minimum supported app version window) is stated
- [ ] These baselines are stated here so MiniApp and Epic PRDs only document deviations

### PRD-PLATFORM-004: Public Platform Surface
**Severity**: HIGH

- [ ] Every contract MiniApps consume from the platform is listed with an ID `cpt-{hierarchy-prefix}-interface-{slug}`
- [ ] Each interface declares Type, Stability (stable / unstable / experimental), and Breaking Change Policy
- [ ] External integration contracts declare Direction, Capability, and Compatibility guarantees
- [ ] Deep-link scheme ownership is explicit (which segment of the scheme belongs to the platform vs each MiniApp)
- [ ] No endpoint, payload, or schema detail — only business-level capability and compatibility

### PRD-PLATFORM-005: NFR Inheritance Contract
**Severity**: HIGH

- [ ] Each platform NFR states a quantitative Threshold with units and measurement conditions
- [ ] Each platform NFR states `Applies To` (all MiniApps, or a specific list)
- [ ] Quality attributes deliberately not constrained platform-wide are listed in NFR Exclusions with reasoning
- [ ] NFRs are business-level outcomes, not implementation instructions

### PRD-PLATFORM-006: Requirement ID And Priority Contract
**Severity**: HIGH

- [ ] Every actor, FR, NFR, interface, contract, and use case is a checkbox with a priority marker and ID: `- [ ] \`pN\` - **ID**: \`cpt-...\``
- [ ] Priorities `p1`-`p9` are assigned by business impact, not by author convenience
- [ ] All IDs follow `cpt-{hierarchy-prefix}-{kind}-{slug}` with the hierarchy prefix registered in `artifacts.toml`
- [ ] No duplicate IDs within the document (verified with `cfs list-ids`)

### PRD-PLATFORM-007: MiniApp Map
**Severity**: MEDIUM

- [ ] The MiniApp inventory lists each MiniApp with its primary actors and the platform FRs it consumes
- [ ] Each listed MiniApp links to its PRD, or is marked as not yet documented
- [ ] The map is consistent with `artifacts.toml` registration
- [ ] Sequencing, effort, and dependency ordering are delegated to DECOMPOSITION-PLATFORM, not duplicated here

### PRD-PLATFORM-008: ID Reference Appendix
**Severity**: LOW

- [ ] The appendix documents every ID pattern used in the document with a concrete example
- [ ] The meaning of `{hierarchy-prefix}` is explained and matches this platform's registered prefix

---

## Layer Delta: MUST NOT HAVE

These are additional to the base checklist's MUST NOT HAVE items (`ARCH-PRD-NO-001/002`, `BIZ-PRD-NO-001/002`, `DATA-PRD-NO-001`, `INT-PRD-NO-001`, `TEST-PRD-NO-001`, `OPS-PRD-NO-001`, `SEC-PRD-NO-001`, `MAINT-PRD-NO-001`), all of which apply here unchanged.

### PRD-PLATFORM-NO-001: No MiniApp-Internal Requirements
**Severity**: HIGH

**What to check**:
- [ ] No requirement whose only consumer is a single MiniApp
- [ ] No MiniApp-specific business rules or content models
- [ ] No MiniApp-internal navigation or state handling

**Where it belongs**: `PRD-MINIAPP` for the owning MiniApp

### PRD-PLATFORM-NO-002: No Screen-Level UI Specifications
**Severity**: MEDIUM

**What to check**:
- [ ] No per-screen layouts, component inventories, or interaction tables
- [ ] No screen state machines (loading / empty / error variants of a specific screen)
- [ ] No copy or microcopy specifications

**Where it belongs**: `PRD-EPIC` (requirements) and `DESIGN-EPIC` (component design)

### PRD-PLATFORM-NO-003: No Kernel Implementation Detail
**Severity**: HIGH

**What to check**:
- [ ] No module/package structure of the shared kernel
- [ ] No dependency-injection, threading, or storage engine choices
- [ ] No KMP/Swift/Kotlin API signatures

**Where it belongs**: `DESIGN-PLATFORM` (structure), `ADR` (decisions), `IMPL-KMP`/`IMPL-IOS`/`IMPL-ANDROID` (implementation reference)

---

## Layer Delta: Mobile-Specific Criteria

### MOBILE-PLATFORM-001: Offline Policy
**Severity**: HIGH

- [ ] The platform-wide offline expectation is stated (which classes of flow must work without network)
- [ ] Sync/conflict expectations are stated at business level, not as an algorithm
- [ ] Offline behavior of authentication and session validity is stated

### MOBILE-PLATFORM-002: Cross-Platform Parity
**Severity**: HIGH

- [ ] The default parity rule between iOS and Android is stated (full parity, or documented exceptions)
- [ ] Any platform-conditional capability is listed with the reason (OS API, store policy, hardware)

### MOBILE-PLATFORM-003: Notification Capability
**Severity**: HIGH

- [ ] Push notification capability, channel/category ownership, and permission-prompt policy are stated
- [ ] Delivery expectations are business-level (e.g., "delivered within 1 minute at p95"), not APNs/FCM configuration

### MOBILE-PLATFORM-004: Store And Release Constraints
**Severity**: MEDIUM

- [ ] App Store and Google Play policy constraints that shape requirements are stated (e.g., account deletion, in-app purchase rules, data-safety declarations)
- [ ] Release cadence and staged-rollout expectations are stated at business level

### MOBILE-PLATFORM-005: Accessibility Baseline
**Severity**: HIGH

- [ ] The platform-wide accessibility target is stated with a standard reference (e.g., WCAG 2.2 AA as adapted for native mobile)
- [ ] Platform assistive-technology support (VoiceOver, TalkBack, Dynamic Type, high contrast) is stated as a requirement all MiniApps inherit

---

## Reporting

Use the **base checklist's Reporting section** — `{cf-studio-path}/config/kits/sdlc/artifacts/PRD/checklist.md` — without modification: the Validation Summary, Explicit Handling Verification, Reporting Readiness Checklist, Full/Compact report formats, and Reporting Commitment.

Additional reporting requirements for this layer:

- [ ] Report base findings and delta findings in one merged report, ordered by severity
- [ ] State the base checklist version/source used, so a reviewer can reproduce the pass
- [ ] For each expertise domain marked Narrowed or delegated in the scope table, confirm the PRD delegates it explicitly rather than omitting it silently

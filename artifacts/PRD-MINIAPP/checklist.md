# PRD-MINIAPP Checklist

**Artifact**: PRD-MINIAPP  
**Kit**: mobile-superapp  
**Level**: L1 (MiniApp)

This checklist provides semantic quality criteria for MiniApp-level Product Requirements Documents in mobile SuperApp projects.

---

## Table of Contents

1. [MUST HAVE Requirements](#must-have-requirements)
2. [SHOULD HAVE Requirements](#should-have-requirements)
3. [MUST NOT HAVE (Violations)](#must-not-have-violations)
4. [Mobile-Specific Criteria](#mobile-specific-criteria)
5. [Reporting](#reporting)

---

## MUST HAVE Requirements

### PRD-MINIAPP-001: Overview Completeness

**Priority**: CRITICAL

The MiniApp PRD MUST include:

- [ ] Clear purpose statement (1-2 paragraphs)
- [ ] Link to parent Platform PRD
- [ ] Version and status metadata
- [ ] In-scope capabilities list
- [ ] Out-of-scope exclusions list

**Why it matters**: Without clear scope definition, development will drift and stakeholders will have misaligned expectations.

### PRD-MINIAPP-002: Platform Traceability

**Priority**: CRITICAL

The PRD MUST include traces to Platform PRD:

- [ ] Table mapping MiniApp to Platform requirements
- [ ] Relation type for each trace (refines, inherits, extends)
- [ ] `cpt-superapp-fr-{slug}` references for refined FRs
- [ ] `cpt-superapp-nfr-{slug}` references for inherited NFRs

**Why it matters**: MiniApp requirements must demonstrate they contribute to Platform-level goals.

### PRD-MINIAPP-003: Actor Definition

**Priority**: HIGH

The PRD MUST define actors:

- [ ] Primary actors table with MiniApp-specific context
- [ ] Actor IDs following `cpt-superapp-actor-{slug}` pattern
- [ ] Description of how each actor uses this MiniApp

**Why it matters**: Actor definitions ensure requirements are user-centered and traceable.

### PRD-MINIAPP-004: Functional Requirements Structure

**Priority**: CRITICAL

Each Functional Requirement MUST include:

- [ ] Checkbox with priority marker: `- [ ] \`pN\` - **ID**: ...` (priority `p1`-`p9` by business impact)
- [ ] Unique ID following `cpt-{miniapp}-fr-{slug}` pattern
- [ ] Verifiable MUST statement (what the system must do)
- [ ] Traces To field (parent Platform FR or "MiniApp-specific" with `miniapp-specific` tag)
- [ ] Actors field referencing `cpt-superapp-actor-{slug}`
- [ ] Rationale (business value or parent requirement)
- [ ] Acceptance criteria (measurable)

**Why it matters**: Well-structured FRs enable traceability, prioritization, and validation.

### PRD-MINIAPP-005: Non-Functional Requirements

**Priority**: HIGH

> **NFR framing**: NFRs MUST be stated as business-level quality expectations — user/business outcomes, SLAs, and measurable targets (e.g., "course list opens in <2s at p95 on a mid-tier device"). Technical implementation (caching strategy, technology stack, component tuning) belongs in DESIGN/ADR.

Each NFR MUST include:

- [ ] Checkbox with priority marker: `- [ ] \`pN\` - **ID**: ...`
- [ ] Unique ID following `cpt-{miniapp}-nfr-{slug}` pattern
- [ ] Business-level MUST statement (user/business outcome, not implementation)
- [ ] Traces To field (parent Platform NFR)
- [ ] Category (Performance, Security, Usability, etc.)
- [ ] Threshold (quantitative target with units and conditions)
- [ ] Rationale for MiniApp-specific value

**Why it matters**: NFRs ensure quality attributes are explicitly defined and measurable.

### PRD-MINIAPP-006: Use Cases

**Priority**: HIGH

The PRD MUST include use cases:

- [ ] Unique ID following `cpt-{miniapp}-usecase-{slug}` pattern
- [ ] Traces To field (which FR it implements)
- [ ] Primary actor reference
- [ ] Preconditions
- [ ] Main flow (numbered steps)
- [ ] Postconditions
- [ ] Exception handling

**Why it matters**: Use cases bridge requirements to implementation by describing user journeys.

### PRD-MINIAPP-007: Dependencies

**Priority**: HIGH

The PRD MUST document dependencies:

- [ ] Platform dependencies table (Kernel services)
- [ ] External dependencies table (Backend, APIs)
- [ ] Dependency types (Required, Optional)
- [ ] Integration descriptions

**Why it matters**: Dependencies define integration scope and external team coordination.

### PRD-MINIAPP-008: Traceability Matrix

**Priority**: CRITICAL

The PRD MUST include traceability matrices:

- [ ] Platform FR → MiniApp FR coverage table
- [ ] Coverage status (Full, Partial, Not in scope)
- [ ] MiniApp FR → Epic coverage table
- [ ] Status for each mapping

**Why it matters**: Traceability ensures complete coverage and enables change impact analysis.

### PRD-MINIAPP-012: Authorization as Exact Permissions

**Priority**: CRITICAL

> **Note**: That every protected capability requires authentication and authorization is assumed and need not be restated per requirement. Instead, specify the **exact permissions**.

The PRD MUST specify:

- [ ] Exact permissions per actor and operation (which actor may perform which action on which resource)
- [ ] Data access boundaries per actor
- [ ] No blanket "all operations require authentication/authorization" statements restated per requirement

**Why it matters**: Exact per-actor permissions are testable and drive access-control design; blanket statements add noise without information.

---

## SHOULD HAVE Requirements

### PRD-MINIAPP-009: MiniApp-Specific Tags

**Priority**: MEDIUM

Requirements that don't trace to Platform SHOULD:

- [ ] Have `miniapp-specific` tag
- [ ] Include rationale for why it's MiniApp-level only
- [ ] Not duplicate Platform-level requirements

### PRD-MINIAPP-010: Acceptance Criteria Checklist

**Priority**: MEDIUM

The PRD SHOULD include summary acceptance criteria:

- [ ] All Platform FRs in scope are refined
- [ ] All MiniApp FRs have epic-level detailing
- [ ] All use cases have corresponding features
- [ ] Traceability matrix complete

### PRD-MINIAPP-011: ID Reference Appendix

**Priority**: LOW

The PRD SHOULD include ID pattern reference:

- [ ] ID patterns documented (PRD, FR, NFR, UseCase)
- [ ] Examples for each pattern
- [ ] Purpose of each ID type

---

## MUST NOT HAVE (Violations)

### PRD-MINIAPP-NO-001: No Technical Implementation

**Priority**: HIGH

The PRD MUST NOT contain:

- [ ] Architecture decisions (belongs in ADR)
- [ ] Module structures (belongs in DESIGN)
- [ ] Code examples (belongs in DESIGN/FEATURE)
- [ ] Data schema definitions (belongs in DESIGN-MINIAPP)

**Why it matters**: PRD defines WHAT, not HOW.

### PRD-MINIAPP-NO-005: No API Specifications

**Priority**: HIGH

The PRD MUST NOT contain:

- [ ] REST endpoints or HTTP methods
- [ ] HTTP/REST status code specifications (e.g., 200/201/400/401/403/404/409/500)
- [ ] API contract / OpenAPI / Swagger definitions
- [ ] Authentication header specifications (which header, auth scheme, required/optional)
- [ ] Standardized error response formats (status codes, error body schema/fields)

**Where it belongs**: DESIGN-MINIAPP (API contract specs); API design decisions belong in ADR.

**Why it matters**: API specifications in the PRD lock design decisions prematurely and drift from the actual contracts.

### PRD-MINIAPP-NO-002: No Platform Duplication

**Priority**: HIGH

The PRD MUST NOT:

- [ ] Redefine Platform-level requirements (only refine)
- [ ] Duplicate actor definitions (reference Platform actors)
- [ ] Repeat Platform constraints verbatim

**Why it matters**: Duplication creates inconsistency and maintenance burden.

### PRD-MINIAPP-NO-003: No Untraceable Requirements

**Priority**: CRITICAL

The PRD MUST NOT contain requirements without:

- [ ] Unique ID
- [ ] Clear traceability (to Platform or marked as MiniApp-specific)
- [ ] Priority assignment

**Why it matters**: Untraceable requirements cannot be validated or prioritized.

### PRD-MINIAPP-NO-004: No Vague Acceptance Criteria

**Priority**: HIGH

The PRD MUST NOT contain:

- [ ] Acceptance criteria without measurable outcomes
- [ ] Subjective terms ("fast", "good", "user-friendly") without metrics
- [ ] Incomplete criteria (missing success/failure conditions)

**Why it matters**: Vague criteria cannot be tested or verified.

---

## Mobile-Specific Criteria

### MOBILE-PRD-001: Offline Requirements

**Priority**: HIGH

MiniApp PRD MUST address offline behavior:

- [ ] Core offline capabilities defined
- [ ] Data sync requirements specified
- [ ] Offline limitations documented

### MOBILE-PRD-002: Cross-Platform Parity

**Priority**: HIGH

MiniApp PRD MUST specify platform parity:

- [ ] iOS-specific requirements (if any)
- [ ] Android-specific requirements (if any)
- [ ] Shared requirements clearly marked
- [ ] Platform differences documented

### MOBILE-PRD-003: Deep Link Requirements

**Priority**: MEDIUM

MiniApp PRD SHOULD include:

- [ ] Deep link entry points
- [ ] Deep link parameters
- [ ] Deep link handling requirements

### MOBILE-PRD-004: Push Notification Requirements

**Priority**: MEDIUM

If MiniApp uses notifications:

- [ ] Notification types defined
- [ ] Notification triggers documented
- [ ] User preference requirements

---

## Reporting

### Report Format

For each issue found, report:

```markdown
## Issue: {CHECKLIST-ID}

**Severity**: CRITICAL | HIGH | MEDIUM | LOW

**Why Applicable**: {Why this requirement applies to this MiniApp}

**Issue**: {What is wrong}

**Evidence**: {Quote from document or "Not found"}

**Impact**: {Why this matters}

**Proposal**: {How to fix}
```

### Reporting Commitment

- [ ] I reported all issues I found
- [ ] I used the exact report format
- [ ] I included evidence for each issue
- [ ] I proposed concrete fixes
- [ ] I did not hide or omit known problems

# PRD-EPIC Checklist

**Artifact**: PRD-EPIC  
**Kit**: mobile-superapp  
**Level**: L2 (Epic)

This checklist provides semantic quality criteria for Epic-level Product Requirements Documents in mobile SuperApp projects.

---

## Table of Contents

1. [MUST HAVE Requirements](#must-have-requirements)
2. [SHOULD HAVE Requirements](#should-have-requirements)
3. [MUST NOT HAVE (Violations)](#must-not-have-violations)
4. [Mobile-Specific Criteria](#mobile-specific-criteria)
5. [Reporting](#reporting)

---

## MUST HAVE Requirements

### PRD-EPIC-001: Overview Completeness

**Priority**: CRITICAL

The Epic PRD MUST include:

- [ ] Clear purpose statement
- [ ] Epic type (Screen, Capability, Flow, Widget)
- [ ] Link to parent MiniApp PRD
- [ ] Link to parent Platform PRD
- [ ] Version and status metadata
- [ ] In-scope items list
- [ ] Out-of-scope exclusions

**Why it matters**: Epic scope must be clearly bounded to enable focused development.

### PRD-EPIC-002: Parent Traceability

**Priority**: CRITICAL

The PRD MUST include traces to MiniApp PRD:

- [ ] Table mapping Epic to MiniApp requirements
- [ ] Relation type (details) for each trace
- [ ] `cpt-{miniapp}-fr-{slug}` references
- [ ] Indirect Platform trace documented

**Why it matters**: Epic requirements must demonstrate they detail MiniApp-level FRs.

### PRD-EPIC-003: Actors and Entry Points

**Priority**: HIGH

The PRD MUST define:

- [ ] Primary actors table with Epic-specific role
- [ ] Entry points table (deep link, navigation, push notification)
- [ ] Source and trigger for each entry point

**Why it matters**: Entry points define how users access this Epic functionality.

### PRD-EPIC-004: Functional Requirements Structure

**Priority**: CRITICAL

Each Functional Requirement MUST include:

- [ ] Checkbox with priority marker: `- [ ] \`pN\` - **ID**: ...` (priority `p1`-`p9` by business impact)
- [ ] Unique ID following `cpt-{miniapp}-epic-{epic}-fr-{slug}` pattern
- [ ] Verifiable MUST statement (specific behavior)
- [ ] Traces To field (parent MiniApp FR or "Epic-specific" with `epic-specific` tag and rationale)
- [ ] Actors field referencing `cpt-superapp-actor-{slug}`
- [ ] UI element reference
- [ ] Acceptance criteria

**Why it matters**: Epic FRs are more detailed than MiniApp FRs and closer to implementation.

### PRD-EPIC-005: State Requirements

**Priority**: HIGH

The PRD MUST define screen states:

- [ ] State table with ID `cpt-{miniapp}-epic-{epic}-state`
- [ ] All states defined (Loading, Content, Empty, Error, Offline)
- [ ] Conditions for each state
- [ ] UI behavior for each state

**Why it matters**: State definitions ensure consistent UX across all scenarios.

### PRD-EPIC-006: Error Handling

**Priority**: HIGH

The PRD MUST include error handling:

- [ ] Error types table
- [ ] User message for each error
- [ ] Recovery action for each error

**Why it matters**: Error handling requirements prevent poor UX during failures.

### PRD-EPIC-007: UI/UX Requirements

**Priority**: HIGH

The PRD MUST include UI requirements:

- [ ] Screen layout wireframe/diagram
- [ ] Components table with IDs `cpt-{miniapp}-{epic}-widget-{slug}`
- [ ] Interactions table (trigger, result)

**Why it matters**: UI requirements bridge product to design.

### PRD-EPIC-008: Data Requirements

**Priority**: HIGH

The PRD MUST specify data needs at business level:

- [ ] Required data table (data, owning backend capability, freshness/offline expectation)
- [ ] No endpoints, HTTP methods, or payload specifications (API contracts belong in DESIGN-EPIC)

**Why it matters**: Data requirements enable backend coordination without locking API design prematurely.

### PRD-EPIC-009: Traceability Matrices

**Priority**: CRITICAL

The PRD MUST include:

- [ ] MiniApp FR → Epic FR coverage table
- [ ] Epic FR → Feature mapping table
- [ ] Full traceability chain diagram (Platform → MiniApp → Epic)

**Why it matters**: Complete traceability ensures coverage validation.

### PRD-EPIC-013: Authorization as Exact Permissions

**Priority**: CRITICAL

> **Note**: That every protected capability requires authentication and authorization is assumed and need not be restated per requirement. Instead, specify the **exact permissions**.

The PRD MUST specify:

- [ ] Exact permissions per actor and operation within this Epic (which actor may perform which action on which resource)
- [ ] Data access boundaries per actor
- [ ] No blanket "all operations require authentication/authorization" statements restated per requirement

**Why it matters**: Exact per-actor permissions are testable and drive access-control design; blanket statements add noise without information.

---

## SHOULD HAVE Requirements

### PRD-EPIC-010: Epic-Specific Tags

**Priority**: MEDIUM

Requirements that don't trace to MiniApp SHOULD:

- [ ] Have `epic-specific` tag
- [ ] Include rationale for Epic-level only
- [ ] Document why not in MiniApp PRD

### PRD-EPIC-011: Acceptance Criteria Summary

**Priority**: MEDIUM

The PRD SHOULD include summary:

- [ ] All MiniApp FRs in scope detailed
- [ ] All Epic FRs have feature specifications
- [ ] All states designed
- [ ] All error scenarios handled
- [ ] Traceability chain verified

### PRD-EPIC-012: ID Reference Appendix

**Priority**: LOW

The PRD SHOULD include ID patterns:

- [ ] Epic PRD ID pattern
- [ ] Epic FR ID pattern
- [ ] State ID pattern
- [ ] Widget ID pattern

---

## MUST NOT HAVE (Violations)

### PRD-EPIC-NO-001: No Technical Architecture

**Priority**: HIGH

The PRD MUST NOT contain:

- [ ] Component architecture (belongs in DESIGN-EPIC)
- [ ] State management implementation (belongs in DESIGN)
- [ ] Code structures (belongs in DESIGN/FEATURE)
- [ ] Platform-specific implementation details

**Why it matters**: PRD defines WHAT, not HOW.

### PRD-EPIC-NO-002: No MiniApp Duplication

**Priority**: HIGH

The PRD MUST NOT:

- [ ] Redefine MiniApp-level requirements (only detail)
- [ ] Duplicate MiniApp constraints verbatim
- [ ] Redefine actors (only add Epic context)

**Why it matters**: Duplication creates inconsistency.

### PRD-EPIC-NO-003: No Feature-Level Details

**Priority**: MEDIUM

The PRD MUST NOT contain:

- [ ] CDSL flow definitions (belongs in FEATURE)
- [ ] Step-by-step implementation (belongs in FEATURE)
- [ ] Definition of Done (belongs in FEATURE)

**Why it matters**: Epic PRD defines requirements, not implementation steps.

### PRD-EPIC-NO-004: No Missing IDs

**Priority**: CRITICAL

The PRD MUST NOT contain:

- [ ] Requirements without unique IDs
- [ ] States without IDs
- [ ] Components without IDs
- [ ] Widgets without IDs

**Why it matters**: IDs enable traceability and automation.

### PRD-EPIC-NO-005: No API Specifications

**Priority**: HIGH

The PRD MUST NOT contain:

- [ ] REST endpoints or HTTP methods
- [ ] HTTP/REST status code specifications (e.g., 200/201/400/401/403/404/409/500)
- [ ] API contract / OpenAPI / Swagger definitions
- [ ] Authentication header specifications (which header, auth scheme, required/optional)
- [ ] Standardized error response formats (status codes, error body schema/fields)

**Where it belongs**: DESIGN-EPIC (API contract specs); API design decisions belong in ADR.

**Why it matters**: API specifications in the PRD lock design decisions prematurely and drift from the actual contracts.

---

## Mobile-Specific Criteria

### MOBILE-EPIC-001: State Coverage

**Priority**: CRITICAL

Epic PRD MUST include all mobile states:

- [ ] Loading state defined
- [ ] Content state defined
- [ ] Empty state defined
- [ ] Error state defined
- [ ] Offline state defined

### MOBILE-EPIC-002: Interaction Patterns

**Priority**: HIGH

Epic PRD MUST specify mobile interactions:

- [ ] Pull-to-refresh behavior (if applicable)
- [ ] Tap interactions
- [ ] Long press interactions (if applicable)
- [ ] Swipe gestures (if applicable)

### MOBILE-EPIC-003: Deep Link Handling

**Priority**: HIGH

If Epic is deep-linkable:

- [ ] Deep link format specified (`constructor://{miniapp}/{epic}`)
- [ ] Parameters documented
- [ ] Entry point behavior defined

### MOBILE-EPIC-004: Platform-Specific UI

**Priority**: MEDIUM

If platforms differ:

- [ ] iOS-specific UI requirements
- [ ] Android-specific UI requirements
- [ ] Material Design vs Human Interface alignment

---

## Reporting

### Report Format

For each issue found, report:

```markdown
## Issue: {CHECKLIST-ID}

**Severity**: CRITICAL | HIGH | MEDIUM | LOW

**Why Applicable**: {Why this requirement applies to this Epic}

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

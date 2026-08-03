# PRD — {MiniApp Name} MiniApp

> **Level**: L1 (MiniApp)
> **Parent**: [Platform PRD](../../architecture/PRD.md) `cpt-superapp-prd`
> **Version**: 1.0
> **Status**: Draft

---

## 1. Overview

### 1.1 Purpose

This PRD defines requirements for the **{MiniApp Name}** MiniApp within the Constructor Mobile SuperApp.

{1-2 paragraphs: What is this MiniApp and what problem does it solve? What are the key capabilities?}

### 1.2 Scope

**In Scope:**
- {capability 1}
- {capability 2}

**Out of Scope:**
- {explicitly excluded capability}

### 1.3 Traces To Platform

| Platform Requirement | Relation | Description |
|---------------------|----------|-------------|
| `cpt-superapp-fr-{slug}` | refines | {How this MiniApp refines Platform FR} |
| `cpt-superapp-nfr-{slug}` | inherits | {Which Platform NFRs apply} |

---

## 2. Actors

> **Note**: Actors are defined at Platform level. Reference platform actor IDs and add only MiniApp-specific context — do not redefine actors.

| Actor ID | Role | MiniApp-Specific Context |
|----------|------|------------------------|
| `cpt-superapp-actor-student` | Primary | {How student uses this MiniApp} |
| `cpt-superapp-actor-instructor` | Secondary | {How instructor uses this MiniApp} |

**Permissions**: {Exact per-actor permissions — which actor may perform which action on which resource, e.g., "student: read own enrollments; instructor: read/update courses they teach". Do not restate the generic "all operations require authentication/authorization" — it is assumed.}

---

## 3. Functional Requirements

Functional requirements define WHAT the MiniApp must do. Each is a checkbox with a priority marker `p1`-`p9` (assigned by business impact).

### 3.1 Core Capabilities

#### {Feature Name}

- [ ] `p1` - **ID**: `cpt-{miniapp}-fr-{slug}`

The MiniApp **MUST** {do something specific and verifiable}.

**Traces To**: `cpt-superapp-fr-{parent-slug}` (refines)

**Actors**: `cpt-superapp-actor-{actor}`

**Rationale**: {Why this requirement exists — business value or parent requirement.}

**Acceptance**: {Measurable acceptance criteria}

**Verification Method** (optional): {Only if non-standard: analysis | inspection | demonstration}

---

#### {MiniApp-Specific Feature}

- [ ] `p2` - **ID**: `cpt-{miniapp}-fr-{slug}`

The MiniApp **MUST** {MiniApp-specific capability not derived from Platform}.

**Tags**: `miniapp-specific`

**Traces To**: — (MiniApp-specific requirement)

**Actors**: `cpt-superapp-actor-{actor}`

**Rationale**: {Why this is needed at MiniApp level only}

**Acceptance**: {Measurable acceptance criteria}

---

## 4. Non-Functional Requirements

> **NFR framing**: State NFRs as business-level quality expectations — user/business outcomes, SLAs, and measurable targets (e.g., "course list opens in <2s at p95 on a mid-tier device"). Do NOT specify technical implementation (caching strategy, technology stack, component tuning) — those belong in DESIGN/ADR.

#### {Quality Attribute}

- [ ] `p2` - **ID**: `cpt-{miniapp}-nfr-{slug}`

The MiniApp **MUST** {measurable business-level quality expectation}.

**Traces To**: `cpt-superapp-nfr-{parent-slug}` (extends)

**Category**: Performance | Security | Usability | Reliability

**Threshold**: {Quantitative target with units and conditions}

**Rationale**: {Why this MiniApp needs a stricter/different requirement}

---

## 5. Use Cases

#### {Use Case Name}

- [ ] `p2` - **ID**: `cpt-{miniapp}-usecase-{slug}`

**Traces To**: `cpt-{miniapp}-fr-{slug}`

**Actor**: `cpt-superapp-actor-{actor}`

**Preconditions**:
- {Required state before execution}

**Main Flow**:
1. {Actor action or system response}
2. {Next step}

**Postconditions**:
- {State after successful completion}

**Alternative Flows**:
- **{Condition}**: {What happens instead}

---

## 6. Dependencies

> **Note**: Name dependencies at capability level (which service provides what data or operation). API contracts, endpoints, and payloads belong in DESIGN-MINIAPP.

### 6.1 Platform Dependencies

| Dependency | Type | Description |
|------------|------|-------------|
| Auth Kernel | Required | `cpt-superapp-component-auth-kernel` |
| Storage Kernel | Required | `cpt-superapp-component-storage-kernel` |

### 6.2 External Dependencies

| System | Capability Provided | Criticality |
|--------|--------------------|-------------|
| {Backend Service} | {What data/operations it provides, business level} | {p1/p2/p3} |

---

## 7. Assumptions

- {Assumption about environment, users, or dependent systems}

---

## 8. Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| {Risk description} | {Potential impact} | {Mitigation strategy} |

---

## 9. Traceability Matrix

### 9.1 Platform FR → MiniApp FR Coverage

| Platform FR | MiniApp FRs | Coverage Status |
|-------------|-----------|-----------------|
| `cpt-superapp-fr-{slug-1}` | `cpt-{miniapp}-fr-{a}`, `cpt-{miniapp}-fr-{b}` | Full |
| `cpt-superapp-fr-{slug-2}` | `cpt-{miniapp}-fr-{c}` | Partial |
| `cpt-superapp-fr-{slug-3}` | — | Not in scope |

### 9.2 MiniApp FR → Epic Coverage

| MiniApp FR | Target Epics | Status |
|-----------|--------------|--------|
| `cpt-{miniapp}-fr-{slug}` | Home, Settings | Planned |

---

## 10. Acceptance Criteria

Business-level acceptance criteria for the PRD as a whole.

- [ ] All Platform FRs in scope are refined
- [ ] All MiniApp FRs have epic-level detailing
- [ ] All use cases have corresponding features
- [ ] Traceability matrix complete

---

## Appendix: ID Reference

| ID Pattern | Example | Purpose |
|------------|---------|---------|
| `cpt-{miniapp}-prd` | `cpt-student-prd` | MiniApp PRD anchor |
| `cpt-{miniapp}-fr-{slug}` | `cpt-student-fr-course-list` | Functional requirement |
| `cpt-{miniapp}-nfr-{slug}` | `cpt-student-nfr-offline` | Non-functional requirement |
| `cpt-{miniapp}-usecase-{slug}` | `cpt-student-usecase-browse` | Use case |

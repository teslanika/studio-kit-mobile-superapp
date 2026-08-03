# Artifact Types

The Mobile SuperApp Kit provides 13 artifact types organized across 4 hierarchy levels.

## Summary Table

| Level | Artifact | Purpose | ID Pattern |
|-------|----------|---------|------------|
| **L0: Platform** | `PRD-PLATFORM` | Platform-wide requirements | `cpt-superapp-fr-{slug}` |
| | `DESIGN-PLATFORM` | Platform architecture | `cpt-superapp-component-{slug}` |
| | `DECOMPOSITION-PLATFORM` | MiniApp breakdown | `cpt-superapp-miniapp-{slug}` |
| **L1: MiniApp** | `PRD-MINIAPP` | MiniApp requirements | `cpt-{hierarchy-prefix}-fr-{slug}` |
| | `DESIGN-MINIAPP` | MiniApp architecture | `cpt-{hierarchy-prefix}-component-{slug}` |
| | `DECOMPOSITION-MINIAPP` | Epic breakdown | `cpt-{hierarchy-prefix}-epic-{slug}` |
| **L2: Epic** | `PRD-EPIC` | Epic requirements | `cpt-{hierarchy-prefix}-fr-{slug}` |
| | `DESIGN-EPIC` | Epic architecture | `cpt-{hierarchy-prefix}-component-{slug}` |
| | `DECOMPOSITION-EPIC` | Feature breakdown | `cpt-{hierarchy-prefix}-feature-{slug}` |
| **L3: Feature** | `FEATURE-MOBILE` | MVI feature design | `cpt-{hierarchy-prefix}-flow-{feature}-{slug}` |
| | `IMPL-KMP` | Shared code reference map | `@cpt-algo:cpt-{hierarchy-prefix}-algo-{feature}-viewmodel:p1` |
| | `IMPL-ANDROID` | Android code reference map | `@cpt-algo:cpt-{hierarchy-prefix}-algo-{feature}-android:p1` |
| | `IMPL-IOS` | iOS code reference map | `@cpt-algo:cpt-{hierarchy-prefix}-algo-{feature}-ios:p1` |

## Artifact Structure

Each artifact type includes three files:

```
artifacts/{ARTIFACT-TYPE}/
├── template.md    # Document structure
├── rules.md       # Generation and validation rules
└── checklist.md   # Review criteria
```

---

## PRD Artifacts

### PRD-PLATFORM

Platform-wide product requirements document.

**Contains:**
- Actors (Student, Instructor, Admin)
- Functional Requirements (FR)
- Non-Functional Requirements (NFR)
- Use Cases
- Constraints

**Example IDs:**
- `cpt-superapp-actor-student`
- `cpt-superapp-fr-offline-support`
- `cpt-superapp-nfr-launch-time`

### PRD-MINIAPP

MiniApp-level requirements that refine platform requirements.

**Contains:**
- MiniApp-specific actors
- Domain requirements
- References to Platform FRs

**Example IDs:**
- `cpt-superapp-learn-fr-browse-courses`
- `cpt-superapp-learn-fr-offline-courses`

### PRD-EPIC

Epic-level user stories and acceptance criteria.

**Contains:**
- User stories
- Acceptance criteria
- References to MiniApp FRs

**Example IDs:**
- `cpt-superapp-learn-course-catalog-story-view-courses`
- `cpt-superapp-learn-course-catalog-ac-pagination`

---

## DESIGN Artifacts

### DESIGN-PLATFORM

Platform architecture defining shared infrastructure.

**Contains:**
- KMP module structure
- Shared components (Auth, Push, Navigation)
- Data architecture
- API contracts

**Example IDs:**
- `cpt-superapp-component-auth-service`
- `cpt-superapp-module-constructor-sdk`

### DESIGN-MINIAPP

MiniApp architecture within platform constraints.

**Contains:**
- ViewModels
- Repositories
- Navigation graph
- Data models

**Example IDs:**
- `cpt-superapp-learn-component-course-repository`
- `cpt-superapp-learn-viewmodel-course-list`

### DESIGN-EPIC

Epic-level component design.

**Contains:**
- Screen components
- Sequences
- State machines

**Example IDs:**
- `cpt-superapp-learn-course-catalog-component-list-screen`
- `cpt-superapp-learn-course-catalog-seq-load-courses`

---

## DECOMPOSITION Artifacts

### DECOMPOSITION-PLATFORM

Breaks platform into MiniApps.

**Contains:**
- MiniApp list with descriptions
- Dependencies between MiniApps
- Priority/order

### DECOMPOSITION-MINIAPP

Breaks MiniApp into Epics.

**Contains:**
- Epic list with descriptions
- Dependencies between Epics
- Implementation order

### DECOMPOSITION-EPIC

Breaks Epic into Features.

**Contains:**
- Feature list with descriptions
- Dependencies between Features
- Implementation order

---

## FEATURE-MOBILE

The core artifact for implementing mobile features.

**Contains:**
- MVI definitions (State, Intent, Effect)
- CDSL flows with instructions
- Algorithms
- State machines
- Platform-specific implementation sections (KMP, Android, iOS)
- Acceptance criteria per platform
- Definition of Done

See [MVI Pattern](MVI-Pattern) for details.

---

## IMPL Artifacts

Implementation tracking documents for each platform.

### IMPL-KMP

Tracks KMP shared code implementation.

### IMPL-ANDROID

Tracks Android/Compose implementation.

### IMPL-IOS

Tracks iOS/SwiftUI implementation.

See [Code Markers](Code-Markers) for traceability.

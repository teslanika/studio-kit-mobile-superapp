# ID Naming Conventions

All IDs in the Mobile SuperApp Kit follow a consistent pattern for traceability.

## General Pattern

```
cpt-{scope}-{kind}-{slug}
```

Where:
- `cpt` — Constructor Studio prefix (required)
- `{scope}` — Hierarchy context (platform, miniapp, epic)
- `{kind}` — Element type (fr, component, flow, etc.)
- `{slug}` — Kebab-case identifier

## By Level

### L0: Platform

| Kind | Pattern | Example |
|------|---------|---------|
| Actor | `cpt-superapp-actor-{slug}` | `cpt-superapp-actor-student` |
| FR | `cpt-superapp-fr-{slug}` | `cpt-superapp-fr-offline-support` |
| NFR | `cpt-superapp-nfr-{slug}` | `cpt-superapp-nfr-launch-time` |
| Component | `cpt-superapp-component-{slug}` | `cpt-superapp-component-auth` |
| Module | `cpt-superapp-module-{slug}` | `cpt-superapp-module-sdk` |
| MiniApp | `cpt-superapp-miniapp-{slug}` | `cpt-superapp-miniapp-learn` |

### L1: MiniApp

| Kind | Pattern | Example |
|------|---------|---------|
| FR | `cpt-{hierarchy-prefix}-fr-{slug}` | `cpt-superapp-learn-fr-browse-courses` |
| Component | `cpt-{hierarchy-prefix}-component-{slug}` | `cpt-superapp-learn-component-repository` |
| Epic | `cpt-{hierarchy-prefix}-epic-{slug}` | `cpt-superapp-learn-epic-course-catalog` |

### L2: Epic

| Kind | Pattern | Example |
|------|---------|---------|
| Story | `cpt-{hierarchy-prefix}-story-{slug}` | `cpt-superapp-learn-course-catalog-story-view` |
| AC | `cpt-{hierarchy-prefix}-ac-{slug}` | `cpt-superapp-learn-course-catalog-ac-pagination` |
| Component | `cpt-{hierarchy-prefix}-component-{slug}` | `cpt-superapp-learn-course-catalog-component-list` |
| Feature | `cpt-{hierarchy-prefix}-feature-{slug}` | `cpt-superapp-learn-course-catalog-feature-search` |

### L3: Feature

| Kind | Pattern | Example |
|------|---------|---------|
| Flow | `cpt-{hierarchy-prefix}-flow-{feature}-{slug}` | `cpt-superapp-learn-flow-course-list-load` |
| Algo | `cpt-{hierarchy-prefix}-algo-{feature}-{slug}` | `cpt-superapp-learn-algo-course-list-cache` |
| State | `cpt-{hierarchy-prefix}-state-{feature}-{slug}` | `cpt-superapp-learn-state-course-list-screen` |
| DoD | `cpt-{hierarchy-prefix}-dod-{feature}-{slug}` | `cpt-superapp-learn-dod-course-list-tests` |

### Code Markers

Code markers reference the **design ID**, not a separate per-platform ID. The
target is distinguished by the design element the marker points at.

| Mode | Pattern | Example |
|------|---------|---------|
| FULL, scope | `@cpt-{kind}:{cpt-id}:p{N}` | `@cpt-algo:cpt-superapp-learn-algo-course-list-viewmodel:p1` |
| FULL, block | `@cpt-begin:{cpt-id}:p{N}:inst-{local}` … `@cpt-end:…` | `@cpt-begin:cpt-superapp-learn-algo-course-list-viewmodel:p1:inst-vm-1` |
| DOCS-ONLY | `@cpt-impl {cpt-id}` | `@cpt-impl cpt-superapp-learn-algo-course-list-viewmodel` |

## Rules

### Slug Rules

- Lowercase letters, numbers, hyphens only
- No spaces, underscores, or special characters
- No leading/trailing hyphens
- Use meaningful names (not abbreviations)

**Good:**
- `course-list`
- `offline-support`
- `auth-service`

**Bad:**
- `CourseList` (uppercase)
- `course_list` (underscore)
- `cl` (too short)
- `-course-list-` (leading/trailing hyphen)

### Uniqueness

IDs must be unique within their scope:
- Platform IDs: unique across platform
- MiniApp IDs: unique within MiniApp
- Epic IDs: unique within Epic
- Feature IDs: unique within Feature

### Traceability References

When referencing parent IDs, use the full ID:

```markdown
## Traceability

### Platform References
- Implements: `cpt-superapp-fr-offline-support`

### MiniApp References  
- Refines: `cpt-superapp-learn-fr-offline-courses`
```

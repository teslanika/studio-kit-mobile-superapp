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
| Actor | `cpt-platform-actor-{slug}` | `cpt-platform-actor-student` |
| FR | `cpt-platform-fr-{slug}` | `cpt-platform-fr-offline-support` |
| NFR | `cpt-platform-nfr-{slug}` | `cpt-platform-nfr-launch-time` |
| Component | `cpt-platform-component-{slug}` | `cpt-platform-component-auth` |
| Module | `cpt-platform-module-{slug}` | `cpt-platform-module-sdk` |
| MiniApp | `cpt-platform-miniapp-{slug}` | `cpt-platform-miniapp-learn` |

### L1: MiniApp

| Kind | Pattern | Example |
|------|---------|---------|
| FR | `cpt-{miniapp}-fr-{slug}` | `cpt-learn-fr-browse-courses` |
| Component | `cpt-{miniapp}-component-{slug}` | `cpt-learn-component-repository` |
| Epic | `cpt-{miniapp}-epic-{slug}` | `cpt-learn-epic-course-catalog` |

### L2: Epic

| Kind | Pattern | Example |
|------|---------|---------|
| Story | `cpt-{miniapp}-{epic}-story-{slug}` | `cpt-learn-course-catalog-story-view` |
| AC | `cpt-{miniapp}-{epic}-ac-{slug}` | `cpt-learn-course-catalog-ac-pagination` |
| Component | `cpt-{miniapp}-{epic}-component-{slug}` | `cpt-learn-course-catalog-component-list` |
| Feature | `cpt-{miniapp}-{epic}-feature-{slug}` | `cpt-learn-course-catalog-feature-search` |

### L3: Feature

| Kind | Pattern | Example |
|------|---------|---------|
| Flow | `cpt-{miniapp}-flow-{feature}-{slug}` | `cpt-learn-flow-course-list-load` |
| Algo | `cpt-{miniapp}-algo-{feature}-{slug}` | `cpt-learn-algo-course-list-cache` |
| State | `cpt-{miniapp}-state-{feature}-{slug}` | `cpt-learn-state-course-list-screen` |
| DoD | `cpt-{miniapp}-dod-{feature}-{slug}` | `cpt-learn-dod-course-list-tests` |

### Code Markers

| Platform | Pattern | Example |
|----------|---------|---------|
| KMP | `cpt-kmp-{module}-{type}-{slug}` | `cpt-kmp-learn-viewmodel-courselist` |
| Android | `cpt-android-{module}-{type}-{slug}` | `cpt-android-learn-screen-courselist` |
| iOS | `cpt-ios-{module}-{type}-{slug}` | `cpt-ios-learn-view-courselist` |

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
- Implements: `cpt-platform-fr-offline-support`

### MiniApp References  
- Refines: `cpt-learn-fr-offline-courses`
```

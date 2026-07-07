# Greenfield Guide — Mobile SuperApp

Use this guide when starting a new mobile app from scratch.

All prompts work through the Constructor Studio skill — enable it with `cfs on` and use natural language prompts.

## Goal

Create a validated 4-level architecture baseline before writing mobile code.

## What You Will Produce

Constructor Studio artifacts registered in `{cf-studio-path}/config/artifacts.toml`:

| Level | Artifacts | Default Location |
|-------|-----------|------------------|
| L0: Platform | PRD-PLATFORM, DESIGN-PLATFORM, DECOMPOSITION-PLATFORM | `architecture/platform/` |
| L1: MiniApp | PRD-MINIAPP, DESIGN-MINIAPP, DECOMPOSITION-MINIAPP | `architecture/miniapps/{slug}/` |
| L2: Epic | PRD-EPIC, DESIGN-EPIC, DECOMPOSITION-EPIC | `architecture/miniapps/{miniapp}/epics/{slug}/` |
| L3: Feature | FEATURE-MOBILE | `architecture/miniapps/{miniapp}/epics/{epic}/features/{slug}.md` |

---

## Workflow Sequence

### Phase 1: Platform Level (L0)

#### 1.1 PRD-PLATFORM

**Create**

| Prompt | What happens |
|--------|--------------|
| `cfs make PRD-PLATFORM` | Creates platform PRD interactively |
| `cfs make PRD-PLATFORM for Constructor SuperApp` | Creates PRD with context |
| `cfs draft PRD-PLATFORM from README` | Extracts from existing docs |

**Provide context:**
```
cfs make PRD-PLATFORM for Constructor SuperApp
Context:
- Product: Educational mobile platform
- Users: students, instructors, admins
- MiniApps: Learn, Assess, Communicate
- Platforms: iOS (SwiftUI), Android (Compose), shared KMP
- Key NFRs: offline-first, <3s launch, 60fps animations
```

**Validate**

| Prompt | What happens |
|--------|--------------|
| `cfs validate PRD-PLATFORM` | Full validation |
| `cfs validate PRD-PLATFORM semantic` | Semantic only |
| `cfs validate PRD-PLATFORM structural` | Structural only |

#### 1.2 DESIGN-PLATFORM

**Create**

| Prompt | What happens |
|--------|--------------|
| `cfs make DESIGN-PLATFORM` | Creates platform architecture |
| `cfs make DESIGN-PLATFORM from PRD-PLATFORM` | Transforms PRD into architecture |

**Provide context:**
```
cfs make DESIGN-PLATFORM
Context:
- Architecture: KMP shared + native UI
- Shared modules: constructor-sdk (domain, data, presentation)
- Native apps: android-app (Compose), ios-app (SwiftUI)
- DI: Koin (KMP), Hilt (Android)
- Navigation: Decompose (KMP) + platform coordinators
- Offline: Room (Android), Core Data (iOS), shared cache strategy
```

**Validate**

| Prompt | What happens |
|--------|--------------|
| `cfs validate DESIGN-PLATFORM` | Full validation |
| `cfs validate DESIGN-PLATFORM refs` | Cross-references to PRD |

#### 1.3 DECOMPOSITION-PLATFORM

**Create**

| Prompt | What happens |
|--------|--------------|
| `cfs make DECOMPOSITION-PLATFORM` | Creates MiniApp breakdown |
| `cfs decompose platform into miniapps` | Alternative phrasing |

**Provide context:**
```
cfs make DECOMPOSITION-PLATFORM
Context:
- MiniApps:
  - learn (course catalog, progress, certificates)
  - assess (exams, proctoring, results)
  - communicate (chat, notifications, announcements)
- Shared: auth, settings, profile
```

**Validate**

| Prompt | What happens |
|--------|--------------|
| `cfs validate DECOMPOSITION-PLATFORM` | Full validation |
| `cfs validate DECOMPOSITION-PLATFORM refs` | Cross-references |

---

### Phase 2: MiniApp Level (L1)

For each MiniApp from DECOMPOSITION-PLATFORM:

#### 2.1 PRD-MINIAPP

**Create**

| Prompt | What happens |
|--------|--------------|
| `cfs make PRD-MINIAPP for learn` | Creates Learn MiniApp PRD |
| `cfs make PRD-MINIAPP for assess` | Creates Assess MiniApp PRD |

**Provide context:**
```
cfs make PRD-MINIAPP for learn
Context:
- MiniApp: Learn
- Parent: cpt-platform (references platform FRs)
- Capabilities: course browsing, enrollment, progress tracking, certificates
- Actors: student, instructor
- Offline requirements: course content, progress sync
```

**Validate**

| Prompt | What happens |
|--------|--------------|
| `cfs validate PRD-MINIAPP for learn` | Full validation |
| `cfs validate PRD-MINIAPP for learn refs` | References to platform |

#### 2.2 DESIGN-MINIAPP

**Create**

| Prompt | What happens |
|--------|--------------|
| `cfs make DESIGN-MINIAPP for learn` | Creates MiniApp architecture |
| `cfs make DESIGN-MINIAPP for learn from PRD-MINIAPP` | From MiniApp PRD |

**Provide context:**
```
cfs make DESIGN-MINIAPP for learn
Context:
- MiniApp: Learn
- KMP modules: learn-domain, learn-data, learn-presentation
- Features: course-catalog, course-player, progress-tracker
- Data: CourseRepository, ProgressRepository
- Navigation: LearnNavGraph, LearnCoordinator
```

**Validate**

| Prompt | What happens |
|--------|--------------|
| `cfs validate DESIGN-MINIAPP for learn` | Full validation |
| `cfs validate DESIGN-MINIAPP for learn refs` | References |

#### 2.3 DECOMPOSITION-MINIAPP

**Create**

| Prompt | What happens |
|--------|--------------|
| `cfs make DECOMPOSITION-MINIAPP for learn` | Creates Epic breakdown |
| `cfs decompose miniapp learn into epics` | Alternative phrasing |

**Provide context:**
```
cfs make DECOMPOSITION-MINIAPP for learn
Context:
- Epics:
  - course-catalog (browse, search, filter, enroll)
  - course-player (video, content, quizzes)
  - progress-tracker (completion, achievements, certificates)
```

---

### Phase 3: Epic Level (L2)

For each Epic from DECOMPOSITION-MINIAPP:

#### 3.1 PRD-EPIC

| Prompt | What happens |
|--------|--------------|
| `cfs make PRD-EPIC for course-catalog` | Creates Epic requirements |
| `cfs validate PRD-EPIC for course-catalog` | Validates Epic PRD |

**Provide context:**
```
cfs make PRD-EPIC for course-catalog
Context:
- Epic: Course Catalog
- MiniApp: Learn
- User stories: browse courses, search, filter by category, view details, enroll
- Acceptance criteria per story
```

#### 3.2 DESIGN-EPIC

| Prompt | What happens |
|--------|--------------|
| `cfs make DESIGN-EPIC for course-catalog` | Creates Epic architecture |
| `cfs validate DESIGN-EPIC for course-catalog` | Validates Epic design |

**Provide context:**
```
cfs make DESIGN-EPIC for course-catalog
Context:
- Components: CourseListViewModel, CourseDetailViewModel, CourseRepository
- Data flow: API → Repository → ViewModel → UI
- States: Loading, Content, Empty, Error
- Navigation: CourseList → CourseDetail → Enrollment
```

#### 3.3 DECOMPOSITION-EPIC

| Prompt | What happens |
|--------|--------------|
| `cfs make DECOMPOSITION-EPIC for course-catalog` | Creates Feature breakdown |
| `cfs decompose epic course-catalog into features` | Alternative phrasing |

**Provide context:**
```
cfs make DECOMPOSITION-EPIC for course-catalog
Context:
- Features:
  - course-list (browse, pagination, pull-to-refresh)
  - course-search (search, filters, suggestions)
  - course-detail (info, syllabus, reviews, enrollment)
```

---

### Phase 4: Feature Level (L3)

For each Feature from DECOMPOSITION-EPIC:

#### 4.1 FEATURE-MOBILE

| Prompt | What happens |
|--------|--------------|
| `cfs make FEATURE-MOBILE for course-list` | Creates feature design |
| `cfs validate FEATURE-MOBILE for course-list` | Validates feature |

**Provide context:**
```
cfs make FEATURE-MOBILE for course-list
Context:
- Feature: Course List
- Epic: Course Catalog
- Actor flows: browse courses, pull to refresh, load more
- States: Loading, Content(courses), Empty, Error(message)
- Intents: Load, Refresh, LoadMore, SelectCourse
- Effects: NavigateToCourse, ShowError
- Edge cases: empty list, network error, pagination end
```

#### 4.2 CODE Implementation

**Implement all platforms**

| Prompt | What happens |
|--------|--------------|
| `cfs implement course-list` | Generates KMP + Android + iOS |
| `cfs implement course-list step by step` | With confirmation |
| `cfs implement course-list tests first` | TDD approach |

**Implement specific platform**

| Prompt | What happens |
|--------|--------------|
| `cfs implement course-list kmp` | KMP ViewModel, UseCase, Repository |
| `cfs implement course-list android` | Compose UI |
| `cfs implement course-list ios` | SwiftUI + KMP wrapper |

**Validate code**

| Prompt | What happens |
|--------|--------------|
| `cfs validate code for course-list` | Validates markers and coverage |
| `cfs validate code coverage for course-list` | Coverage report |
| `cfs validate code orphans` | Finds orphaned markers |

---

## Iteration Rules

1. **Design flows down**: Platform → MiniApp → Epic → Feature
2. **Changes propagate up**: If feature needs platform change, update platform first
3. **Validate before implementing**: Always validate artifact before using it
4. **Code matches design**: If code contradicts design, fix design at appropriate level

---

## Quick Reference

### Full Pipeline

| Step | Generate | Validate |
|------|----------|----------|
| 1 | `cfs make PRD-PLATFORM` | `cfs validate PRD-PLATFORM` |
| 2 | `cfs make DESIGN-PLATFORM` | `cfs validate DESIGN-PLATFORM` |
| 3 | `cfs make DECOMPOSITION-PLATFORM` | `cfs validate DECOMPOSITION-PLATFORM` |
| 4 | `cfs make PRD-MINIAPP for {miniapp}` | `cfs validate PRD-MINIAPP for {miniapp}` |
| 5 | `cfs make DESIGN-MINIAPP for {miniapp}` | `cfs validate DESIGN-MINIAPP for {miniapp}` |
| 6 | `cfs make DECOMPOSITION-MINIAPP for {miniapp}` | `cfs validate DECOMPOSITION-MINIAPP for {miniapp}` |
| 7 | `cfs make PRD-EPIC for {epic}` | `cfs validate PRD-EPIC for {epic}` |
| 8 | `cfs make DESIGN-EPIC for {epic}` | `cfs validate DESIGN-EPIC for {epic}` |
| 9 | `cfs make DECOMPOSITION-EPIC for {epic}` | `cfs validate DECOMPOSITION-EPIC for {epic}` |
| 10 | `cfs make FEATURE-MOBILE for {feature}` | `cfs validate FEATURE-MOBILE for {feature}` |
| 11 | `cfs implement {feature}` | `cfs validate code for {feature}` |

### Validation Modes

Append to any `validate` command:
- `semantic` — content quality, completeness, mobile patterns
- `structural` — format, IDs, template compliance
- `refs` — cross-references across levels
- `quick` — critical issues only (fast)

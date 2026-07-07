# Brownfield Guide — Mobile SuperApp

Use this guide when you already have a mobile codebase and want to adopt Constructor Studio.

All prompts work through the Constructor Studio skill — enable it with `cfs on` and use natural language prompts.

## Goal

Adopt Constructor Studio incrementally — start with what makes sense for your mobile project, not a fixed sequence.

## Key Principle: Start Anywhere

Unlike greenfield projects, **brownfield has no required order**. You can:

- Start with **any level** — Platform, MiniApp, Epic, or Feature
- Work **top-down** (Platform → Feature → CODE) or **bottom-up** (CODE → Feature → Platform)
- Adopt **incrementally** — use only what you need, add more later
- Use **code-only mode** — just Constructor Studio's code generation with MVI pattern guidance

**Even with zero artifacts**, Constructor Studio's mobile code generation uses the `codebase-checklist` internally for quality guidance.

---

## Adoption Scenarios

### Scenario A: Code-Only

You just want better mobile code generation. No artifacts needed.

| Prompt | What happens |
|--------|--------------|
| `cfs implement feature auth` | Generates KMP/Android/iOS code with MVI |
| `cfs add markers to shared/src/` | Adds traceability markers to existing KMP |
| `cfs add markers to android-app/` | Adds markers to Android code |
| `cfs validate code` | Validates code quality and markers |

**Benefits**: MVI pattern guidance, consistent architecture, code traceability.

### Scenario B: Feature-First (Bottom-Up)

You want to document existing mobile features, then build up.

```
1. cfs reverse FEATURE-MOBILE from shared/feature/auth/
   → Creates FEATURE-MOBILE from existing KMP code

2. cfs reverse FEATURE-MOBILE from shared/feature/courses/
   → Creates another FEATURE from code

3. cfs make DECOMPOSITION-EPIC from features
   → Creates DECOMPOSITION-EPIC from FEATUREs

4. cfs make DESIGN-EPIC from DECOMPOSITION-EPIC
   → Creates DESIGN-EPIC from structure

5. (optional) Continue up to MiniApp and Platform levels
```

**When to use**: You want to document what exists without changing code.

### Scenario C: MiniApp-First (Middle-Out)

You want to capture MiniApp architecture, then decompose into features.

```
1. cfs reverse DESIGN-MINIAPP for learn from codebase
   → Extracts Learn MiniApp architecture from code

2. cfs make DECOMPOSITION-MINIAPP for learn
   → Creates Epic breakdown

3. cfs make FEATURE-MOBILE for {slug}
   → Creates detailed features

4. cfs implement {slug}
   → Implements with traceability markers
```

**When to use**: You want architectural control over a specific MiniApp.

### Scenario D: Full Top-Down

You want complete 4-level documentation from platform to code.

```
1. cfs reverse PRD-PLATFORM from codebase
   → Extracts platform requirements

2. cfs reverse DESIGN-PLATFORM from codebase
   → Documents current architecture

3. Continue through all levels...

4. cfs implement {feature}
   → Implements with full traceability
```

**When to use**: New team members, compliance requirements, or major refactoring.

### Scenario E: Gradual Adoption

Start minimal, add artifacts as needed.

```
Week 1: cfs implement {feature}        → Code-only, with MVI checklist
Week 2: cfs make FEATURE-MOBILE        → Add features for complex work
Week 3: cfs make DECOMPOSITION-EPIC    → Organize features into epics
Later:  cfs make DESIGN-MINIAPP         → Document MiniApp architecture
```

**When to use**: You want low-friction adoption with growing benefits.

---

## Reverse Engineering Prompts

### From Existing KMP Code

| Prompt | What happens |
|--------|--------------|
| `cfs reverse FEATURE-MOBILE from shared/feature/auth/` | Creates FEATURE from KMP module |
| `cfs reverse DESIGN-MINIAPP from shared/feature/learn/` | Creates MiniApp design from module |
| `cfs reverse DESIGN-PLATFORM from shared/` | Documents platform architecture |

### From Existing Android Code

| Prompt | What happens |
|--------|--------------|
| `cfs reverse FEATURE-MOBILE from android-app/feature/auth/` | Creates FEATURE from Android module |
| `cfs analyze android-app/feature/auth/` | Systematic code analysis |

### From Existing iOS Code

| Prompt | What happens |
|--------|--------------|
| `cfs reverse FEATURE-MOBILE from ios-app/Features/Auth/` | Creates FEATURE from iOS module |
| `cfs analyze ios-app/Features/Auth/` | Systematic code analysis |

### From Existing Docs

| Prompt | What happens |
|--------|--------------|
| `cfs make PRD-PLATFORM from README` | Creates PRD from README |
| `cfs make DESIGN-MINIAPP from docs/architecture.md` | Creates design from existing docs |
| `cfs import OpenAPI as DESIGN-MINIAPP` | Converts API spec into design |

---

## Adding Features to Existing Code

### 1. Add to Appropriate Level

| Prompt | What happens |
|--------|--------------|
| `cfs add miniapp notifications to platform` | Adds MiniApp to platform decomposition |
| `cfs add epic push-notifications to miniapp notifications` | Adds Epic to MiniApp |
| `cfs add feature notification-list to epic push-notifications` | Adds Feature to Epic |

### 2. Create FEATURE-MOBILE

| Prompt | What happens |
|--------|--------------|
| `cfs make FEATURE-MOBILE for notification-list` | Creates feature design |
| `cfs reverse FEATURE-MOBILE from shared/feature/notifications/` | From existing code |

**Provide context:**
```
cfs make FEATURE-MOBILE for notification-list
Context:
- Feature: Notification List
- Epic: Push Notifications
- MiniApp: Notifications
- Existing code: shared/feature/notifications/
- States: Loading, Content(notifications), Empty
- Intents: Load, MarkRead, Delete
```

### 3. Validate and Implement

| Prompt | What happens |
|--------|--------------|
| `cfs validate FEATURE-MOBILE for notification-list` | Validates feature |
| `cfs implement notification-list` | Generates code |
| `cfs implement notification-list remaining` | Only unimplemented parts |

---

## Sync and Compare

When code and design drift apart:

| Prompt | What happens |
|--------|--------------|
| `cfs compare DESIGN-MINIAPP for learn to code` | Shows drift |
| `cfs compare FEATURE-MOBILE for course-list to code` | Shows feature drift |
| `cfs sync DESIGN-MINIAPP for learn from code` | Updates design from code |
| `cfs sync FEATURE-MOBILE for course-list from code` | Updates feature from code |
| `cfs sync code with FEATURE-MOBILE for course-list` | Updates code from feature |

---

## Adding Markers to Existing Code

### KMP Shared Code

```kotlin
// Before: no markers
class CourseListViewModel(
    private val loadCoursesUseCase: LoadCoursesUseCase
) : ViewModel() {
    fun loadCourses() { ... }
}

// After: with markers
// @cpt-impl cpt-learn-course-list-viewmodel-kmp
class CourseListViewModel(
    private val loadCoursesUseCase: LoadCoursesUseCase
) : ViewModel() {
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-1
    fun loadCourses() { ... }
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-1
}
```

### Android Compose

```kotlin
// @cpt-impl cpt-learn-course-list-screen-android
@Composable
fun CourseListScreen(
    viewModel: CourseListViewModel = hiltViewModel()
) {
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-android-1
    val state by viewModel.state.collectAsStateWithLifecycle()
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-android-1
}
```

### iOS SwiftUI

```swift
// @cpt-impl cpt-learn-course-list-view-ios
struct CourseListView: View {
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-ios-1
    @StateObject private var viewModel = CourseListViewModelWrapper()
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-ios-1
}
```

### Prompts for Adding Markers

| Prompt | What happens |
|--------|--------------|
| `cfs add markers to shared/feature/courses/` | Adds markers to KMP module |
| `cfs add markers for course-list` | Adds markers matching FEATURE |
| `cfs fix markers in android-app/feature/` | Fixes incorrect markers |

---

## Common Scenarios

### Requirements Changed at Platform Level

```
cfs update PRD-PLATFORM
cfs validate PRD-PLATFORM
cfs propagate PRD-PLATFORM changes to DESIGN-PLATFORM
cfs validate DESIGN-PLATFORM
# Continue down through affected MiniApps/Epics/Features
```

### MiniApp Design Changed

```
cfs update DESIGN-MINIAPP for learn
cfs validate DESIGN-MINIAPP for learn
cfs propagate DESIGN-MINIAPP changes to affected epics
# Continue down through affected Epics/Features
```

### Feature Design Changed

```
cfs update FEATURE-MOBILE for course-list
cfs validate FEATURE-MOBILE for course-list
cfs sync code with FEATURE-MOBILE for course-list
cfs validate code for course-list
```

### Code Changed Without Design Update

```
cfs compare FEATURE-MOBILE for course-list to code
cfs sync FEATURE-MOBILE for course-list from code
cfs validate FEATURE-MOBILE for course-list
```

---

## Quick Reference

### By Adoption Level

| Level | What you do | Benefits |
|-------|-------------|----------|
| **Code-only** | `cfs implement {slug}` | MVI checklist, consistent patterns |
| **+ FEATURE** | Add `cfs make FEATURE-MOBILE` | Flows, states, edge cases documented |
| **+ DECOMPOSITION** | Add `cfs make DECOMPOSITION-EPIC` | Feature organization, dependencies |
| **+ DESIGN** | Add `cfs make DESIGN-{LEVEL}` | Architecture, components, data model |
| **+ PRD** | Add `cfs make PRD-{LEVEL}` | Requirements, full 4-level traceability |

### Top-Down (Full)

| Step | Generate | Validate |
|------|----------|----------|
| 1 | `cfs reverse PRD-PLATFORM` | `cfs validate PRD-PLATFORM` |
| 2 | `cfs reverse DESIGN-PLATFORM` | `cfs validate DESIGN-PLATFORM` |
| 3 | `cfs make DECOMPOSITION-PLATFORM` | `cfs validate DECOMPOSITION-PLATFORM` |
| ... | Continue through all levels | ... |
| N | `cfs implement {feature}` | `cfs validate code for {feature}` |

### Bottom-Up (Feature-First)

| Step | Generate | Validate |
|------|----------|----------|
| 1 | `cfs reverse FEATURE-MOBILE from {path}` | `cfs validate FEATURE-MOBILE` |
| 2 | `cfs make DECOMPOSITION-EPIC from features` | `cfs validate DECOMPOSITION-EPIC` |
| 3 | `cfs make DESIGN-EPIC` | `cfs validate DESIGN-EPIC` |
| ... | Continue up as needed | ... |

### Code-Only

| Prompt | What happens |
|--------|--------------|
| `cfs implement {slug}` | Generates code with MVI guidance |
| `cfs add markers to {path}` | Adds traceability to existing code |
| `cfs validate code` | Validates code quality |

**Validation modes** (append to any `validate` command):
- `semantic` — content quality, completeness, mobile patterns
- `structural` — format, IDs, template compliance
- `refs` — cross-references across levels
- `quick` — critical issues only (fast)

## Iteration Rules

- Start with what you need — add more artifacts as value becomes clear
- If code changes affect feature behavior, update FEATURE-MOBILE first
- Re-validate the FEATURE design
- Run `cfs validate code` to ensure design and code remain consistent
- If code contradicts design, decide: update design OR update code

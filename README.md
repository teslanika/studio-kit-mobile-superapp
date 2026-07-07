# Mobile SuperApp Kit

> A [Cyber Pilot](https://github.com/cyberfabric/cyber-pilot) kit for mobile SuperApp development with multi-level documentation hierarchy and cascading requirement traceability.

## Installation

```bash
# Install (--version is optional, defaults to latest)
cfs kit install teslanika/studio-kit-mobile-superapp

# Update
cfs kit update mobile-superapp

# Validate
cfs validate-kits .
```

## Overview

**Mobile SuperApp Kit** provides a 4-level documentation hierarchy designed specifically for large-scale mobile applications that combine multiple "mini-apps" (MiniApps) into a single host application.

### Key Features

- **4-Level Documentation Hierarchy**: Platform → MiniApp → Epic → Feature
- **Cascading Requirement Traceability**: Every requirement traces from high-level platform goals down to code
- **Mobile-Specific Templates**: KMP, Android (Compose), iOS (SwiftUI) implementation patterns
- **MVI State Management**: Consistent state management across all MiniApps

### Documentation Hierarchy

```
L0: Platform PRD (architecture/PRD.md)
    └── Shared kernel: Auth, Push, Deep Links, MiniApp Container, NFRs

L1: MiniApp PRD (miniapps/{miniapp}/PRD.md)
    └── Domain requirements: Student, Proctor, Groups

L2: Epic PRD (miniapps/{miniapp}/capabilities/{epic}/PRD.md)
    └── Screen-level: Notification History, Course Catalog, etc.

L3: Feature (miniapps/{miniapp}/capabilities/{epic}/features/{feature}/FEATURE.md)
    └── CDSL specifications with platform-specific implementation
```

### Traceability Chain

```
Platform FR: cpt-superapp-fr-inapp-notifications
    │ refined-by
    ▼
MiniApp FR: cpt-student-fr-notifications
    │ detailed-by
    ▼
Epic FR: cpt-student-epic-notification-history-fr-badge
    │ specified-by
    ▼
Feature: cpt-student-feature-notification-badge
    │ implemented-by
    ▼
Code: @cpt-impl:cpt-student-feature-notification-badge
```

## What the Kit Provides

| Level | Artifact | Purpose |
|-------|----------|---------|
| **L0: Platform** | `PRD-PLATFORM` | Platform-wide requirements (actors, FRs, NFRs) |
| | `DESIGN-PLATFORM` | Platform architecture (KMP modules, shared components) |
| | `DECOMPOSITION-PLATFORM` | Platform → MiniApps breakdown |
| **L1: MiniApp** | `PRD-MINIAPP` | MiniApp domain requirements |
| | `DESIGN-MINIAPP` | MiniApp architecture (ViewModels, repositories) |
| | `DECOMPOSITION-MINIAPP` | MiniApp → Epics breakdown |
| **L2: Epic** | `PRD-EPIC` | Epic user stories and acceptance criteria |
| | `DESIGN-EPIC` | Epic components and sequences |
| | `DECOMPOSITION-EPIC` | Epic → Features breakdown |
| **L3: Feature** | `FEATURE-MOBILE` | MVI design (State, Intent, Effect, CDSL flows) |
| | `IMPL-KMP` | KMP shared implementation tracking |
| | `IMPL-ANDROID` | Android/Compose implementation tracking |
| | `IMPL-IOS` | iOS/SwiftUI implementation tracking |

Each artifact type includes:
- `template.md` — Document structure
- `rules.md` — Generation and validation rules
- `checklist.md` — Review criteria

## Quick Start

### 1. Create Platform PRD

```bash
# Use standard SDLC PRD for platform level
cfs generate PRD --path architecture/PRD.md
```

### 2. Create Platform DESIGN

```bash
cfs generate DESIGN-PLATFORM --path architecture/DESIGN.md
```

### 3. Create MiniApp

```bash
# PRD for MiniApp
cfs generate PRD-MINIAPP --path miniapps/student/PRD.md

# DESIGN for MiniApp
cfs generate DESIGN-MINIAPP --path miniapps/student/DESIGN.md
```

### 4. Create Epic

```bash
# PRD for Epic
cfs generate PRD-EPIC --path miniapps/student/capabilities/notification-history/PRD.md

# DESIGN for Epic
cfs generate DESIGN-EPIC --path miniapps/student/capabilities/notification-history/DESIGN.md
```

### 5. Create Feature

```bash
cfs generate FEATURE-MOBILE --path miniapps/student/capabilities/notification-history/features/badge/FEATURE.md
```

## Project Structure

```
mobile-superapp/
├── architecture/
│   ├── PRD.md                    # Platform PRD (L0)
│   ├── DESIGN.md                 # Platform DESIGN
│   └── DECOMPOSITION.md          # Platform → MiniApps
│
└── miniapps/
    └── student/
        ├── PRD.md                # MiniApp PRD (L1)
        ├── DESIGN.md             # MiniApp DESIGN
        ├── DECOMPOSITION.md      # MiniApp → Epics
        │
        └── capabilities/
            └── notification-history/
                ├── PRD.md        # Epic PRD (L2)
                ├── DESIGN.md     # Epic DESIGN
                ├── DECOMPOSITION.md
                │
                └── features/
                    └── badge/
                        └── FEATURE.md  # Feature (L3)
```

## ID Naming Conventions

| Level | Pattern | Example |
|-------|---------|---------|
| Platform FR | `cpt-{platform}-fr-{slug}` | `cpt-superapp-fr-offline` |
| Platform Component | `cpt-{platform}-component-{slug}` | `cpt-superapp-component-auth` |
| MiniApp FR | `cpt-{miniapp}-fr-{slug}` | `cpt-student-fr-courses` |
| MiniApp Epic | `cpt-{miniapp}-epic-{slug}` | `cpt-student-epic-home` |
| Epic FR | `cpt-{miniapp}-epic-{epic}-fr-{slug}` | `cpt-student-epic-home-fr-streak` |
| Feature | `cpt-{miniapp}-feature-{slug}` | `cpt-student-feature-daily-goal` |
| KMP Impl | `cpt-kmp-{module}-{type}-{slug}` | `cpt-kmp-home-usecase-load` |
| Android Impl | `cpt-android-{module}-{type}-{slug}` | `cpt-android-home-screen-main` |
| iOS Impl | `cpt-ios-{module}-{type}-{slug}` | `cpt-ios-home-view-main` |

## Validation

```bash
# Validate single artifact
cfs validate --artifact miniapps/student/PRD.md

# Validate FR traceability cascade
cfs validate --check=fr-cascade

# Check Platform FR → MiniApp FR coverage
cfs validate --check=platform-fr-coverage

# Check Feature implementation coverage
cfs validate --check=feature-impl-coverage
```

## Technology Stack (Target)

| Layer | Technology |
|-------|------------|
| **KMP Shared** | Kotlin Multiplatform, Ktor, SQLDelight |
| **Android UI** | Jetpack Compose, Hilt, Navigation Compose |
| **iOS UI** | SwiftUI, Combine, Swift Concurrency |
| **State Management** | MVI (Model-View-Intent) |
| **Architecture** | Clean Architecture, Modular |

## Design Rationale

### Why 4 Levels?

Standard SDLC approaches (PRD → DESIGN → FEATURE → CODE) work well for monolithic apps, but **SuperApps** present unique challenges:

1. **Scale**: A SuperApp contains 5-10+ mini-apps, each with 10-50+ features
2. **Team Structure**: Different teams own different MiniApps, need isolated documentation
3. **Requirements Cascade**: Platform-level requirements (e.g., "offline support") must be traced down to every MiniApp that implements them
4. **Shared Kernel vs Domain Logic**: Auth, push notifications, deep links are shared; course content, proctoring logic are domain-specific

The **4-level hierarchy** emerged from real-world mobile development:

| Level | Scope | Team | Example |
|-------|-------|------|---------|
| **L0: Platform** | Entire app, shared infrastructure | Platform team | "App must work offline" |
| **L1: MiniApp** | Single mini-app domain | Feature team | "Student MiniApp needs course access" |
| **L2: Epic** | User-facing capability | Feature team | "Notification history screen" |
| **L3: Feature** | Single implementable behavior | Developer | "Unread badge counter" |

### Why Cascading FR Traceability?

In mobile development, requirements often get "lost" between high-level goals and actual implementation:

```
Product Manager: "The app should work offline"
Developer: "Which screens? What data? How fresh?"
```

**Cascading FR traceability** solves this by requiring explicit links at each level:

```
Platform FR: cpt-platform-fr-offline-support
    ↓ "refined by"
MiniApp FR: cpt-learn-fr-offline-courses
    ↓ "detailed by"  
Epic Story: cpt-learn-course-catalog-story-cache-courses
    ↓ "specified by"
Feature Flow: cpt-learn-flow-course-list-load-cached
    ↓ "implemented by"
Code: @cpt-flow:cpt-learn-flow-course-list-load-cached:p1
```

Benefits:
- **Impact Analysis**: Change platform FR → see all affected MiniApps/Features
- **Coverage Check**: Ensure every platform requirement reaches code
- **Audit Trail**: For compliance, security reviews

### Why MVI Pattern?

Mobile apps require consistent state management across platforms. After evaluating MVVM, MVC, Redux:

**MVI (Model-View-Intent)** was chosen because:

1. **Unidirectional Data Flow**: State → UI → Intent → Reducer → State
2. **Cross-Platform**: Same pattern in KMP, Compose, SwiftUI
3. **Testability**: Pure functions (reducer), predictable state transitions
4. **Design-to-Code Mapping**: CDSL flows map directly to Intents

```kotlin
// FEATURE-MOBILE defines:
sealed class CourseListIntent {
    object Load : CourseListIntent()      // maps to CDSL flow: load
    object Refresh : CourseListIntent()   // maps to CDSL flow: refresh
}

// Code implements with markers:
// @cpt-flow:cpt-learn-flow-course-list-load:p1
fun processIntent(intent: CourseListIntent) { ... }
```

### Why Platform-Specific Implementation Sections?

KMP shares logic, but **UI is inherently platform-specific**:

| Concern | KMP Shared | Android | iOS |
|---------|------------|---------|-----|
| Business Logic | ✅ ViewModel, UseCase | - | - |
| State | ✅ StateFlow | collectAsStateWithLifecycle | Combine wrapper |
| Navigation | Decompose/Voyager | NavController | NavigationStack |
| DI | Koin | Hilt | Manual/Factory |
| UI | - | Compose | SwiftUI |

FEATURE-MOBILE includes separate implementation sections because:
- **Different APIs**: Compose `LazyColumn` vs SwiftUI `List`
- **Different Patterns**: `@Composable` vs `View` protocol
- **Different Edge Cases**: Android lifecycle vs iOS scene phases

### Why Block Markers (`@cpt-begin`/`@cpt-end`)?

Simple `@cpt-impl` markers show "this file implements X", but don't show **which code implements which CDSL instruction**.

Block markers provide **line-level traceability**:

```kotlin
// @cpt-flow:cpt-learn-flow-course-list-load:p1
fun loadCourses() {
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-1
    viewModelScope.launch {
        _state.update { it.copy(isLoading = true) }
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-1
    
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-2
        val result = repository.getCourses()
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-2
    
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-3
        _state.update { it.copy(courses = result, isLoading = false) }
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-3
    }
}
```

Benefits:
- **Checkbox Cascade**: When all `inst-*` markers exist → mark CDSL step `[x]`
- **Code Review**: Reviewer sees exactly which design step each block implements
- **Refactoring Safety**: Move/rename code, markers stay with the logic

### Evolution from SDLC Kit

This kit started as an extension of the standard [SDLC Kit](https://github.com/cyberfabric/cyber-pilot-kit-sdlc), then diverged to address mobile-specific needs:

| SDLC Kit | Mobile SuperApp Kit | Reason |
|----------|---------------------|--------|
| 1-level hierarchy | 4-level hierarchy | SuperApp scale |
| PRD, DESIGN, FEATURE | PRD-*, DESIGN-*, DECOMPOSITION-* per level | Team isolation |
| Generic FEATURE | FEATURE-MOBILE with MVI | Mobile state management |
| CODE markers | Platform-specific IMPL markers | KMP/Android/iOS separation |
| Single codebase rules | Platform-specific rules | Different patterns per platform |

The kit reuses SDLC concepts (CDSL, traceability, validation) while adding mobile-specific structure.

## License

MIT License — see [LICENSE](LICENSE)

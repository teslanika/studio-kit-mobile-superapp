# 4-Level Hierarchy

The Mobile SuperApp Kit uses a 4-level documentation hierarchy designed for large-scale mobile applications.

## Overview

```
L0: Platform     → Entire app, shared infrastructure
L1: MiniApp       → Single mini-app domain  
L2: Epic         → User-facing capability
L3: Feature      → Single implementable behavior
```

## Visual Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ L0: PLATFORM                                                │
│ PRD-PLATFORM → DESIGN-PLATFORM → DECOMPOSITION-PLATFORM     │
└─────────────────────────┬───────────────────────────────────┘
                          │ contains MiniApps
┌─────────────────────────▼───────────────────────────────────┐
│ L1: MINIAPP (Learn, Assess, Communicate, ...)                │
│ PRD-MINIAPP → DESIGN-MINIAPP → DECOMPOSITION-MINIAPP           │
└─────────────────────────┬───────────────────────────────────┘
                          │ contains Epics
┌─────────────────────────▼───────────────────────────────────┐
│ L2: EPIC (Course Catalog, Exam Session, Chat, ...)          │
│ PRD-EPIC → DESIGN-EPIC → DECOMPOSITION-EPIC                 │
└─────────────────────────┬───────────────────────────────────┘
                          │ contains Features
┌─────────────────────────▼───────────────────────────────────┐
│ L3: FEATURE (Course List, Search, Enrollment, ...)          │
│ FEATURE-MOBILE → IMPL-KMP / IMPL-ANDROID / IMPL-IOS         │
└─────────────────────────────────────────────────────────────┘
```

---

## L0: Platform

**Scope**: Entire app, shared infrastructure  
**Team**: Platform team  
**Example**: "App must work offline"

### Artifacts

| Artifact | Purpose |
|----------|---------|
| `PRD-PLATFORM` | Platform-wide requirements (actors, FRs, NFRs) |
| `DESIGN-PLATFORM` | Platform architecture (KMP modules, shared components) |
| `DECOMPOSITION-PLATFORM` | Platform → MiniApps breakdown |

### Create

```bash
cfs make PRD-PLATFORM
cfs make DESIGN-PLATFORM
cfs make DECOMPOSITION-PLATFORM
```

### File Location

```
architecture/
├── PRD.md
├── DESIGN.md
└── DECOMPOSITION.md
```

---

## L1: MiniApp

**Scope**: Single mini-app domain  
**Team**: Feature team  
**Example**: "Student MiniApp needs course access"

### Artifacts

| Artifact | Purpose |
|----------|---------|
| `PRD-MINIAPP` | MiniApp domain requirements |
| `DESIGN-MINIAPP` | MiniApp architecture (ViewModels, repositories) |
| `DECOMPOSITION-MINIAPP` | MiniApp → Epics breakdown |

### Create

```bash
cfs make PRD-MINIAPP for learn
cfs make DESIGN-MINIAPP for learn
cfs make DECOMPOSITION-MINIAPP for learn
```

### File Location

```
miniapps/learn/
├── PRD.md
├── DESIGN.md
└── DECOMPOSITION.md
```

---

## L2: Epic

**Scope**: User-facing capability  
**Team**: Feature team  
**Example**: "Notification history screen"

### Artifacts

| Artifact | Purpose |
|----------|---------|
| `PRD-EPIC` | Epic user stories and acceptance criteria |
| `DESIGN-EPIC` | Epic components and sequences |
| `DECOMPOSITION-EPIC` | Epic → Features breakdown |

### Create

```bash
cfs make PRD-EPIC for course-catalog
cfs make DESIGN-EPIC for course-catalog
cfs make DECOMPOSITION-EPIC for course-catalog
```

### File Location

```
miniapps/learn/capabilities/course-catalog/
├── PRD.md
├── DESIGN.md
└── DECOMPOSITION.md
```

---

## L3: Feature

**Scope**: Single implementable behavior  
**Team**: Developer  
**Example**: "Unread badge counter"

### Artifacts

| Artifact | Purpose |
|----------|---------|
| `FEATURE-MOBILE` | MVI design (State, Intent, Effect, CDSL flows) |
| `IMPL-KMP` | KMP shared implementation tracking |
| `IMPL-ANDROID` | Android/Compose implementation tracking |
| `IMPL-IOS` | iOS/SwiftUI implementation tracking |

### Create

```bash
cfs make FEATURE-MOBILE for course-list
cfs implement course-list
```

### File Location

```
miniapps/learn/capabilities/course-catalog/features/course-list/
└── FEATURE.md
```

---

## Why 4 Levels?

Standard SDLC (PRD → DESIGN → FEATURE → CODE) works for monolithic apps, but **SuperApps** present unique challenges:

| Challenge | How 4-Level Solves It |
|-----------|----------------------|
| **Scale**: 5-10+ mini-apps, 10-50+ features each | Each MiniApp has isolated documentation |
| **Team Structure**: Different teams own different MiniApps | Clear ownership at each level |
| **Requirements Cascade**: Platform requirements must reach code | Explicit traceability links at each level |
| **Shared vs Domain**: Auth is shared, courses are domain-specific | L0 for shared, L1-L3 for domain |

# Mobile SuperApp Kit Quick Start

**Learn Constructor Studio Mobile SuperApp in 10 minutes with real prompts and examples**

Constructor Studio Mobile SuperApp works through the Constructor Studio skill — enable it with `cfs on` and use natural language prompts prefixed with `cf`. The skill handles artifact discovery, template loading, validation, and traceability automatically.

---

## What You'll Learn

1. **4-Level Hierarchy** — Platform → MiniApp → Epic → Feature
2. **Exact prompts to type** — copy-paste into your AI chat
3. **Mobile-specific pipeline** — from requirements to KMP/Android/iOS code
4. **Cascading traceability** — requirements flow down all levels

---

## The Pipeline

Mobile SuperApp Kit = **4-Level Design First, Platform Code Second**

```mermaid
flowchart LR
    subgraph L0[Platform Level]
        PRD0[PRD-PLATFORM]
        DESIGN0[DESIGN-PLATFORM]
        DECOMP0[DECOMPOSITION-PLATFORM]
    end
    
    subgraph L1[MiniApp Level]
        PRD1[PRD-MINIAPP]
        DESIGN1[DESIGN-MINIAPP]
        DECOMP1[DECOMPOSITION-MINIAPP]
    end
    
    subgraph L2[Epic Level]
        PRD2[PRD-EPIC]
        DESIGN2[DESIGN-EPIC]
        DECOMP2[DECOMPOSITION-EPIC]
    end
    
    subgraph L3[Feature Level]
        FEATURE[FEATURE-MOBILE]
        IMPL[IMPL]
    end
    
    PRD0 --> DESIGN0 --> DECOMP0 --> PRD1
    PRD1 --> DESIGN1 --> DECOMP1 --> PRD2
    PRD2 --> DESIGN2 --> DECOMP2 --> FEATURE
    FEATURE --> IMPL
```

| Level | Artifacts | Purpose |
|-------|-----------|---------|
| **L0: Platform** | PRD-PLATFORM, DESIGN-PLATFORM, DECOMPOSITION-PLATFORM | Overall mobile platform architecture |
| **L1: MiniApp** | PRD-MINIAPP, DESIGN-MINIAPP, DECOMPOSITION-MINIAPP | Individual mini-app (Learn, Assess, etc.) |
| **L2: Epic** | PRD-EPIC, DESIGN-EPIC, DECOMPOSITION-EPIC | User-facing capability group |
| **L3: Feature** | FEATURE-MOBILE, IMPL | Single implementable behavior |

**Key principle**: Design flows down the hierarchy. If code contradicts design, fix design first at the appropriate level.

Learn what each artifact means: [TAXONOMY.md](TAXONOMY.md)

---

## Getting Started

| Prompt | What happens |
|--------|--------------|
| `Constructor Studio on` | Enables Constructor Studio mode, discovers config, loads project context |
| `cfs init` | Creates `.cf-studio/` directory with `.core/`, `.gen/`, `config/` and initializes `artifacts.toml` |
| `cfs show pipeline` | Displays current artifact hierarchy and validation status |

**Install the kit:**
```bash
cfs kit install mobile-superapp
```

---

## Adopting After the Constructor Studio Migration

The repo was migrated from Cypilot to Constructor Studio. `git pull` gives you the
tracked config, `.cf-workspace.toml`, and agent integration files — but **not** the
framework runtime (`.cf-studio/.core/`, `.cf-studio/.gen/`), which is gitignored and
installed per-machine. Each developer does this once:

**1. Replace the CLI** (old `cypilot`/`cpt` → `constructor-studio`/`cfs`):
```bash
pipx uninstall cypilot
pipx install git+https://github.com/constructorfabric/studio.git
cfs --version
```

**2. Materialize the runtime in the repo:**
```bash
git pull
cfs update        # populates/repairs .cf-studio/.core/ and .gen/
```
(Use `cfs init` instead if `.cf-studio/.core/` is missing after a fresh clone.)

**3. Activate in your AI coding tool** — keyword, not a terminal command:
`cf` to enable, then `cf-help`, `cf-explore: ...`, `cf-coding: ...`.

**Notes**
- Agent integration files (`.claude/`, `.cursor/`, `.github/`, `.agents/`, `.codex/`,
  `.windsurf/`) are tracked, so `cfs generate-agents` is **not** required — you get them
  from git. Only regenerate to repair.
- Pin one `constructor-studio` CLI version across the team so `.core` stays aligned with
  the tracked `.cf-studio/version.toml`.

| Was (cypilot) | Now (studio) |
|---|---|
| CLI `cpt` | `cfs` |
| `/cypilot-*` | `/cf-*` |
| `.cypilot-workspace.toml` | `.cf-workspace.toml` |

---

## Example Prompts — New Mobile App

### Platform Level (L0)

| Prompt | What the agent does |
|--------|---------------------|
| `cfs make PRD-PLATFORM` | Creates platform PRD with actors, capabilities, NFRs |
| `cfs make PRD-PLATFORM for Constructor SuperApp` | Generates PRD with context |
| `cfs make DESIGN-PLATFORM` | Creates platform architecture (KMP, modules, navigation) |
| `cfs make DECOMPOSITION-PLATFORM` | Breaks platform into MiniApps |
| `cfs validate PRD-PLATFORM` | Full validation |

### MiniApp Level (L1)

| Prompt | What the agent does |
|--------|---------------------|
| `cfs make PRD-MINIAPP for learn` | Creates Learn MiniApp requirements |
| `cfs make DESIGN-MINIAPP for learn` | Creates Learn MiniApp architecture |
| `cfs make DECOMPOSITION-MINIAPP for learn` | Breaks MiniApp into Epics |
| `cfs validate DESIGN-MINIAPP for learn` | Validates MiniApp design |

### Epic Level (L2)

| Prompt | What the agent does |
|--------|---------------------|
| `cfs make PRD-EPIC for course-catalog` | Creates Epic requirements |
| `cfs make DESIGN-EPIC for course-catalog` | Creates Epic architecture |
| `cfs make DECOMPOSITION-EPIC for course-catalog` | Breaks Epic into Features |
| `cfs validate PRD-EPIC for course-catalog` | Validates Epic PRD |

### Feature Level (L3)

| Prompt | What the agent does |
|--------|---------------------|
| `cfs make FEATURE-MOBILE for course-list` | Creates feature with MVI, CDSL, platform sections |
| `cfs validate FEATURE-MOBILE for course-list` | Full validation (flows, states, DoD) |
| `cfs implement course-list` | Generates KMP + Android + iOS code |
| `cfs implement course-list kmp` | KMP shared code only |
| `cfs implement course-list android` | Android Compose UI only |
| `cfs implement course-list ios` | iOS SwiftUI only |

---

## Mobile-Specific Patterns

### MVI State Management

All features use Model-View-Intent:

```kotlin
// @cpt-impl cpt-learn-course-list-state-kmp
data class CourseListState(
    val isLoading: Boolean = false,
    val courses: List<Course> = emptyList(),
    val error: String? = null
)

sealed class CourseListIntent {
    object Load : CourseListIntent()
    data class Search(val query: String) : CourseListIntent()
    data class SelectCourse(val id: String) : CourseListIntent()
}

sealed class CourseListEffect {
    data class NavigateToCourse(val id: String) : CourseListEffect()
    data class ShowError(val message: String) : CourseListEffect()
}
```

### Platform Implementation Order

Always implement in this order:
1. **KMP First** — Shared ViewModel, UseCase, Repository
2. **Android Second** — Compose UI with KMP integration
3. **iOS Third** — SwiftUI with KMP wrapper

### Traceability Markers

```kotlin
// Simplified (DOCS-ONLY mode)
// @cpt-impl cpt-learn-course-list-viewmodel-kmp

// Full traceability (FULL mode)
// @cpt-flow:cpt-learn-flow-course-list-load:p1
class CourseListViewModel {
    // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-kmp-1
    fun loadCourses() { ... }
    // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-kmp-1
}
```

---

## Cascading FR Traceability

Requirements cascade through all four levels:

```
Platform FR: cpt-platform-fr-offline-support
    ↓ referenced by
MiniApp FR: cpt-learn-fr-offline-courses
    ↓ referenced by
Epic FR: cpt-course-catalog-fr-cache-courses
    ↓ referenced by
Feature: cpt-course-list-flow-load-cached
    ↓ implemented by
Code: @cpt-flow:cpt-course-list-flow-load-cached:p1
```

### Traceability Queries

| Prompt | What happens |
|--------|--------------|
| `cfs trace cpt-platform-fr-offline-support` | Shows full path to code |
| `cfs trace cpt-learn-course-list-flow-load` | Shows feature to code path |
| `cfs find orphans` | Lists IDs with no downstream refs |
| `cfs coverage report` | Implementation coverage by level |

---

## Validation

### Per-Level Validation

| Prompt | What happens |
|--------|--------------|
| `cfs validate PRD-PLATFORM` | Platform requirements validation |
| `cfs validate DESIGN-MINIAPP for learn` | MiniApp architecture validation |
| `cfs validate FEATURE-MOBILE for course-list` | Feature validation (CDSL, MVI, DoD) |
| `cfs validate code for course-list` | Code marker validation |

### Validation Modes

Append to any `validate` command:
- `semantic` — content quality, completeness, mobile patterns
- `structural` — format, IDs, template compliance
- `refs` — cross-references across levels
- `quick` — critical issues only (fast)

### Cross-Level Validation

| Prompt | What happens |
|--------|--------------|
| `cfs validate all` | Validates entire 4-level hierarchy |
| `cfs validate all refs` | Validates all cross-references |
| `cfs validate code coverage` | Reports implementation coverage % |

---

## Quick Reference

### Create Pipeline (Top-Down)

| Step | Prompt |
|------|--------|
| 1 | `cfs make PRD-PLATFORM for {app-name}` |
| 2 | `cfs make DESIGN-PLATFORM` |
| 3 | `cfs make DECOMPOSITION-PLATFORM` |
| 4 | `cfs make PRD-MINIAPP for {miniapp}` |
| 5 | `cfs make DESIGN-MINIAPP for {miniapp}` |
| 6 | `cfs make DECOMPOSITION-MINIAPP for {miniapp}` |
| 7 | `cfs make PRD-EPIC for {epic}` |
| 8 | `cfs make DESIGN-EPIC for {epic}` |
| 9 | `cfs make DECOMPOSITION-EPIC for {epic}` |
| 10 | `cfs make FEATURE-MOBILE for {feature}` |
| 11 | `cfs implement {feature}` |

### Validate Pipeline

| Step | Prompt |
|------|--------|
| 1 | `cfs validate PRD-PLATFORM` |
| 2 | `cfs validate DESIGN-PLATFORM` |
| ... | Continue for each artifact |
| Final | `cfs validate all` |

---

## Guides by Scenario

| Scenario | Guide | Key Point |
|----------|-------|-----------|
| **Greenfield** | [GREENFIELD.md](GREENFIELD.md) | Start from Platform PRD, work down to code |
| **Brownfield** | [BROWNFIELD.md](BROWNFIELD.md) | Start anywhere — code-only, bottom-up, or full |

## Reference

- Artifact taxonomy: [TAXONOMY.md](TAXONOMY.md)
- Kit overview: [README.md](../README.md)

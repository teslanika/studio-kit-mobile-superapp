# Implementation Reference — Android UI

## Overview

This document links the Android implementation to its product documentation.

**Module**: `android-app/feature/{module}/`

## References

| Document | Path | ID |
|----------|------|-----|
| Feature | [miniapps/{miniapp}/.../features/{feature}/FEATURE.md](../../miniapps/{miniapp}/.../features/{feature}/FEATURE.md) | `cpt-{miniapp}-feature-{slug}` |
| Epic DESIGN | [miniapps/{miniapp}/.../DESIGN.md](../../miniapps/{miniapp}/.../DESIGN.md) | `cpt-{miniapp}-epic-{epic}` |
| MiniApp DESIGN | [miniapps/{miniapp}/DESIGN.md](../../miniapps/{miniapp}/DESIGN.md) | `cpt-{miniapp}-design` |

## Scope

This Android module implements:
- Section 3.2 (Android UI) from FEATURE.md
- Android-specific components from DESIGN.md
- Jetpack Compose UI, navigation, and platform integration

## Implementation Notes

{Android-specific decisions, Compose patterns used, navigation setup}

## Traceability Table

| Design Component ID | Code File | Implementation ID |
|---------------------|-----------|-------------------|
| `cpt-{miniapp}-{epic}-screen-{slug}` | `ui/{feature}/{Feature}Screen.kt` | `@cpt-impl cpt-android-{module}-screen-{slug}` |
| `cpt-{miniapp}-{epic}-widget-{slug}` | `ui/{feature}/components/{Widget}.kt` | `@cpt-impl cpt-android-{module}-widget-{slug}` |
| `cpt-{miniapp}-{epic}-nav` | `navigation/{Feature}NavGraph.kt` | `@cpt-impl cpt-android-{module}-nav-{slug}` |
| `cpt-{miniapp}-algo-{feature-slug}-android` | `ui/{feature}/{Feature}Screen.kt` | `@cpt-impl cpt-android-{module}-ui-{slug}` |

## Directory Structure

```
android-app/feature/{module}/
├── IMPL.md                           ← This file
├── src/main/kotlin/
│   └── com/constructor/android/feature/{module}/
│       ├── ui/
│       │   ├── {Feature}Screen.kt    # Main screen composable
│       │   └── components/           # Reusable UI components
│       │       ├── {Widget1}.kt
│       │       └── {Widget2}.kt
│       ├── navigation/
│       │   └── {Feature}NavGraph.kt  # Navigation graph
│       └── di/
│           └── {Feature}Module.kt    # Hilt module
├── src/main/res/
│   ├── values/
│   │   └── strings.xml               # Feature strings
│   └── drawable/                     # Feature drawables
└── build.gradle.kts
```

## Code Markers

All implementations include `@cpt-impl` markers for traceability:

```kotlin
// @cpt-impl cpt-android-{module}-screen-{slug}
@Composable
fun {Feature}Screen(
    viewModel: {Feature}ViewModel = hiltViewModel(),
    onNavigate: (String) -> Unit
) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    
    // UI Implementation
}
```

## Dependencies

| Dependency | Purpose |
|------------|---------|
| `constructor-sdk/feature/{module}` | KMP shared logic (ViewModel, UseCase) |
| `android-app/common/ui` | Design system components |
| `android-app/common/navigation` | Navigation utilities |

## Validation

Run `cfs validate --artifact android-app/feature/{module}/` to verify:
- All design components have `@cpt-impl` markers in code
- All code markers reference valid design IDs
- Coverage meets minimum threshold

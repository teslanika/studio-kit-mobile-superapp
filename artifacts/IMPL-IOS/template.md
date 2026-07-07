# Implementation Reference — iOS UI

## Overview

This document links the iOS implementation to its product documentation.

**Module**: `ios-app/Features/{Module}/`

## References

| Document | Path | ID |
|----------|------|-----|
| Feature | [miniapps/{miniapp}/.../features/{feature}/FEATURE.md](../../miniapps/{miniapp}/.../features/{feature}/FEATURE.md) | `cpt-{miniapp}-feature-{slug}` |
| Epic DESIGN | [miniapps/{miniapp}/.../DESIGN.md](../../miniapps/{miniapp}/.../DESIGN.md) | `cpt-{miniapp}-epic-{epic}` |
| MiniApp DESIGN | [miniapps/{miniapp}/DESIGN.md](../../miniapps/{miniapp}/DESIGN.md) | `cpt-{miniapp}-design` |

## Scope

This iOS module implements:
- Section 3.3 (iOS UI) from FEATURE.md
- iOS-specific components from DESIGN.md
- SwiftUI views, navigation, and platform integration

## Implementation Notes

{iOS-specific decisions, SwiftUI patterns used, navigation coordinators}

## Traceability Table

| Design Component ID | Code File | Implementation ID |
|---------------------|-----------|-------------------|
| `cpt-{miniapp}-{epic}-screen-{slug}` | `Views/{Feature}/{Feature}View.swift` | `@cpt-impl cpt-ios-{module}-view-{slug}` |
| `cpt-{miniapp}-{epic}-widget-{slug}` | `Views/{Feature}/Components/{Widget}.swift` | `@cpt-impl cpt-ios-{module}-widget-{slug}` |
| `cpt-{miniapp}-{epic}-nav` | `Navigation/{Feature}Coordinator.swift` | `@cpt-impl cpt-ios-{module}-nav-{slug}` |
| `cpt-{miniapp}-algo-{feature-slug}-ios` | `Views/{Feature}/{Feature}View.swift` | `@cpt-impl cpt-ios-{module}-ui-{slug}` |

## Directory Structure

```
ios-app/Features/{Module}/
├── IMPL.md                           ← This file
├── Views/
│   ├── {Feature}View.swift           # Main SwiftUI view
│   └── Components/                   # Reusable UI components
│       ├── {Widget1}.swift
│       └── {Widget2}.swift
├── Navigation/
│   └── {Feature}Coordinator.swift    # Navigation coordinator
├── ViewModels/
│   └── {Feature}ViewModelWrapper.swift  # KMP ViewModel wrapper (if needed)
└── Resources/
    ├── Localizable.strings           # Feature strings
    └── Assets.xcassets/              # Feature assets
```

## Code Markers

All implementations include `@cpt-impl` markers for traceability:

```swift
// @cpt-impl cpt-ios-{module}-view-{slug}
struct {Feature}View: View {
    @StateObject private var viewModel: {Feature}ViewModelWrapper
    
    var body: some View {
        // UI Implementation
    }
}
```

## KMP Integration

```swift
// Wrapper to bridge KMP ViewModel to SwiftUI
class {Feature}ViewModelWrapper: ObservableObject {
    private let kmpViewModel: {Feature}ViewModel
    
    @Published var state: {Feature}State
    
    init() {
        self.kmpViewModel = {Feature}ViewModel()
        // Observe KMP state flow
    }
    
    func send(_ intent: {Feature}Intent) {
        kmpViewModel.processIntent(intent)
    }
}
```

## Dependencies

| Dependency | Purpose |
|------------|---------|
| `ConstructorSDK` | KMP shared logic framework |
| `ios-app/Common/UI` | Design system components |
| `ios-app/Common/Navigation` | Navigation utilities |

## Validation

Run `cfs validate --artifact ios-app/Features/{Module}/` to verify:
- All design components have `@cpt-impl` markers in code
- All code markers reference valid design IDs
- Coverage meets minimum threshold

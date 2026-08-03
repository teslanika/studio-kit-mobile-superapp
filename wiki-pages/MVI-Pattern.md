# MVI Pattern

The Mobile SuperApp Kit uses **Model-View-Intent (MVI)** for consistent state management across platforms.

## Why MVI?

After evaluating MVVM, MVC, and Redux, MVI was chosen because:

| Benefit | Description |
|---------|-------------|
| **Unidirectional Flow** | State → UI → Intent → Reducer → State |
| **Cross-Platform** | Same pattern in KMP, Compose, SwiftUI |
| **Testability** | Pure functions, predictable state transitions |
| **Design-to-Code** | CDSL flows map directly to Intents |

## Core Components

### State

Immutable data class representing UI state.

```kotlin
data class CourseListState(
    val isLoading: Boolean = false,
    val courses: List<Course> = emptyList(),
    val error: String? = null,
    val searchQuery: String = ""
)
```

**Rules:**
- Must be immutable `data class`
- Must have default values for all properties
- Must NOT contain mutable collections

### Intent

Sealed class representing user actions.

```kotlin
sealed class CourseListIntent {
    object Load : CourseListIntent()
    object Refresh : CourseListIntent()
    data class Search(val query: String) : CourseListIntent()
    data class SelectCourse(val id: String) : CourseListIntent()
}
```

**Rules:**
- Must be `sealed class`
- Each intent = one user action
- Maps to CDSL flow

### Effect

Sealed class for one-time events (navigation, toasts).

```kotlin
sealed class CourseListEffect {
    data class NavigateToCourse(val id: String) : CourseListEffect()
    data class ShowError(val message: String) : CourseListEffect()
    object ScrollToTop : CourseListEffect()
}
```

**Rules:**
- Must be `sealed class`
- One-time events only (not UI state)
- Consumed once by UI

## Data Flow

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   User   │────▶│  Intent  │────▶│ ViewModel│────▶│  State   │
│  Action  │     │          │     │ (Reducer)│     │          │
└──────────┘     └──────────┘     └──────────┘     └────┬─────┘
                                        │               │
                                        │               ▼
                                        │         ┌──────────┐
                                        └────────▶│    UI    │
                                       Effect     └──────────┘
```

## Platform Implementation

### KMP ViewModel

```kotlin
// @cpt-impl cpt-superapp-learn-course-list-viewmodel-kmp
class CourseListViewModel(
    private val loadCoursesUseCase: LoadCoursesUseCase
) : ViewModel() {
    
    private val _state = MutableStateFlow(CourseListState())
    val state: StateFlow<CourseListState> = _state.asStateFlow()
    
    private val _effects = MutableSharedFlow<CourseListEffect>()
    val effects: SharedFlow<CourseListEffect> = _effects.asSharedFlow()
    
    fun processIntent(intent: CourseListIntent) {
        when (intent) {
            is CourseListIntent.Load -> loadCourses()
            is CourseListIntent.Refresh -> refresh()
            is CourseListIntent.Search -> search(intent.query)
            is CourseListIntent.SelectCourse -> selectCourse(intent.id)
        }
    }
    
    private fun loadCourses() {
        viewModelScope.launch {
            _state.update { it.copy(isLoading = true) }
            val result = loadCoursesUseCase()
            _state.update { 
                it.copy(isLoading = false, courses = result) 
            }
        }
    }
}
```

### Android Compose

```kotlin
// @cpt-impl cpt-superapp-learn-course-list-screen-android
@Composable
fun CourseListScreen(
    viewModel: CourseListViewModel = hiltViewModel(),
    onNavigateToCourse: (String) -> Unit
) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    
    LaunchedEffect(Unit) {
        viewModel.processIntent(CourseListIntent.Load)
        
        viewModel.effects.collect { effect ->
            when (effect) {
                is CourseListEffect.NavigateToCourse -> 
                    onNavigateToCourse(effect.id)
                is CourseListEffect.ShowError -> 
                    // Show snackbar
            }
        }
    }
    
    CourseListContent(
        state = state,
        onRefresh = { viewModel.processIntent(CourseListIntent.Refresh) },
        onSearch = { viewModel.processIntent(CourseListIntent.Search(it)) },
        onSelectCourse = { viewModel.processIntent(CourseListIntent.SelectCourse(it)) }
    )
}
```

### iOS SwiftUI

```swift
// @cpt-impl cpt-superapp-learn-course-list-view-ios
struct CourseListView: View {
    @StateObject private var viewModel = CourseListViewModelWrapper()
    let onNavigateToCourse: (String) -> Void
    
    var body: some View {
        CourseListContent(
            state: viewModel.state,
            onRefresh: { viewModel.send(.Refresh()) },
            onSearch: { viewModel.send(.Search(query: $0)) },
            onSelectCourse: { viewModel.send(.SelectCourse(id: $0)) }
        )
        .onAppear {
            viewModel.send(.Load())
        }
        .onReceive(viewModel.effects) { effect in
            switch effect {
            case let .NavigateToCourse(id):
                onNavigateToCourse(id)
            case let .ShowError(message):
                // Show alert
            }
        }
    }
}
```

## FEATURE-MOBILE Template

In FEATURE-MOBILE documents, define MVI components:

```markdown
## MVI Definition

### State

\`\`\`kotlin
data class CourseListState(
    val isLoading: Boolean = false,
    val courses: List<Course> = emptyList(),
    val error: CourseListError? = null
)
\`\`\`

### Intent

\`\`\`kotlin
sealed class CourseListIntent {
    object Load : CourseListIntent()
    object Refresh : CourseListIntent()
}
\`\`\`

### Effect

\`\`\`kotlin
sealed class CourseListEffect {
    data class NavigateToCourse(val id: String) : CourseListEffect()
}
\`\`\`
```

## Mapping CDSL to Intents

CDSL flows map directly to Intents:

| CDSL Flow | Intent |
|-----------|--------|
| `flow cpt-superapp-learn-flow-course-list-load` | `CourseListIntent.Load` |
| `flow cpt-superapp-learn-flow-course-list-refresh` | `CourseListIntent.Refresh` |
| `flow cpt-superapp-learn-flow-course-list-search` | `CourseListIntent.Search` |

This ensures design-to-code traceability.

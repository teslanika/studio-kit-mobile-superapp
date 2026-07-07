# Examples

Real-world examples of using the Mobile SuperApp Kit.

## Complete Feature Example

See the full example in the repository:
- [examples/FEATURE-MOBILE/course-list.md](https://github.com/teslanika/studio-kit-mobile-superapp/blob/main/examples/FEATURE-MOBILE/course-list.md)

## Quick Examples

### Platform PRD (L0)

```markdown
# Platform PRD: Constructor Mobile

## Actors

| ID | Name | Description |
|----|------|-------------|
| `cpt-platform-actor-student` | Student | Learner using the app |
| `cpt-platform-actor-instructor` | Instructor | Course creator |

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| `cpt-platform-fr-offline-support` | App works without internet | P0 |
| `cpt-platform-fr-push-notifications` | Receive course updates | P1 |

## Non-Functional Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| `cpt-platform-nfr-launch-time` | Cold start time | < 3s |
| `cpt-platform-nfr-memory` | Memory usage | < 200MB |
```

### MiniApp PRD (L1)

```markdown
# MiniApp PRD: Learn

## Traceability

### Platform Requirements
| Platform FR | MiniApp FR |
|-------------|-----------|
| `cpt-platform-fr-offline-support` | `cpt-learn-fr-offline-courses` |

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| `cpt-learn-fr-browse-courses` | Browse course catalog | P0 |
| `cpt-learn-fr-offline-courses` | Access cached courses offline | P0 |
```

### FEATURE-MOBILE (L3)

```markdown
# FEATURE-MOBILE: Course List

## Meta

| Field | Value |
|-------|-------|
| Feature ID | `cpt-learn-course-catalog-feature-course-list` |
| Epic | Course Catalog |
| Status | DESIGNED |

## MVI Definition

### State

\`\`\`kotlin
data class CourseListState(
    val isLoading: Boolean = false,
    val courses: List<Course> = emptyList(),
    val error: String? = null
)
\`\`\`

### Intent

\`\`\`kotlin
sealed class CourseListIntent {
    object Load : CourseListIntent()
    object Refresh : CourseListIntent()
}
\`\`\`

## Actor Flows

### Flow: Load Courses `cpt-learn-flow-course-list-load` `to_code="true"`

\`\`\`cdsl
flow cpt-learn-flow-course-list-load {
  actor: Student
  
  p1: [x] User opens course catalog `inst-open`
  p2: [x] System shows loading `inst-loading`
  p3: [x] System fetches courses `inst-fetch`
  p4: [x] System displays list `inst-display`
  
  error: [ ] If error → show retry `inst-error`
}
\`\`\`
```

### KMP Implementation

```kotlin
// @cpt-impl cpt-learn-course-list-viewmodel-kmp
class CourseListViewModel(
    private val repository: CourseRepository
) : ViewModel() {
    
    private val _state = MutableStateFlow(CourseListState())
    val state: StateFlow<CourseListState> = _state.asStateFlow()
    
    // @cpt-flow:cpt-learn-flow-course-list-load:p1
    fun loadCourses() {
        // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-loading
        _state.update { it.copy(isLoading = true) }
        // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-loading
        
        viewModelScope.launch {
            // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-fetch
            val result = repository.getCourses()
            // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-fetch
            
            // @cpt-begin:cpt-learn-flow-course-list-load:p1:inst-display
            _state.update { 
                it.copy(isLoading = false, courses = result) 
            }
            // @cpt-end:cpt-learn-flow-course-list-load:p1:inst-display
        }
    }
}
```

### Android Compose

```kotlin
// @cpt-impl cpt-learn-course-list-screen-android
@Composable
fun CourseListScreen(
    viewModel: CourseListViewModel = hiltViewModel()
) {
    val state by viewModel.state.collectAsStateWithLifecycle()
    
    LaunchedEffect(Unit) {
        viewModel.loadCourses()
    }
    
    when {
        state.isLoading -> LoadingIndicator()
        state.error != null -> ErrorState(state.error)
        else -> CourseList(state.courses)
    }
}
```

### iOS SwiftUI

```swift
// @cpt-impl cpt-learn-course-list-view-ios
struct CourseListView: View {
    @StateObject private var viewModel = CourseListViewModelWrapper()
    
    var body: some View {
        Group {
            if viewModel.state.isLoading {
                ProgressView()
            } else if let error = viewModel.state.error {
                ErrorView(message: error)
            } else {
                List(viewModel.state.courses) { course in
                    CourseRow(course: course)
                }
            }
        }
        .onAppear {
            viewModel.loadCourses()
        }
    }
}
```

## Project Structure Example

```
mobile-superapp/
├── architecture/
│   ├── PRD.md                          # Platform PRD
│   ├── DESIGN.md                       # Platform DESIGN
│   └── DECOMPOSITION.md                # → MiniApps
│
├── miniapps/
│   └── learn/
│       ├── PRD.md                      # Learn MiniApp PRD
│       ├── DESIGN.md                   # Learn MiniApp DESIGN
│       ├── DECOMPOSITION.md            # → Epics
│       │
│       └── capabilities/
│           └── course-catalog/
│               ├── PRD.md              # Epic PRD
│               ├── DESIGN.md           # Epic DESIGN
│               ├── DECOMPOSITION.md    # → Features
│               │
│               └── features/
│                   └── course-list/
│                       └── FEATURE.md  # Feature spec
│
├── constructor-sdk/                    # KMP shared
│   └── feature/learn/
│       └── courselist/
│           ├── CourseListViewModel.kt
│           ├── CourseListState.kt
│           └── IMPL.md
│
├── android-app/                        # Android
│   └── feature/learn/
│       └── courselist/
│           ├── CourseListScreen.kt
│           └── IMPL.md
│
└── ios-app/                           # iOS
    └── Features/Learn/
        └── CourseList/
            ├── CourseListView.swift
            └── IMPL.md
```

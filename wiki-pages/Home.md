# Mobile SuperApp Kit

Welcome to the Mobile SuperApp Kit wiki!

This kit provides a **4-level documentation hierarchy** for large-scale mobile applications that combine multiple mini-apps (MiniApps) into a single host application.

## Quick Links

| Page | Description |
|------|-------------|
| [Installation](Installation) | How to install and configure the kit |
| [4-Level Hierarchy](4-Level-Hierarchy) | Platform → MiniApp → Epic → Feature |
| [Artifact Types](Artifact-Types) | All 13 artifact types explained |
| [ID Naming Conventions](ID-Naming-Conventions) | How to name your IDs |
| [MVI Pattern](MVI-Pattern) | State, Intent, Effect in mobile |
| [Code Markers](Code-Markers) | @cpt-impl and @cpt-begin/@cpt-end |
| [Traceability](Traceability) | Cascading FR traceability |
| [Examples](Examples) | Real-world examples |

## Key Features

- **4-Level Documentation Hierarchy**: Platform → MiniApp → Epic → Feature
- **Cascading Requirement Traceability**: Every requirement traces from platform to code
- **Mobile-Specific Templates**: KMP, Android (Compose), iOS (SwiftUI)
- **MVI State Management**: Consistent across all MiniApps

## Getting Started

```bash
# Install the kit
cfs kit install teslanika/studio-kit-mobile-superapp

# Enable in chat
cfs on

# Create your first artifact
cfs make PRD-PLATFORM
```

## Support

- [GitHub Issues](https://github.com/teslanika/studio-kit-mobile-superapp/issues)
- [Documentation Site](https://teslanika.github.io/studio-kit-mobile-superapp)

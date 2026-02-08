# Research: Phase I: In-Memory Python Console Todo App

## Decision Log

### 1. Testing Approach
- **Decision**: Adopt informal testing approach during development, acknowledging that formal tests are outside scope per feature specification
- **Rationale**: The feature specification explicitly states "No tests" as a constraint. The constitution's Test-First approach must be balanced with the explicit feature requirements.
- **Alternatives considered**:
  - Full TDD approach (rejected - violates feature constraints)
  - Informal manual testing (selected - balances constitution with feature requirements)

### 2. Test-First Approach Conflict Resolution
- **Decision**: Document the conflict between constitution (II. Test-First) and feature specification (no tests), proceed with informal verification
- **Rationale**: Per feature spec: "Not building: Tests, AI features, or web UI". However, we'll ensure basic functionality verification during development.
- **Alternatives considered**:
  - Strict adherence to constitution (rejected - would contradict feature requirements)
  - Flexible interpretation balancing both (selected - pragmatic approach)

### 3. Technology Stack
- **Decision**: Use pure Python 3.13+ with built-in libraries only
- **Rationale**: Aligns with constraints "Python 3.13+", "No external frameworks or persistence", and "Package manager: UV"
- **Alternatives considered**:
  - Third-party CLI libraries like Click or Argparse (rejected - spec says "No external frameworks")
  - Built-in argparse module (considered but rejected as unnecessary for simple CLI)

### 4. Data Structure for In-Memory Storage
- **Decision**: Use Python list for storing Todo objects in memory
- **Rationale**: Simple, efficient for single-process application with no persistence requirements
- **Alternatives considered**:
  - Dictionary with ID keys (considered but list with indices sufficient)
  - Custom in-memory database (rejected - violates "No external frameworks")
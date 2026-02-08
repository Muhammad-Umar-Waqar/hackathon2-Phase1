---
description: "Task list for Phase I: In-Memory Python Console Todo App implementation"
---

# Tasks: Phase I: In-Memory Python Console Todo App

**Input**: Design documents from `/specs/1-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/
- [x] T002 Initialize Python 3.13+ project with pyproject.toml for UV package manager
- [x] T003 [P] Create directory structure src/todo_app/, src/todo_app/models/, src/todo_app/services/, src/todo_app/cli/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create base Task model in src/todo_app/models/todo.py
- [x] T005 Create base TodoList container in src/todo_app/models/todo.py
- [x] T006 Create TodoManager service in src/todo_app/services/todo_manager.py
- [x] T007 Create initial CLI interface skeleton in src/todo_app/cli/cli_interface.py
- [x] T008 Create main application entry point in src/main.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list and view all existing tasks through the console application

**Independent Test**: Can be fully tested by adding multiple tasks and viewing the list to confirm they appear correctly. Delivers the fundamental value of a todo application.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Manual verification test for add command behavior per CLI contract
- [ ] T010 [P] [US1] Manual verification test for view command behavior per CLI contract

### Implementation for User Story 1

- [x] T011 [P] [US1] Implement Task class with id, title, completed attributes in src/todo_app/models/todo.py
- [x] T012 [US1] Implement TodoList class with tasks list and next_id counter in src/todo_app/models/todo.py
- [x] T013 [US1] Implement add_task method in TodoManager service in src/todo_app/services/todo_manager.py
- [x] T014 [US1] Implement get_all_tasks method in TodoManager service in src/todo_app/services/todo_manager.py
- [x] T015 [US1] Implement command parsing for 'add' and 'view' in CLI interface in src/todo_app/cli/cli_interface.py
- [x] T016 [US1] Implement CLI output formatting for task lists in src/todo_app/cli/cli_interface.py
- [x] T017 [US1] Integrate TodoManager with CLI interface for add/view functionality in src/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P2)

**Goal**: Enable users to modify existing tasks or remove completed tasks from their list through update and delete commands

**Independent Test**: Can be tested by adding tasks, updating their content or deleting them, then verifying the changes persist in the application.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Manual verification test for update command behavior per CLI contract
- [ ] T019 [P] [US2] Manual verification test for delete command behavior per CLI contract

### Implementation for User Story 2

- [x] T020 [US2] Implement update_task method in TodoManager service in src/todo_app/services/todo_manager.py
- [x] T021 [US2] Implement delete_task method in TodoManager service in src/todo_app/services/todo_manager.py
- [x] T022 [US2] Implement command parsing for 'update' and 'delete' in CLI interface in src/todo_app/cli/cli_interface.py
- [x] T023 [US2] Add validation for update command parameters in src/todo_app/cli/cli_interface.py
- [x] T024 [US2] Add validation for delete command parameters in src/todo_app/cli/cli_interface.py
- [x] T025 [US2] Integrate TodoManager with CLI interface for update/delete functionality in src/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks Complete (Priority: P3)

**Goal**: Enable users to mark tasks as complete to track their progress without removing them from the list

**Independent Test**: Can be tested by adding tasks, marking them complete, and verifying they show as completed while remaining visible.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T026 [P] [US3] Manual verification test for complete command behavior per CLI contract

### Implementation for User Story 3

- [x] T027 [US3] Implement mark_task_complete method in TodoManager service in src/todo_app/services/todo_manager.py
- [x] T028 [US3] Implement mark_task_pending method in TodoManager service in src/todo_app/services/todo_manager.py
- [x] T029 [US3] Implement command parsing for 'complete' in CLI interface in src/todo_app/cli/cli_interface.py
- [x] T030 [US3] Add validation for complete command parameters in src/todo_app/cli/cli_interface.py
- [x] T031 [US3] Update task display to show completion status in src/todo_app/cli/cli_interface.py
- [x] T032 [US3] Integrate TodoManager with CLI interface for complete functionality in src/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T033 [P] Add input validation and error handling for all commands in src/todo_app/cli/cli_interface.py
- [x] T034 [P] Implement error messages per CLI contract specification in src/todo_app/cli/cli_interface.py
- [x] T035 Add quit command functionality to CLI interface in src/todo_app/cli/cli_interface.py
- [x] T036 [P] Add edge case handling for invalid IDs, empty descriptions in src/todo_app/services/todo_manager.py
- [x] T037 Update main loop to handle quit command and gracefully exit in src/main.py
- [x] T038 [P] Documentation updates for usage instructions in README.md
- [x] T039 Run quickstart.md validation to ensure all commands work as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Manual verification test for add command behavior per CLI contract"
Task: "Manual verification test for view command behavior per CLI contract"

# Launch all models for User Story 1 together:
Task: "Implement Task class with id, title, completed attributes in src/todo_app/models/todo.py"
Task: "Implement TodoList class with tasks list and next_id counter in src/todo_app/models/todo.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
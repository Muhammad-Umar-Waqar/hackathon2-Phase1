# Data Model: Phase I: In-Memory Python Console Todo App

## Entities

### Task
Represents a single todo item in the application

- **id**: integer - Unique identifier for the task (auto-incremented)
- **title**: string - Brief description/title of the task
- **completed**: boolean - Status indicating whether the task is completed
- **created_at**: datetime - Timestamp when the task was created (optional)

### TodoList
Container for managing multiple tasks

- **tasks**: list<Task> - Collection of Task objects
- **next_id**: integer - Counter for assigning next available ID

## Validations

### Task Validations
- id must be unique within the TodoList
- title must not be empty or None
- completed must be a boolean value
- title must be a string with reasonable length limits (e.g., max 500 characters)

### TodoList Validations
- All tasks must have unique IDs
- No duplicate tasks allowed
- Operations must maintain data integrity

## State Transitions

### Task State Transitions
- Pending → Completed (when marked complete)
- Completed → Pending (when marked incomplete - optional feature)

## Relationships

- TodoList "contains" multiple Tasks (one-to-many relationship)
- Each Task belongs to exactly one TodoList (during its lifetime in memory)
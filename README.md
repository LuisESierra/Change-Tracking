# Change Tracking Skill

This is a Bionic skill designed to track meaningful modifications made to a project. It helps future agent runs understand what changed without having to reconstruct the entire development history.

## Features

- Records changes to project files in a structured changelog
- Maintains current project state documentation
- Tracks pending and completed tasks
- Provides insights into project evolution over time

## Usage

The Change Tracking skill can be used by importing the `ChangeTracker` class from `src.change_tracker` and using its methods to record changes, update project state, and manage TODO items.

## Structure

- `SKILL.md`: Main documentation for the skill
- `src/change_tracker.py`: Core functionality for tracking changes
- `.ai/CHANGELOG.md`: Contains the change history
- `.ai/PROJECT_STATE.md`: Contains current project status and architecture
- `.ai/TODO.md`: Contains pending tasks and work items

## Implementation Details

The skill maintains three key documentation files:
1. CHANGELOG.md - Records significant modifications with context
2. PROJECT_STATE.md - Tracks current project architecture, features, bugs, decisions, and status
3. TODO.md - Manages pending and completed tasks

This approach ensures that the history of meaningful changes is preserved and can be understood by future agents without needing to reconstruct the full development history.
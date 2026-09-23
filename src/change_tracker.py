"""
Change Tracker - A module to track meaningful modifications to project files.

This module provides functionality to:
- Monitor file changes
- Record significant modifications
- Maintain changelog entries
- Update project state documentation
"""

import os
import json
import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ChangeTracker:
    """A class to track and manage project changes."""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.changelog_path = self.project_root / ".ai" / "CHANGELOG.md"
        self.project_state_path = self.project_root / ".ai" / "PROJECT_STATE.md"
        self.todo_path = self.project_root / ".ai" / "TODO.md"
        
        # Ensure directories exist
        (self.project_root / ".ai").mkdir(exist_ok=True)
        
    def record_change(self, 
                     files: List[str], 
                     description: str, 
                     reason: str, 
                     impact: str,
                     status: str = "Completed") -> None:
        """
        Record a change in the changelog.
        
        Args:
            files: List of file paths that were changed
            description: Brief description of what was implemented or modified
            reason: Why the change was necessary
            impact: What behavior, architecture, dependency, or functionality was affected
            status: Status of the change (Completed/In Progress/Blocked)
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Format the changelog entry
        entry = f"""### {timestamp} — {description}

**Files:**
{chr(10).join([f'* `{file}`' for file in files])}

**Changed:**
{description}

**Reason:**
{reason}

**Impact:**
{impact}

**Status:**
{status}
"""
        
        # Append to changelog
        with open(self.changelog_path, 'a', encoding='utf-8') as f:
            f.write(f"\n{entry}")
            
    def update_project_state(self, 
                           architecture: str = "",
                           features: str = "",
                           bugs: str = "",
                           decisions: str = "",
                           status: str = "") -> None:
        """
        Update the project state documentation.
        
        Args:
            architecture: Current project architecture
            features: Current features
            bugs: Known bugs
            decisions: Key architectural decisions
            status: Overall project status
        """
        # Create or update PROJECT_STATE.md
        content = f"""# Project State

## Architecture
{architecture}

## Features
{features}

## Bugs
{bugs}

## Decisions
{decisions}

## Status
{status}
"""
        
        with open(self.project_state_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    def update_todo(self, 
                   tasks: List[Dict[str, str]], 
                   completed_tasks: List[Dict[str, str]] = None) -> None:
        """
        Update the TODO.md file with current tasks.
        
        Args:
            tasks: List of pending tasks
            completed_tasks: List of completed tasks (optional)
        """
        content = "# TODO\n\n"
        
        if tasks:
            content += "## Pending Tasks\n\n"
            for task in tasks:
                content += f"- [{task.get('status', ' ') or ' '}] {task['description']}\n"
                if 'assignee' in task:
                    content += f"  - Assignee: {task['assignee']}\n"
                if 'priority' in task:
                    content += f"  - Priority: {task['priority']}\n"
                content += "\n"
        
        if completed_tasks:
            content += "## Completed Tasks\n\n"
            for task in completed_tasks:
                content += f"- [x] {task['description']}\n"
                if 'assignee' in task:
                    content += f"  - Assignee: {task['assignee']}\n"
                content += "\n"
        
        with open(self.todo_path, 'w', encoding='utf-8') as f:
            f.write(content)


def main():
    """Main function for testing the change tracker."""
    # Create a change tracker instance
    tracker = ChangeTracker()
    
    # Example usage
    files = ["src/change_tracker.py", "SKILL.md"]
    description = "Initial implementation of Change Tracking skill"
    reason = "Need a mechanism to track meaningful modifications to project files"
    impact = "Provides foundation for understanding project evolution over time"
    
    tracker.record_change(files, description, reason, impact)
    
    # Update project state
    tracker.update_project_state(
        architecture="Bionic Skill structure",
        features="Change tracking functionality",
        bugs="None",
        decisions="Use markdown files for changelog and project state",
        status="Initial implementation complete"
    )
    
    # Update TODO
    tasks = [
        {
            "description": "Add automatic change detection",
            "status": " ",
            "priority": "High"
        },
        {
            "description": "Implement file diff analysis",
            "status": " ",
            "priority": "Medium"
        }
    ]
    
    tracker.update_todo(tasks)


if __name__ == "__main__":
    main()
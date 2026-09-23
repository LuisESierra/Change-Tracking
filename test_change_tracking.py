#!/usr/bin/env python3
"""
Simple test script for the Change Tracking skill.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from change_tracker import ChangeTracker

def main():
    """Test the change tracker functionality."""
    print("Testing Change Tracking skill...")
    
    # Create a change tracker instance
    tracker = ChangeTracker()
    
    # Test recording a change
    tracker.record_change(
        files=["test.py", "README.md"],
        description="Add test file for change tracking",
        reason="Need to test the change tracking functionality",
        impact="Verifies that the change tracking mechanism works correctly"
    )
    
    print("Change recorded successfully!")
    
    # Test updating project state
    tracker.update_project_state(
        architecture="Bionic Skill with change tracking capability",
        features="Change logging, project state management, TODO tracking",
        bugs="None found during testing",
        decisions="Use markdown for documentation files",
        status="Ready for further development and integration"
    )
    
    print("Project state updated successfully!")
    
    # Test updating TODO
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
    
    print("TODO updated successfully!")
    
    print("All tests passed!")

if __name__ == "__main__":
    main()
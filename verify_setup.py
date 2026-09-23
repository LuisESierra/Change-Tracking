#!/usr/bin/env python3
"""
Verification script for the Change Tracking skill setup.
"""

import os
import sys

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def verify_files_exist():
    """Verify all required files exist."""
    print("Verifying files exist...")
    
    required_files = [
        'SKILL.md',
        '.ai/CHANGELOG.md', 
        '.ai/PROJECT_STATE.md',
        '.ai/TODO.md',
        'src/change_tracker.py',
        'src/__init__.py'
    ]
    
    base_path = os.path.dirname(__file__)
    missing_files = []
    
    for file_path in required_files:
        full_path = os.path.join(base_path, file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)
            print(f"  [FAIL] Missing: {file_path}")
        else:
            print(f"  [PASS] Found: {file_path}")
    
    if missing_files:
        print(f"\n[FAIL] Missing files: {missing_files}")
        return False
    else:
        print("\n[PASS] All required files found!")
        return True

def verify_functionality():
    """Verify basic functionality."""
    print("\nVerifying functionality...")
    
    try:
        from change_tracker import ChangeTracker
        tracker = ChangeTracker()
        print("  [PASS] ChangeTracker class imported successfully")
        
        # Test that we can access the methods
        methods = ['record_change', 'update_project_state', 'update_todo']
        for method in methods:
            if hasattr(tracker, method):
                print(f"  [PASS] Method '{method}' found")
            else:
                print(f"  [FAIL] Method '{method}' not found")
                return False
                
        print("  [PASS] All functionality verified!")
        return True
        
    except Exception as e:
        print(f"  [FAIL] Error verifying functionality: {e}")
        return False

def main():
    """Main verification function."""
    print("=== Change Tracking Skill Verification ===\n")
    
    success = True
    success &= verify_files_exist()
    success &= verify_functionality()
    
    if success:
        print("\n[SUCCESS] All verifications passed! The Change Tracking skill is properly set up.")
        return 0
    else:
        print("\n[ERROR] Some verifications failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
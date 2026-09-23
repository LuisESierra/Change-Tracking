# Change Tracking

## Overview

The Change Tracking skill provides a mechanism to monitor and record meaningful modifications made to a project. This allows future agent runs to understand what changed without having to reconstruct the entire development history.

## Purpose

Track meaningful modifications made to the project so that future agent runs can understand what changed without having to reconstruct the entire development history.

## Features

- Records changes to project files
- Maintains a changelog of significant modifications
- Tracks project state and status
- Provides insights into project evolution over time

## Files

* `.ai/CHANGELOG.md` - Contains the change history
* `.ai/PROJECT_STATE.md` - Contains current project status and architecture
* `.ai/TODO.md` - Contains pending tasks and work items
* `src/change_tracker.py` - Core functionality for tracking changes

## Usage

The Change Tracking skill automatically records changes when files are modified. It maintains a structured changelog that can be used to understand the evolution of the project.

## Implementation

This skill works by monitoring file changes and updating the appropriate documentation files when significant modifications occur.
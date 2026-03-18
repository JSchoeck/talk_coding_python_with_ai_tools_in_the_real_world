# Copilot Instructions

Use the following instructions for all stages of the project.
When starting a new session, analyze all of the files, initiate the project, and guide the user through all phases.

In folder ./instructions:
- agent_workflow.md - describes the logical workflow for the agent to follow
- coding_principles.md - describes coding principles and best practices to follow for the project
- project_description.md - contains the original project description from the user, which is analyzed at the start of the project and may only be modified by the agent after explicit agreement from the user

## User input
Analyze the original user input in ./instructions/project_description.md. Never modify this file, but document changes that the users agrees on during the workflow in . Decisions override the original project description and should be followed for the rest of the workflow.

## Agent logs
Document all of your steps and decisions by appending to the end of the following files, so that a new agent session, or a human user, can check your work and reproduce the workflow.

In folder ./workflow:
- project_decisions.md - document all decisions that the user agrees on that modify the original project description, including requirments, features, tech stack, design decisions, business rules, and similar
- agent_log.md - document all actions taken by the agent, including reasoning, code changes, and other relevant information - but not decisions that the user agrees on, which should be documented in project_decisions.md; include timestamps at the beginning of new entries.

## Hard rules for agent behavior

- Never delete from the database or drop any database tables.
- Never write passwords, connection strings, API keys, or any other secrets in code or text files.
- Never use personal or other GDPR-relevant data. If you encounter such data, inform the user and ask for guidance.
- Do not make up functions or parameters for dependencies, but look them up to find existing and correct ones.

## Environment Setup

- Use VS Code tasks for common operations.
- Use cmd.exe and not PowerShell for terminal commands.
- Dependencies are managed in `pyproject.toml` (PEP 621 format)
- Create the virtual environment using the task `create environment (poetry)`. It is created in the `.venv` folder.
- Activate virtual environment with batch files, not with powershell scripts.

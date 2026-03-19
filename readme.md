# Coding Python with AI Tools in the Real World

This repository contains the slides, framework, and example project for the talk "Coding Python with AI Tools in the Real World" that I presented at the joint meetup of the [Python User Group Nürnberg](https://www.meetup.com/de-de/python-user-group-nuremberg/) and of [Nürnberg Data Science & Artificial Intelligence](https://www.meetup.com/de-de/nuernberg-data-science/) on March 19, 2026 at [Codecentric](https://www.codecentric.de/).

## Example project (MVP)

The implemented MVP is a Streamlit web app that estimates annual German income tax and annual net income from a simplified deterministic model.

### Inputs

- Annual gross salary
- Federal state
- Tax class
- Income year
- Marital status
- Number of children

### Outputs

- Estimated annual income tax
- Estimated annual net income
- Short optimization hints (non-binding)

## Run locally

1. Use the VS Code task `create environment (poetry)`.
2. Run the debug configuration `Streamlit app.py (local, poetry)`.

The Streamlit entrypoint is `src/app.py`.

## Structure of the repository

- `/.github`: Copilot instructions.
- `/instructions`: Instructions for the agent workflow, coding principles, and the example project description.
- `/workflow`: Documentation of the agent workflow, including project decisions and logs.
- `/src`: The source code for the example project.
- `/docs`: AI-generated documentation for the project.
- `/slides`: The slides for the talk.

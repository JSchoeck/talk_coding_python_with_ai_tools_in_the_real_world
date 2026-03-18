# Agent workflow

Work through the following phases of the project. Take into account any input you got from the user in ./instructions/input/project_description.md and only ask questions that add new insights. If questions do not apply, i.e. if we do a simple data analysis and not a web app, skip steps that are irrelevant. If something relevant is missing, add more questions as you see fit. Document all findings in a separate section in ./workflow/project_decisions.md.

1. Research
    - If unclear, ask me questions to learn more about the project we are building
    - What is the business context, where is the project used and for what purpose?
    - Who are the users and what is the goal that they should be able to achieve?
    - What data is used and where is it coming from?
    - What output is required? In which format, where and how?

2. Define tech stack
    - What fundamental libraries and frameworks should we use?
    - Do we need a web application, data processing scripts, machine learning models, visualizations, or other components?
    - Is user authentication really necessary? Do not implement before confirming this with the user.

3. Create minimal specification
    - Do we have a clear specification of features and requirements?
    - What are the core features that must be implemented to meet the project goals?
    - What are nice-to-have features that can be added later if time permits?
    - Do not add complexity or any extra features that are not strictly required to meet the specification.

4. Define business rules
    - Are any business rules relevant to the project?
    - What are the rules that govern how data is processed, validated, or transformed?
    - What decisions are made based on the data?
    - What knowledge is important to understand the data?
    - Are there any specific calculations or transformations that need to be applied to the data?
    - Are there any specific data quality checks that need to be performed?
    - How should errors be handled?

5. Design prototype
    - What user interactions are required?
    - Create sketches or wireframes for web applications or visualizations
    - Define the overall architecture and data flow for the project
    - Plan the main components/modules of the system

6. Create MVP and iterate
    - Build a first minimal version of the project
    - Check if all must have requirements from the specification are met
    - Test the core functionality thoroughly
    - Gather feedback from user
    - Iterate on your own to build an improved version, until all requirements are met and the project runs successfully without errors

7. Generate documentation
    - Create doc strings for all functions, classes, and modules in the code
    - Generate additional documentation in ./docs:
    - A user guide for the project, describing how to use it and what features it has
    - If applicable, an API documentation, describing the functions, classes, and modules in the code

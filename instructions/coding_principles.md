# Coding Rules

## Python Conventions

- Follow **PEP 8** style guidelines
- **Naming**: `snake_case` for variables/functions, `CamelCase` for classes
- **Type hints**: Always include for function parameters, return types, class properties, and global variables
- **Docstrings**: Required for all public modules, classes, functions, and methods
- **Comments**: Explain important parts, complex operations and hard-to-read code (e.g. regex)

## Internal Coding Principles

- Use an isolated virtual environment created with poetry in the local folder.
- Have a clear structure and one file that contains the overall processing logic (e.g. `main.py` or `main.ipynb`).
- Write high level documentation first, then write the code. Have the documentation describe what happens step by step in your main processing file.
- Optimize code for readability, not for highest performance. If you write complex code for performance, comment it well.
- Comment the crucial steps in your code, but not trivial steps.
- Use variable and function names that everyone can easily understand (e.g. `df_sales_ltm_per_day` instead of `df_sales_1`).

## Optimization

- Prefer vectorized operations over loops when working with data (with numpy, polars, pandas).
- Use efficient data structures (e.g., sets for membership tests, dictionaries for lookups).
- Increase performance by using caching for expensive function calls with `functools.cache` where applicable.
- When processing or loading large amounts of data, make sure to cache intermediate results to avoid re-computation and re-loading. Use feather files for caching dataframes.
- When changing existing code, change as little as possible to achieve the goal. Do not move code into new functions or classes, or refactor in another way, unless the user agrees to your proposal.
- When optimizing code for performance, ensure that readability is not significantly compromised. Always comment complex optimizations.

## Structure

- Put all configuration values (e.g. file paths, constants) in a separate `config.py` file
- Put parameters and settings (e.g. scaling factors, categories) in `settings.yaml`
- Use data classes for structured data and collections of input parameters.

## Notebooks

- Use notebooks for exploration, prototyping, and visualization, unless building a function or web app.
- Use marimo or jupyter notebooks - ask the user for their preference.
- Keep notebooks organized with clear headings and sections.
- Put functions and reusable code into separate .py files and import them into the notebook.
- Add proper explanatory text and comments to make the notebook understandable for others.
- Save notebooks regularly and use version control if possible.
- Use the local virtual environment to run notebooks to ensure consistent dependencies.
- After implementing new cells at the bottom of the notebook, run the new cells. If changing previous cells, run the whole notebook to ensure everything works as expected.

## Logging

- Add logging where it makes sense to debug and monitor applications.
- Set the logging level to INFO or DEBUG depending on the use case.
- Log important steps in the processing, including start and end of major functions or processes.

## Libraries and frameworks

- For data manipulation, prefer pandas.
- For machine learning, prefer scikit-learn.
- For web applications, prefer Streamlit.
- For data visualization, prefer hvplot and bokeh.
- Check which dependencies are available in the virtual environment at the start of the project. When adding new ones, check if they are already available and ask user before installing anything.
- When adding new dependencies, ensure they are well-maintained and widely used in the community.
- For unit testing, use pytest as much as possible and only use mocking if it is absolutely necessary.

## Agent behavior

- Unless specified otherwise, do not implement code changes, but only suggest them and ask if they should be implemented.
- Do not delete user written code, unless the user confirms its removal.
- If you need to implement code that would be suitable to be reused in other requests or projects, suggest to the user to create a Copilot skill. Co-develop this skill with the user if they agree and then use it in the current request.

## Testing and validation

- After implementing new code, create new tests, asking the user for edge cases that would be important to cover. Use the business rules defined in the documentation to create meaningful test cases.
- Use pytest for unit tests and aim for high code coverage of critical components.
- When modifying existing code, run all existing unit tests to ensure nothing is broken.
- When working with data, validate the data at crucial steps in the processing pipeline to ensure data quality and correctness.
- Do not add unnecessary data validation steps in functions. If the function has good type hints, trust that the user will pass the correct data.
- For web apps, test them locally after changes using the debug configuration `Streamlit app.py (local, poetry)`.
- If it is just a local script or module, run it normally with the local virtual environment.

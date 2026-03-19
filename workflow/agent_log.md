## 2026-03-19 19:12:42

- Started MVP implementation based on confirmed scope from user.
- Added decision documentation to `workflow/project_decisions.md`.
- Updated `pyproject.toml` project metadata and added runtime dependencies: `streamlit`, `pyyaml`.
- Implemented settings/config loading in `src/config.py` with typed settings model and cached YAML loading.
- Added deterministic tax model parameters in `src/settings.yaml`.
- Implemented calculator logic and dataclass input model in `src/tax_calculator.py`.
- Built Streamlit UI in `src/app.py` with required input fields, result metrics, hints, and minimal yellow/blue accent styling.
- Added package marker `src/__init__.py`.
- Added focused tests in `tests/test_tax_calculator.py`.
- Added user documentation in `docs/user_guide.md` and updated `readme.md` for MVP usage.
- Resolved type and lint errors; applied import ordering fixes with Ruff.
- Validation: `poetry run python -m pytest tests/test_tax_calculator.py -q` passed (`4 passed`).
- Added pytest config in `pyproject.toml` (`[tool.pytest.ini_options] pythonpath = ["."]`) to ensure direct `poetry run pytest` path resolution.
- Final validation: `poetry run pytest tests/test_tax_calculator.py -q` passed (`4 passed`).

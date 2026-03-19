"""Configuration helpers for the Streamlit tax MVP app."""

from __future__ import annotations

from functools import cache
from pathlib import Path
from typing import TypedDict, cast

import yaml


class AppSettings(TypedDict):
    """Typed structure for application settings."""

    supported_years: list[int]
    base_rate_by_year: dict[int, float]
    tax_class_adjustments: dict[str, float]
    state_adjustments: dict[str, float]
    married_allowance: float
    child_allowance_per_child: float
    max_children_for_allowance: int
    min_effective_tax_rate: float
    max_effective_tax_rate: float


BASE_DIR: Path = Path(__file__).resolve().parent.parent
SETTINGS_PATH: Path = BASE_DIR / "src" / "settings.yaml"


@cache
def load_settings() -> AppSettings:
    """Load application settings from YAML."""
    with SETTINGS_PATH.open("r", encoding="utf-8") as settings_file:
        raw_settings = yaml.safe_load(settings_file)

    if not isinstance(raw_settings, dict):
        raise ValueError("Invalid settings format. Expected a dictionary in settings.yaml.")

    loaded_settings: AppSettings = cast(AppSettings, raw_settings)
    return loaded_settings

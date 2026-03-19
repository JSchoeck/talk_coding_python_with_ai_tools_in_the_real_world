"""Tax calculation logic for the German income tax Streamlit MVP."""

from __future__ import annotations

from dataclasses import dataclass

from src.config import load_settings

HIGH_INCOME_HINT_THRESHOLD: float = 75000.0


@dataclass(frozen=True)
class TaxInput:
    """Input parameters for the deterministic tax estimate."""

    annual_salary: float
    federal_state: str
    tax_class: str
    income_year: int
    is_married: bool
    number_of_children: int


def _build_effective_tax_rate(tax_input: TaxInput) -> float:
    """Build an effective tax rate from configured factors."""
    settings = load_settings()

    base_rate_by_year = settings["base_rate_by_year"]
    tax_class_adjustments = settings["tax_class_adjustments"]
    state_adjustments = settings["state_adjustments"]

    base_rate: float = float(base_rate_by_year[tax_input.income_year])
    class_adjustment: float = float(tax_class_adjustments[tax_input.tax_class])
    state_adjustment: float = float(state_adjustments[tax_input.federal_state])

    effective_tax_rate: float = base_rate + class_adjustment + state_adjustment
    min_rate: float = float(settings["min_effective_tax_rate"])
    max_rate: float = float(settings["max_effective_tax_rate"])

    return min(max(effective_tax_rate, min_rate), max_rate)


def _calculate_taxable_income(tax_input: TaxInput) -> float:
    """Calculate taxable income after simplified allowances."""
    settings = load_settings()

    married_allowance: float = float(settings["married_allowance"])
    child_allowance_per_child: float = float(settings["child_allowance_per_child"])
    max_children_for_allowance: int = int(settings["max_children_for_allowance"])

    total_allowance: float = 0.0
    if tax_input.is_married:
        total_allowance += married_allowance

    children_for_allowance: int = min(tax_input.number_of_children, max_children_for_allowance)
    total_allowance += children_for_allowance * child_allowance_per_child

    return max(tax_input.annual_salary - total_allowance, 0.0)


def calculate_estimated_tax(tax_input: TaxInput) -> float:
    """Calculate estimated annual income tax."""
    taxable_income: float = _calculate_taxable_income(tax_input)
    effective_tax_rate: float = _build_effective_tax_rate(tax_input)
    return round(taxable_income * effective_tax_rate, 2)


def calculate_estimated_net_income(tax_input: TaxInput) -> float:
    """Calculate estimated annual net income."""
    estimated_tax: float = calculate_estimated_tax(tax_input)
    return round(max(tax_input.annual_salary - estimated_tax, 0.0), 2)


def build_optimization_hints(tax_input: TaxInput) -> list[str]:
    """Create simple non-binding optimization hints for the user."""
    hints: list[str] = []

    if not tax_input.is_married and tax_input.tax_class in {"I", "IV"}:
        hints.append(
            "If your personal situation changes (for example marriage), check if a different tax class may lower your withholding."
        )

    if tax_input.number_of_children == 0:
        hints.append("If you have children, verify eligibility for child-related tax benefits.")

    if tax_input.annual_salary > HIGH_INCOME_HINT_THRESHOLD:
        hints.append("At higher income levels, documented deductible expenses can significantly impact taxable income.")

    if not hints:
        hints.append("Review deductible costs annually and keep records to improve your tax position.")

    return hints

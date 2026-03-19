"""Unit tests for deterministic tax calculator logic."""

from __future__ import annotations

import pytest

from src import tax_calculator

EXPECTED_BASELINE_TAX: float = 12100.0


def test_calculate_estimated_tax_baseline_case() -> None:
    """Calculate tax for a baseline scenario with no allowances."""
    tax_input = tax_calculator.TaxInput(
        annual_salary=50000.0,
        federal_state="Bavaria",
        tax_class="I",
        income_year=2026,
        is_married=False,
        number_of_children=0,
    )

    calculated_tax: float = tax_calculator.calculate_estimated_tax(tax_input)
    assert calculated_tax == pytest.approx(EXPECTED_BASELINE_TAX)


def test_allowances_reduce_tax_for_married_with_children() -> None:
    """Reduce taxable income when married and with children."""
    single_input = tax_calculator.TaxInput(
        annual_salary=60000.0,
        federal_state="Berlin",
        tax_class="I",
        income_year=2025,
        is_married=False,
        number_of_children=0,
    )
    family_input = tax_calculator.TaxInput(
        annual_salary=60000.0,
        federal_state="Berlin",
        tax_class="I",
        income_year=2025,
        is_married=True,
        number_of_children=2,
    )

    assert tax_calculator.calculate_estimated_tax(family_input) < tax_calculator.calculate_estimated_tax(single_input)


def test_estimated_net_income_is_salary_minus_tax() -> None:
    """Ensure net income is computed as salary minus estimated tax."""
    tax_input = tax_calculator.TaxInput(
        annual_salary=70000.0,
        federal_state="Hamburg",
        tax_class="IV",
        income_year=2024,
        is_married=True,
        number_of_children=1,
    )

    estimated_tax: float = tax_calculator.calculate_estimated_tax(tax_input)
    estimated_net_income: float = tax_calculator.calculate_estimated_net_income(tax_input)

    assert estimated_net_income == round(70000.0 - estimated_tax, 2)


def test_optimization_hints_include_child_benefit_hint_when_no_children() -> None:
    """Include child hint when the input has no children."""
    tax_input = tax_calculator.TaxInput(
        annual_salary=45000.0,
        federal_state="Hesse",
        tax_class="I",
        income_year=2024,
        is_married=False,
        number_of_children=0,
    )

    hints: list[str] = tax_calculator.build_optimization_hints(tax_input)
    assert any("children" in hint.lower() for hint in hints)

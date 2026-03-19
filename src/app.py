"""Streamlit MVP app for deterministic German income tax estimation."""

from __future__ import annotations

import streamlit as st

from src.config import load_settings
from src.tax_calculator import (
    TaxInput,
    build_optimization_hints,
    calculate_estimated_net_income,
    calculate_estimated_tax,
)


def _render_header() -> None:
    """Render app title and disclaimer."""
    st.set_page_config(page_title="German Tax MVP", page_icon="💶", layout="centered")
    st.markdown(
        """
        <style>
            .mvp-banner {
                background: linear-gradient(90deg, #3776ab 0%, #ffde57 100%);
                color: #0f172a;
                padding: 0.75rem 1rem;
                border-radius: 0.5rem;
                font-weight: 600;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="mvp-banner">German Income Tax Estimator (MVP)</div>', unsafe_allow_html=True)
    st.caption("This app uses a simplified deterministic model and does not replace official tax advice.")


def _build_tax_input() -> TaxInput:
    """Collect user inputs and build a tax input object."""
    settings = load_settings()

    supported_years: list[int] = [int(value) for value in settings["supported_years"]]
    available_states: list[str] = list(settings["state_adjustments"].keys())
    tax_classes: list[str] = list(settings["tax_class_adjustments"].keys())

    annual_salary: float = st.number_input("Annual gross salary (€)", min_value=0.0, value=50000.0, step=1000.0)
    federal_state: str = st.selectbox("Federal state", options=available_states)
    tax_class: str = st.selectbox("Tax class", options=tax_classes, index=0)
    income_year: int = st.selectbox("Income year", options=supported_years, index=len(supported_years) - 1)
    is_married: bool = st.checkbox("Married", value=False)
    number_of_children: int = int(st.number_input("Number of children", min_value=0, max_value=10, value=0, step=1))

    return TaxInput(
        annual_salary=annual_salary,
        federal_state=federal_state,
        tax_class=tax_class,
        income_year=income_year,
        is_married=is_married,
        number_of_children=number_of_children,
    )


def main() -> None:
    """Run the Streamlit app."""
    _render_header()
    tax_input: TaxInput = _build_tax_input()

    if st.button("Calculate", type="primary"):
        estimated_tax: float = calculate_estimated_tax(tax_input)
        estimated_net_income: float = calculate_estimated_net_income(tax_input)

        st.subheader("Result")
        st.metric(label="Estimated annual income tax", value=f"€ {estimated_tax:,.2f}")
        st.metric(label="Estimated annual net income", value=f"€ {estimated_net_income:,.2f}")

        st.subheader("Optimization hints")
        for hint in build_optimization_hints(tax_input):
            st.write(f"- {hint}")


if __name__ == "__main__":
    main()

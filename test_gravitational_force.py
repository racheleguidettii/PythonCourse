import pytest
from gravitational_force import gravitational_force

def test_gravitational_force_unit():
    """Unit test for the gravitational_force function."""
    assert gravitational_force(1.0, 1.0, 1.0) == pytest.approx(6.67430e-11, rel=1e-2)

def test_gravitational_force_regression():
    """Regression test to check if the gravitational_force function still returns correct results."""
    # Known test cases (previously passed, kept for regression)
    assert gravitational_force(1.0, 1.0, 1.0) == pytest.approx(6.67430e-11, rel=1e-2)

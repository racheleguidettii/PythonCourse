import pytest
from gravitational_force import gravitational_force

def test_gravitational_force_unit():
    """Unit test for the gravitational_force function."""
    # Testing a case with simple, easy-to-calculate values
    result = gravitational_force(10.0, 20.0, 2.0)  # Expected: G * (10 * 20) / (2^2)
    expected = 6.67430e-11 * (10 * 20) / (2 ** 2)
    assert result == pytest.approx(expected, rel=1e-5)

def test_gravitational_force_regression():
    """Regression test for gravitational_force using a previously verified result."""
    # Known values from past tests (e.g., stored in documentation or logs)
    result = gravitational_force(5.0, 5.0, 1.0)  # Known result: G * (5 * 5) / 1^2
    expected = 6.67430e-11 * (5 * 5) / (1 ** 2)
    assert result == pytest.approx(expected, rel=1e-5)


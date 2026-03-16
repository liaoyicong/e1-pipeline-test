"""
Test module for calculator.py

This module contains unit tests for the calculator module to ensure
all operations work correctly and error handling is implemented properly.
"""

import calculator


def test_add():
    """Test addition function."""
    assert calculator.add(5, 3) == 8
    assert calculator.add(-1, 1) == 0
    assert calculator.add(2.5, 1.5) == 4.0
    assert calculator.add(0, 0) == 0
    print("✓ Add function tests passed")


def test_subtract():
    """Test subtraction function."""
    assert calculator.subtract(10, 3) == 7
    assert calculator.subtract(5, 5) == 0
    assert calculator.subtract(-2, -5) == 3
    assert calculator.subtract(5.5, 2.5) == 3.0
    print("✓ Subtract function tests passed")


def test_multiply():
    """Test multiplication function."""
    assert calculator.multiply(4, 5) == 20
    assert calculator.multiply(-3, 4) == -12
    assert calculator.multiply(0, 100) == 0
    assert calculator.multiply(2.5, 3) == 7.5
    print("✓ Multiply function tests passed")


def test_divide():
    """Test division function."""
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(7, 4) == 1.75
    assert calculator.divide(-8, 2) == -4.0
    assert calculator.divide(0, 5) == 0.0
    print("✓ Divide function tests passed")


def test_divide_by_zero():
    """Test division by zero error handling."""
    try:
        calculator.divide(10, 0)
        assert False, "Expected ZeroDivisionError was not raised"
    except ZeroDivisionError as e:
        assert str(e) == "Cannot divide by zero"
        print("✓ Division by zero error handling test passed")


def test_calculate_function():
    """Test the generic calculate function."""
    assert calculator.calculate('add', 5, 3) == 8
    assert calculator.calculate('subtract', 10, 4) == 6
    assert calculator.calculate('multiply', 3, 7) == 21
    assert calculator.calculate('divide', 15, 3) == 5.0
    print("✓ Calculate function tests passed")


def test_invalid_operation():
    """Test error handling for invalid operations."""
    try:
        calculator.calculate('invalid', 1, 2)
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert "Unsupported operation: invalid" in str(e)
        print("✓ Invalid operation error handling test passed")


def run_all_tests():
    """Run all tests."""
    print("Running Calculator Module Tests")
    print("=" * 35)

    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
    test_calculate_function()
    test_invalid_operation()

    print("\n🎉 All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()
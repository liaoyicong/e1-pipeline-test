"""
Example usage of the calculator module.

This file demonstrates how to use the calculator module in different ways,
including the new class-based structure and type validation.
"""

import calculator
from calculator import Calculator

def main():
    """Demonstrate calculator usage."""
    print("Calculator Module Usage Examples")
    print("=" * 35)

    # Using individual functions
    print("\n1. Using individual functions:")
    print(f"5 + 3 = {calculator.add(5, 3)}")
    print(f"10 - 4 = {calculator.subtract(10, 4)}")
    print(f"6 × 7 = {calculator.multiply(6, 7)}")
    print(f"15 ÷ 3 = {calculator.divide(15, 3)}")

    # Using the generic calculate function
    print("\n2. Using the generic calculate function:")
    operations = [
        ('add', 12, 8),
        ('subtract', 20, 5),
        ('multiply', 4, 9),
        ('divide', 24, 6)
    ]

    for op, a, b in operations:
        result = calculator.calculate(op, a, b)
        symbol = {
            'add': '+',
            'subtract': '-',
            'multiply': '×',
            'divide': '÷'
        }[op]
        print(f"{a} {symbol} {b} = {result}")

    # Error handling examples
    print("\n3. Error handling examples:")

    # Division by zero
    try:
        result = calculator.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Division by zero: {e}")

    # Invalid operation
    try:
        result = calculator.calculate('power', 2, 3)
    except ValueError as e:
        print(f"Invalid operation: {e}")

    # Working with floats
    print("\n4. Working with decimal numbers:")
    print(f"3.14 + 2.86 = {calculator.add(3.14, 2.86)}")
    print(f"10.5 ÷ 2.1 = {calculator.divide(10.5, 2.1):.2f}")

    # Class-based usage (new approach)
    print("\n5. Using the Calculator class:")
    calc = Calculator()
    print(f"Using class instance:")
    print(f"8 + 7 = {calc.add(8, 7)}")
    print(f"20 - 6 = {calc.subtract(20, 6)}")
    print(f"5 × 4 = {calc.multiply(5, 4)}")
    print(f"18 ÷ 3 = {calc.divide(18, 3)}")
    print(f"Generic method: {calc.calculate('add', 15, 25)}")

    # Type validation examples
    print("\n6. Type validation examples:")
    calc = Calculator()

    # Valid types
    print(f"Integer + Float: {calc.add(5, 3.5)}")

    # Invalid types (will raise errors)
    print("Testing invalid input types:")

    invalid_inputs = [
        ("string + number", lambda: calc.add("5", 3)),
        ("list + number", lambda: calc.subtract([1, 2], 3)),
        ("None × number", lambda: calc.multiply(None, 4)),
        ("dict ÷ number", lambda: calc.divide({"x": 1}, 2)),
        ("non-string operation", lambda: calc.calculate(123, 5, 3))
    ]

    for description, operation in invalid_inputs:
        try:
            result = operation()
            print(f"  {description}: Unexpected success - {result}")
        except (TypeError, ValueError) as e:
            print(f"  {description}: ✓ Caught expected error - {type(e).__name__}")

if __name__ == "__main__":
    main()
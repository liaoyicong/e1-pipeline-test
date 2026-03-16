"""
Example usage of the calculator module.

This file demonstrates how to use the calculator module in different ways.
"""

import calculator

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

if __name__ == "__main__":
    main()
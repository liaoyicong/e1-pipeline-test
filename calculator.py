"""
Calculator Module

A simple calculator module providing basic arithmetic operations with proper error handling.

This module provides four basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division (with division by zero error handling)

Example usage:
    >>> import calculator
    >>> calculator.add(5, 3)
    8
    >>> calculator.divide(10, 2)
    5.0
    >>> calculator.divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Cannot divide by zero
"""


def add(a, b):
    """
    Add two numbers.

    Args:
        a (int|float): First number
        b (int|float): Second number

    Returns:
        int|float: Sum of a and b

    Example:
        >>> add(5, 3)
        8
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.

    Args:
        a (int|float): Number to subtract from
        b (int|float): Number to subtract

    Returns:
        int|float: Difference of a and b (a - b)

    Example:
        >>> subtract(10, 3)
        7
        >>> subtract(5.5, 2.5)
        3.0
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int|float): First number
        b (int|float): Second number

    Returns:
        int|float: Product of a and b

    Example:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 3)
        7.5
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number.

    Args:
        a (int|float): Dividend (number to be divided)
        b (int|float): Divisor (number to divide by)

    Returns:
        float: Quotient of a and b (a / b)

    Raises:
        ZeroDivisionError: If divisor (b) is zero

    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 3)
        2.3333333333333335
        >>> divide(10, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Cannot divide by zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# Convenience function for interactive use
def calculate(operation, a, b):
    """
    Perform a calculation based on the specified operation.

    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
        a (int|float): First number
        b (int|float): Second number

    Returns:
        int|float: Result of the operation

    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If dividing by zero

    Example:
        >>> calculate('add', 5, 3)
        8
        >>> calculate('divide', 10, 2)
        5.0
        >>> calculate('invalid', 1, 2)
        Traceback (most recent call last):
            ...
        ValueError: Unsupported operation: invalid
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](a, b)


if __name__ == "__main__":
    # Simple interactive demonstration
    print("Calculator Module Demo")
    print("======================")

    # Test all operations
    test_cases = [
        ('add', 10, 5),
        ('subtract', 10, 5),
        ('multiply', 10, 5),
        ('divide', 10, 5),
        ('divide', 10, 2),
    ]

    for op, x, y in test_cases:
        try:
            result = calculate(op, x, y)
            print(f"{op}({x}, {y}) = {result}")
        except Exception as e:
            print(f"{op}({x}, {y}) = Error: {e}")

    # Test division by zero
    print("\nTesting division by zero:")
    try:
        result = divide(10, 0)
        print(f"divide(10, 0) = {result}")
    except ZeroDivisionError as e:
        print(f"divide(10, 0) = Error: {e}")
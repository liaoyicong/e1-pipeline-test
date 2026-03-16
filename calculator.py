"""
Calculator Module

A simple calculator module providing basic arithmetic operations with proper error handling.

This module provides four basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division (with division by zero error handling)

The module includes proper type validation and a clean class-based structure.

Example usage:
    >>> from calculator import Calculator
    >>> calc = Calculator()
    >>> calc.add(5, 3)
    8
    >>> calc.divide(10, 2)
    5.0
    >>> calc.divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Cannot divide by zero
"""


class Calculator:
    """
    A calculator class providing basic arithmetic operations with proper error handling.

    This class implements four basic arithmetic operations (add, subtract, multiply, divide)
    with comprehensive type validation and error handling.
    """

    def __init__(self):
        """Initialize the Calculator instance."""
        pass

    def _validate_input(self, *args):
        """
        Validate that all arguments are numeric types (int or float).

        Args:
            *args: Variable number of arguments to validate

        Raises:
            TypeError: If any argument is not a number
        """
        for i, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argument {i+1} must be a number (int or float), got {type(arg).__name__}")

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a (int|float): First number
            b (int|float): Second number

        Returns:
            int|float: Sum of a and b

        Raises:
            TypeError: If arguments are not numeric

        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
            >>> calc.add(2.5, 1.5)
            4.0
        """
        self._validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        """
        Subtract second number from first number.

        Args:
            a (int|float): Number to subtract from
            b (int|float): Number to subtract

        Returns:
            int|float: Difference of a and b (a - b)

        Raises:
            TypeError: If arguments are not numeric

        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7
            >>> calc.subtract(5.5, 2.5)
            3.0
        """
        self._validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (int|float): First number
            b (int|float): Second number

        Returns:
            int|float: Product of a and b

        Raises:
            TypeError: If arguments are not numeric

        Example:
            >>> calc = Calculator()
            >>> calc.multiply(4, 5)
            20
            >>> calc.multiply(2.5, 3)
            7.5
        """
        self._validate_input(a, b)
        return a * b

    def divide(self, a, b):
        """
        Divide first number by second number.

        Args:
            a (int|float): Dividend (number to be divided)
            b (int|float): Divisor (number to divide by)

        Returns:
            float: Quotient of a and b (a / b)

        Raises:
            TypeError: If arguments are not numeric
            ZeroDivisionError: If divisor (b) is zero

        Example:
            >>> calc = Calculator()
            >>> calc.divide(10, 2)
            5.0
            >>> calc.divide(7, 3)
            2.3333333333333335
            >>> calc.divide(10, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: Cannot divide by zero
        """
        self._validate_input(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def calculate(self, operation, a, b):
        """
        Perform a calculation based on the specified operation.

        Args:
            operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
            a (int|float): First number
            b (int|float): Second number

        Returns:
            int|float: Result of the operation

        Raises:
            TypeError: If arguments are not numeric or operation is not a string
            ValueError: If operation is not supported
            ZeroDivisionError: If dividing by zero

        Example:
            >>> calc = Calculator()
            >>> calc.calculate('add', 5, 3)
            8
            >>> calc.calculate('divide', 10, 2)
            5.0
            >>> calc.calculate('invalid', 1, 2)
            Traceback (most recent call last):
                ...
            ValueError: Unsupported operation: invalid
        """
        if not isinstance(operation, str):
            raise TypeError(f"Operation must be a string, got {type(operation).__name__}")

        operations = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }

        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")

        return operations[operation](a, b)


# Create a default instance for backward compatibility
_calculator_instance = Calculator()

# Function-based API for backward compatibility
def add(a, b):
    """Add two numbers (backward compatibility function)."""
    return _calculator_instance.add(a, b)

def subtract(a, b):
    """Subtract two numbers (backward compatibility function)."""
    return _calculator_instance.subtract(a, b)

def multiply(a, b):
    """Multiply two numbers (backward compatibility function)."""
    return _calculator_instance.multiply(a, b)

def divide(a, b):
    """Divide two numbers (backward compatibility function)."""
    return _calculator_instance.divide(a, b)

def calculate(operation, a, b):
    """Perform calculation (backward compatibility function)."""
    return _calculator_instance.calculate(operation, a, b)


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
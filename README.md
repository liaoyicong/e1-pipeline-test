# e1-pipeline-test
E1 full pipeline test repo — auto-created by E1 daemon

## Calculator Module

This repository now includes a Python calculator module with basic arithmetic operations.

### Features

- **Four basic operations**: addition, subtraction, multiplication, division
- **Class-based structure**: Clean, object-oriented design with Calculator class
- **Type validation**: Comprehensive input validation with descriptive error messages
- **Proper error handling**: Division by zero protection and invalid input handling
- **Well-documented**: Comprehensive docstrings and examples for all methods
- **Type flexible**: Works with both integers and floating-point numbers
- **Backward compatible**: Function-based API still available for existing code
- **Clean API**: Both class-based and function-based interfaces

### Files

- `calculator.py` - Main calculator module with all arithmetic functions
- `test_calculator.py` - Comprehensive test suite to verify functionality
- `example_usage.py` - Usage examples and demonstrations

### Quick Usage

#### Class-based approach (recommended):
```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(6, 7)   # 42
result = calc.divide(15, 3)    # 5.0

# Generic method
result = calc.calculate('add', 5, 3)  # 8

# Error handling
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero

# Type validation
try:
    result = calc.add("5", 3)  # Will raise TypeError
except TypeError as e:
    print(f"Error: {e}")  # Error: Argument 1 must be a number
```

#### Function-based approach (backward compatibility):
```python
import calculator

# Basic operations
result = calculator.add(5, 3)        # 8
result = calculator.subtract(10, 4)  # 6
result = calculator.multiply(6, 7)   # 42
result = calculator.divide(15, 3)    # 5.0

# Generic function
result = calculator.calculate('add', 5, 3)  # 8
```

### Running Tests

```bash
python test_calculator.py
```

### Examples

```bash
python example_usage.py
python calculator.py  # Built-in demo
```

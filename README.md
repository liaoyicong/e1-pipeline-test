# e1-pipeline-test
E1 full pipeline test repo — auto-created by E1 daemon

## Calculator Module

This repository now includes a Python calculator module with basic arithmetic operations.

### Features

- **Four basic operations**: addition, subtraction, multiplication, division
- **Proper error handling**: Division by zero protection with descriptive error messages
- **Well-documented**: Comprehensive docstrings and examples for all functions
- **Type flexible**: Works with both integers and floating-point numbers
- **Clean API**: Individual functions for each operation plus a generic calculate function

### Files

- `calculator.py` - Main calculator module with all arithmetic functions
- `test_calculator.py` - Comprehensive test suite to verify functionality
- `example_usage.py` - Usage examples and demonstrations

### Quick Usage

```python
import calculator

# Basic operations
result = calculator.add(5, 3)        # 8
result = calculator.subtract(10, 4)  # 6
result = calculator.multiply(6, 7)   # 42
result = calculator.divide(15, 3)    # 5.0

# Generic function
result = calculator.calculate('add', 5, 3)  # 8

# Error handling
try:
    result = calculator.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero
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

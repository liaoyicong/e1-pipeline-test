# e1-pipeline-test
E1 完整流水线测试仓库 — 由 E1 守护进程自动创建

## 计算器模块

此仓库现在包含一个提供基本算术运算的 Python 计算器模块。

### 特性

- **四种基本运算**：加法、减法、乘法、除法
- **基于类的结构**：具有 Calculator 类的清晰面向对象设计
- **类型验证**：具有描述性错误消息的全面输入验证
- **正确的错误处理**：除零保护和无效输入处理
- **文档完整**：为所有方法提供全面的文档字符串和示例
- **类型灵活**：同时支持整数和浮点数
- **向后兼容**：基于函数的 API 仍可用于现有代码
- **简洁的 API**：同时提供基于类和基于函数的接口

### 文件

- `calculator.py` - 包含所有算术函数的主计算器模块
- `test_calculator.py` - 验证功能的综合测试套件
- `example_usage.py` - 用法示例和演示

### 快速使用

#### 基于类的方法（推荐）：
```python
from calculator import Calculator

# 创建计算器实例
calc = Calculator()

# 基本运算
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(6, 7)   # 42
result = calc.divide(15, 3)    # 5.0

# 通用方法
result = calc.calculate('add', 5, 3)  # 8

# 错误处理
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Error: Cannot divide by zero

# 类型验证
try:
    result = calc.add("5", 3)  # 将抛出 TypeError
except TypeError as e:
    print(f"Error: {e}")  # Error: Argument 1 must be a number
```

#### 基于函数的方法（向后兼容）：
```python
import calculator

# 基本运算
result = calculator.add(5, 3)        # 8
result = calculator.subtract(10, 4)  # 6
result = calculator.multiply(6, 7)   # 42
result = calculator.divide(15, 3)    # 5.0

# 通用函数
result = calculator.calculate('add', 5, 3)  # 8
```

### 运行测试

```bash
python test_calculator.py
```

### 示例

```bash
python example_usage.py
python calculator.py  # 内置演示
```

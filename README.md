# Python Learning Notes

## **Day 1: Python Basics**

### 1. Variables and Data Types
**Notes:**
- **Variables**: Containers to store data.
- **Data Types**:
  - `int`: Integer numbers.
  - `float`: Decimal numbers.
  - `str`: Strings (text).
  - `bool`: Boolean values (`True`, `False`).
  - `list`: Ordered collection of items.
  - `tuple`: Immutable collection of items.
  - `dict`: Key-value pairs.
  - `set`: Unordered, unique items.

**Examples:**
```python
# Variables
age = 25
name = "John"
height = 5.9
is_student = True

# Print variables
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# Data types
numbers = [1, 2, 3]  # List
tuple_example = (1, 2, 3)  # Tuple
dict_example = {"name": "John", "age": 25}  # Dictionary
set_example = {1, 2, 3, 4}  # Set
```

---

### 2. Conditional Statements
**Notes:**
- Use `if`, `elif`, `else` to execute code blocks based on conditions.
- Syntax:
  ```python
  if condition:
      # Code block
  elif another_condition:
      # Code block
  else:
      # Code block
  ```

**Examples:**
```python
# Check if a number is positive, negative, or zero
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

### 3. Loops
**Notes:**
- **For Loop**: Iterates over a sequence.
- **While Loop**: Repeats until a condition is false.
- Use `break` to exit a loop and `continue` to skip the current iteration.

**Examples:**
```python
# For loop
for i in range(5):
    print(i)  # Outputs: 0, 1, 2, 3, 4

# While loop
n = 3
while n > 0:
    print(n)  # Outputs: 3, 2, 1
    n -= 1
```

---

### 4. Functions
**Notes:**
- Functions allow you to reuse code.
- Syntax:
  ```python
  def function_name(parameters):
      # Code block
      return value
  ```
- **Default arguments**: Provide a default value for parameters.
- **Variable-length arguments**:
  - `*args`: For multiple positional arguments.
  - `**kwargs`: For multiple keyword arguments.
- Recursion: A function calling itself.

**Examples:**
```python
# Function with default argument
def greet(name="Guest"):
    return f"Hello, {name}!"

# Recursion: Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Test
print(greet())           # Output: Hello, Guest!
print(greet("Jasjeet"))  # Output: Hello, Jasjeet!
print(factorial(5))      # Output: 120
```


This file combines notes and examples for all topics covered day-wise. Problems will be stored in separate files for clarity.

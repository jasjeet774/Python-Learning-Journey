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


# Day 2: Data Structures - Lists, Tuples, Sets, Dictionaries

## Lists
Lists are ordered, mutable collections in Python. They allow duplicate elements and are versatile for various operations.

### Key Features
- Ordered collection (elements have a specific position).
- Mutable (can be changed after creation).
- Allows duplicate elements.

### Common Operations
```python
# Create a list
numbers = [1, 2, 3, 4, 5]

# Add elements
numbers.append(6)  # [1, 2, 3, 4, 5, 6]

# Insert at specific index
numbers.insert(2, 99)  # [1, 2, 99, 3, 4, 5, 6]

# Remove elements
numbers.remove(3)  # Removes the first occurrence of 3

# Slicing
print(numbers[1:4])  # [2, 99, 4]

# Iteration
for num in numbers:
    print(num)

# List comprehension
squared = [x**2 for x in numbers]  # [1, 4, 9801, 16, 25, 36]
```

---

## Tuples
Tuples are ordered, immutable collections in Python. They are used for fixed collections of items.

### Key Features
- Ordered collection.
- Immutable (cannot be changed after creation).
- Allows duplicate elements.

### Common Operations
```python
# Create a tuple
data = (10, 20, 30)

# Access elements
print(data[1])  # 20

# Count occurrences
print(data.count(20))  # 1

# Find index
print(data.index(30))  # 2

# Tuple unpacking
a, b, c = data
print(a, b, c)  # 10 20 30
```

---

## Sets
Sets are unordered collections of unique elements. They are used for membership testing and removing duplicates.

### Key Features
- Unordered collection.
- No duplicate elements.
- Mutable (can add/remove elements).

### Common Operations
```python
# Create a set
fruits = {"apple", "banana", "cherry"}

# Add elements
fruits.add("orange")

# Remove elements
fruits.remove("banana")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))       # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
print(set1.difference(set2))    # {1, 2}
```


---

## Dictionaries
Dictionaries are key-value pairs in Python. They are unordered and mutable.

### Key Features
- Unordered collection.
- Key-value pairs.
- Keys must be unique and immutable.

### Common Operations
```python
# Create a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Access elements
print(person["name"])  # Alice

# Add or update key-value pairs
person["age"] = 26

# Remove a key
person.pop("city")

# Iterate through keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Check if key exists
if "name" in person:
    print("Name exists")
```


---

## Summary
- **Lists**: Ordered, mutable, allows duplicates.
- **Tuples**: Ordered, immutable, allows duplicates.
- **Sets**: Unordered, mutable, no duplicates.
- **Dictionaries**: Key-value pairs, unordered, mutable.

Mastering these data structures is essential for efficient problem-solving in Python.




This file combines notes and examples for all topics covered day-wise. Problems will be stored in separate files for clarity.

# Chapter 3: Comparing Strings and Lists

Both strings and lists are **sequence types** in Python, which means they share certain characteristics and behaviors.

## Key Similarities

### Indexing
Both support accessing elements by position using square bracket notation:

```python
# String indexing
text = "hello"
print(text[1])  # 'e'

# List indexing
numbers = [1, 2, 3]
print(numbers[1])  # 2
```

### Slicing
Both support slicing with the same `[start:stop:step]` syntax:

```python
# String slicing
print(text[1:4])  # 'ell'

# List slicing
print(numbers[1:3])  # [2, 3]
```

### Iteration
Both can be iterated over using `for` loops:

```python
# String iteration
for char in "hello":
    print(char)

# List iteration
for item in [1, 2, 3]:
    print(item)
```

### Common Operations
Both support these operations:
- `len()` - get length
- `in` - membership testing
- `+` - concatenation
- `*` - repetition

```python
# Works for both strings and lists
print(len("abc"))       # 3
print(len([1, 2, 3]))   # 3

print("a" in "abc")     # True
print(1 in [1, 2, 3])  # True

print("a" + "b")       # "ab"
print([1] + [2])       # [1, 2]

print("a" * 3)         # "aaa"
print([1] * 3)         # [1, 1, 1]
```

## Key Differences

### Mutability
- **Strings are immutable** (cannot be changed after creation)
- **Lists are mutable** (can be modified after creation)

```python
# Strings - cannot modify
s = "hello"
# s[0] = "H"  # TypeError!

# Lists - can modify
lst = [1, 2, 3]
lst[0] = 100  # Valid
```

### Element Types
- **Strings** can only contain characters
- **Lists** can contain any Python objects (mixed types)

```python
# Strings - only characters
text = "abc123"

# Lists - any objects
mixed = [1, "two", 3.0, [4, 5], True]
```

## Available Methods
Each type has its own specialized methods:

### String Methods (focused on text manipulation)
```python
s = "Hello World"
print(s.lower())       # "hello world"
print(s.split())       # ['Hello', 'World']
print(s.replace("H", "J"))  # "Jello World"
```

### List Methods (focused on collection modification)
```python
lst = [1, 2, 3]
lst.append(4)       # [1, 2, 3, 4]
lst.insert(0, 0)    # [0, 1, 2, 3, 4]
lst.remove(2)       # [0, 1, 3, 4]
```

## Memory and Performance
- **Strings** are generally more memory efficient
- **Lists** require more memory but offer more flexibility

## When to Use Each

### Use Strings When:
- Working with text data
- You need immutable sequences
- Memory efficiency is important
- You need text-specific operations (splitting, case conversion, etc.)


### Use Lists When:
- You need to modify the collection
- Storing heterogeneous data types
- You need collection-specific operations (sorting, appending, etc.)
- Building dynamic collections that change size


## Conversion Between Types
You can convert between them (with limitations):

```python
# String to list
s = "hello"
lst = list(s)  # ['h', 'e', 'l', 'l', 'o']

# List to string (if elements are strings)
lst = ['a', 'b', 'c']
s = "".join(lst)  # "abc"

# Numbers need conversion first
nums = [1, 2, 3]
s = "".join(str(x) for x in nums)  # "123"
```

## Homework

### Task 1: Compare Elements One by One

**Description:**
Check whether two sequences (string and list) have the same characters in the same order.
You may assume the string contains only characters and the list contains single-character strings.

**Input Example:**

```python
text = "python"  
letters = ['p', 'y', 't', 'h', 'o', 'n']
```

**Expected Output:**

```python
True
```

### Task 2: Find Common Elements (Ignore Order)

**Description:**
Find and print all unique characters that appear in both the string and the list, regardless of order or position.

**Input Example:**

```python
text = "developer"  
items = ['d', 'e', 'x', 'o', 't']
```

**Expected Output:**

```python
['d', 'e', 'o']
```

### Task 3: Count Differences

**Description:**
Count how many positions differ between a string and a list of the same length.

**Input Example:**

```python
text = "banana"  
guess = ['b', 'o', 'n', 'u', 'n', 'a']
```

**Expected Output:**

```python
3
```

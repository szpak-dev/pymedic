# Chapter 4: Looping With `for .. in`

`for` loops let you iterate through sequences (like strings and lists) to access each element one by one.

## Basic Syntax:

```python
for element in sequence:
    # do something with element
```

## Iterating Strings

**Example 1:** Print each character
```python
word = "Python"
for char in word:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n
```

**Example 2:** Count vowels
```python
text = "Hello World"
vowel_count = 0

for letter in text:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"Number of vowels: {vowel_count}")  # Output: 3
```

**Example 3:** Build a new string
```python
original = "abc123"
new_string = ""

for char in original:
    if char.isdigit():
        new_string += char * 2  # double digits
    else:
        new_string += char.upper()  # uppercase letters

print(new_string)  # Output: ABC112233
```

## Iterating Lists

**Example 1:** Print each item
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

**Example 2:** Modify list elements
```python
numbers = [1, 2, 3, 4]
squared = []

for num in numbers:
    squared.append(num ** 2)

print(squared)  # Output: [1, 4, 9, 16]
```

**Example 3:** Nested list iteration
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # new line after each row

# Output:
# 1 2 3 
# 4 5 6 
# 7 8 9
```

## Accessing Index and Value Together

### Using `enumerate()`
```python
colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Index {index} has color {color}")

# Output:
# Index 0 has color red
# Index 1 has color green
# Index 2 has color blue
```

## Practical Applications

**Example 1:** Password strength checker
```python
password = "Python3!"
requirements = {
    "length": False,
    "uppercase": False,
    "digit": False,
    "special": False
}

for char in password:
    if len(password) >= 8:
        requirements["length"] = True
    if char.isupper():
        requirements["uppercase"] = True
    if char.isdigit():
        requirements["digit"] = True
    if not char.isalnum():
        requirements["special"] = True

print("Password meets requirements:", all(requirements.values()))
```

**Example 2:** Shopping cart total
```python
cart = [
    {"item": "Shirt", "price": 25.99, "qty": 2},
    {"item": "Pants", "price": 39.99, "qty": 1},
    {"item": "Socks", "price": 8.50, "qty": 3}
]

total = 0.0

for product in cart:
    total += product["price"] * product["qty"]

print(f"Total: ${total:.2f}")  # Output: Total: $110.47
```

## Common Patterns

**Pattern 1:** Filtering elements
```python
numbers = [12, 7, 24, 5, 18, 3]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  # Output: [12, 24, 18]
```

**Pattern 2:** Finding maximum
```python
temperatures = [22.5, 18.7, 25.3, 20.1, 16.8]
max_temp = temperatures[0]

for temp in temperatures[1:]:
    if temp > max_temp:
        max_temp = temp

print(f"Highest temperature: {max_temp}")  # Output: 25.3
```

## Key Takeaways
1. Strings and lists both work with `for` loops
2. Strings iterate character by character
3. Lists iterate item by item
4. You can modify lists during iteration (but be careful!)
5. `enumerate()` gives you both index and value
6. Loops are powerful for processing sequence data

## Homework

### Task 1: Remove Vowels from String

**Description:**
Loop through the string and create a new string without vowels (`a, e, i, o, u`).

**Input Example:**

```python
text = "education"
```

**Expected Output:**

```python
"dctn"
```

### Task 2: Count Uppercase Letters

**Description:**
Loop through the string and count how many uppercase letters it contains.

**Input Example:**

```python
text = "PyThOn ProGRamMinG"
```

**Expected Output:**

```python
8
```

### Task 3: Double Each Character

**Description:**
Create a new string where every character from the original string appears twice.

**Input Example:**

```python
word = "loop"
```

**Expected Output:**

```python
"llooooooopp"
```

### Task 4: Reverse List Without Slicing

**Description:**
Loop through a list and build a new list in reverse order (don’t use `[::-1]` or `reverse()`).

**Input Example:**

```python
[1, 2, 3, 4]
```

**Expected Output:**

```python
[4, 3, 2, 1]
```

### Task 5: Find Index of All Occurrences

**Description:**
Loop through a list and print the indices of all occurrences of a given value.

**Input Example:**

```python
List: [3, 1, 4, 3, 5, 3]  
Value: 3
```

**Expected Output:**

```python
[0, 3, 5]
```

### Task 6: Swap Adjacent Elements

**Description:**
Create a new list where each pair of adjacent elements is swapped.
If the list has an odd number of elements, leave the last one as is.

**Input Example:**

```python
[1, 2, 3, 4, 5]
```

**Expected Output:**

```python
[2, 1, 4, 3, 5]
```

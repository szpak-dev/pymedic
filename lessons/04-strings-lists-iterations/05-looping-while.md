# hapter 5: Looping with `while ..`

`while` loops continue executing as long as a condition remains true, making them ideal for situations where you need more control than a `for` loop provides.

## Basic Syntax:
```python
while condition:
    # loop body
```

## Looping Through Sequences with Counters

**Example 1:** String iteration with counter

```python
text = "Python"
index = 0  # Initialize counter

while index < len(text):
    print(f"Character at position {index}: {text[index]}")
    index += 1  # Increment counter

# Output:
# Character at position 0: P
# Character at position 1: y
# Character at position 2: t
# Character at position 3: h
# Character at position 4: o
# Character at position 5: n
```

**Example 2:** List iteration with condition

```python
numbers = [10, 20, 30, 40, 50]
total = 0
i = 0

while i < len(numbers) and total < 100:
    total += numbers[i]
    print(f"Added {numbers[i]}, current total: {total}")
    i += 1

# Output:
# Added 10, current total: 10
# Added 20, current total: 30
# Added 30, current total: 60
# Added 40, current total: 100
```

## Common Patterns

**Pattern 1:** Finding an element

```python
fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"
found = False
position = 0

while position < len(fruits) and not found:
    if fruits[position] == target:
        found = True
        print(f"Found {target} at index {position}")
    position += 1

# Output: Found cherry at index 2
```

**Pattern 1:** Building a new sequence

```python
original = "Hello123"
filtered = ""
i = 0

while i < len(original):
    if original[i].isalpha():
        filtered += original[i].upper()
    i += 1

print(filtered)  # Output: HELLO
```

## Practical Applications

**Example 1:** Password retry system

```python
max_attempts = 3
attempts = 0
correct_password = "Python123"
access_granted = False

while attempts < max_attempts and not access_granted:
    password = input("Enter password: ")
    if password == correct_password:
        access_granted = True
        print("Access granted!")
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong password. {remaining} attempts remaining.")

if not access_granted:
    print("Account locked. Too many failed attempts.")
```

**Pattern 2:** Processing until sentinel value

```python
numbers = []
print("Enter numbers (type 'done' to finish):")

while True:
    user_input = input("> ")
    if user_input.lower() == 'done':
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please enter a number or 'done'")

print(f"You entered: {numbers}")
print(f"Sum: {sum(numbers)}")
```

## Differences from `for` Loops

### When to use `while` instead of `for`:

1. When you need complex termination conditions
2. When the number of iterations isn't known in advance
3. When you need to modify the sequence during iteration
4. When implementing sentinel-controlled loops

### Comparison Example:

```python
# For loop (definite iteration)
for i in range(5):
    print(i)

# While equivalent (requires manual counter)
i = 0
while i < 5:
    print(i)
    i += 1
```

## Important Considerations

1. **Avoid infinite loops** - Always ensure the condition will eventually become false
2. **Initialize counters** before the loop
3. **Update counters** within the loop body
4. **Use `break`** for early termination when needed

```python
# Safe while loop pattern in pseudo-code

initialize variables
while condition:
    perform operations
    update condition variables
```

**Example:** List modification

```python
data = [1, 2, 3, "a", 4, 5, "b", 6]
i = 0

while i < len(data):
    if not isinstance(data[i], int):
        data.pop(i)
    else:
        data[i] *= 2  # double the number
        i += 1

print(data)  # Output: [2, 4, 6, 8, 10, 12]
```

## Key Takeaways
1. `while` loops offer more control than `for` loops
2. Always initialize and update your counter variable
3. Useful for processing sequences until complex conditions are met
4. Can modify sequences during iteration (unlike `for` loops)
5. Essential for user input validation and interactive programs

## Homework

### Task 1: Print Characters Until Space

**Description:**
Loop through a string using `while` and print each character until the first space.

**Input Example:**

```python
text = "Hello World"
```

**Expected Output:**

```python
H  
e  
l  
l  
o
```

### Task 2: Count Digits in String

**Description:**
Loop using `while` to count how many numeric characters are in the string.

**Input Example:**

```python
s = "a1b2c3"
```

**Expected Output:**

```python
3
```

### Task 3: Build Reversed String

**Description:**
Use `while` loop to reverse a string (don’t use slicing or `reversed()`).

**Input Example:**

```python
text = "python"
```

**Expected Output:**

```python
"nohtyp"
```

### Task 4: Sum All Elements

**Description:**
Use `while` to compute the sum of all numbers in a list.

**Input Example:**

```python
[4, 6, 1]
```

**Expected Output:**

```python
11
```

### Task 5: Find First Negative

**Description:**
Loop using `while` to find the first negative number and print it. Stop the loop immediately after.

**Input Example:**

```python
[3, 5, -2, 4]
```

**Expected Output:**

```python
-2
```

### Task 6: Remove All Zeros

**Description:**
Remove all zeros from a list using a `while` loop (modify list in place if possible).

**Input Example:**

```python
[0, 1, 2, 0, 3]
```

**Expected Output:**

```python
[1, 2, 3]
```

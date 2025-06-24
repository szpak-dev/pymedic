# Chapter 2: Lists
Lists are ordered, mutable sequences that can hold elements of different data types. They are one of Python's most versatile data structures.

```python
my_list = [1, 2, 3, "hello", True, 3.14]
```

## List Syntax
Lists are created with square brackets `[]` with elements separated by commas.

```python
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 42, True, 3.14]
nested = [[1, 2], [3, 4]]  # List of lists
```

## Indexing and Slicing (Similar to Strings)
Lists support the same indexing and slicing operations as strings.

```python
print(numbers[0])     # 1 - first element
print(numbers[-1])    # 5 - last element
print(numbers[1:4])   # [2, 3, 4] - slice from index 1 to 3
print(numbers[::2])   # [1, 3, 5] - every 2nd element
print(numbers[::-1])  # [5, 4, 3, 2, 1] - reversed list
```

## Mutability (Key Difference from Strings)
Unlike strings, lists are mutable - you can change their contents after creation.

```python
numbers[0] = 10  # Change first element
print(numbers)   # [10, 2, 3, 4, 5]

numbers[1:3] = [20, 30]  # Change slice
print(numbers)           # [10, 20, 30, 4, 5]
```

## Common List Methods

### Adding Elements
```python
fruits = ["apple", "banana"]

fruits.append("orange")  # Add to end
print(fruits)            # ['apple', 'banana', 'orange']

fruits.insert(1, "kiwi") # Insert at specific position
print(fruits)            # ['apple', 'kiwi', 'banana', 'orange']

fruits.extend(["grape", "mango"])  # Add multiple items
print(fruits)           # ['apple', 'kiwi', 'banana', 'orange', 'grape', 'mango']
```

### Removing Elements
```python
fruits.remove("banana")  # Remove first occurrence
print(fruits)            # ['apple', 'kiwi', 'orange', 'grape', 'mango']

popped = fruits.pop(1)   # Remove and return item at index
print(popped)            # 'kiwi'
print(fruits)            # ['apple', 'orange', 'grape', 'mango']

fruits.clear()           # Empty the list
print(fruits)            # []
```

### Other Useful Methods
```python
numbers = [5, 2, 8, 1, 3]

numbers.sort()           # In-place sorting
print(numbers)           # [1, 2, 3, 5, 8]

numbers.reverse()        # Reverse in-place
print(numbers)           # [8, 5, 3, 2, 1]

print(numbers.index(5))  # 1 - find index of value

numbers_copy = numbers.copy()  # Create shallow copy
```

## List vs String Comparison
| Feature        | Strings | Lists |
|---------------|---------|-------|
| Mutable       | No      | Yes   |
| Element Type  | Chars   | Any   |
| Syntax        | "" or '' | []   |
| Memory       | Smaller | Larger |


## Important Notes

- Lists can contain mixed data types
- List operations modify the original list (unlike strings which create new ones)
- `append()` adds single items, `extend()` adds multiple items
- Slicing works the same as with strings but can be used for modification
- A shallow copy of a list creates a new list object, but it copies references to the original elements—not the elements themselves
    - For primitive types (int, str, float, etc.), a shallow copy behaves like a full copy, since they are immutable.
    - For nested or mutable elements (e.g. lists inside lists), both the original and the shallow copy share references to those inner objects.


## Homework

### Task 1: Rotate List Left

**Description:**
Given a list of integers, rotate the elements one position to the left.
The first element moves to the end.

**Input Example:**

```python
[10, 20, 30, 40, 50]
```

**Expected Output:**

```python
[20, 30, 40, 50, 10]
```

### Task 2: Remove All Duplicates

**Description:**
Remove all duplicate elements from the list while preserving the original order.

**Input Example:**

```python
[1, 3, 2, 3, 1, 4]
```

**Expected Output:**

```python
[1, 3, 2, 4]
```

### Task 3: Count Frequencies

**Description:**
Count how many times each element appears in the list and print each element with its count (once per unique element).

**Input Example:**

```python
['a', 'b', 'a', 'c', 'b', 'a']
```

**Expected Output:**

```python
a: 3  
b: 2  
c: 1
```

### Task 4: Merge and Sort Two Lists

**Description:**
Merge two lists and sort the result in ascending order without using the `sort()` method.

**Input Example:**

```python
List A: [4, 1, 7]  
List B: [3, 6, 2]
```

**Expected Output:**

```python
[1, 2, 3, 4, 6, 7]
```

### Task 5: Split List into Even and Odd

**Description:**
Given a list of numbers, split it into two separate lists: one containing even numbers and one containing odd numbers.

**Input Example:**

```python
[10, 3, 5, 8, 2, 11]
```

**Expected Output:**

```python
Evens: [10, 8, 2]  
Odds: [3, 5, 11]
```

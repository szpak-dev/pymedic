# Chapter 1: Tuples

In this lesson, you'll learn about **tuples** in Python. Tuples are immutable sequences used to store collections of items.


## What is a Tuple?

A tuple is an ordered, immutable collection of elements.

```python
t: tuple[int, int, int] = (1, 2, 3)
```

## Creating Tuples

You can create tuples with or without parentheses.

```python
a: tuple[int, int] = (10, 20)
b: tuple[str, int] = 'hello', 42
c: tuple[str] = tuple(['one', 'two'])
d: tuple = ()
e: tuple[int] = (5,)
```

**Note**: A one-element tuple must have a trailing comma.


## 3. Accessing Elements

Use indexing and slicing.

```python
t: tuple[str, str, str] = ('red', 'green', 'blue')
first: str = t[0]
last_two: tuple[str, str] = t[1:]
```

## Tuple Immutability

Tuples cannot be changed after creation.

```python
t: tuple[int, int] = (1, 2)
# t[0] = 5  # Error: cannot assign to a tuple element
```

## Tuple Unpacking

You can unpack tuples into variables.

```python
coordinates: tuple[int, int] = (4, 5)
x, y = coordinates
```

Supports ignoring values:

```python
a, _, b = (1, 2, 3)
```

## Tuple Methods

Tuples support basic methods like `count` and `index`.

```python
t: tuple[int, int, int] = (1, 2, 1)
t.count(1)  # 2
t.index(2)  # 1
```

## Nested Tuples

Tuples can contain other tuples or collections.

```python
data: tuple[str, tuple[int, int]] = ('point', (2, 3))
```

## Using Tuples in Functions

Tuples are useful for returning multiple values.

```python
def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)
```

## Tuple vs List

| Feature     | Tuple      | List          |
| ----------- | ---------- | ------------- |
| Syntax      | `(1, 2)`   | `[1, 2]`      |
| Mutable     | No         | Yes           |
| Methods     | Few        | Many          |
| Performance | Faster     | Slower        |
| Use Cases   | Fixed data | Changing data |


## When Tuples Are Better

* **Coordinates**: `(latitude, longitude)` because their structure should never change.
* **RGB Colors**: `(255, 0, 0)` for red; fixed-length and immutable.
* **Database Rows**: often returned as tuples since the structure is constant.
* **Dictionaries as Keys**: tuples can be used as keys because they are hashable, lists cannot.


## Why Tuples Are Faster

Tuples are stored in a more compact form than lists. Since they are immutable:

* Python can make optimizations that it cannot do for lists.
* Memory allocation is smaller and simpler.
* Access is faster due to the fixed size and layout.


## Homework

1. Create a tuple `person` with your name, age, and city. Print each element using indexing.

2. Define a tuple `rgb` representing a color like `(128, 64, 32)`. Unpack the tuple into `r`, `g`, `b` and print each value.

3. Try to change one value of the `rgb` tuple and explain the error that occurs.

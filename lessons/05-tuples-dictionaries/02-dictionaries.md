# Chapter 2: Dictionaries

A **dictionary** in Python is a collection of key-value pairs. It is useful when you want to associate a unique identifier (the key) with some data (the value).

```python
d: dict[str, int] = {'apple': 3, 'banana': 5, 'cherry': 2}
```

## Basic Operations

### Creating a Dictionary

```python
inventory: dict[str, int] = {'pen': 10, 'notebook': 5, 'eraser': 3}
```

Dictionaries can be created instantly and hold mixed data types as values. They are commonly used to represent structured data like records or database rows.

### Accessing Values

```python
print(inventory['pen'])
```

Dictionaries provide fast access to values by key. Attempting to access a key that doesn't exist will raise a `KeyError`, so it's often useful to check first.

### Adding or Updating Entries

```python
inventory['marker'] = 7
inventory['pen'] = 12
```

Adding a new key or updating an existing one takes the same syntax. This operation is very efficient, making dictionaries ideal for dynamic data.

### Removing Entries

```python
del inventory['eraser']
```

Deleting a key-value pair removes it completely from the dictionary. This is useful for managing memory or cleaning up processed data.

### Checking if a Key Exists

```python
if 'notebook' in inventory:
    print('We have notebooks')
```

Using `in` to check for key existence is faster than searching through a list. This is one reason dictionaries outperform other data structures in many scenarios.

### Looping Through a Dictionary

```python
for item, count in inventory.items():
    print(f'{item}: {count}')
```

Looping with `.items()` gives access to both keys and values simultaneously. You can also loop through just keys using `.keys()` or just values with `.values()`.

## Real-World Use Cases

### Example 1: Phonebook

```python
phonebook: dict[str, str] = {
    'Alice': '123-456-789',
    'Bob': '987-654-321',
    'Charlie': '555-666-777'
}
```

Instead of using a list of tuples, a dictionary allows you to look up a number instantly by name.

### Example 2: Counting Occurrences

```python
words: list[str] = ['apple', 'banana', 'apple', 'cherry', 'banana']
counts: dict[str, int] = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
```

Dictionaries are ideal for frequency analysis.

### Example 3: Configuration Settings

```python
settings: dict[str, bool] = {
    'dark_mode': True,
    'notifications': False,
    'auto_save': True
}
```

Dictionaries let you represent named options clearly.

## Dictionaries vs Lists and Tuples

* **Tuples** are immutable and ordered. Use them for fixed records:

```python
user: tuple[str, int] = ('Alice', 25)
```

* **Lists** are ordered and mutable. Use them when order matters:

```python
users: list[str] = ['Alice', 'Bob', 'Charlie']
```

* **Dictionaries** are unordered (Python 3.7+ maintains insertion order) and optimized for fast key lookups:

```python
user_ages: dict[str, int] = {'Alice': 25, 'Bob': 30}
```

Dictionaries are faster than lists when looking up data by a unique identifier.


## Homework

1. Create a dictionary of 7 cities and their populations. Print only the cities with a population over 1 million, then calculate and display the total population of printed (> 1M) cities.

2. You have a list of names: `['Anna', 'Tom', 'Anna', 'Eli', 'Tom', 'Eli', 'Anna']`. Count how many times each name appears using a dictionary, then print the most frequent name.

3. Represent the weekly availability of a tutor as a dictionary where keys are days of the week and values are booleans. Print all available days, count how many days the tutor is available, and display a message if they are available for more than 4 days.

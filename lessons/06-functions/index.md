# Lesson 6: Functions

* Understand how to define and call functions in Python
* Learn about parameters, arguments, return values
* Use type hints for clarity and type safety
* Explore advanced topics: recursion, higher-order functions, and lambdas


## Function Basics

### Definition:

```python
def greet(name: str) -> None:
    print(f'Hello, {name}!')
```

### Calling:

```python
greet('Alice')
```

### Use Case:

Creating reusable actions like greetings, logging, or alerts.

### Real-World Usage:

Used in web apps, CLI tools, and chatbots for dynamic interactions.


## Parameters and Return Values

### Returning a value:

```python
def square(number: float) -> float:
    return number ** 2
```

### Calling and using the return value:

```python
result: float = square(5.0)
print(result)
```

### Use Case:

Computing and reusing the result in larger calculations.

### Real-World Usage:

Common in scientific applications, simulations, and financial software.


## Default and Keyword Arguments

### Default values:

```python
def power(base: float, exponent: int = 2) -> float:
    return base ** exponent
```

### Calling with and without the default:

```python
print(power(3))      # uses default exponent=2
print(power(3, 3))   # overrides default
```

### Use Case:

Providing sensible fallbacks while allowing customization.

### Real-World Usage:

Seen in plotting libraries, API configurations, and function interfaces.


## Variable Number of Arguments

### \*args and \*\*kwargs:

```python
def print_args(*args: str) -> None:
    for arg in args:
        print(arg)

def print_kwargs(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f'{key}: {value}')
```

### Use Case:

Writing generic functions that handle flexible inputs.

### Real-World Usage:

Used in logging frameworks, UI builders, and data processors.


## Recursive Functions

### Example: Factorial

```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Use Case:

Solving divide-and-conquer problems or traversing structures.

### Real-World Usage:

Used in compilers, game logic (decision trees), and parsing tasks.


## Lambda Functions

### Anonymous inline functions:

```python
add: Callable[[int, int], int] = lambda x, y: x + y
print(add(2, 3))
```

### Use Case:

Defining small functions without cluttering code.

### Real-World Usage:

Used in data analysis (e.g., Pandas), sorting, and GUI event handling.


## Higher-Order Functions

### Passing functions as arguments:

```python
def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))

def increment(x: int) -> int:
    return x + 1

print(apply_twice(increment, 3))
```

### Use Case:

Manipulating or composing behaviors dynamically.

### Real-World Usage:

Common in decorators, middleware pipelines, and testing frameworks.

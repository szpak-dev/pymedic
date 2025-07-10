# Chapter 3: Conditionals

Learn how to use `if`, `elif`, and `else` in Python to make decisions. Along the way, discover quirky facts and real-world analogies.


## What Are Conditionals?

Conditionals let a program decide what to do **based on a condition**.

```python
if temperature > 30:
    print('It\'s a hot day!')
```

**Fact:** Python uses **indentation instead of braces** (like `{}` in other languages) to group blocks of code. That makes code cleaner and enforces readability.


## Basic `if` Statement

```python
x: int = 10
if x > 5:
    print('x is greater than 5')
```

Python checks the condition (`x > 5`). If it's `True`, the indented code runs.

**Fact:** The `if` keyword dates back to early programming languages like Fortran (1957)!


## Adding `else`

```python
x: int = 2

if x > 5:
    print('x is big')
else:
    print('x is small')
```

`else` runs when the `if` condition is false.

**Analogy:** Think of `if/else` like a fork in the road—you go one way or the other.


## The `elif` Chain

```python
color: str = 'green'

if color == 'red':
    print('Stop')
elif color == 'yellow':
    print('Slow down')
elif color == 'green':
    print('Go')
else:
    print('Invalid color')
```

**Fun Fact:** Python checks each condition top to bottom. As soon as one is true, it stops checking the rest.


## Boolean Logic in Conditions

```python
age: int = 20
has_ticket: bool = True

if age >= 18 and has_ticket:
    print('Entry allowed')
```

**Tip:** Use `and`, `or`, `not` to combine conditions.


## Truthy and Falsy Values

Python considers these as **False**:

* `0`
* `''` (empty string)
* `[]`, `{}`, `()` (empty containers)
* `None`

Everything else is **Truthy**.

```python
name: str = ''

if name:
    print('Hello,', name)
else:
    print('Who are you?')
```

**Fact:** This behavior lets Python code be more concise and expressive.


## Nested Conditionals

```python
x: int = 10

if x > 0:
    if x % 2 == 0:
        print('Positive even number')
```

**Tip:** Avoid deep nesting when possible—consider using `elif` or logical operators instead.


## Summary

* Use `if` to test conditions
* Use `else` for fallback
* Use `elif` for multiple conditions
* Combine with `and`, `or`, `not`
* Python values can be truthy or falsy

**Fun Fact:** Python was named after *Monty Python*, not the snake. That's why you often see joke references in Python documentation.


## Homework

1. **Build a simple login system:**

* Ask the user to enter a username and password.
* If either is empty, show an error.
* If both are correct (use hardcoded values), print a welcome message.
* Otherwise, deny access.

2. **Create a number classification program:**

* Ask the user for a number.
* Print whether it is odd/even.
* Indicate whether it is positive, negative, or zero.
* If it's a multiple of both 3 and 5, print 'FizzBuzz'.

3. **Create a basic shopping cart simulator:**

* Ask if the user is a member (yes/no).
* Ask for total cart value.
* Apply a discount if the user is a member and the value is over a threshold.
* Show the final price after discount or state that no discount is applied.

# Lesson 3: Variables, Data Types and Basic Operations

In Python, variables are used to store data values. Each variable has a data type that defines what kind of value it holds. Python is dynamically typed, but you can specify types using annotations.


## Variable Declaration and Type Annotations

```python
x: int = 5
y: float = 3.14
z: bool = True
name: str = "Python"
```

## int (Integer)

Integers represent whole numbers without decimals.

```python
a: int = 42
b: int = -7
c: int = 0
```

### Example

```python
population: int = 8_000_000_000
binary_flag: int = 0b101010
hex_value: int = 0xFF
```

## float (Floating-Point Number)

Floats represent real numbers with decimals.

```python
pi: float = 3.14159
temperature: float = -273.15
e: float = 2.71828
```

### Example

```python
scientific: float = 6.02e23
irrational: float = (2.0 + 3.0) ** 0.5
```


## bool (Boolean)

Booleans represent truth values: `True` or `False`.

```python
is_active: bool = True
is_empty: bool = False
```

### Built from Numbers

* `bool(0)` → `False`
* `bool(1)` → `True`
* Any non-zero number converts to `True`

### Example

```python
valid: bool = bool(len("Hello"))
truthy_number: bool = bool(-999)
```

## str (String)

Strings are sequences of Unicode characters.

```python
language: str = "Python"
empty: str = ""
quote: str = 'Single quotes work too'
```

### Example

```python
greeting: str = f"Hello, {language.upper()}!"
unicode_str: str = "💡 = idea"
```

## Type Conversions

```python
num_str: str = str(123)
str_to_int: int = int("456")
str_to_float: float = float("3.14")
bool_from_str: bool = bool("non-empty")
```


## Building Other Types from Numbers

Numbers can be used to create booleans and strings.

```python
zero_bool: bool = bool(0)
nonzero_bool: bool = bool(42)
int_to_str: str = str(1000)
```

## Basic Operations

### Arithmetic

```python
a: int = 10 + 5
b: float = 7.0 / 2.0
c: int = 10 % 3
d: float = 2 ** 3
```

### Boolean Logic

```python
result: bool = True and False
toggle: bool = not True
inclusive: bool = True or False
```

### String Operations

```python
combined: str = "Hello" + " " + "World"
repeated: str = "Na" * 4
char: str = "Python"[0]
```


## Homework

**1. Declare variables using all four types. Create examples based on:**

* hospital patient
* medical records

**2. Use type conversions between int, float, str, and bool to simulate a login system:**

* Convert a password attempt into a boolean
* Count failed attempts and lock account after 3

**3. Bonus**

Create a Python script that prints a table of variables with their names, types, and values (simulated output formatting).

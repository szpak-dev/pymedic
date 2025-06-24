# Lesson 3: Variables, Primitive Data Types and Basic Operations

In Python, variables are used to store data values. Each variable has a data type that defines what kind of value it holds. 

Python is dynamically typed, but you can specify types using annotations.


## Primitives

Primitive data types are the most basic types of data built into a programming language. In Python, the key primitive types include int (integers), float (decimal numbers), bool (boolean values), and str (strings or text).

These types represent simple, indivisible values that are used as the building blocks of more complex structures. For example:

- `42` is an int, 
- `3.14` is a float, 
- `True` is a bool, 
- `"Hello"` is a str.

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

## From Number To Text And Back

In Python, you can convert between characters and their ASCII numeric values using the built-in functions:

- `ord(str: char) -> int` 
- `chr(int: number) -> str`

### ASCII Character-To-Number
The `ord()` function takes a single character (e.g., 'A', 'z', '0') and returns its corresponding ASCII (or Unicode) integer value. 

For example, ord('A') returns 65, and ord('a') returns 97. This is useful when you need to perform operations based on a character’s position in the ASCII table, such as sorting or encoding.

```python
char: str = 'A'
ascii_a: int = ord(char)
print(ascii_a)  # Output: 65
```

```python
char: str = 'z'
ascii_z: int = ord(char)
print(ascii_z)  # Output: 122
```

### ASCII Number-To-Character

Conversely, the `chr()` function does the reverse: it takes an integer and returns the corresponding character. For instance, `chr(65)` gives `'A'`. 

This is useful when generating characters from numeric codes or shifting letters in ciphers like Caesar shift. Keep in mind that the ASCII range covers values from 0 to 127, while `chr()` and `ord()` also support extended Unicode characters beyond that, although for ASCII-specific tasks you should stick to values within the standard ASCII range.

```python
code: int = 66
char_b: str = chr(code)
print(char_b)  # Output: 'B'
```

```python
code: int = 97
char_a: str = chr(code)
print(char_a)  # Output: 'a'
```

## Homework

### Task 1: Budget Breakdown Analyzer

**Description:**
Simulate basic budget planning using variables and arithmetic operations.

**Instructions:**

* Create variables:

  * `income` (monthly income as float)
  * `rent`, `groceries`, `transport`, `entertainment` (monthly expenses as floats)
* Calculate:

  * Total expenses
  * Remaining balance
  * Percentage of income spent per category (rounded to 2 decimals)
* Print a breakdown like:

```python
Rent: 35.71% of income  
Groceries: 18.57% of income  
...  
Remaining balance: 650.50
```

**Extra:** Use f-strings to format values to 2 decimal places.

### Task 2: Dynamic Type Evaluator

**Description:**
Work with mixed data types and convert them dynamically based on type.

**Instructions:**

* Create three variables of different types:
  Example: `"42"` (str), `17` (int), `False` (bool)
* For each variable:

  * Check its type
  * If it's a string of digits, convert to int and add 10
  * If it's a boolean, convert to int and double it
  * Print original value/type and transformed value/type
* Output format:

```python
Original: '42' (str) → Transformed: 52 (int)
Original: False (bool) → Transformed: 0 (int)
```

### Task 3: Operation Parser Simulator

**Description:**
Emulate a simple parser that interprets a string as a math operation.

**Instructions:**

* Create variables:

  * `operand1 = 12`
  * `operand2 = 4`
  * `operator = "divide"`
* Based on the operator (`"add"`, `"subtract"`, `"multiply"`, `"divide"`):

  * Perform the operation
  * Print result in format: `12 / 4 = 3.0`
* **Extras:**

  * Handle division by zero
  * Handle invalid operators with: `"Unknown operation"`


Here’s an additional **Task 4** for the same homework, focused on **ASCII characters and character encoding**.


### Task 4: ASCII Character Inspector

**Description:**
Work with ASCII codes to analyze and transform characters.

**Instructions:**

* Create a string of any characters, e.g. `"Hello123!"`
* For each character in the string:

  * Print its ASCII code using `ord()`
  * If it's a letter (a–z or A–Z), shift it by 1 using `chr(ord(char) + 1)`

    * Example: `'a'` becomes `'b'`, `'Z'` becomes `'['`
* Print both the **original character and its ASCII**, and the **shifted character and new ASCII**

**Example Output:**

```python
'H' > 72 > 'I' > 73  
'e' > 101 > 'f' > 102  
'1' > 49 > '1' > 49  
...
```

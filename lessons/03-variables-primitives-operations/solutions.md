




### Task 1 Solution:

```python
income = 3500.0
rent = 1250.0
groceries = 650.0
transport = 300.0
entertainment = 200.0

total_expenses = rent + groceries + transport + entertainment
remaining = income - total_expenses

print(f"Rent: {rent / income * 100:.2f}% of income")
print(f"Groceries: {groceries / income * 100:.2f}% of income")
print(f"Transport: {transport / income * 100:.2f}% of income")
print(f"Entertainment: {entertainment / income * 100:.2f}% of income")
print(f"Remaining balance: {remaining:.2f}")
```


### Task 2 Solution:

```python
a = "42"
b = 17
c = False

variables = [a, b, c]

for v in variables:
    original_type = type(v).__name__
    if isinstance(v, str) and v.isdigit():
        new_value = int(v) + 10
    elif isinstance(v, bool):
        new_value = int(v) * 2
    elif isinstance(v, int):
        new_value = v
    else:
        new_value = v

    new_type = type(new_value).__name__
    print(f"Original: {repr(v)} ({original_type}) → Transformed: {new_value} ({new_type})")
```

### Task 3 Solution:

```python
operand1 = 12
operand2 = 4
operator = "divide"

if operator == "add":
    result = operand1 + operand2
    symbol = "+"
elif operator == "subtract":
    result = operand1 - operand2
    symbol = "-"
elif operator == "multiply":
    result = operand1 * operand2
    symbol = "*"
elif operator == "divide":
    if operand2 != 0:
        result = operand1 / operand2
        symbol = "/"
    else:
        print("Error: Division by zero")
        result = None
else:
    print("Unknown operation")
    result = None

if result is not None:
    print(f"{operand1} {symbol} {operand2} = {result}")
```


### Task 4 Solution:

```python
text = "Hello123!"

i = 0
while i < len(text):
    char = text[i]
    code = ord(char)

    if char.isalpha():
        shifted = chr(code + 1)
        shifted_code = ord(shifted)
    else:
        shifted = char
        shifted_code = code
   
    print(f"'{char}' > {code} > '{shifted}' > {shifted_code}")
    
    i += 1
```
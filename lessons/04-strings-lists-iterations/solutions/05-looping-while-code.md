### Task 1: Print Characters Until Space

```python
text = "Hello World"
i = 0

while i < len(text) and text[i] != " ":
    print(text[i])
    i += 1
```

### Task 2: Count Digits in String

```python
s = "a1b2c3"
i = 0
count = 0

while i < len(s):
    if s[i].isdigit():
        count += 1
    i += 1

print(count)
```

### Task 3: Build Reversed String

```python
text = "python"
i = len(text) - 1
reversed_text = ""
while i >= 0:
    reversed_text += text[i]
    i -= 1
print(reversed_text)
```

### Task 4: Sum All Elements

```python
numbers = [4, 6, 1]
i = 0
total = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

print(total)
```

### Task 5: Find First Negative

```python
nums = [3, 5, -2, 4]
i = 0

while i < len(nums):
    if nums[i] < 0:
        print(nums[i])
        break
    
    i += 1
```

### Task 6: Remove All Zeros

```python
lst = [0, 1, 2, 0, 3]
i = 0

while i < len(lst):
    if lst[i] == 0:
        lst.pop(i)
    else:
        i += 1

print(lst)
```

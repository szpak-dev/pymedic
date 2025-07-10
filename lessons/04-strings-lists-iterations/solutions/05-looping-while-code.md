### Task 1: Print Characters Until Space

```python
text: str = "Hello World"
i: int = 0

while i < len(text) and text[i] != " ":
    print(text[i])
    i += 1
```

### Task 2: Count Digits in String

```python
s: str = "a1b2c3"
i: int = 0
count: int = 0

while i < len(s):
    if s[i].isdigit():
        count += 1
    i += 1

print(count)
```

### Task 3: Build Reversed String

```python
text: str = "python"
i: int = len(text) - 1
reversed_text: str = ""

while i >= 0:
    reversed_text += text[i]
    i -= 1

print(reversed_text)
```

### Task 4: Sum All Elements

```python
numbers: list[int] = [4, 6, 1]
i: int = 0
total: int = 0

while i < len(numbers):
    total += numbers[i]
    i += 1

print(total)
```

### Task 5: Find First Negative

```python
nums: list[int] = [3, 5, -2, 4]
i: int = 0

while i < len(nums):
    if nums[i] < 0:
        print(nums[i])
        break
    
    i += 1
```

### Task 6: Remove All Zeros

```python
nums: list[int] = [0, 1, 2, 0, 3]
i: int = 0

while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)
    else:
        i += 1

print(nums)
```

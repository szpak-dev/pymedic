Here are **3 tasks for looping over strings** and **3 tasks for looping over lists**, with **descriptions** and **separate typed solutions**.
### Task 1: Remove Vowels from String

```python
text = "education"
result = ""

for char in text:
    if char not in "aeiou":
        result += char

print(result)
```

### Task 2: Count Uppercase Letters

```python
text = "PyThOn ProGRamMinG"
count = 0

for char in text:
    if char.isupper():
        count += 1

print(count)
```

### Task 3: Double Each Character

```python
word = "loop"
doubled = ""

for char in word:
    doubled += char * 2

print(doubled)
```

### Task 4: Reverse List Without Slicing

```python
original = [1, 2, 3, 4]
reversed_list = []
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])
print(reversed_list)
```

### Task 5: Find Index of All Occurrences

```python
nums = [3, 1, 4, 3, 5, 3]
value = 3
indices = []

for i in range(len(nums)):
    if nums[i] == value:
        indices.append(i)

print(indices)
```

### Task 6: Swap Adjacent Elements

```python
items = [1, 2, 3, 4, 5]
swapped = []
i = 0

while i < len(items):
    if i + 1 < len(items):
        swapped.append(items[i + 1])
        swapped.append(items[i])
        i += 2
    else:
        swapped.append(items[i])
        i += 1

print(swapped)
```

### Task 1: Compare Elements One by One

```python
text = "python"
letters = ['p', 'y', 't', 'h', 'o', 'n']
same = list(text) == letters

print(same)
```

### Task 2: Find Common Elements (Ignore Order)

```python
text = "developer"
items = ['d', 'e', 'x', 'o', 't']
common = []

for char in items:
    if char in text and char not in common:
        common.append(char)

print(common)
```

### Task 3: Count Differences

```python
text = "banana"
guess = ['b', 'o', 'n', 'u', 'n', 'a']
diff_count = 0

for i in range(len(text)):
    if text[i] != guess[i]:
        diff_count += 1

print(diff_count)
```

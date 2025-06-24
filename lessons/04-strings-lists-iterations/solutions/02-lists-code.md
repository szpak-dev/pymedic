
### Task 1: Rotate List Left

```python
numbers = [10, 20, 30, 40, 50]
rotated = numbers[1:] + [numbers[0]]

print(rotated)
```

### Task 2: Remove All Duplicates

```python
original = [1, 3, 2, 3, 1, 4]
unique = []

for item in original:
    if item not in unique:
        unique.append(item)

print(unique)
```

### Task 3: Count Frequencies

```python
items = ['a', 'b', 'a', 'c', 'b', 'a']
checked = []

for item in items:
    if item not in checked:
        count = items.count(item)
        print(f"{item}: {count}")
        checked.append(item)
```

### Task 4 Solution:

```python
a = [4, 1, 7]
b = [3, 6, 2]

merged = a + b
sorted_list = []

while merged:
    smallest = min(merged)
    sorted_list.append(smallest)
    merged.remove(smallest)

print(sorted_list)
```

### Task 5 Solution:

```python
numbers = [10, 3, 5, 8, 2, 11]
evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Evens:", evens)
print("Odds:", odds)
```

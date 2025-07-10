# Task 1

```python
cities: dict[str, int] = {
    'New York': 8419000,
    'Los Angeles': 3980000,
    'Chicago': 2716000,
    'Houston': 2328000,
    'Phoenix': 1690000,
    'Austin': 964000,
    'Miami': 467000
}

total: int = 0
for city, population in cities.items():
    if population > 1000000:
        print(city)
        total += population

print('Total population:', total)
```

# Task 2

```python
names: list[str] = ['Anna', 'Tom', 'Anna', 'Eli', 'Tom', 'Eli', 'Anna']
counts: dict[str, int] = {}

for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1

max_count = max(counts.values())

for name, count in counts.items():
    if count == max_count:
        print(name)
    else:
        continue
```

# Task 3

```python
availability: dict[str, bool] = {
    'Monday': True,
    'Tuesday': False,
    'Wednesday': True,
    'Thursday': True,
    'Friday': True,
    'Saturday': False,
    'Sunday': True
}

count: int = 0
for day, available in availability.items():
    if available:
        print(day)
        count += 1

print('Available days:', count)

if count > 4:
    print('Available most of the week')
```

# Task 1

```python
person = ('John Doe', 30, 'New York')

print(person[0])
print(person[1])
print(person[2])
```

# Task 2

```python
rgb = (128, 64, 32)
r, g, b = rgb

print(r)
print(g)
print(b)
```

# Task 3

```python
rgb = (128, 64, 32)

try:
    rgb[0] = 255
except TypeError as e:
    print(f'Error: {e}')
    print('Tuples are immutable in Python, so their elements cannot be changed after creation.')
```

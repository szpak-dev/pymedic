# Task 1

```python
username: str = input('Username: ')
password: str = input('Password: ')

if username == '' or password == '':
    print('Error')
elif username == 'admin' and password == '1234':
    print('Welcome')
else:
    print('Access denied')
```

# Task 2

```python
n: int = int(input('Number: '))

if n % 2 == 0:
    print('Even')
else:
    print('Odd')

if n > 0:
    print('Positive')
elif n < 0:
    print('Negative')
else:
    print('Zero')

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
```

# Task 3

```python
member: str = input('Are you a member [yes]: ')
value: float = float(input('What is a cart value?: '))

if member.lower() == 'yes' and value > 100:
    value *= 0.9

print(f'Final value: {value:.2f}')
```

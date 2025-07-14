string: str = 'abc'

numbers = "0123456789"
i = 0
digits_number = 0

while i < len(string):
    if string[i] in numbers:
        digits_number += 1
    i += 1

print(digits_number)
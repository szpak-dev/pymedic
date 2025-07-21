number = int(input('Enter number:'))

print(number)

if number == 0:
    print('Number is zero')
else:
    if number % 2 == 0:
        print('Number is odd.')
    else:
        print('Number is even')
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')

if number < 0:
    print('Number is negative')
if number >0:
    print('Number is positive')
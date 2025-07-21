def is_even(number: int) -> bool:
    return number % 2 == 0


test_cases = {
    1: False,
    2: False,
    3: False,
}

results = []

for value, expected_result in test_cases.items():
    result = is_even(value) == expected_result
    results.append(result)

if all(results):
    print('OK')
else:
    print('Failed')

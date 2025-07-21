from typing import Callable


def add(num1: float, num2: float) -> float:
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    return num1 - num2


def modular_calc(operation: Callable, num1: float, num2: float) -> float:
    return operation(num1, num2)


def calculator(operation: str, num1: float, num2: float, greeting: str = 'Jasio') -> float:
    result = 0

    if operation == 'add':
        result = num1 + num2

    elif operation == 'subtract':
        result = num1 - num2

    elif operation == 'multiply':
        result = num1 * num2
        
    elif operation == 'divide':
        result = num1 / num2
    
    else:
        raise RuntimeError(f'Unknown operation: {operation}')
    
    if greeting is not None:
        if len(greeting) < 1:
            raise RuntimeError('Greeting must contain at least one character')
        
        print(f'Hello, {greeting}')
    
    return result


def main():
    r1_args = ['add', 4, 5, 'John']
    r1 = calculator(*r1_args)
    print(f'Result 1 = {r1}')

    r2_kwargs = {'operation': 'add', 'num1': 4, 'num2': 5}
    r2 = calculator(**r2_kwargs)
    print(f'Result 2 = {r2}')



result = modular_calc(subtract, 12, 45)
print(result)

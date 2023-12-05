import math, json  # GPTLint: Avoid multiple imports on one line (PEP 8: E401).

def fibonacci(n):
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def check_prime(number):
    if number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False

class User:
    def __init__(user, name, age):  # GPTLint: First parameter of a method should be 'self' (PEP 8: N804).
        user.name = name
        user.age = age

def json_export(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def math_operations(x, y):
    if x > y or x <= y:  # GPTLint: This condition always evaluates to True.
        result = (x ** y) ** 0.5
    return result  # GPTLint: 'result' may be referenced before assignment if 'x > y or x <= y' is False.

def area_of_circle(radius):
    return pi * radius ** 2  # GPTLint: 'pi' is not defined, consider importing 'pi' from 'math'.

if __name__ == '__main__':
    print(f"Fibonacci Series: {fibonacci(5)}")
    print(f"Is 5 Prime? {check_prime(5)}")
    user = User('Alice', 30)
    json_export({"name": user.name, "age": user.age}, 'user.json')
    print(f"Math Operation Result: {math_operations(4, 3)}")
    print(f"Area of Circle: {area_of_circle(5)}")

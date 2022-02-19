def sum_list(lst):
    # return 0 if len(lst) == 0 else lst[0] + sum_list(lst[1:])
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

def factorial(number):
    # return 1 if number < 1 else number * factorial(number - 1)
    if number < 1:
        return 1
    return number * factorial(number - 1)

def gcd(number1, number2):
    # return number1 if number2 == 0 else gcd(number2, number1 % number2)
    if number2 == 0:
        return number1
    return gcd(number2, number1 % number2)

def fibonacci(index):
    # return index if index <= 1 else fibonacci(index - 1) + fibonacci(index - 2)
    if index <= 1:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)

print(factorial(2990))

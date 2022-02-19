def sum_list(lst):
    result = 0
    for num in lst:
        result += num
    return result

def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
        
    return result

def gcd(number1, number2):
    minimum = min(number1, number2) 
    
    while minimum > 1:
        if number1 % minimum == 0 and number2 % minimum == 0:
            return minimum
        minimum -= 1

    return 1

def fibonacci(index):
    if index <= 1:
        return index
    
    a, b = 0, 1
    for i in range(index):
        a, b = b, a + b
    return a


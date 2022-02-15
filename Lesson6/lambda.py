# def is_even(number):
#     return number % 2 == 0

# def is_odd(number):
#     return number % 2 != 0

# def div_by_three(number):
#     return number % 3 == 0

# def square(number):
#     return number * number

is_even =      lambda x: x % 2 == 0
is_odd =       lambda x: x % 2 != 0
div_by_three = lambda x: x % 3 == 0
square =       lambda x: x * x

print(is_even(1))
print(is_odd(1))
print(div_by_three(6))
print(square(5))

L = [1, 0, -5, 4, 3, 0]
L.sort(key=lambda x: x * x)
print(L)

# 1 => Direct print
print("Hello, world!")

# 2 => Using variable
hello = "Hello, world!"
print(hello)

# 3 => Easy arithmetical operations
x = 5
y = 12
print(x + y)

# 4 => Storing result in a variable
result = x + y
print(result)

# 5 => Change of 'x' doesn't affect on 'y'
x = 3
y = x

x += 1
print("x =", x)
print("y =", y)

# 6 => Arithmetical operations
x = 5
y = 12

Sum = x + y
Difference = x - y
Product = x * y
Division = x / y             # always float
IntegralDivision = x // y    # always integer
Modulus = x % y
Degree = x ** y

print("Sum:", Sum)
print("Difference:", Difference)
print("Product:", Product)
print("Division:", Division)
print("IntegralDivision:", IntegralDivision)
print("Modulus:", Modulus)
print("Degree:", Degree)

# 7 => Assignment operations
x = 5

x += 4
print(x)

x //= 3
print(x)

x **= 2
print(x)

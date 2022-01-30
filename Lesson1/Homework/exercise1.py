number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
operation = input("Select an operation (+-*/): ")

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    result = number_1 / number_2
else:
    result = "Error"
    
print(result)

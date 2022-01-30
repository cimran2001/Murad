count = int(input("Enter the number of elements: "))

result = 0
for i in range(0, count):
    number = int(input("Enter an element: "))
    result += number
    
print("Sum is:", result)

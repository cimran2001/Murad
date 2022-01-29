# if condition

number = 123

if number > 0:
    print("Number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative.")
    
    
if number % 2 == 0 and number % 3 == 0:
    print("Number is divisible by 6.")
else:
    print("Number is not divisible by 6.")

# while loop

a = 0
b = 1

while a < 100: # Fibonacci numbers less than 100
    print(a)
    temp = a
    a = b
    b += temp
# Search more on Google

# for loop

for i in range(1, 10):
    print(i)
    
    
for i in "Hello, world!":
    print(i)
    
    
# continue operator

for i in range(1, 10): # All odd numbers in range from 1 to 10
    if i % 2 == 0:
        continue
    print(i)

# break operator

for i in "Hello, world!": # All symbols before comma
    if i == ",":
        break
    print(i)
    
# else keyword

for i in "Hello, world!": # Checking whether there is a question mark
    if i == "?":
        break
else:
    print("There is no question mark in this sentence.")
    

for i in "What's your name?": # Checking whether there is a question mark
    if i == "?":
        break
else:
    print("There is no question mark in this sentence.")


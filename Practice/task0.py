'''
Create a list of integers of a concrete size
'''


# First solution!

# L = []
# size = input("How many numbers do you want to have in the list? ").strip()

# if not size.isnumeric():
#     print("This is not a number!")
#     exit()

# size = int(size)


# for i in range(size):
#     element = input("Enter a number: ").strip()
#     if not element.isnumeric():
#         print("This is not a number!")
#         break
    
#     element = int(element)
#     L.append(element)

# print(L)


# Second solution!

L = []

while True:
    element = input("Enter a number: ")
    
    if element == "":
        break
    
    if not element.isnumeric():
        print("This is not a number! ")
        break
    
    element = int(element)
    L.append(element)
    
print(L)

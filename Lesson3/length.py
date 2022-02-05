L = [1, 2, 5, 4, 6]
string = "My name is Murad."

# L_size = len(L)
# string_size = len(string)

# print(L_size)
# print(string_size)

'''
The same result:

for symbol in string:
    print(symbol)

for i in range(len(string)):
    print(string[i])
'''


for i in range(len(L)):
    # number = L[i]
    # number **= 2
    # L[i] = number
    L[i] **= 2


print(L)

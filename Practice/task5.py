'''
Find the mean of a list of integers
'''

# L = [1, 5, 3, 6, 7, 1, 0]

L = []

# mean = sum(L) / len(L)

if len(L) == 0:
    print("Empty list! No mean!")
    exit()

summa = 0

for number in L:
    summa += number
    
mean = summa / len(L)

print(mean)
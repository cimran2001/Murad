'''
Swap the first and the last element of the list
'''

L = [1, 2, 3, 4, 5]

if len(L) < 1:
    exit()

L[0], L[-1] = L[-1], L[0]

# L[0], L[len(L) - 1] = L[len(L) - 1], L[0]

# temp = L[0]  # temp == 1
# L[0] = L[-1] # L == [5, 2, 3, 4, 5]
# L[-1] = temp # L == [5, 2, 3, 4, 1]

print(L)

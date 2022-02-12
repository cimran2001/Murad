'''
Swap two elements of the list by indexes
'''

L = [1, 2, 3, 4, 5] 

index1 = input("Enter the first index: ").strip()
if not index1.isnumeric():
    exit()
index1 = int(index1)


if index1 < -len(L) or index1 >= len(L):
    exit()

index2 = input("Enter the second index: ").strip()
if not index2.isnumeric():
    exit()
index2 = int(index2)

if index2 < -len(L) or index2 >= len(L):
    exit()

L[index1], L[index2] = L[index2], L[index1]

print(L)

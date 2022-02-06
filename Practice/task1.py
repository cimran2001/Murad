'''
Sort a list of integers
'''


# Unoptimized Bubble Sort


# L = [-7, 0, 1, 3, 3, 5, 100, 200]

# for i in range(len(L)):
#     for j in range(len(L) - 1):
#         if L[j] > L[j + 1]:
#             L[j], L[j + 1] = L[j + 1], L[j]

# print(L)


# Optimized Bubble Sort

# L = [200, 1, 5, 3, -7, 0, 100, 3]

L = [1, 2, 3, 5, 4]

swapped = True
while swapped:
    swapped = False
    for j in range(len(L) - 1):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            swapped = True

print(L)
    

# [1, 2, 3, 5, 4] swapped = False => True
# [1, 2, 3, 4, 5] swapped = False
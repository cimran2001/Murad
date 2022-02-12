'''
Find the median of a list of integers
'''

# L = [1, 5, 3, 6, 7, 1]

L = []

if len(L) == 0:
    print("Empty list! No median!")
    exit()

swapped = True
while swapped:
    swapped = False
    for j in range(len(L) - 1):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            swapped = True

# Odd
if len(L) % 2 == 1:
    middle_index = len(L) // 2
    print(f"Median: {L[middle_index]}")

# Even
else:  
    bigger = len(L) // 2
    smaller = bigger - 1
    
    median = (L[bigger] + L[smaller]) / 2
    print(f"Median: {median}")

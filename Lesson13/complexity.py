# Linear search => O(n)

L1 = [1, 5, 3, 8, 7, 6, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

item = 0
for i in range(len(L1)):
    print("L1 tested")
    if L1[i] == item:
        print(i)
        break

# Binary search => O(logn)

L2 = sorted(L1)
print(L2)

item = 8

start = 0
end = len(L2)

middle = (start + end) // 2
while L2[middle] != item:
    print("L2 tested")
    if L2[middle] > item:
        end = middle
    elif L2[middle] < item:
        start = middle + 1
    middle = (start + end) // 2

print(middle)


# Bubble sort => O(n^2)
L3 = L1.copy()

for i in range(len(L3)):
    for j in range(len(L3) - 1):
        if (L3[j] > L3[j + 1]):
            L3[j], L3[j + 1] = L3[j + 1], L3[j]
            
print(L3)



# Bubble sort + Binary search => O(n^2)

L3 = L1.copy()

for i in range(len(L3)):
    for j in range(len(L3) - 1):
        if (L3[j] > L3[j + 1]):
            L3[j], L3[j + 1] = L3[j + 1], L3[j]
            
print(L3)

item = 8

start = 0
end = len(L3)

middle = (start + end) // 2
while L3[middle] != item:
    print("L3 tested")
    if L3[middle] > item:
        end = middle
    elif L3[middle] < item:
        start = middle + 1
    middle = (start + end) // 2

print(middle)

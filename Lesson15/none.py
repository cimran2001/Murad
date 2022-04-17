def search(lst, num):
    for i in range(len(lst)):
        if lst[i] == num:
            return i
    return None
        
        

L = [1, 4, 3, 5, 5, 7]

index = search(L, 3)
if index is not None:
    L[index] = -1

print(L)

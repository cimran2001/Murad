L = [1, 5, 3, 6.0, 2, 3, "Hello", 10, 666, 10]


summa = 0

for element in L:
    if isinstance(element, float):
        continue
    if isinstance(element, str):
        break
    
    summa += element
else:
    print("ELSE")
    
print(summa)

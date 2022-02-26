L = [1, 2, 5, 6, 8, 3, 0]


def func():
    global L2
    L2 = L.sort()
    
    
L2 = L 

func()
print(L2)

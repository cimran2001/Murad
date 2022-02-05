L = []

# Methods

L.append(2)
L.append("Hi!")  # AND NOT L = L.Append(obj) !!!
L.append(3)
print(L)


additional = [1, 5, 4]
L.extend(additional)
print(L)


L.insert(2, "Hello!")
print(L)

# if L.count("Hi") > 0:
if "Hi!" in L:          # True
    index = L.index("Hi!")
    print(f"{index=}")  

# if L.count(0) > 0:
if 0 in L:              # False  
    index = L.index(0)
    print(f"{index=}")

print(f"{L.count('Hi!')=}")
print(f"{L.count(0)=}")


if 1 in L:
    index = L.index(1)
    # L.pop(index)
    element = L.pop(index)
    print(f"{L=}")
    print(f"{element=}")


# Remove first
if 3 in L:
    L.remove(3)
    print(f"{L=}")

# Remove all
while 3 in L:
    L.remove(3)


L.clear()
print(f"{L=}")

L.extend([5, 3, 7, 6, -1, -3, 0, 9])
print(f"{L=}")

L.reverse()
print(f"{L=}")

L.sort() # ascending
print(f"{L=}")

L.sort(reverse=True) # descending
print(f"{L=}")



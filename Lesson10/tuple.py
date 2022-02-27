# How swapping works

x, y = 3, 6
# This: x, y = y, x
# Becomes this:
temp = (y, x)
x, y = temp


# Size difference

primes_tuple = (2, 3, 5, 7, 11, 13, 17, 19)
primes_list  = [2, 3, 5, 7, 11, 13, 17, 19]

# print(primes_tuple.__sizeof__())
# print(primes_list.__sizeof__())

coords = (5, 3)
row, col = coords


# Usage in functions

Map = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [3, 5, 4, 3, 2],
    [1, 9, 6, 6, 3]
]

def get_place(Map, number):
    for row in range(len(Map)): # 0, 1, 2, 3
        for col in range(len(Map[0])): # 0, 1, 2, 3, 4
            if Map[row][col] == number:
                return row, col
    return None


coords = get_place(Map, 9)
if coords is not None:
    row, col = coords
    print(f"{row=}")
    print(f"{col=}")



# List in tuple

Tuple = (1, [2, 3])
print(Tuple)

Tuple[1].append(5)
print(Tuple)

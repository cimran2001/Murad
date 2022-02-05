# Empty list

list1 = list()
list2 = []

print(list1)
print(list2)


# Prefilled list

list1 = list("Hello, world!")
list2 = [1, 2, "Hello, world!", True, 3.14, 1 + 2j]

print(list1)
print(list2)


# List via generator

squares_list = [number ** 2 for number in range(1, 10)]
print(f"{squares_list=}")


alpha_list = [symbol for symbol in "Hello, world!" if symbol.isalpha()]
print(f"{alpha_list=}")

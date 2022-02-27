# # s = set()

# # s.add(1)
# # print(s)

# # s.add(2)
# # print(s)

# # s.add(2)
# # print(s)

# # s.add(3)
# # print(s)


# # List = [1, 2, 3, 5, 3, 6, 6, 9]
# # Set_of_List = set(List)
# # print(Set_of_List)

# # List_without_Dublicates = list(set(List))# list(Set_of_List)
# # print(List_without_Dublicates)

# # Set methods

# s = {1, 3, 5, 3, 4, 6}
# print(s)

# s.add(10)
# print(s)

# result = s.remove(3) 
# print(s)
# print(f"{result=}")

# s2 = s.copy()
# s2.add(100)
# print(s)
# print(s2)

# s = {1, 2, 4}

# s.discard(3) 
# print(s)

# Raises KeyError
# s.remove(3)
# print(s)


# Set operation

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Union => .union() method or |
result = s1 | s2
print(f"Union: {result}")

# result = s1.union(s2)
# print(f"Union: {result}")
# print(f"{s1=}")
# print(f"{s2=}")

# s1 |= s2 # s1 = s1 | s2
# s1 = s1.union(s2)
# s1.update(s2)
# s1.update([1, 2, 3, 4])
# s1.update((4, 4, 9, 10))

# Intersection => .intersection() method or & 
result = s1 & s2
print(f"Intersection: {result}")


# Difference => .difference() method or -
result1 = s1 - s2
result2 = s2 - s1

print(f"s1 - s2 = {result1}")
print(f"s2 - s1 = {result2}")

# Symmetric difference => .symmetric_difference() method or ^
result = s1 ^ s2
print(f"Symmetric difference: {result}")


result.clear()
print(result)
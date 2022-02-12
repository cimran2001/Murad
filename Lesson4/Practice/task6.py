'''
Create a new list using only unique elements of the given list
'''

# [1, 5, 3, 3, 2, 6, 2] => [1, 5, 6]

old_list = [1, 5, 3, 3, 2, 6, 2]

# new_list = []

# for number in old_list:
#     if old_list.count(number) == 1:
#         new_list.append(number)
        
new_list = [number for number in old_list if old_list.count(number) == 1]
        
print(new_list)

# [1, 5, 3, 3, 2, 6, 2] => [1, 5, 3, 2, 6]

# FIRST SOLUTION!
# new_list = []

# for number in old_list:
#     if number not in new_list:
#         new_list.append(number)

# SECOND SOLUTION!
# new_list = []
# for i in range(len(old_list)):
#     if old_list[i] not in old_list[:i]:
#         new_list.append(old_list[i])

# THIRD SOLUTION! (SIMPLIFIED SECOND SOLUTION)
new_list = [old_list[i] for i in range(len(old_list)) if old_list[i] not in old_list[:i]]

print(new_list)

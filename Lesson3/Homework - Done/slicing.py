base_list = [85, 34, 6, -3, 0, 6, 7, -5, 9]

# Non-positives
non_pos = [i for i in base_list if i <= 0]
print(f"a) {non_pos}")

# Step
steps = base_list[1::3]
print(f"b) {steps}")

# First three
first_three = base_list[:3]
print(f"c) {first_three}")

# Reversed
reversed1 = base_list[::-1]
reversed2 = list(reversed(base_list))

print(f"d) {reversed1}", end=" - ")
print(reversed1 == reversed2)

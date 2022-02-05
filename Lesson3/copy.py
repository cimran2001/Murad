x = 1
y = x

x += 2

print(f"{x=} {y=}")


x = "Hello, "
y = "World! "

x += y

print(f"{x=} {y=}")


x = [1, 5, 3]
# y = [i for i in x]
y = x.copy()

# x += [1, 3, 5]
x.append(1)

print(f"{x=} {y=}")


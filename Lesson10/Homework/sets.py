U = {i for i in range(2, 101)}

A = {i for i in U if i % 2 == 0}
B = {i for i in U if i % 3 == 0}
C = {i for i in U if i % 5 == 0 or i % 7 == 0}

a = A | B
b = A | C
c = B - C
d = A ^ B
e =  b | B

print(f"\t{a=}")
print(f"\t{b=}")
print(f"\t{c=}")
print(f"\t{d=}")
print(f"\t{e=}")

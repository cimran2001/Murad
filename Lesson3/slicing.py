# string = "Hello, world!"
# print(string)
# print(string[0:5:2]) # start = 0 : stop = len(list) : step = 1


L = [1, -3, 5, 8, 7, 10]
print(f"{L=}")
print(f"{L[:1]=}") 
print(f"{L[2:]=}")
print(f"{L[1::2]=}")

L[0] = 0
print(f"{L=}")

L[1:3] = [1, 2, 3]
print(f"{L=}")

del L[-1]
print(f"{L=}")

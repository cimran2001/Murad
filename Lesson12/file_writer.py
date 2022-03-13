# file = open("text.txt", "w+")    # write (a: append)

# file.write("Hello, world!\n")
# file.write("My name is Murad.\n")

# file.close()


# Binary mode: 
L = [1, 2, 3, 4]

with open("text.txt", "wb") as f:
    f.write(bytearray(L))


# Text mode:
# L = [1, 2, 3, 4, "5", "hello"]
# with open("text.txt", "w+") as f:
#     for i in L:
#         f.write(f"{i}\n")
# Case 1
with open("file.txt", "r") as f:
    while line := f.readline():
        print(line)


# Case 2
number = 12

if (square := number * number) > 100:
    print(square)

# file = open("text.txt", "r")    # read

# line = file.readline()
# while len(line) != 0:
#     print(line)
#     line = file.readline()
# file.close()

# # Binary
# with open("text.txt", "rb") as f:
#     data = f.read()
#     print(list(data))
    
# Text mode:     
with open("text.txt", "r") as f:
    text = f.readlines()
    print(text)

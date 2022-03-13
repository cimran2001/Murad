text = []

while True:
    line = input() + "\n"
    text.append(line.replace("#", ""))
    if "#" in line:
        break
    
with open("text.txt", "w+") as f:
    f.writelines(text)
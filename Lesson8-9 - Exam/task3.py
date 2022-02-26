string = "\t\t\tImran Jabrayilov,Urfat\n \t"

new_string = string.replace(',', ' ').casefold().strip().split(' ')[1].capitalize()

print(new_string)

string = "Jabrayilov"
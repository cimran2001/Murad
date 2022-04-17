import own_math as om


L = []
for i in range(5):
    number = int(input("Enter a number: "))
    L.append(number)
    
print(f"Summa = {om.summa(*L)}")

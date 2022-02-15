# PV = nRT

R = 8.31446261815324
n = 1

element_to_calc = input("What to calculate (P/V/T)? ").casefold()

if element_to_calc.startswith("v"):
    T = int(input("Enter temperature: "))
    P = float(input("Enter pression: "))
    V = n * R * T / P
    print(f"Volume: {V}")
elif element_to_calc.startswith("p"):
    T = int(input("Enter temperature: "))
    V = float(input("Enter volume: "))
    P = n * R * T / V
    print(f"Pression: {P}")
elif element_to_calc.startswith("t"):
    V = float(input("Enter volume: "))
    P = float(input("Enter pression: "))
    T = P * V / (n * R)
    print(f"Temperature: {T}")
else:
    print("Not a correct input. ")
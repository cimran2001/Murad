import math


mu = float(input("Enter μ: "))
sigma = float(input("Enter σ: "))
x = float(input("Enter x: "))

fraction = 1 / (sigma * math.sqrt(2 * math.pi)) # (2 * math.pi) ** 0.5

power = -((x - mu) ** 2) / (2 * sigma ** 2)

y = fraction * math.exp(power)

print(y)

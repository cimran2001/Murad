import sys
import math


mu = float(input("Enter mu: "))
sigma = float(input("Enter sigma: "))
x = float(input("Enter x: "))

if sigma == 0:
    print("Sigma cannot be zero.")
    sys.exit() # Correct way to end the program


coef = 1 / (sigma * math.sqrt(2 * math.pi))
power = - math.pow(x - mu, 2) / (2 * math.pow(sigma, 2))

y = coef * math.exp(power)
print(f"{y=}")

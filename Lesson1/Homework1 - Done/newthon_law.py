G = 6.674E-11 # 6.674 * 10^-11

sun_mass = 1.989E30
earth_mass = 5.972E24

distance = 149_597_870_000 

F = G * (sun_mass * earth_mass) / (distance * distance)

print("F =", F)

ns = [2, 3, 7, 9]

for n in ns:
    L = [i for i in range(1, 101) if i % n == 0]
    print(f"n = {n} => {L}")

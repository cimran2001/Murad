import random

L = [random.randint(1, 100) for _ in range(10)]

del L[-11.]

print(L)

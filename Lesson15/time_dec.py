from time import time

count: int

def counter(func):
    def inner(*args, **kwargs):
        global count
        value = func(*args, **kwargs)
        count += 1
        return value
    return inner


def cache(func):
    cache = {}
    def inner(n):
        if cache.get(n):
            return cache[n]
        
        value = func(n)
        cache[n] = value
        return value
    return inner



def time_elapsed(func):
    def inner(*args, **kwargs):
        start = time()
        value = func(*args, **kwargs)
        print(f"{time() - start} s.")
        return value
    return inner


@counter
@time_elapsed
@cache
def fib(n):
    if n <= 1:
        return n
    
    value = fib(n - 1) + fib(n - 2)
    return value

count = 0
result = fib(30)
print(f"{result=}")
print(f"{count=}")


count = 0
result = fib(30)
print(f"{result=}")
print(f"{count=}")

count = 0
result = fib(30)
print(f"{result=}")
print(f"{count=}")

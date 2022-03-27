cache = {}

def fib(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    if n <= 1:
        return n
    
    if cache.get(n):
        return cache[n]
    
    value = fib(n - 1) + fib(n - 2)
    cache[n] = value
    return value


print(fib(35))

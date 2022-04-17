def cache(func):
    cache = {}
    def inner(n):
        if cache.get(n):
            return cache[n]
        
        value = func(n)
        cache[n] = value
        return value
    return inner


@cache
def fib(n):
    if n <= 1:
        return n
    
    value = fib(n - 1) + fib(n - 2)
    return value


print(fib(100))

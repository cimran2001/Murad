# def summa(a, b, c = 0):
#     return a + b + c

# print(summa())
# print(summa(1))
# print(summa(1, 2))
# print(summa(1, 2, 3))
# print(summa(b = 3))
# print(summa(1, 2, 3))

def summa(*args):
    s = 0
    for i in args:
        s += i
    return s

print(summa(1, 5, 4, 3.2, 6.6))


def func(**kwargs):
    d = dict()
    for key in kwargs:
        d[key] = kwargs[key]
    print(d)


func(Azerbaijan="Baku", Japan="Tokyo")

result = (lambda x, y: x + y)(1, 2)
print(result)

result = (lambda *args: args)(1, 2, 3, 4)
print(result)

def summa(*args):
    s = 0
    for i in args: 
        s += i
    return s


def prod(*args):
    p = 1
    for i in args:
        p *= i
    return p


if __name__ == "__main__":
    assert summa(1, 2, 3) == 6
    assert prod(1, 2, 3) == 6

    print("EVERYTHING WORKS")

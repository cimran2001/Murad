def func1():
    def inner():
        global x
        x = 20
    
    x = 10
    inner()
    print(f"Func1: {x}")


def func2():
    def inner():
        nonlocal x
        x = 20
     
    x = 10
    inner()   
    print(f"Func2: {x}")


x = 5
func1()
func2()
print(f"Global: {x}")


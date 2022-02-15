# global
def func1():
    def inner():
        global x
        x = 20
    
    x = 10
    inner()
    print(f"Func1: {x}")


# nonlocal
def func2():
    def inner():
        nonlocal x
        x = 20
     
    x = 10 # nonlocal
    inner()   
    print(f"Func2: {x}")


x = 5 # global
func2()
print(f"Global: {x}")

# func1()
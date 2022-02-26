def myfunc():
    nonlocal x
    x += 2
    print(x)
    

x = 1
myfunc()

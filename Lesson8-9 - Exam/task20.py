def foo():
    bar()
    
def bar():
    foo()
    
    
print(foo())

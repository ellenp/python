# L → E → G → B
# Local → Enclosing → Global → Built-in

# +------------------------------+
# | Built-in Scope (B)           |  ← e.g., len(), print()
# +------------------------------+
# | Global Scope (G)             |  ← variables defined at top level of a .py file
# +------------------------------+
# | Enclosing Scope (E)          |  ← variables in outer/nested functions
# +------------------------------+
# | Local Scope (L)              |  ← variables defined in the current function
# +------------------------------+


x = "global"  # G

def outer():
    x = "enclosing"  # E

    def inner():
        x = "local"  # L
        print(x)

    inner()

outer()


x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        nonlocal x
        x = "modified by inner"
    
    inner()
    print("outer x:", x)

outer()
print("global x:", x)


x = "global"

def outer():
    def inner():
        global x
        x = "modified by inner"
    
    inner()
    print("outer can't see x")  # outer has no local x

outer()
print("global x:", x)

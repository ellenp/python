# L --> E --> G --> B
# Local --> Enclosing --> Global --> Built-in

# +------------------------------+
# | Built-in Scope (B)           |  ← e.g., len(), print()
# +------------------------------+
# | Global Scope (G)             |  ← variables defined at top level of a .py file
# +------------------------------+
# | Enclosing Scope (E)          |  ← variables in outer/nested functions
# +------------------------------+
# | Local Scope (L)              |  ← variables defined in the current function
# +------------------------------+

print("──────────────────────────────────────────────────────────────────────")
print("──────────────────── global - enclosing - local ──────────────────────")
print("──────────────────────────────────────────────────────────────────────")

x = "global"  # G

def outer():
    x = "enclosing"  # E

    def inner():
        x = "local"  # L
        print(x) # 3

    print(x) # 2
    inner()
    print(x) # 4

print(x) # 1
outer()
print(x) # 5


print("──────────────────────────────────────────────────────────────────────")
print("──────────────────── modify enclosing in local ───────────────────────")
print("──────────────────────────────────────────────────────────────────────")


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

print("──────────────────────────────────────────────────────────────────────")
print("───────────────────── modify global in local ─────────────────────────")
print("──────────────────────────────────────────────────────────────────────")


x = "global"

def outer():
    def inner():
        global x
        x = "modified by inner"
    
    inner()
    print("outer can't see x")  # outer has no local x

outer()
print("global x:", x)

print("──────────────────────────────────────────────────────────────────────")
print("───────────────────── never modify built-in ──────────────────────────")
print("──────────────────────────────────────────────────────────────────────")

# list = ["Japan", "North Korea", "South Korea", "China", "Taiwan"]
# city_list = list("Tokyo", "Kyoto", "Osaka", "Sapporo")
# TypeError: 'list' object is not callable

# sum = 1 + 8
# print(sum(x for x in range(100)))
# TypeError: 'int' object is not callable
# ───────────────────────────────────────────────────────────────────────────
# LAMBDA FUNCTIONS
# --> Use this when an anonymous function is required for a short period of time.
# 
# lambda arguments : expression
# ───────────────────────────────────────────────────────────────────────────

def anonymous_func(x):
    return x + 1

print("──────────────────────────────────────────────────────────────────────")
print("─────────────────── assign the result to var ─────────────────────────")
print("──────────────────────────────────────────────────────────────────────")

h = anonymous_func(10)

print("h(10): ", h)
print("type(h): ", type(h))

print("──────────────────────────────────────────────────────────────────────")
print("────────────── assign the entire function to var ─────────────────────")
print("──────────────────────────────────────────────────────────────────────")

g = anonymous_func

print("g(10): ", g(10))
print("type(g): ", type(g))

print("──────────────────────────────────────────────────────────────────────")
print("──────────────────────── using lambda ────────────────────────────────")
print("──────────────────────────────────────────────────────────────────────")

f = lambda x: x + 1

print("f(10): ", f(10))
print("type(f): ", type(f))

print("──────────────────────────────────────────────────────────────────────")
print("────────────────────── multiple arguments ────────────────────────────")
print("──────────────────────────────────────────────────────────────────────")

p = lambda x, y : x * y
print("p(5, 6):", p(5, 6))
print("p(9, 7):", p(9, 7))

# def p(x, y):
#    return x * y


print("──────────────────────────────────────────────────────────────────────")
print("────────────────────── multiple arguments ────────────────────────────")
print("──────────────────────────────────────────────────────────────────────")

def f(tax_percent):
  return lambda gross_pay : gross_pay - (gross_pay * (tax_percent/100))

level_1_tax_bracket = f(10)
level_2_tax_bracket = f(20)

print(level_1_tax_bracket(20000))
print(level_1_tax_bracket(25000))
print(level_2_tax_bracket(50000))
print(level_2_tax_bracket(60000))

# ───────────────────────────────────────────────────────────────────────────
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("people sorted by age: ", sorted(people, key=lambda person: person['age']))
print("people sorted by name: ", sorted(people, key=lambda person: person['name']))

# ───────────────────────────────────────────────────────────────────────────

# f = lambda x: print(x); x + 2

def f(x):
    print(x)
    return x + 2

# Not recommended in practice, but works
f = lambda x: (print(x), x + 2)[1]
print(f(5))  # Prints 5, then returns 7

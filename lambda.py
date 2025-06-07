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
print("──────────────────────────── closure ─────────────────────────────────")
print("──────────────────────────────────────────────────────────────────────")

# lambda inside a function

def f(tax_percent):
  return lambda gross_pay : gross_pay - (gross_pay * (tax_percent / 100))

level_1_tax_bracket = f(10)
level_2_tax_bracket = f(20)

print(level_1_tax_bracket(20000))
print(level_1_tax_bracket(25000))
print(level_2_tax_bracket(50000))
print(level_2_tax_bracket(60000))

# however, you might notice that tax_percent is a variable defined outside of lambda
# this is where the concept of closure comes.

# Closure has 3 requirements:

# 1. A nested function (function inside a function)
# 2. The inner function uses variables from the outer function
# 3. The outer function returns the inner function (or otherwise inner function escapes the outer function’s scope)

def outer():
    x = 10
    def inner():
        return x + 1
    return inner  # <--- returns the function itself

f = outer() # <--- here, you are assigning the function itself
print(f())  # Outputs 11
print(type(f))

# not a closure:

# Inner function uses variable from outer (x)
# Inner function is called immediately and doesn’t escape outer()
# Not a closure in the technical sense

def outer():
    x = 10
    def inner():
        return x + 1
    result = inner()
    return result

f = outer() # <--- here, you are assigning the function itself
print(f)  # Still outputs 11, but you did not have to pass emptry argument, because this is an int.
print(type(f))



# multiple variables accessed from the outer function:

def tax_calculator(tax_percent):
    pag_ibig = 100
    def calc_net_pay(gross_pay):
        return gross_pay - (gross_pay * (tax_percent / 100)) - pag_ibig
    return calc_net_pay

level_a_tax_bracket = tax_calculator(10)
level_b_tax_bracket = tax_calculator(20)

print(level_a_tax_bracket(20000))
print(level_a_tax_bracket(25000))
print(level_b_tax_bracket(50000))
print(level_b_tax_bracket(60000))

# proof that variables are still being carried around:

print(level_a_tax_bracket.__closure__)  # shows the captured variables
print(level_a_tax_bracket.__closure__[0].cell_contents)  # outputs: 100 - pag_ibig
print(level_a_tax_bracket.__closure__[1].cell_contents)  # outputs: 10 - tax_percent
# print(level_a_tax_bracket.__closure__[2].cell_contents)  # outputs: IndexError: tuple index out of range

print(level_b_tax_bracket.__closure__)  # shows the captured variables
print(level_b_tax_bracket.__closure__[0].cell_contents)  # outputs: 100 - pag_ibig
print(level_b_tax_bracket.__closure__[1].cell_contents)  # outputs: 20 - tax_percent
# print(level_b_tax_bracket.__closure__[2].cell_contents)  # outputs: IndexError: tuple index out of range

# Can't I just use class and let multiple variables handle this behavior?

# 1. Use class if you need multiple methods, closure if it's just 1 simple behavior.
# 2. Use class if state needs to be stored over time, closure for quick capture.

def make_retry_limiter(max_retries):
    attempts = 0
    def should_retry():
        nonlocal attempts
        if attempts < max_retries:
            attempts += 1
            return True
        return False
    return should_retry

can_retry = make_retry_limiter(3)

while can_retry():
    print("Trying...")
# After 3 tries, stops printing


def make_tracker():
    count = 0
    def tracker():
        nonlocal count
        count += 1
        print(f"Called {count} times")
    return tracker


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

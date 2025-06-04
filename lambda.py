# ───────────────────────────────────────────────────────────────────────────
# LAMBDA FUNCTIONS
# --> Use this when an anonymous function is required for a short period of time.
# lambda arguments : expression
# ───────────────────────────────────────────────────────────────────────────

a_variable_that_holds_the_call_to_an_unnamed_function_that_simply_adds_10_to_your_input = lambda num : num + 10
print(a_variable_that_holds_the_call_to_an_unnamed_function_that_simply_adds_10_to_your_input(5))
print(type(a_variable_that_holds_the_call_to_an_unnamed_function_that_simply_adds_10_to_your_input))
# <class 'function'>

# ───────────────────────────────────────────────────────────────────────────

product = lambda multiplicand_whatever, multiplier_whatever : multiplicand_whatever * multiplier_whatever
print(product(5, 6))

# def product(multiplicand_whatever, multiplier_whatever):
#    return multiplicand_whatever * multiplier_whatever

# ───────────────────────────────────────────────────────────────────────────

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

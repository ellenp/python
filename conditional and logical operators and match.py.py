"""
───────────────────────────────────────────────────────────────────────────
───────────────────────────────────────────────────────────────────────────
CONDITIONALS
a == b
a != b
a < b
a <= b
a > b
a >= b
───────────────────────────────────────────────────────────────────────────
───────────────────────────────────────────────────────────────────────────
"""

"""
───────────────────────────────────────────────────────────────────────────
if <condition>:
elif <condition>:
else:

One Line:
if <condition>: <do this>
───────────────────────────────────────────────────────────────────────────
"""

a = 200
b = 200

if b == a:
    print("a and b are equal.")

if b == a: print("a and b are equal.")

if b > a:
    print("b is greater than a.")
elif b < a:
    print("b is lesser than a.")
else:
    print("a and b are equal.")

if b > a: print("b is greater than a.")
elif b < a: print("b is lesser than a.")
else: print("a and b are equal.")

# if b > a: print("b is greater than a.") elif b < a: print("b is lesser than a.") else: print("a and b are equal.")
# SyntaxError: invalid syntax

# ───────────────────────────────────────────────────────────────────────────
# Ternary operator or Conditional expression
#
# <do this> if <condition> else <do this>
# <do this> if <condition> else <do this> if <condition> else <do this
# ───────────────────────────────────────────────────────────────────────────

a = 200
b = 200
print("b is greater than a.") if b > a else print("b is lesser than a.") if b < a else print("a and b are equal.")

# print("b is greater than a.") if b > a else
# print("b is lesser than a.") if b < a else
# print("a and b are equal.")
# SyntaxError: invalid syntax

# print("b is greater than a.") if b > a
# SyntaxError: expected 'else' after 'if' expression

"""
───────────────────────────────────────────────────────────────────────────
LOGICAL OPERATORS
and
or
not
───────────────────────────────────────────────────────────────────────────
"""

# ───────────────────────────────────────────────────────────────────────────
# PASS
# ───────────────────────────────────────────────────────────────────────────

a = 33
b = 200

if b > a:
  print("This statement, BEFORE PASS, will print.")
  pass
  print("This statement, AFTER PASS, will print.")

print("This one, OUTSIDE THE CONTEXT OF IF, will also print.")

# ───────────────────────────────────────────────────────────────────────────
# Why will you need pass?
# ───────────────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────────────────────
# 1. Do nothing for now, implement later.
# ───────────────────────────────────────────────────────────────────────────

def process_payment():
    pass  # To be implemented later

class PaymentProcessor:
    pass  # Define structure first, implement details later

def handle_event(event):
    if event == "click":
        print("Clicked!")
    elif event == "hover":
        pass  # We ignore hover for now
    else:
        print("Unhandled event:", event)

# ───────────────────────────────────────────────────────────────────────────
# 2. Abstraction
# ───────────────────────────────────────────────────────────────────────────

class Animal:
    def make_sound(self):
        pass  # Subclass should implement this

"""
───────────────────────────────────────────────────────────────────────────
match <expression>:
  case <1st_match_of_expression>:
    <do this>
  case <2nd_match_of_expression>:
    <do this>
  case <3rd_match_of_expression>:
    <do this>
  case _:
    <do this by default>
───────────────────────────────────────────────────────────────────────────
"""

───────────────────────────────────────────────────────────────────────────
# Piping and Guards
───────────────────────────────────────────────────────────────────────────

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


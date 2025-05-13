# ───────────────────────────────────────────────────────────────────────────
# SHOWING OUTPUTS
# ───────────────────────────────────────────────────────────────────────────
print(4) 
print("Number: ",4) # Oh! we used multi-parameter print.
print ("Hello!") # You can even have a space
print('─' * 10, "This is like a separator", '─' * 10)
print('─' * 20, "This is like a separator", '─' * 20)


# ───────────────────────────────────────────────────────────────────────────
# COMMENTS
# ───────────────────────────────────────────────────────────────────────────

# single line comment
#you actually don't need the space


"""
multi
line
comment
"""

"""how about this"""

import sys

print(sys.version) # This is a comment after a statement.

# ───────────────────────────────────────────────────────────────────────────
# VARIABLES
# IMPORTANT:
#     - no need to declare variable (separately)
#     - no need to define data type
#     - just declare and assign
# OTHERS:
# A variable name must start with a letter or the underscore character.
# A variable name cannot start with a number.
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# Variable names are case-sensitive (age, Age and AGE are three different variables).
# A variable name cannot be any of the Python keywords.
# ───────────────────────────────────────────────────────────────────────────

num = 1
NUM = 2
NuM = 3
_num = 4
num_1 = 5

print(num)
print(NUM)
print(NuM)
print(_num)
print(num_1)

# my-num = 6
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

# my&num = 7
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

# 4h = 8
# SyntaxError: invalid decimal literal

# and = 9
# SyntaxError: invalid syntax


# ───────────────────────────────────────────────────────────────────────────
# variables and strings
# ───────────────────────────────────────────────────────────────────────────

str1 = "This is a string."
str2 = 'This is another string.'

str3 = """This
is
a
multi
line
string."""


str4 = '''This
is
antother
multi
line
string.'''


print(str1)
print(str2)
print(str3)
print(str4)


# ───────────────────────────────────────────────────────────────────────────
# type casting variables
# ───────────────────────────────────────────────────────────────────────────

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print("x type: ", type(x))
print("y type: ", type(y))
print("z type: ", type(z))


# ───────────────────────────────────────────────────────────────────────────
# MULTIPLE VARIABLE ASSIGNMENT
# ───────────────────────────────────────────────────────────────────────────
name, age, height = "Juan", 18, 180
print(name)
print(age)
print(height)

grade_student_14 = grade_student_25 = grade_student_32 = 100
print (grade_student_14)
print (grade_student_25)
print (grade_student_32)

print('Hello', 'World') # Output will have a space
print('Hello' + 'World') # Output does not have a space, this is just like a concatenation
# print('Age is ' + 5) # TypeError: can only concatenate str (not "int") to str
print('Age is ', 5) # This will work.
# ───────────────────────────────────────────────────────────────────────────
# UNPACKING
# ───────────────────────────────────────────────────────────────────────────

array = ["apple", "banana", "cherry"]
arr1, arr2, arr3 = array
print(arr1)
print(arr2)
print(arr3)

# ───────────────────────────────────────────────────────────────────────────
# global variables
# ───────────────────────────────────────────────────────────────────────────
global_var = "awesome!"

def modify_a_global_var_not_working():
  global_var = "very very slow."

modify_a_global_var_not_working()

print("Python is " + global_var)

def modify_a_global_var():
  global global_var
  global_var = "fantastic!"

modify_a_global_var()

print("Python is " + global_var)










# ───────────────────────────────────────────────────────────────────────────
# ───────────────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────────────────────
# ───────────────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────────────────────
# ───────────────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────────────────────
# ───────────────────────────────────────────────────────────────────────────



# ───────────────────────────────────────────────────────────────────────────
# INDENTATION
# ───────────────────────────────────────────────────────────────────────────

"""
if 5 > 2:
print("Five is greater than two!")

IndentationError: expected an indented block after 'if' statement on line 1
"""

"""
if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 

This will work.
"""

"""
if 5 > 2:
 print("Five is greater than two!") 
        print("Five is greater than two!")

IndentationError: unexpected indent
"""

"""
if 5 > 2:
    print("Five is greater than two!") 
     print("Five is greater than two!")

IndentationError: unexpected indent
"""
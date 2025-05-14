"""
───────────────────────────────────────────────────────────────────────────
Text Type:		str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:		set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:		NoneType
───────────────────────────────────────────────────────────────────────────
"""

# ───────────────────────────────────────────────────────────────────────────
# STRING
# ───────────────────────────────────────────────────────────────────────────

double_quoted_string = "Hello World"
single_quoted_string = 'Hello World'

print("double_quoted_string: ", double_quoted_string)
print("single_quoted_string: ", single_quoted_string)

double_quoted_string_2 = str("Hello World") # explicit type casting
single_quoted_string_2 = str('Hello World') # explicit type casting

print("double_quoted_string_2: ", double_quoted_string_2)
print("single_quoted_string_2: ", single_quoted_string_2)

single_quote_inside_a_string = "My name is 'Alexa'"
double_quote_inside_a_string = 'My name is "Lucas"'

print("single_quote_inside_a_string: ", single_quote_inside_a_string)
print("double_quote_inside_a_string: ", double_quote_inside_a_string)

# import sys
# print(sys.maxsize)
# 9,223,372,036,854,775,807 - 64 bit systems
# 9,223,372,036,854,775,758 daw (49 diff)


"""
───────────────────────────────────────────────────────────────────────────
3 TYPES OF NUMBERS:
	1. INT
		- whole number, positive or negative, unlimited length
		- (unbounded)
		- SOURCE: https://docs.python.org/3/whatsnew/3.0.html#integers
	2. FLOAT
		- with decimal value, positive or negative, unbounded.
		- Can be used with e to denote power of 10
		- e or E (case insensitive)
	3. COMPLEX

───────────────────────────────────────────────────────────────────────────
"""


# ───────────────────────────────────────────────────────────────────────────
# INT
# ───────────────────────────────────────────────────────────────────────────

num_1 = 20
num_2 = int(20) # explicit type casting

print("num_1: ", num_1)
print("num_2: ", num_2)

# ───────────────────────────────────────────────────────────────────────────
# FLOAT
# ───────────────────────────────────────────────────────────────────────────

float_1 = 1.10
float_2 = float(1.10) # explicit type casting
float_3 = 1.0
float_4 = -35.59
float_5 = 35e3
float_6 = 12E4
float_7 = -87.7e100

print("float_1: ", float_1)
print("float_2: ", float_2)
print("float_3: ", float_3)
print("float_4: ", float_4)
print("float_5: ", float_5)
print("float_6: ", float_6)
print("float_7: ", float_7)

# ───────────────────────────────────────────────────────────────────────────
# COMPLEX
# ───────────────────────────────────────────────────────────────────────────

complex_num_1 = 1j
complex_num_2 = complex(1j) # explicit type casting

print("complex_num_1: ", complex_num_1)
print("complex_num_2: ", complex_num_2)

num = 3 + 4j
print("num: ", num)
print("num.real: ", num.real)
print("num.imag: ", num.imag)


"""
───────────────────────────────────────────────────────────────────────────
Why does Python use j instead of i for imaginary number?

* Python was heavily influenced by engineering and scientific computing communities (like NumPy and MATLAB).
* In electrical engineering, the letter i typically represents current, so they use j for the imaginary unit to avoid confusion.
* Python aligns with tools like MATLAB, Octave, Scilab to make it easier for engineers and scientists to adopt and switch between languages.

SOURCES:
1. https://bugs.python.org/issue10562
2. Stubbings, George Wilfred (1945). Elementary vectors for electrical engineers. London: I. Pitman. p. 69.
3. Boas, Mary L. (2006). Mathematical Methods in the Physical Sciences (3rd ed.). New York [u.a.]: Wiley. p. 49. ISBN 0-471-19826-9.
───────────────────────────────────────────────────────────────────────────
"""

# ───────────────────────────────────────────────────────────────────────────
# TYPE CASTING
# ───────────────────────────────────────────────────────────────────────────

int_num = 4
float_num = 5.999999
complex_num = 4j

# convert from int to float:
int_to_float = float(int_num)

# convert from int to complex:
int_to_complex = complex(int_num)

# convert from float to int:
float_to_int = int(float_num)

# convert from float to complex:
float_to_complex = complex(float_num)

print("int_to_float: ",int_to_float)
print("int_to_complex: ",int_to_complex)
print("float_to_int: ", float_to_int)
print("float_to_complex: ", float_to_complex)

# convert from complex to int:
# complex_to_int = int(complex_num)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# convert from complex to float:
# complex_to_float = float(complex_num)
# TypeError: float() argument must be a string or a real number, not 'complex'

"""
───────────────────────────────────────────────────────────────────────────
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:		set, frozenset

───────────────────────────────────────────────────────────────────────────
"""

# ───────────────────────────────────────────────────────────────────────────
# LIST
# ───────────────────────────────────────────────────────────────────────────

fruit_list_1 = ["mango", "banana", "watermelon", "papaya", "avocado", "pineapple"]
fruit_list_2 = list(("mango", "banana", "watermelon", "papaya", "avocado", "pineapple")) # explicit type casting

print("fruit_list_1:", fruit_list_1)
print("fruit_list_2:", fruit_list_2)

#retrieve entries

fruit_list_entry_1 = fruit_list_1[0]
fruit_list_entry_2 = fruit_list_1[1]
fruit_list_entry_3 = fruit_list_1[2]
fruit_list_entry_4 = fruit_list_1[3]
fruit_list_entry_5 = fruit_list_1[4]
fruit_list_entry_6 = fruit_list_1[5]

print("fruit_list_entry_1: ", fruit_list_entry_1)
print("fruit_list_entry_2: ", fruit_list_entry_2)
print("fruit_list_entry_3: ", fruit_list_entry_3)
print("fruit_list_entry_4: ", fruit_list_entry_4)
print("fruit_list_entry_5: ", fruit_list_entry_5)
print("fruit_list_entry_6: ", fruit_list_entry_6)

# negative indexing

print("fruit_list_last_item: ", fruit_list_1[-1])
print("fruit_list_2nd_last_item: ", fruit_list_1[-2])
print("fruit_list_3rd_last_item: ", fruit_list_1[-3])
print("fruit_list_4th_last_item: ", fruit_list_1[-4])
print("fruit_list_5th_last_item: ", fruit_list_1[-5])
print("fruit_list_6th_last_item: ", fruit_list_1[-6])
# print("fruit_list_7th_last_item: ", fruit_list_1[-7])
# IndexError: list index out of range


# range of indexes

print("index 2 (included) to 5 (excluded): ", fruit_list_1[2:5])
print("beginning to 4 (excluded): ", fruit_list_1[:4])
print("index 2 to end: ", fruit_list_1[2:])
print("4th to last (included) to 2nd to last (excluded): ", fruit_list_1[-4:-2])

# in

if "apple" in fruit_list_1:
	print("apple is in the list.")
else:
	print("apple is not in the list")

if "avocado" in fruit_list_1:
	print("avocado is in the list.")
else:
	print("avocado is not in the list")

# length

list_length = len(fruit_list_1)
print("list_length:", list_length)

# diff data type
list_3 = ["Juan", 2, 45.0, 7j, True]
print("list_3: ", list_3)


print("length of list / the number of items in a list is retrieved by len():", len(fruit_list_1))

# ───────────────────────────────────────────────────────────────────────────
# TUPLE
# ───────────────────────────────────────────────────────────────────────────

# x = tuple(("apple", "banana", "cherry"))	tuple	

# ───────────────────────────────────────────────────────────────────────────
# RANGE
# ───────────────────────────────────────────────────────────────────────────

# x = range(6)	range	


# x = dict(name="John", age=36)	dict	
# x = set(("apple", "banana", "cherry"))	set	
# x = frozenset(("apple", "banana", "cherry"))	frozenset	

# ───────────────────────────────────────────────────────────────────────────
# BOOL
# What evaluates to False?
# Empty values, such as (), [], {}, "", the number 0, and the value None.
# Of course, the value False evaluates to False.
# ───────────────────────────────────────────────────────────────────────────

bool1 = True
bool2 = False

# bool1 = true
# NameError: name 'true' is not defined. Did you mean: 'True'?

# bool2 = false
# NameError: name 'false' is not defined. Did you mean: 'False'?

print("bool1: ", bool1)
print("bool2: ", bool2)

bool_sum = bool1 + bool2
bool_diff = bool1 - bool2
bool_prod = bool1 * bool2

# bool_div = bool1 / bool2
# ZeroDivisionError: division by zero

bool_div = bool2 / bool1

print("bool_sum: ", bool_sum)
print("bool_diff: ", bool_diff)
print("bool_prod: ", bool_prod)
print("bool_div: ", bool_div)

any_string = "Hi"
pos_num = 1
neg_num = 1

zero_string = "0"
empty_string = ""
zero = 0
neg_zero = -0

print("any_string: ", bool(any_string))
print("zero_string: ", bool(zero_string))
print("pos_num: ", bool(pos_num))
print("neg_num: ", bool(neg_num))
print("empty_string: ", bool(empty_string))
print("zero: ", bool(zero))
print("neg_zero???: ", bool(neg_zero))


# x = bytes(5)	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))



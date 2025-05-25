
# ───────────────────────────────────────────────────────────────────────────
# HOW TO ACCESS ITEMS
# ───────────────────────────────────────────────────────────────────────────

fruit_list = ["mango", "banana", "watermelon", "papaya", "avocado", "pineapple"]

print("fruit_list:", fruit_list)

#retrieve entries

fruit_list_entry_1 = fruit_list[0]
fruit_list_entry_2 = fruit_list[1]
fruit_list_entry_3 = fruit_list[2]
fruit_list_entry_4 = fruit_list[3]
fruit_list_entry_5 = fruit_list[4]
fruit_list_entry_6 = fruit_list[5]

print("fruit_list_entry_1: ", fruit_list_entry_1)
print("fruit_list_entry_2: ", fruit_list_entry_2)
print("fruit_list_entry_3: ", fruit_list_entry_3)
print("fruit_list_entry_4: ", fruit_list_entry_4)
print("fruit_list_entry_5: ", fruit_list_entry_5)
print("fruit_list_entry_6: ", fruit_list_entry_6)

# negative indexing

print("fruit_list_last_item: ", fruit_list[-1])
print("fruit_list_2nd_last_item: ", fruit_list[-2])
print("fruit_list_3rd_last_item: ", fruit_list[-3])
print("fruit_list_4th_last_item: ", fruit_list[-4])
print("fruit_list_5th_last_item: ", fruit_list[-5])
print("fruit_list_6th_last_item: ", fruit_list[-6])
# print("fruit_list_7th_last_item: ", fruit_list[-7])
# IndexError: list index out of range


# range of indexes

print("index 2 (included) to 5 (excluded): ", fruit_list[2:5])
print("beginning to 4 (excluded): ", fruit_list[:4])
print("index 2 to end: ", fruit_list[2:])
print("4th to last (included) to 2nd to last (excluded): ", fruit_list[-4:-2])

# in

if "apple" in fruit_list:
	print("apple is in the list.")
else:
	print("apple is not in the list")

if "avocado" in fruit_list:
	print("avocado is in the list.")
else:
	print("avocado is not in the list")

# ───────────────────────────────────────────────────────────────────────────
# LENGTH
# ───────────────────────────────────────────────────────────────────────────

list_length = len(fruit_list)
print("list_length:", list_length)

# ───────────────────────────────────────────────────────────────────────────
# DATATYPES
# ───────────────────────────────────────────────────────────────────────────

list_3 = ["Juan", 2, 45.0, 7j, True]
print("list_3: ", list_3)


# ───────────────────────────────────────────────────────────────────────────
# MODIFY VALUES
# ───────────────────────────────────────────────────────────────────────────

# market ran out of "avocado". we will use "coconut".
fruit_list[4] = "coconut"
print("fruit_list:", fruit_list)

# wait, "banana", "watermelon", "papaya" are hard to find? Okay, let's just make "mango float" since we have "mango"
# we're replacing 3 items with just 2.
# start at the index you want (inclusive), end at the index + 1 (exclusives)
fruit_list[1:4] = ["graham crackers", "milk"]
print("fruit_list:", fruit_list)

# ───────────────────────────────────────────────────────────────────────────
# ADD VALUES
# ───────────────────────────────────────────────────────────────────────────

# we will need "crushed graham". Insert it between index 1, "graham crackers", and index 2, "milk" 
fruit_list.insert(2,"crushed graham")
print("fruit_list:", fruit_list)

# Maria bought mango and graham crackers.
fruit_list.extend(["mango", "graham crackers"])
print("fruit_list:", fruit_list)

# Julio also bought mango and graham crackers. But this time, let's store it in another list, cause Julio's main char LOL
julio_fruits = ["mango", "graham crackers"]
fruit_list.extend(julio_fruits)
print("fruit_list:", fruit_list)


# ───────────────────────────────────────────────────────────────────────────
# REMOVE VALUES
# ───────────────────────────────────────────────────────────────────────────

# we have a "milk", we don't need "coconut"
fruit_list.remove("coconut")
print("fruit_list:", fruit_list)

# last item does not make sense. let's remove it.
fruit_list.pop()
print("fruit_list:", fruit_list)

# actually, you can store the pop to a variable.
last_fruit = fruit_list.pop()
print("last_fruit:", last_fruit)
print("fruit_list:", fruit_list)

# you can also pop based on index
index_1_fruit = fruit_list.pop(1)
print("index_1_fruit:", index_1_fruit)
print("fruit_list:", fruit_list)


# ───────────────────────────────────────────────────────────────────────────
# LIST COMPREHENSION

# newlist = [expression for item in iterable if condition == True]

# newlist = []
# for item in iterable:
#   if condition == True:
#     newlist.append(expression)

# ───────────────────────────────────────────────────────────────────────────

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits if "n" in x]

print(newlist)


fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = []

for x2 in fruits2:
	if "n" in x2:
		newlist2.append(x2.upper())

print(newlist2)

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)


fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = []

for x2 in fruits2:
	newlist2.append(x2.upper())

print(newlist2)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Example: "Return the item if it is not banana, if it is banana return orange".

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)


fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = []

for x2 in fruits2:
    if x2 != "banana":
        newlist2.append(x2)
    else:
        newlist2.append("orange")

print(newlist2)



# ───────────────────────────────────────────────────────────────────────────
# LIST SORTING
# ───────────────────────────────────────────────────────────────────────────


fruit_list = ["mango", "banana", "watermelon", "papaya", "avocado", "pineapple"]
print("fruit_list.sort(): ",fruit_list.sort())
print("fruit_list: ", fruit_list)
print("fruit_list.sort(reverse = True): ",fruit_list.sort(reverse = True))
print("fruit_list: ", fruit_list)


def myfunc(n):
  return len(n)

fruit_list.sort(key = myfunc)
print("fruit_list: ", fruit_list)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# ───────────────────────────────────────────────────────────────────────────
# LIST COPY
# ───────────────────────────────────────────────────────────────────────────


fruit_list = ["mango", "banana", "watermelon", "papaya", "avocado", "pineapple"]
fruit_salad = fruit_list
print("fruit_list: ", fruit_list)
print("fruit_salad: ", fruit_salad)

fruit_list.pop()

print("fruit_list: ", fruit_list)
print("fruit_salad: ", fruit_salad)

fruit_list = ["aaaaaaah your data", "is corrupted", "xnc,nxb75?/!&*kdjf12348"]

print("fruit_list: ", fruit_list)
print("fruit_salad: ", fruit_salad)
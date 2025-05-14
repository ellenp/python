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

# length

list_length = len(fruit_list)
print("list_length:", list_length)

# diff data type
list_3 = ["Juan", 2, 45.0, 7j, True]
print("list_3: ", list_3)
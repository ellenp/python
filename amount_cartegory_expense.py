category_list = {"FOOD", "TRANSPORTATION", "GROCERY"}

print("-"*50)
print(f"CATEGORIES: {category_list}")
print("-"*50)

expenses = []

while True:
	amount = input("Input mount: ")

	while True:
		category = input("Input category: ")
		if category in category_list:
			break
		else:
			print("Wrong category!")
			continue

	description = input("Input description: ")

	expenses.append([amount, category, description])

	while True:
		continue_flag = input("Do you want to add another item? YES/NO: ")
		if continue_flag == "YES" or continue_flag == "NO":
			break
		else:
			print("Wrong input!")
			continue
	if continue_flag == "YES":
		continue
	else:
		break


print("-"*50)
print("expenses: ", expenses)
print("-"*50)
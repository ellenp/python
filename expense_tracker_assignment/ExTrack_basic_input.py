category_list = {"FOOD", "TRANSPORTATION", "GROCERY"}

print("─"*50)
print(f"CATEGORIES: {category_list}")
print("─"*50)


amount = input("Input mount: ")

while True:
	category = input("Input category: ")
	if category in category_list:
		break
	else:
		print("Wrong category!")
		continue

description = input("Input description: ")

print("─"*50)
print("amount: ", amount)
print("category: ", category)
print("description: ", description)
print("─"*50)
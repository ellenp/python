# how duplicate entries behave:
tropical_fruit_set = {"mango", "banana", "pineapple", "watermelon", "mango"}

print("tropical_fruit_set: ", tropical_fruit_set)


# use case

# fast retrieval: O(1)

s = set([1, 2, 2, 3])
print(s)  # Output: {1, 2, 3}

2 in s

# avoid duplicate entries
raw_emails = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
    "bob@example.com"
]

# Remove duplicates using a set
unique_emails = set(raw_emails)

# Now you can send one email per person
for email in unique_emails:
    send_newsletter(email)


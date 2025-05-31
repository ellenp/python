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

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# ───────────────────────────────────────────────────────────────────────────
# The values True and 1 are considered the same value.
# The same goes for False and 0.
# ───────────────────────────────────────────────────────────────────────────

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

print("set1: ", set1)
print("set2: ", set2)
# ───────────────────────────────────────────────────────────────────────────
# INTERSECTION - to get common items
# ───────────────────────────────────────────────────────────────────────────


skills_required = {"Python", "SQL", "Git", "Docker"}
applicant_skill = {"Python", "Git", "HTML"}

skill_passed = skills_required & applicant_skill

print("skill_passed: ", skill_passed)

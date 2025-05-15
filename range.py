"""
───────────────────────────────────────────────────────────────────────────

range(start, stop, step)

	start: (Optional) The beginning of the sequence. Defaults to 0 if not specified.

	stop: (Required) The end of the sequence (not included in the result).

	step: (Optional) The difference between each number in the sequence. Defaults to 1.

───────────────────────────────────────────────────────────────────────────
"""

print("printing simple range from 0 to 4...")
for i in range(5):
    print(i)

print("printing simple range from 2 to 6...")
for i in range(2, 7):
    print(i)

print("printing odd numbers...")
for i in range(1, 10, 2):
    print(i)

print("printing even numbers...")
for i in range(2, 10, 2):
    print(i)

print("print stuff in reverse...")
for i in range(10, 0, -2):
    print(i)


print("you can also do this...")
print(list(range(5)))
print(tuple(range(5)))
print(set(range(5)))

# ───────────────────────────────────────────────────────────────────────────
# Use cases
# ───────────────────────────────────────────────────────────────────────────

# Batch Processing / Looping Over Fixed Iterations
print("Processing files named file1.txt to file10.txt...")

# for i in range(1, 11):
#     filename = f"file{i}.txt"
#     print(f"Processing {filename}")

# ───────────────────────────────────────────────────────────────────────────

# Creating Dummy/Test Data
print("Generating 100 fake user IDs...")
user_ids = [f"user_{i}" for i in range(1, 101)]
print(user_ids[:5])  # Just showing the first 5

# ───────────────────────────────────────────────────────────────────────────

# Scheduling Tasks
print("Running job every hour from 8 AM to 5 PM...")
for hour in range(8, 18):
    print(f"Scheduled task at {hour}:00")

# ───────────────────────────────────────────────────────────────────────────

# Working with Grids or Pixels (e.g., Image Processing)
print("Iterating over a 5x5 image grid...")
for x in range(5):
    for y in range(5):
        print(f"Pixel at ({x},{y})")

# ───────────────────────────────────────────────────────────────────────────

# Scientific Simulations
print("Simulate a process for 1000 steps...")
# for step in range(1000):
#     # simulate step logic
#     pass

# ───────────────────────────────────────────────────────────────────────────

# Random Sampling from a Dataset
print("Combining range() with tools like random.sample()...")
print("Printing 10 indices from 0-999")

import random

sample_indices = random.sample(range(1000), 10)
print(sample_indices)
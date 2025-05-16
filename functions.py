# ───────────────────────────────────────────────────────────────────────────
# 1. Use Descriptive Names
# Choose meaningful names for your functions and parameters
# to make your code self-explanatory.
# ───────────────────────────────────────────────────────────────────────────

# Bad
def calc(a, b):
    return a + b

# Good
def calculate_sum(number1, number2):
    return number1 + number2

# ───────────────────────────────────────────────────────────────────────────
# 2. Keep Functions Focused (Single Responsibility Principle)
# A function should do one thing and do it well.
# Avoid cramming multiple tasks into one function.
# ───────────────────────────────────────────────────────────────────────────

# Bad
def process_data(data):
    clean_data = [d.strip() for d in data]
    filtered_data = [d for d in clean_data if len(d) > 3]
    return filtered_data

# Good
def clean_data(data):
    return [d.strip() for d in data]

def filter_data(data):
    return [d for d in data if len(d) > 3]


# ───────────────────────────────────────────────────────────────────────────
# 3. Use Default Arguments Wisely
# Default arguments make your functions more flexible and user-friendly.
# ───────────────────────────────────────────────────────────────────────────
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!



# ───────────────────────────────────────────────────────────────────────────
# 4. Leverage Type Hints
# Type hints improve code readability and help catch errors early.
# ───────────────────────────────────────────────────────────────────────────

def multiply_numbers(a: int, b: int) -> int:
    return a * b



# ───────────────────────────────────────────────────────────────────────────
# 5. Write Docstrings
# Document your functions to explain their purpose, parameters, and return values.
# ───────────────────────────────────────────────────────────────────────────

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2


# ───────────────────────────────────────────────────────────────────────────
# 6. Avoid Hardcoding Values
# Use parameters or constants instead of hardcoding values.
# ───────────────────────────────────────────────────────────────────────────

# Bad
def calculate_discount(price):
    return price * 0.10

# Good
DISCOUNT_RATE = 0.10
def calculate_discount(price, discount_rate=DISCOUNT_RATE):
    return price * discount_rate

# ───────────────────────────────────────────────────────────────────────────
# 7. Handle Errors Gracefully
# Use try-except blocks to make your functions robust.
# ───────────────────────────────────────────────────────────────────────────

def divide_numbers(dividend: float, divisor: float) -> float:
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return float('inf')  # Return infinity for division by zero


# ───────────────────────────────────────────────────────────────────────────
# 8. Keep Functions Short
# Aim for functions that fit within 20-30 lines.
# If it’s longer, consider breaking it into smaller functions.
# ───────────────────────────────────────────────────────────────────────────



# ───────────────────────────────────────────────────────────────────────────
# 9. Use List Comprehensions and Built-in Functions
# Simplify your code by using Python's powerful built-in features.
# ───────────────────────────────────────────────────────────────────────────

# Bad
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

# Good
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# ───────────────────────────────────────────────────────────────────────────
# 10. Test Your Functions
# Write test cases to ensure your functions work as expected.
# ───────────────────────────────────────────────────────────────────────────

def add(a: int, b: int) -> int:
    return a + b

# Test
assert add(2, 3) == 5
assert add(-1, 1) == 0

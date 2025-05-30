# ───────────────────────────────────────────────────────────────────────────
print("This is a temperature converter")
# ───────────────────────────────────────────────────────────────────────────

c = input("Enter Celsius (°C): ")
f = (float(c)*(9/5))+32

print(f"Fahrenheit (°F) equivalent: {f}!")

f = input("Enter Fahrenheit (°F): ")
c = (float(f)-32)*(5/9)

print(f"Celsius (°C) equivalent: {c}!")
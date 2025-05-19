import pandas as pd
import random

# Sample data
first_names = ['Juan', 'Maria', 'Jose', 'Ana', 'Pedro', 'Liza', 'Carlos', 'Luisa', 'Ramon', 'Elena', 'Miguel', 'Isabel']
last_names = ['Dela Cruz', 'Santos', 'Rizal', 'Reyes', 'Gonzales', 'Moreno', 'Torres', 'Lopez', 'Garcia', 'Mendoza', 'Navarro', 'Silva']
email_domains = ['@gmail.com', '@yahoomail.com']

# Generate 50 fake contact entries
data = []
for _ in range(50):
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = f"{first} {last}"
    email_username = f"{first.lower()}.{last.lower()}{random.randint(1, 99)}"
    email = email_username + random.choice(email_domains)
    phone = f"+639{random.randint(10, 99)}{random.randint(1000000, 9999999)}"
    data.append([name, email, phone])

# Create a DataFrame and save it to CSV
df = pd.DataFrame(data, columns=['Name', 'Email', 'Phone Number'])
df.to_csv("philippines_contacts.csv", index=False)

print("CSV file 'philippines_contacts.csv' created successfully!")
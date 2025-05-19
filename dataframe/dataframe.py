import pandas as pd


df_ph_contacts = pd.read_csv('philippines_contacts.csv')

# print first 5 rows including headers
print(df_ph_contacts.head())



# what happens when there are no headers in the csv file?

df_mall_promos = pd.read_csv('megamallpromo.csv')

print("Notice this one has no header...")
print(df_mall_promos)


# we can define our own headers
column_names = ['Name', 'Email', 'Phone Number']

# Read the CSV without using the first row as header
df_mall_promos_with_header = pd.read_csv('megamallpromo.csv', header=None, names=column_names)

print("This has new headers, and 1st row is now a data instead of a header...")
print(df_mall_promos_with_header.head())

unique_names =  set(df_ph_contacts['Name']) | set(df_mall_promos_with_header['Name'])  # Union of two sets
print(unique_names)
print(len(unique_names))
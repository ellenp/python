import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
print(df)


df = pd.read_json('data.json')

print(df.to_string())


data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 


print(df.head(10))
print(df.head())
print(df.tail())
print(df.info())

new_df = df.dropna()

print(new_df)
df.dropna(inplace = True)

print(df)

df.fillna(130, inplace = True)
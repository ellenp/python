import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('typhoon_data.csv', parse_dates=['Date'])

# Preprocessing
df.set_index('Date', inplace=True)
category_counts = df['Category'].value_counts()
yearly_avg_wind = df.groupby('Year')['Max Wind Speed (km/h)'].mean()
yearly_avg_pressure = df.groupby('Year')['Pressure (hPa)'].mean()

# Create 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Typhoon Statistics in the Philippines', fontsize=16)

# Plot 1: Max Wind Speed over Time
axs[0, 0].plot(df.index, df['Max Wind Speed (km/h)'], marker='o', linestyle='-')
axs[0, 0].set_title('Max Wind Speed Over Time')
axs[0, 0].set_xlabel('Date')
axs[0, 0].set_ylabel('Wind Speed (km/h)')
axs[0, 0].grid(True)

# Plot 2: Number of Typhoons per Category
category_counts.plot(kind='bar', color='coral', ax=axs[0, 1])
axs[0, 1].set_title('Number of Typhoons per Category')
axs[0, 1].set_xlabel('Category')
axs[0, 1].set_ylabel('Count')

# Plot 3: Average Wind Speed per Year
yearly_avg_wind.plot(kind='bar', color='skyblue', ax=axs[1, 0])
axs[1, 0].set_title('Average Wind Speed per Year')
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Wind Speed (km/h)')

# Plot 4: Average Central Pressure per Year
yearly_avg_pressure.plot(marker='o', color='green', ax=axs[1, 1])
axs[1, 1].set_title('Average Central Pressure per Year')
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Pressure (hPa)')
axs[1, 1].grid(True)

# Auto-layout
plt.tight_layout(rect=[0, 0, 1, 0.95])  # adjust for suptitle
plt.show()

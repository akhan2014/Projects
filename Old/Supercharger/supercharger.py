import os
print("Current working directory:", os.getcwd())
import pandas as pd
import matplotlib.pyplot as plt

#1. Load data
data = pd.read_csv('Supercharger/tesla_supercharger.csv')

#2. Clean the data

data['Chargers'] = data['Chargers'].fillna(0) #fill in missing chargers with 0 (assuming no chargers reported yet)

data['Open_Date'] = data['Open_Date'].fillna('Unknown') #fill missing Open_date with 'Unknown'

data['Open_Date'] = pd.to_datetime(data['Open_Date'], #convert to date time
                                   errors='coerce') # coerce changes non datetime items to 'NaT (Not a Time)

data['Year'] = data['Open_Date'].dt.year # Extract Year

#3. Initial Analysis

total_stations = data['Stations'].sum()
total_chargers = data['Chargers'].sum()
avg_chargers_per_station = total_chargers / total_stations

print("Tesla Superchager Data (Cleaned): ")
print(data)
print(f"\nTotal Supercharger Stations: {total_stations}")
print(f"Total Chargers:  {total_chargers}")
print(f"Average Chargers per Station: {avg_chargers_per_station}")
print(avg_chargers_per_station)


# 4. Visualize Bar Chart of Chargers per City
plt.style.use('dark_background')
plt.bar(data['City'], data['Chargers'], color= "red")
plt.title('Tesla Superchargers: Chargers per City', color='white')
plt.xlabel('City', color='white')
plt.ylabel('Number of Chargers', color='white')
plt.xticks(rotation=45, color='white') # rotate names for readablility
plt.yticks(color='white')
plt.show()

# 5. Analysis - Chargers per Year

chargers_per_year = data.groupby('Year')['Chargers'].sum().dropna() #first sorts data by year, then sum of chargers made that year, and drops na values
print("\nChargers Opened Per Year: ")
print(chargers_per_year)

# 6. Line Plot: Chargers per Year
plt.style.use('dark_background')
plt.plot(chargers_per_year.index, chargers_per_year.values, color='red', marker='o') #plots years on x and sum of superchargers on y
plt.title('Tesla Supercharger Opened per Year', color="white")
plt.xlabel('Year', color='white')
plt.ylabel('Number of Chargers', color='white')
plt.xticks(chargers_per_year.index, rotation=45, color='white') #sets ticks as year value
plt.yticks(color='white')
plt.grid(True, linestyle='--', alpha=0.3) #
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

#1. Load data
data = pd.read_csv('tesla_supercharger.csv')

#2. Clean the data

#fill in missing chargers with 0 (assuming no chargers reported yet)
data['Chargers'] = data['Chargers'].fillna(0)

#fill missing Open_date with 'Unknown'
data['Open_Date'] = data['Open_Date'].fillna('Unknown')


#3. Basic Analysis

total_stations = data['Stations'].sum()
total_chargers = data['Chargers'].sum()
avg_chargers_per_station = total_chargers / total_stations

#print results

print("Tesla Superchager Data (Cleaned): ")
print(data)
print(f"\nTotal Supercharger Stations: {total_stations}")
print(f"Total Chargers:  {total_chargers}")
print(f"Average Chargers per Station: {avg_chargers_per_station}")
print(avg_chargers_per_station)


# 4. Visualize Bar Chart of Chargers per City
plt.bar(data['City'], data['Chargers'], color= "red")
plt.title('Tesla Superchargers: Chargers per City')
plt.xlabel('City')
plt.ylabel('Number of Chargers')
plt.xticks(rotation=45) # rotate names for readablility
plt.show()
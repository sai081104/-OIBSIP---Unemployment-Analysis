# Unemployment Analysis in India - OIBSIP Data Science Task

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Display the first 5 rows
print("Dataset Preview:\n", data.head())

# Check for missing values
print("\nMissing Values:\n", data.isnull().sum())

# Data Preprocessing
# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m')

# Check the unique regions
print("\nRegions:\n", data['Region'].unique())

# Descriptive statistics
print("\nStatistical Summary:\n", data.describe())

# Plot Unemployment Rate over Time for India
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Unemployment Rate', data=data, label='India')
plt.title('Unemployment Rate in India Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# Plot Unemployment Rate by Region
plt.figure(figsize=(14, 8))
sns.lineplot(x='Date', y='Unemployment Rate', hue='Region', data=data)
plt.title('Unemployment Rate by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Top 5 Regions with Highest Unemployment Rate in November 2020
nov_2020 = data[data['Date'] == '2020-11-01']
top_regions = nov_2020.sort_values(by='Unemployment Rate', ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='Unemployment Rate', y='Region', data=top_regions, palette='coolwarm')
plt.title('Top 5 Regions with Highest Unemployment Rate (Nov 2020)')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Region')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

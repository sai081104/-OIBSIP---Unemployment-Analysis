# 📉 Task 2: Unemployment Analysis - OIBSIP Data Science Internship

# This task analyzes unemployment data in India and visualizes trends
# using line plots by region over time.

# ✅ Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Step 1: Load the dataset
# Make sure the dataset 'Unemployment in India.csv' is available locally.
# It should contain columns like: Date, Region, Estimated Unemployment Rate (%)

df = pd.read_csv("Unemployment in India.csv")

# ✅ Step 2: Display basic info and check data types
print("Dataset Info:")
print(df.info())

# ✅ Step 3: Convert 'Date' column to datetime format
# This helps in proper plotting on a timeline
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# ✅ Step 4: Preview the cleaned data
print("\nCleaned Data Preview:")
print(df.head())

# ✅ Step 5: Create a line plot for Unemployment Rate over time for each Region
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Date", y="Estimated Unemployment Rate (%)", hue="Region", marker='o')

# ✅ Step 6: Add labels and title
plt.title("📈 Unemployment Rate Over Time by Region")
plt.xlabel("Date")
plt.ylabel("Estimated Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()

# ✅ Step 7: Show the plot
plt.show()
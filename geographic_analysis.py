import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

# Drop rows with missing coordinates
df = df.dropna(subset=["Longitude", "Latitude"])

# 1. Scatter plot – All restaurant locations
plt.figure(figsize=(10,6))
plt.scatter(df['Longitude'], df['Latitude'], s=10, color='blue', alpha=0.5)
plt.title("Restaurant Locations Based on Longitude & Latitude")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

# 2. Top 5 cities with most restaurants
top_cities = df['City'].value_counts().head(5).index

# Filter data for top cities (fixed column name)
df_top = df[df['City'].isin(top_cities)]

# Scatter plot – Clusters for top 5 cities
plt.figure(figsize=(10,6))
for city in top_cities:
    city_data = df_top[df_top['City'] == city]
    plt.scatter(city_data['Longitude'], city_data['Latitude'], s=12, label=city)

plt.title("Clusters of Restaurants in Top 5 Cities")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.tight_layout()
plt.show()

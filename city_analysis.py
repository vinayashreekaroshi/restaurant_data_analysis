import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv(r"D:/cognifyz-data analysis/Dataset.csv")

# 1. CITY WITH HIGHEST RESTAURANTS
city_counts = df['City'].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

print("City with highest number of restaurants:")
print(f"{top_city} -> {top_city_count} restaurants\n")

# 2. AVERAGE RATING FOR EACH CITY
avg_rating_per_city = (
    df.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
)

print("Average rating for each city:")
print(avg_rating_per_city)

# 3. CITY WITH HIGHEST AVERAGE RATING
highest_avg_city = avg_rating_per_city.idxmax()
highest_avg_rating = avg_rating_per_city.max()

print("\nCity with highest avg rating:")
print(f"{highest_avg_city} -> {highest_avg_rating:.2f}")

# 4. SMALL GRAPH: RESTAURANT COUNT
city_counts.head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Cities by Restaurant Count", fontsize=10)
plt.xlabel("City", fontsize=8)
plt.ylabel("Count", fontsize=8)
plt.xticks(rotation=45, fontsize=7)
plt.tight_layout()
plt.show()

# 5. SMALL GRAPH: AVERAGE RATING
plt.figure(figsize=(6, 4))   
avg_rating_per_city.head(10).plot(kind="bar", color="lightgreen")
plt.title("Top 10 Cities by Average Rating", fontsize=10)
plt.xlabel("City", fontsize=8)
plt.ylabel("Avg Rating", fontsize=8)
plt.xticks(rotation=45, fontsize=7)
plt.tight_layout()
plt.show()

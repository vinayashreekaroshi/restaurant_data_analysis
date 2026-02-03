import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

df['Cuisines'] = df['Cuisines'].str.strip()

# common cuisine combinations
cuisine_counts = df['Cuisines'].value_counts().head(15)
print("Top 15 most common cuisine combinations:")
print(cuisine_counts)

# Plot – top 15 cuisine combos
plt.figure(figsize=(10,6))
plt.barh(cuisine_counts.index[::-1], cuisine_counts.values[::-1])
plt.xlabel("Number of Restaurants")
plt.title("Top 15 Cuisine Combinations")
plt.tight_layout()
plt.show()

# avg rating for each cuisine combination
cuisine_rating = df.groupby("Cuisines")['Aggregate rating'].mean().sort_values(ascending=False)
print("Cuisine combinations with highest avg rating:\n")
print(cuisine_rating.head(10))

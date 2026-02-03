import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

# Show existing columns
print("Existing columns:", df.columns)

# 1. Distribution of Aggregate Ratings
plt.figure(figsize=(8,5))
plt.hist(df['Aggregate rating'], bins=10, color='lightblue', edgecolor='black')
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurant Ratings")
plt.tight_layout()
plt.show()

# 2. Categorize ratings into bins
rating_bins = [0,1,2,3,4,5]
rating_labels = ["0-1","1-2","2-3","3-4","4-5"]
df['Rating Range'] = pd.cut(df['Aggregate rating'], bins=rating_bins, labels=rating_labels, include_lowest=True)

# Count restaurants in each rating range
rating_range_counts = df['Rating Range'].value_counts().sort_index()

print("\nMost Common Rating Range:")
print(f"{rating_range_counts.idxmax()} -> {rating_range_counts.max()} restaurants")

# Optional: visualize rating ranges
plt.figure(figsize=(7,4))
plt.bar(rating_range_counts.index, rating_range_counts.values, color='salmon')
plt.xlabel("Rating Range")
plt.ylabel("Number of Restaurants")
plt.title("Number of Restaurants by Rating Range")
plt.tight_layout()
plt.show()

# 3. Average number of votes received
avg_votes = df['Votes'].mean()
print("\nAverage number of votes received per restaurant:")
print(f"{avg_votes:.2f}")

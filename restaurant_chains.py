import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

# Identify restaurant chains
chain_counts = df['Restaurant Name'].value_counts()
restaurant_chains = chain_counts[chain_counts > 1]
df_chains = df[df['Restaurant Name'].isin(restaurant_chains.index)]

# Analyze rating and popularity
chain_analysis = df_chains.groupby("Restaurant Name").agg({
    "Aggregate rating": "mean",
    "Votes": "mean"
}).sort_values(by="Aggregate rating", ascending=False)

chain_analysis.rename(columns={
    "Aggregate rating": "Average Rating",
    "Votes": "Average Votes"
}, inplace=True)

# Plot – Top 10 chains by Average Rating
top10_chains = chain_analysis.head(10)

plt.figure(figsize=(10,6))
plt.barh(top10_chains.index[::-1], top10_chains['Average Rating'][::-1], color='skyblue')
plt.xlabel("Average Rating")
plt.title("Top 10 Restaurant Chains by Average Rating")
plt.tight_layout()

# Optional: Display rating values on bars
for i, v in enumerate(top10_chains['Average Rating'][::-1]):
    plt.text(v + 0.02, i, f"{v:.2f}", va='center')

plt.show()

# Optional: Compare Votes with a second chart
plt.figure(figsize=(10,6))
plt.barh(top10_chains.index[::-1], top10_chains['Average Votes'][::-1], color='lightgreen')
plt.xlabel("Average Votes")
plt.title("Top 10 Restaurant Chains by Average Votes")
plt.tight_layout()

# Display vote numbers on bars
for i, v in enumerate(top10_chains['Average Votes'][::-1]):
    plt.text(v + 0.5, i, f"{int(v)}", va='center')

plt.show()

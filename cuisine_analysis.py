import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

# Prepare exploded dataframe for cuisines
df_exp = df.copy()
df_exp['Cuisines'] = df_exp['Cuisines'].str.split(',')
df_exp = df_exp.explode('Cuisines')
df_exp['Cuisines'] = df_exp['Cuisines'].str.strip()

# Total number of unique restaurants
total_restaurants = df['Restaurant ID'].nunique()

# Count cuisines
cuisine_counts = df_exp['Cuisines'].value_counts()

# Top 3 cuisines
top3_cuisines = cuisine_counts.head(3)

print("Top 3 most common cuisines:", top3_cuisines)

# Percentage of restaurants serving top 3 cuisines
percentage = (top3_cuisines / total_restaurants) * 100
print("\nPercentage served by top 3 cuisines:\n", percentage.round(2))

# Plot – Top 3 cuisines
plt.figure(figsize=(8,4))
plt.barh(top3_cuisines.index[::-1], top3_cuisines.values[::-1], color='skyblue')
plt.xlabel("Number of Restaurants")
plt.title("Top 3 Most Popular Cuisines")
plt.tight_layout()
plt.show()

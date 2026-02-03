import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

# Price range distribution
price_counts = df['Price range'].value_counts().sort_index()

# Plot – Price range distribution
plt.figure(figsize=(8,5))
plt.bar(price_counts.index, price_counts.values, color='lightgreen')
plt.xlabel("Price Range Category")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution")
plt.xticks(price_counts.index)  
plt.tight_layout()
plt.show()

# Percentage of restaurants per price category
total = len(df)
percentage = (price_counts / total) * 100

print("Percentage of restaurants in each price category:")
print(percentage.round(2))

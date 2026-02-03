import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/cognifyz-data analysis/Dataset.csv")

# Count restaurants with and without online delivery
online_delivery_counts = df['Has Online delivery'].value_counts()
total_restaurants = len(df)

# Calculate percentages
online_delivery_percentage = (online_delivery_counts.get('Yes', 0) / total_restaurants) * 100
no_online_delivery_percentage = (online_delivery_counts.get('No', 0) / total_restaurants) * 100

print("Percentage of restaurants offering online delivery:")
print(f"Yes: {online_delivery_percentage:.2f}%")
print(f"No: {no_online_delivery_percentage:.2f}%")

# Pie chart
plt.figure(figsize=(6,6))
plt.pie(
    online_delivery_counts.values,
    labels=online_delivery_counts.index,
    autopct="%1.1f%%",
    colors=['skyblue', 'lightcoral'],
    startangle=90,
    explode=(0.05, 0)  
)
plt.title("Online Delivery Availability")
plt.show()

# Compare average ratings
avg_rating_online = df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()
avg_rating_no_online = df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean()

print("\nAverage Ratings:")
print(f"With Online Delivery: {avg_rating_online:.2f}")
print(f"Without Online Delivery: {avg_rating_no_online:.2f}")

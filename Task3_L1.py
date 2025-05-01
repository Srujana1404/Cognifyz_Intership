import pandas as pd
import matplotlib.pyplot as plt

set2 = pd.read_csv('Dataset .csv') 

price_counts = set2['Price range'].value_counts().sort_index()


plt.figure(figsize=(8,5))
bars = price_counts.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Distribution of Price Ranges among Restaurants')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)


for bar in bars.patches:
    plt.text(
        bar.get_x() + bar.get_width() / 2,    
        bar.get_height() + 2,                 
        int(bar.get_height()),                
        ha='center', va='bottom',
        fontsize=10, fontweight='bold', color='black'
    )

plt.tight_layout()
plt.show()

# Problem-2
total_res = set2.shape[0]
percentages = (price_counts / total_res) * 100
print("The percentage of restaurantsin each price range category is:", percentages)



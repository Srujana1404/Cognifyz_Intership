import pandas as pd

data = pd.read_csv('Dataset .csv')

data = data.dropna(subset=['Cuisines'])

totalcuisines = data['Cuisines'].str.split(',').explode().str.strip()

cuisinecounts = totalcuisines.value_counts()

top3 = cuisinecounts.head(3)
print("Top 3 cuisines are:")
for i, (cuisine, _) in enumerate(top3.items(), start=1):
    print(f"{i}. {cuisine}")

print()

total_res = data.shape[0]

print("Percentage of restaurants that serve each of the top:")

percentages = (top3 / total_res) * 100

# result = pd.DataFrame({
#     'Cuisine': top3.index,
#     'Count': top3.values,
#     'Percentage': percentages.values
# })

# print(result)

for i, (cuisine, count, percentage) in enumerate(zip(top3.index, top3.values, percentages), start=1):
    print(f"{i}. {cuisine}: {count}: {percentage:.2f}%")
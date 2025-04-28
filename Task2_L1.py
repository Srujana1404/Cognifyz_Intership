# problem-1
import pandas as pd

set1 = pd.read_csv('Dataset .csv')

countcity = set1['City'].value_counts()
print("The city with the highest number of restaurants in the dataset is:", countcity.idxmax())
# print(countcity.idxmax())
print()


# problem-2
avg = set1.groupby('City')['Aggregate rating'].mean()

with open('average_ratings_by_city.txt', 'w', encoding='utf-8') as f:
    f.write("Average rating for restaurants in each city:\n\n")
    f.write(avg.to_string())

print("The average ratings have been saved to 'average_ratings_by_city.txt'")


# problem-3
print(" The city with the highestaverage rating is:",avg.idxmax())
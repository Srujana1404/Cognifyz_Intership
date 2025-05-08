# problem 1

import pandas as pd

set4 = pd.read_csv('Dataset .csv')
agg =set4 ['Aggregate rating'].value_counts()
print("The most common rating range is:",agg.idxmax())

# problem 2
votes = set4.groupby('Restaurant Name')['Votes'].mean()
with open('average_votes_by_restaurant.txt', 'w', encoding='utf-8') as f:
    f.write("Average votes for each restaurant:\n\n")
    f.write(votes.to_string())


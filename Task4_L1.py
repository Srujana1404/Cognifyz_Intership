
# problem-1
import pandas as pd

set3= pd.read_csv('Dataset .csv')

onlinedelivery= set3['Has Online delivery'].value_counts()  
a=set3.shape[0]
percentages = (onlinedelivery / a) * 100
print("The percentage of restaurants that offer online delivery is:\n", percentages.index[1], "--->", percentages.values[1].round(2), "%")

# problem-2
avgrating= set3.groupby('Has Online delivery')['Aggregate rating'].mean()
print("The average rating for restaurants that offer online delivery is:\n", avgrating.index[1], "--->", avgrating.values[1].round(2))
print("The average rating for restaurants that do not offer online delivery is:\n", avgrating.index[0], "--->", avgrating.values[0].round(2))
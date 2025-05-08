
# problem 1
import pandas as pd

df = pd.read_csv('Dataset .csv')
cuisine_col = 'Cuisines'

df = df.dropna(subset=[cuisine_col])
if 'Restaurant Name' in df.columns:
    df = df.drop_duplicates(subset=['Restaurant Name', cuisine_col])

def normalize_cuisine_combo(cuisine_str):
    cuisines = [c.strip() for c in cuisine_str.split(',')]
    cuisines.sort()
    return ', '.join(cuisines)

df['CuisineCombo'] = df[cuisine_col].apply(normalize_cuisine_combo)

df['CuisineCount'] = df['CuisineCombo'].apply(lambda x: len(x.split(',')))
multi_cuisine_df = df[df['CuisineCount'] >= 2]
combo_counts = multi_cuisine_df['CuisineCombo'].value_counts()

most_common_combo = combo_counts.idxmax()
most_common_count = combo_counts.max()

print("Most common multi-cuisine combination:")
print(f"{most_common_combo} - {most_common_count} restaurants")


# problem 2
import pandas as pd
df = pd.read_csv('Dataset .csv')
cuisine_col = 'Cuisines'
rating_col = 'Aggregate rating'  

df = df.dropna(subset=[cuisine_col, rating_col])
df[rating_col] = pd.to_numeric(df[rating_col], errors='coerce')
df = df.dropna(subset=[rating_col])

def normalize_cuisine_combo(cuisine_str):
    cuisines = [c.strip() for c in cuisine_str.split(',')]
    cuisines.sort()
    return ', '.join(cuisines)

df['CuisineCombo'] = df[cuisine_col].apply(normalize_cuisine_combo)

df['CuisineCount'] = df['CuisineCombo'].apply(lambda x: len(x.split(',')))
df = df[df['CuisineCount'] >= 2]
combo_rating = df.groupby('CuisineCombo')[rating_col].mean().sort_values(ascending=False)

print("Top 10 cuisine combinations by average rating:")
print(combo_rating.head(11))

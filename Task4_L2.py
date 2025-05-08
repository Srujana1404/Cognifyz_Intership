# problem 1
import pandas as pd

df = pd.read_csv('Dataset .csv')

df = df.dropna(subset=['Restaurant Name', 'Latitude', 'Longitude'])

# Group by restaurant name and count unique locations
chain_check = df.groupby('Restaurant Name')[['Latitude', 'Longitude']].nunique()

# Filter for names with more than one unique location
chains = chain_check[(chain_check['Latitude'] > 1) | (chain_check['Longitude'] > 1)]

# Print just the names
with open('Restaurant chains.txt', 'w', encoding='utf-8') as f:
    f.write("Restaurant chains present in the dataset:\n\n")
    f.write(chains.to_string())






# problem 2
import pandas as pd

df = pd.read_csv('Dataset .csv')

# Drop missing values
df = df.dropna(subset=['Restaurant Name', 'Latitude', 'Longitude', 'Aggregate rating', 'Votes'])

# Convert rating and votes to numeric
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

# Drop rows with invalid ratings or votes
df = df.dropna(subset=['Aggregate rating', 'Votes'])

# Identify restaurant chains (names in multiple locations)
loc_count = df.groupby('Restaurant Name')[['Latitude', 'Longitude']].nunique()
chains = loc_count[(loc_count['Latitude'] > 1) | (loc_count['Longitude'] > 1)].index

# Filter only chains
chain_data = df[df['Restaurant Name'].isin(chains)]

# Group by chain and calculate average rating and total votes
chain_summary = chain_data.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',
    'Votes': 'sum'
}).sort_values(by='Votes', ascending=False)

# Rename columns for clarity
chain_summary = chain_summary.rename(columns={
    'Aggregate rating': 'Average Rating',
    'Votes': 'Total Votes'
})

with open('Ratings & popularity-Diff restaurant chains.txt', 'w', encoding='utf-8') as f:
    f.write("Ratings and popularity of different restaurant chains:\n\n")
    f.write(chain_summary.to_string())

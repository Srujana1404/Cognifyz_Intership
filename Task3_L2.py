
# problem 1
import pandas as pd
import folium
df = pd.read_csv('Dataset .csv')
df = df.dropna(subset=['Latitude', 'Longitude'])

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row.get('Restaurant Name', 'Restaurant')
    ).add_to(restaurant_map)
restaurant_map.save("restaurant_locations_map.html")
print("Map saved as restaurant_locations_map.html")



# problem 2
import pandas as pd
import folium
from sklearn.cluster import KMeans

df = df.dropna(subset=['Latitude', 'Longitude'])
kmeans = KMeans(n_clusters=5, random_state=0)

coordinates = df[['Latitude', 'Longitude']]
df['Cluster'] = kmeans.fit_predict(coordinates)

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)

colors = ['red', 'blue', 'green', 'purple', 'orange']
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row.get('Restaurant Name', 'Restaurant'),
        icon=folium.Icon(color=colors[row['Cluster']])
    ).add_to(restaurant_map)

restaurant_map.save("restaurant_clusters_map.html")
print("Map with clusters saved as restaurant_clusters_map.html")



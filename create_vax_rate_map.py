import folium
import requests
import json
import geopandas as gpd

url = "https://opendata.arcgis.com/datasets/da83fdaab14e42f0b3fe198a15c5bad5_0.geojson"

print('Loading geojson file...')
geo_obj = json.loads(requests.get(url).content)

print('Reading geojson file to geopandas dataframe...')
gdf = gpd.read_file(url)

print('Creating map...')
m = folium.Map(location = [32.75, -117.10])
c = folium.features.Choropleth(geo_data = url,
				data = gdf,
				columns = ['zip', 'individuals_vaccinated_with_at_'],
				key_on = 'feature.properties.zip')
c.add_to(m)

m.save('vaccinations_by_county.html')

print('Finished')

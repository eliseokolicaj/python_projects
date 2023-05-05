import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/earthquakes_april_2023.geojson'

with open(filename,encoding='utf-8') as f:
	monthly_eq = json.load(f)

readable_file = 'data/readable_eq_2023.json'
with open(readable_file, 'w') as f:
	json.dump(monthly_eq, f, indent = 4)

all_eq = monthly_eq['features']
title = monthly_eq['metadata']['title']

mags, lons, lats, place = [], [], [], []
for eq in all_eq:
	mags.append(eq['properties']['mag'])
	lons.append(eq['geometry']['coordinates'][0])
	lats.append(eq['geometry']['coordinates'][1])
	place.append(eq['properties']['place'])

#Map the earthquakes
data = [{'type':'scattergeo',
			'lon':lons,
			'lat':lats,
			'text':place,
			'marker':{'size':[1.6**mag for mag in mags],
						'color': mags,
						'colorscale':'Viridis',
						'reversescale':True,
						'colorbar':{'title':'Magnitude'},

					}
	
		}]

my_layout = Layout(title = title)
figure = {'data':data,'layout':my_layout}
offline.plot(figure,filename = 'april_2023_global_earthquakes.html')


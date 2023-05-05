import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)

	for index, header_name in enumerate(header):
		print(index,header_name)

	#Get the data from file	
	lons, lats, brightness = [], [], []
	for row in reader:
		try:
			lon = row[1]
			lat = row[0]
			bright = float(row[2])/290
		except ValueError:
			print("Missing data")
		else:
			lons.append(lon)
			lats. append(lat)
			brightness.append(bright)

#Map the fires in map
data = [{
			'type':'scattergeo',
			'lon':lons,
			'lat':lats,
			'marker':{
						'size':[10*bright for bright in brightness],
						'color':brightness,
						'colorscale':'Bluered',
						'reversescale':True,
						'colorbar':{'title':'Brightness'},
			}
}]

my_layout = Layout(title='World Fires')
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='world_fires.html')


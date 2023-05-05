from dice import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline


#Create a D6
dice = Dice()

#Roll the dice
results = []
for roll_num in range(1000):
	result = dice.roll()
	results.append(result)

#Analyse the results
frequencies = []
for value in range (1, dice.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualise the results in a histogram
x_values = list(range(1, dice.num_sides+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency results'}

my_layout = Layout(title='Results from rolling a dice 1000 times',
	xaxis = x_axis_config,yaxis = y_axis_config)

offline.plot({'data': data, 'layout' : my_layout,}, filename = 'd6.html')
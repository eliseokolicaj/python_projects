import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open (filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	for index, column_name in enumerate(header_row):
		print(index,column_name)

	#Get dates, high and low temperatures from this file
	highs, dates, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[5])
			low = int(row[6])
		except ValueError:
			print(f"Missing the data for this date: {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	#Plot the low ,high temperatures and dates
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates,highs, c = 'red', alpha = 0.5)
	ax.plot(dates, lows, c ='blue', alpha = 0.5)
	#shading the zone between the high and low temp
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

	#Format plot
	plt.title("Daily high and low temperatures,2018", fontsize=24)
	plt.xlabel('', fontsize=16)
	plt.ylabel("Temperature (F)", fontsize=20)
	plt.tick_params(axis='both', which='major', labelsize=16)
	#write the dates diagonally
	fig.autofmt_xdate()

	plt.show()
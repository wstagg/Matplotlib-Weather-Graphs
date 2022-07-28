import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)	

	# Get dates and high temprature from the file.
	dates, rain = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		prcp = float(row[3])
		dates.append(current_date)
		rain.append(prcp)

	# plot the high and low temperatures
	plt.style.use('seaborn-pastel')
	fig, ax = plt.subplots()
	ax.plot(dates, rain, c='blue')
	# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)	

	# format plot
	ax.set_title('Daily rainfall Death Valley - 2018', fontsize=24)
	ax.set_xlabel('', fontsize=16)
	fig.autofmt_xdate()
	ax.set_ylabel('Rainfall (mm)', fontsize=16)
	ax.tick_params(axis='both', which='major', labelsize=16)

	plt.show()


	





import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/heathrow_weather.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)	

	# Get dates and high temprature from the file.
	dates, average = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			av = (int(row[5]) - 32) * 5/9
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			average.append(av)
		

	# plot the high and low temperatures
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, average, c='red')

	

	# format plot
	ax.set_title('Average temperature Heathrow 1948 - 2022', fontsize=24)
	ax.set_xlabel('', fontsize=16)
	fig.autofmt_xdate()
	ax.set_ylabel('Temprature (Cº)', fontsize=16)
	ax.tick_params(axis='both', which='major', labelsize=16)

	plt.show()


	





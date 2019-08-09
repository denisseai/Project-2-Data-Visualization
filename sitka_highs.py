import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get dates and high temperatures from this filename
    dates, highs  = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
#Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
#Format plot
plt.title("Daily high temperature, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

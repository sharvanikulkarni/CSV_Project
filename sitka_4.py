#1) changing the file to include all the data for the year 2018
#2) change the title to - Daily low and high temp 2018
#3) extract low temps from the file and add to chart
#4) share in the area between low and high


import csv
from datetime import datetime
from email import header
import re

open_file = open('death_valley_2018_simple.csv','r')


csv_file = csv.reader(open_file, delimiter=',')


#to skip a line if the file contains a header record
header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []
lows = []
#test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(test_date)


for row in csv_file:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = (int(row[4]))
        low = (int(row[4]))
        

        
    except ValueError:  
        print(f"missing data for {current_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

#print(highs)
#print(dates)
#print(lows)

import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates,highs, c="red")
plt.plot(dates,lows, c='green')

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily low and high temperatures, 2018", fontsize=16)
plt.xlabel("Year 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("highs")
plt.subplot(2,1,2)
plt.plot(dates, lows, c="blue")
plt.title("lows")

plt.suptitle("Highs and lows of 2018")
plt.show()

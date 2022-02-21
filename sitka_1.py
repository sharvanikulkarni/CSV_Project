import csv
from email import header
import re

open_file = open('sitka_weather_07-2018_simple.csv','r')


csv_file = csv.reader(open_file, delimiter=',')


#to skip a line if the file contains a header record
header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
for row in csv_file:
    highs.append(int(row[5]))

print(highs)


import matplotlib.pyplot as plt

plt.plot(highs, c="red")
plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
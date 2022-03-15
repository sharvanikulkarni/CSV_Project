import csv
from datetime import datetime
from email import header
from operator import index
import re


from pyparsing import col

open_file1 = open('sitka_weather_2018_simple.csv','r')
csv_file1 = csv.reader(open_file1, delimiter=',')


#to skip a line if the file contains a header record
header_row1 = next(csv_file1)

print(type(header_row1))

for index1, column_header1 in enumerate(header_row1):
    print(index1, column_header1)
    if column_header1 == "TMAX":
        col_max1 = index1
    if column_header1 == "TMIN":
        col_min1 = index1
    if column_header1 == "NAME":
        col_name1 = index1

highs1 = []
dates1 = []
lows1 = []

for row1 in csv_file1:
    highs1.append(int(row1[col_max1]))
    current_date1 = datetime.strptime(row1[2], '%Y-%m-%d')
    dates1.append(current_date1)
    lows1.append(int(row1[col_min1]))

import matplotlib.pyplot as plt

fig = plt.figure()

'''================================================='''

infile = open("death_valley_2018_simple.csv", 'r')
file_reader = csv.reader(infile, delimiter = ",")

header_row = next(file_reader)

#print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)
    if column_header == "TMAX":
        col_max = index
    if column_header1 == "TMIN":
        col_min = index
    if column_header == "NAME":
        col_name = index

print(col_max)
print(col_min)
highs = []
dates = []
lows = []

test_date = datetime.strptime('2018-07-01','%Y-%m-%d')
print(test_date)



for item in file_reader:

    try:
        current_date = datetime.strptime(item[2],'%Y-%m-%d')
        high = int(item[col_max])
        low = int(item[col_min])
       
   
    except ValueError:
        print(f"Missing data for {current_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
   
   
#print(highs)
#print(dates)


import matplotlib.pyplot as plt

'''=========================================='''
plt.subplot(2, 1, 1)
plt.plot(dates1,highs1, c="red")
plt.plot(dates1,lows1, c="blue")

plt.fill_between(dates1, highs1, lows1, facecolor='blue', alpha=0.1)


#print(row[col_name])
plt.title(row1[col_name1], fontsize=16)
plt.xlabel("Year 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()
#plt.show()
'''=============================================='''
#fig = plt.figure()
plt.subplot(2, 1, 2)
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

#print(item[col_name])
plt.title(item[col_name], fontsize=16)
plt.xlabel("Year 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


fig.autofmt_xdate()
plt.show()
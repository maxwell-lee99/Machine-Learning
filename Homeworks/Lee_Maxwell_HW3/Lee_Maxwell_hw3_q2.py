import os
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(1,1,1) #setting empty figure with one plot

data = pandas.read_csv('weatherdata.csv') #importing the weather data from downloaded csv

x=data.Year #setting x as the Year column of the csv
y=data.Value #setting y as the Value column of the csv

ax.plot(x,y,
        color='r',
        linestyle='--',
        marker='o') #plotting year and value with the appropriate color/line/marker

ax.set_title('Global temperature')
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly')
fig.suptitle('Lee_Maxwell_hw3_q2') #setting labels of table

plt.show()
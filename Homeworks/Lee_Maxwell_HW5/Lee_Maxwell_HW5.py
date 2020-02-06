import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

data = pd.read_csv('avocado (1).csv') #importing avocado data as dataframe
avocado = data[['Date','AveragePrice','Total Volume']] #making new dataframe with desired columns
avocado['Date']=pd.to_datetime(avocado['Date']) #converting date column to datetime format
avocado.set_index('Date', inplace = True) #setting index to date
print(avocado)

fig = plt.figure()
ax1= plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223, sharex= ax1)
ax4=plt.subplot(224, sharex= ax2) #creating subplots with shared x axes

avocado.sort_values(by=['Date'], ascending= True, inplace= True) #sorting the avocado df by date
ax1.scatter(avocado.index, avocado['AveragePrice'])
ax1.set_ylabel('AveragePrice') #scatter plot of date vs average price
ax2.scatter(avocado.index,avocado['Total Volume'])
ax2.set_ylabel('Total Volume') #scatter plot of date vs total volume

plt.setp(ax1.get_xticklabels(), visible= False)
plt.setp(ax2.get_xticklabels(), visible= False) #removing xtick labels from ax1 and ax2

avocado['TotalRevenue']=avocado['AveragePrice']*avocado['Total Volume']
avocado1=avocado.groupby('Date').sum()
avocado1['AveragePrice']=avocado1['TotalRevenue']/avocado1['Total Volume'] #creating the new avocado1 grouped by date
print(avocado1)

ax3.plot(avocado1['AveragePrice'],
         marker='o',
         markersize=2)
ax3.set_ylabel('Average Price') #plotting the grouped average price vs time
ax4.plot(avocado1['Total Volume'],
         marker='o',
         markersize=2)
ax4.set_ylabel('Total Volume') #plotting grouped total volume vs time

fig.autofmt_xdate() #formating xlabels to fit more cleanly

fig.suptitle('Lee_Maxwell_hw5_q2 \n Avocado Prices and Volume Time Series') #setting title of output

fig2=plt.figure()
ax5=plt.subplot(121)
ax6=plt.subplot(122) #creating new figure with subplots

average=avocado1[['AveragePrice']].rolling(20).mean()
total=avocado1[['Total Volume']].rolling(20).mean() #creating series with rolling means of average price and volume

ax5.plot(average,
         marker='o',
         markersize=2)
ax5.set_ylabel('Average Price')#plotting rolling mean average price vs time
ax6.plot(total,
         marker='o',
         markersize=2)
ax6.set_ylabel('Total Volume')#plotting rolling total volume vs time

fig2.autofmt_xdate() #formating xlabels to fit more cleanly
fig2.suptitle('Lee_Maxwell_hw5_q3 \n Avocado Prices and Volume Time Series')#setting title of output

plt.show()

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sb
import numpy as np
from sklearn.linear_model import Ridge
from yellowbrick.regressor import ResidualsPlot #importing necessary modules



commuter= pd.read_csv('CommuteStLouis.csv') #creating a dataframe with the csv

print(commuter.describe()) #giving descriptive statistics for each column of the dataframe


fig = plt.figure()
ax1= fig.add_subplot(111) #setting up a figure with one subplot

ax1.hist(commuter['Age'], bins=68)
ax1.set_xlabel('Age')
ax1.set_ylabel('Frequency')
fig.suptitle('Lee_Maxwell_HW6_q1 \n Distribution of Age for St. Louis Commuters') #creating a histogram with the frequency of each age

commuterclean=commuter.drop(['Sex','City'],axis=1) #removing non-numerical data from the frame

commuterclean['Age']=commuterclean['Age'].astype(float)
commuterclean['Distance']=commuterclean['Distance'].astype(float)
commuterclean['Time']=commuterclean['Time'].astype(float) #casting the numeric columns as floating

print(commuterclean.corr()) #printing a correlation matrix

ax2= sb.pairplot(commuterclean, kind="reg") #printing a scatterplot matrix with regression lines imposed
ax2.fig.suptitle('Lee_Maxwell_HW6_q2 \n Scatter Plot Matrix')

fig2=plt.figure()
ax3=fig2.add_subplot(111)
ax3=sb.boxplot(x="Sex", y="Distance", data=commuter)
ax3.set_title('Lee_Maxwell_HW6_q2c \n Distance of Commute by Sex') #creating a new figure with a boxplot of distance separated by sex

distancetime=commuterclean.drop(['Age'],axis=1) #removing age so that the dataframe only has distance and time

model= LinearRegression(fit_intercept=True)
x=distancetime['Distance']
X=x[:,np.newaxis]
y=distancetime['Time']
model.fit(X,y)
y_predicted=model.predict(X) #creating a linear regression model for the distance and time data

fig4=plt.figure()
fig4.suptitle('Lee_Maxwell_HW6_q3')
ax4=fig4.add_subplot(121)
ax5=fig4.add_subplot(122)
ax4.scatter(X,y)
ax4.plot(X, y_predicted)
ax4.set_xlabel('Distance')
ax4.set_ylabel('Time')
ax4.set_title('Distance of Commute vs Time of Commute Actual and Predicted')#plotting the actual data as a scatterplot and the predicted data as the regression line

ridge=Ridge()
visualizer= ResidualsPlot(ridge)
ax5=visualizer.fit(X,y)
visualizer.show() #creating a residual plot with the Ridge and ResidualsPlot modules


plt.show()
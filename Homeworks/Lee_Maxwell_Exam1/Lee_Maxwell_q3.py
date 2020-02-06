import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

fig=plt.figure()
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2) #setting empty figure with two plots

os.chdir('/Users/maxlee/Desktop/ITP 449') #setting the folder with the csv as the directory

frame = pd.read_csv('White_House_Staff.csv') #creating the dataframe

del frame['Employee Status'] #deleting unnecessary columns
del frame['Pay Basis']
del frame['Position Title']

frame.set_index('Employee Name', inplace=True) #updating the index
print(frame.sort_values(by=['Salary'], ascending=False)) #printing the sorted and updated frame

ax1.hist(frame['Salary'],
         bins=10,
         color='blue')
ax1.set_xlabel('Salary')
ax1.set_ylabel('Frequency') #creating a blue histogram with 10 bins and the appropriate labels

ax2 = sb.swarmplot(x="Gender", y="Salary",data=frame)
ax2 = sb.boxplot(x="Gender", y="Salary",data=frame) #creating a swarmplot and boxplot of salary filtered by gender

plt.show()
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/maxlee/Desktop/ITP 449') #setting the folder with the csv as the directory
frame = pd.read_csv('mtcars.csv') #creating a dataframe by reading the mtcars.csv

data= {'Car Name': frame['Car Name'],
       'Cylinder': frame['cyl'],
       'Gear': frame['gear'],
       'Horsepower': frame['hp'],
       'Miles per Gallon': frame['mpg']} #creating a dictionary with the desired selected columns

newframe=pd.DataFrame(data) #creating a dataframe with that dictionary

newframe.set_index('Car Name', inplace= True) #setting the index to be car name

print(newframe.head()) #printing first five rows of new dataframe

newframe['Powerful']=newframe['Horsepower']>=110 #creating a column to determine if powerful

print(newframe.head()) #printing dataframe with new column

#del newframe['Horsepower'] #deleting the Horsepower column NOTE: this line turned into a comment for rest of steps
#print(newframe.head())

filterframe=newframe[newframe['Miles per Gallon']>=25] #filtering out all MPG >=25

print(filterframe.sort_values(by='Horsepower', ascending= False)) #soting the filtered values by Horsepower

finalfilter=filterframe[filterframe['Powerful'] == True] #creating a new frame with MPG>=25 and Powerful=True

print(finalfilter) #printing the final result






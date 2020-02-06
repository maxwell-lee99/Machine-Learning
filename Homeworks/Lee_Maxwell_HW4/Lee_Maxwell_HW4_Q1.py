import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('/Users/maxlee/Desktop/ITP 449') #setting the folder with the csv as the directory
frame = pd.read_csv('mtcars.csv') #creating a dataframe by reading the mtcars.csv

print(frame.head()) #printing the first 5 rows of the dataframe

frame.set_index('Car Name', inplace= True) #changing the index of the dataframe to the car name column

print(frame.head()) #printing the first 5 rows of the new dataframe


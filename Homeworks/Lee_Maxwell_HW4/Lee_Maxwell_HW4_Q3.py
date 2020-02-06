import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x=[] #creating an empty list x

for i in range(100):
    rand= random.uniform(5.9,7.5)
    x.append(rand) #filling x with 100 random numbers uniformly distributed between 5.9 and 7.5

ser=pd.Series(x) #turning the list x into a series
print(ser) #printing the series

print("20th, 60th and 90th percentile of wing span in ft:", np.percentile(ser, q=[20,60,90])) #printing the 20th, 60th, 90th percentiles of the series

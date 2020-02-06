import os
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure() #creating the figure
ax=fig.add_subplot(1,1,1) #setting the subplot to only produce one plot
x = [np.random.randint(1,200,200,int)]
y= [np.random.randint(1,200,200,int)] #defining x and y as a list of random integers

ax.scatter(x,y,
            color='r') #producing a scatter plot with the dots color red
ax.set_title('Scatter of Random Integers',
             color = 'g')
ax.set_xlabel('Random Integer',
              color = 'b')
ax.set_ylabel('Random Integer',
              color = 'b') #adding the appropriate labels and their colors
fig.suptitle('Lee_Maxwell_hw3_q1')
plt.show()



import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans

data=pd.read_csv('Stores.csv')
print(data)
data.drop(data.columns[0], axis=1, inplace= True)
profit=data['Profit Margin']
data.drop(data.columns[-1], axis=1, inplace= True) #removing profit margin as that is the dependent variable
print(data)
normalizer=Normalizer()
normalizer.fit(data)
data_norm=pd.DataFrame(normalizer.transform(data),columns=data.columns)
print(data_norm) #q1 all necessary data preparation steps

ks=range(1,11)
inertias=[]
for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(data_norm)
    inertias.append(model.inertia_) #q2 running kmeans with k from 1-10
fig=plt.figure()
plt.plot(ks,inertias, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.xticks(ks)
plt.suptitle('Lee_Maxwell_q2')
#plt.show() #q3 plotting k vs inertia
#q4 from the inertias graph, the best k value is k=5
model = KMeans(n_clusters=4)
model.fit(data_norm)
labels=model.predict(data_norm)
data['Profit Margin']=profit
data['Cluster']=pd.Series(labels)
print(data) #q5 adding profit margin and cluster back into the data frame
fig2=plt.figure()
plt.hist(data['Cluster'])
plt.xticks(range(0,4))
plt.title('Frequency of Cluster Number')
plt.xlabel('Cluster Number')
plt.ylabel('Frequency')
plt.suptitle('Lee_Maxwell_q2')
plt.show() #q6


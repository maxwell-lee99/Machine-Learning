import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans

df=pd.read_csv('wineQualityReds(1).csv') #q1 importing the csv file
df.drop(df.columns[[0]],axis=1, inplace=True) #q2 dropping the wine column from the frame
quality=df['quality'] #q3 storing quality in a separate variable
df.drop(df.columns[[-1]],axis=1, inplace=True) #q4 drop quality from the frame
print(df)
print(quality) #q5 printing the frame and quality separately

normalizer=Normalizer()
normalizer.fit(df)
df_norm=pd.DataFrame(normalizer.transform(df),columns=df.columns) #q6 normalizing the data
print(df_norm) #q7 printing the normalized data

ks=range(1,11)
inertias=[]
for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(df_norm)
    inertias.append(model.inertia_) #q8 creating the cluster model for each k and storing the inertia

plt.plot(ks,inertias, '-o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.xticks(ks)
plt.suptitle('Lee_Maxwell_HW8')
plt.show() #q9 plotting the ks vs the inertia

model = KMeans(n_clusters=6) #q10 would pick k=6 as after this point there is minimal decrease in inertia
model.fit(df_norm)
labels=model.predict(df_norm)
df['Cluster']=pd.Series(labels)
print(df) #q11 printing the original dataframe with the clusters added in
df['Quality']=quality #q12 adding quality back into the original frame

crosstab=pd.crosstab(df.Quality,df.Cluster)
print(crosstab) #q13 printing a crosstab of quality and cluster, showing the the cluster does estimate the assigned quality decently well

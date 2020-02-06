import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

wines=pd.read_csv('wineQualityReds(1).csv')
print(wines) #q1 the target variable is quality
x=wines.iloc[:,1:-1]
y=wines.iloc[:,-1] #q2 prepared x to include independent variables, y to be the dependent variable

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.3,random_state=2019)
dt=DecisionTreeClassifier(max_depth=6, random_state=2019)
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test) #q3 built a classification tree model with max depth of 6
print('The number of cases in the training partition is', len(x_train)) #q4
print('The number of cases in the testing partition is', len(x_test)) #q5

test_acc=dt.score(x_test,y_test)
train_acc=dt.score(x_train,y_train)

print('The training accuracy is',train_acc) #q6
print('The testing accuracy is',test_acc) #q7

testwine=np.array([8,0.6,0,2.0,0.076,10,30,.9978,3.20,0.5,10.0]).reshape(1,-1)
testpred=dt.predict(testwine)
numtestpred=testpred[0]
print('The predicted wine quality is', numtestpred) #q8



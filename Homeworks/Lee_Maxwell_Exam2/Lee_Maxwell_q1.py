import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score

iris=pd.read_csv('iris.csv') #loading data
x=iris.iloc[:,0:3] #storing all independent variables in x
y=iris.iloc[:,-1] #storing dependent variable species in y
standardize=StandardScaler()
standardize.fit(x)
x_std=pd.DataFrame(standardize.transform(x),columns=x.columns) #q1 standardizing all independent variables

x_train, x_test, y_train, y_test = train_test_split(x_std,y,test_size=.3,random_state=2019,stratify=y)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test) #q2 building a model for k=5



neighbors=range(1,11)
train_accuracy=[]
test_accuracy=[]
for k in range(1,11):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    train_accuracy.append(knn.score(x_train,y_train))
    test_accuracy.append(knn.score(x_test,y_test))
plt.figure()
plt.title('KNN: Accuracy for Different K Values')
plt.plot(neighbors,train_accuracy, label='Training Accuracy')
plt.plot(neighbors,test_accuracy, label='Testing Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.suptitle('Lee_Maxwell_Q1')
plt.show() #q3 plotting the accuracies for all k values
#q4 based off of the plot, the model is most accurate at k=4. k=5 is also a valid choice, but will be choosing k=4


knn=KNeighborsClassifier(n_neighbors=4)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
print(y_pred) #q5 predicting values for k=4
cf=confusion_matrix(y_test,y_pred)
print('The confusion matrix is \n',cf) #q6
accuracy=accuracy_score(y_pred,y_test)
print('The model accuracy is', accuracy) #q7
recall=recall_score(y_pred,y_test, average='macro')
precision=precision_score(y_pred,y_test, average='macro')
print('The precision is', precision)
print('The recall is', recall) #q8


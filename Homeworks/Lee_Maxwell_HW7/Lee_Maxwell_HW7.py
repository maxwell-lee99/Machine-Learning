import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

data=pd.read_csv('Titanic.csv') #q1
print(data) #2, after examining the data target dependant variable is Survived
data.drop(data.columns[0], axis=1, inplace= True) #q3 dropping the passenger column as it is not necessary
print(data.isnull().sum()) #q4 no data is null

fig=plt.figure()
ax1=fig.add_subplot(221)
ax1=sb.countplot(x="Class", data=data)
ax1.set_title('Class Count')
ax2=fig.add_subplot(222)
ax2=sb.countplot(x="Sex", data=data)
ax2.set_title('Sex Count')
ax3=fig.add_subplot(223)
ax3=sb.countplot(x="Age", data=data)
ax3.set_title('Age Count')
ax4=fig.add_subplot(224)
sb.countplot(x="Survived", data=data)
ax4.set_title('Suvived Count')
fig.suptitle('Lee_Maxwell_HW7') #q5 creating the count plots for each relevant column

catdata= pd.get_dummies(data, columns=['Class','Sex','Age','Survived']) #q6 getting dummy variables
print(catdata.columns)

x=catdata.iloc[:,0:-2]
y=catdata.iloc[:,-1] #preparing categorical data for the split. the y predictor will only the survived_yes column


x_train, x_test, y_train, y_test =train_test_split(x,y, test_size=.3, random_state=0) #q7 splitting the data
logreg= LogisticRegression()
logreg.fit(x_train,y_train) #q8 fitting the data to logistic regression

y_pred=logreg.predict(x_test) #using the test data to predict
cnfmatrix= metrics.confusion_matrix(y_test, y_pred)
print(metrics.accuracy_score(y_test,y_pred)) #q9 printing the accuracy score
print(cnfmatrix) #q10 printing the confusion matrix


testpatient=np.array([0,0,1,0,0,1,1,0]).reshape(1,-1) #creating a sample data set with the desired categories of male, 3rd class, adult

testpatient_pred=logreg.predict(testpatient) #predicting the 3rd class male adult
print(testpatient_pred) #q11 printing the result, which is 0 meaning the 3rd class male adult is not predicted to survive
plt.show()
zimport pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
import math

a = pd.read_csv("mn.csv")
print(a)

print(a.shape)

print(a.head(10))
print("# of passenger in original data:" +str(len(a.index)))
print(a.info())

#DATA WRANGLING
print(a.isnull())

print(a.isnull().sum())

print(a.drop("Cabin", axis = 1, inplace=True))
print(a.head(5))
print(a.dropna(inplace=True))
print(a.isnull().sum())
print(a.head(2))
sex = pd.get_dummies(a['Sex'],drop_first=True)
print(sex) 

print(sex.head(5))

embark = pd.get_dummies(a['Embarked'],drop_first=True)
print(embark) 

print(embark.head(5))

Pcl = pd.get_dummies(a['Pclass'],drop_first=True)
print(Pcl) 

print(Pcl.head(5))

s = pd.concat([a,sex,embark,Pcl],axis=1)
print(s)

print(s.head(5))

print(a.drop(['Sex','Embarked','PassengerId','Name','Ticket'],axis = 1, inplace=True))
print(a.head())

#TRAIN DATA
X = a.drop("Survived",axis=1)
Y = a("Survived")

X_train, X_test, Y_train, Y_test = tran_test_split(X,y, test_size=0.3, random_state=1)


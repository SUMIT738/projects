import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


file = pd.read_csv(r'C:\Users\sumit kumar\Desktop\bank_loan.csv')
#print(file)

x = file.iloc[:,1:5]          #x = file.values[:,1:5]   (alos do that)
print(x.values)                    #extracting data column

y = file.iloc[:,0].values    #y = file.vlues[:,0]

#print(y)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

]o = DecisionTreeClassifier()
ml = o.fit(x_train,y_train)
print(ml)

#print(ml.intercept_)
#print(ml.coef_)

b = ml.predict(x_test)
print(b)


print("accuracy is", accuracy_score(y_test,b)*100)

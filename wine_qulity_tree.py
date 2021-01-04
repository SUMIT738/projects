import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score

data =pd.read_csv(r'C:\Users\sumit kumar\Downloads\archive\wine.csv')

data.head()

data.isnull().sum()

#sns.barplot(x=data['quality'],y=data['pH'])
#plt.show()

x = data[data.columns[:-1]]
y = data['quality']
sc = StandardScaler()
x = sc.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=42)


######## Decision tree

o=DecisionTreeClassifier()

o.fit(x_train,y_train)

c= o.predict(x_test)

classification_report(y_test,c)

##### Random forest

a=RandomForestClassifier()

a.fit(x_train,y_train)

b=a.predict(x_test)

print(classification_report(y_test,b))

s = SGDClassifier()
s.fit(x_train, y_train)
pre= s.predict(x_test)
print(classification_report(y_test, pre))

##########   LogisticRegrassion()

log=LogisticRegression()

log.fit(x_train,y_train)

l=log.predict(x_test)

print(classification_report(y_test,l))

accuracy_score(y_test,l)

## KneighborsClassifier

k=KNeighborsClassifier()

k.fit(x_train,y_train)

kn=k.predict(x_test)

print(accuracy_score(y_test,kn))

print(classification_report(y_test,kn))







import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score



a = pd.read_csv("bank.csv")
print(a)

print(a.shape)
print(a.describe())


c = a.corr()
print(c)

print(a.head())


X = a.drop('Class', axis=1)
print(X)
y = a['Class']
print(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print(len(X))

print(len(X_test))

print(X_test)
print(X_train)



scaler = StandardScaler()
h = scaler.fit(X_train)
print(h)

X_train = scaler.transform(X_train)
print(X_train)
X_test = scaler.transform(X_test)
print(X_test)





#kernel
#linear
#poly
#rbf
#sigmoid

o = SVC(kernel='linear')
lm = o.fit(X_train, y_train)
print(lm)




b = lm.predict(X_test)
print(b)


f = classification_report(y_test,b)
print(f)



m = confusion_matrix(y_test,b)
print(m)

n = accuracy_score(y_test,b)
print(n)






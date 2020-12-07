import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score



a = pd.read_csv("mm.csv")
print(a)

print(a.shape)
print(a.describe())


c = a.corr()
print(c)

print(a.head())

plt.scatter(a['sepal_length'],a['sepal_width'])
plt.show()



X = a.iloc[:, :-1].values
print(X)
y = a.iloc[:, 4].values
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






o = KNeighborsClassifier(n_neighbors=5)
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



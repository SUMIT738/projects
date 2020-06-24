import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score



a = pd.read_csv("Card.csv")
print(a)

print(a.shape)
print(a.describe())


c = a.corr()
print(c)

print(a.head())

plt.scatter(a['PAY_AMT1'],a['MARRIAGE'])
plt.show()

X = a[['PAY_AMT1','MARRIAGE']]
print(X)
Y = a['BILL_AMT1']
print(Y)


x = np.array(X).reshape(-1,1)
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3)

print(len(X))

print(len(X_test))

print(X_test)
print(X_train)

o = LogisticRegression()
lm = o.fit(X_train, Y_train)
print(lm)

b = lm.predict(X_test)
print(b)


f = classification_report(Y_test,b)
print(f)



m = confusion_matrix(Y_test,b)
print(m)

n = accuracy_score(Y_test,b)
print(n)







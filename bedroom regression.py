

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

a = pd.read_csv("kn.csv")
print(a)

print(a.shape)
print(a['price'].describe())


c = a.corr()
print(c)

print(a.head())

x = a['price']
y = a['bedroom']
print(x)
print(y)

x = np.array(x).reshape(-1,1)
print(x)

o = LinearRegression()
lm = o.fit(x, y)

print(lm)
print(lm.intercept_)
print(lm.coef_)

b = lm.predict(x)
print(b)

price = []
for x in range(3):
    a = int(input('enter price :'))
    price.append(a)

price = np.array(price).reshape(-1,1)

print(lm.predict(price))



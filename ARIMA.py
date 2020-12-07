import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA



a = pd.read_csv('ss.csv')
print(a)

print(a.shape)

print(a.head(5))
print(a.describe())


print(a.corr())

print(a.Month[1])

plt.plot(a['Month'],a['Passengers'])
plt.show()

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(311)
fig = plot_acf(a['Passengers'], ax=ax1,
               title="Autocorrelation on Original Series")
plt.show()


plot_pacf(a['Passengers'].diff().dropna(), lags=40)
plt.show()

plot_acf(a['Passengers'].diff().dropna())
plt.show()


model = ARIMA(a['Passengers'], order=(1, 1, 1))
results = model.fit()
print(results)


model = ARIMA(a['Passengers'], order=(1, 1, 1))
results = model.fit()
results.plot_predict(1, 20)
plt.show()



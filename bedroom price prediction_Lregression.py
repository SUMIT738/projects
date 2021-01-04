import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
#from sklearn.metrics import Classification_report
#from sklearn.metrics import accurcy_score
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import mean_absolute_error

pdata=pd.read_csv(r'C:\Users\sumit kumar\Downloads\archive2\melb_data.csv')

pdata.head()

pdata.drop(['Method','Date', 'Distance' ,'Postcode' ,'Car', 'BuildingArea' ,'YearBuilt' ,'CouncilArea', 'Lattitude', 'Regionname', 'Propertycount'],axis=1,inplace=True)

pdata.head()

pdata.drop(['SellerG', 'Longtitude'],axis=1,inplace=True)

pdata.head()

pdata.isnull().sum()  #data is free from null values

y=pdata['Price']
x=pdata[['Rooms','Bedroom2','Bathroom','Landsize']]
sc=StandardScaler()
x=sc.fit_transform(x)

pdata.describe()

sns.lineplot(x=pdata['Price'],y=pdata['Rooms'])
plt.show()

#scatterplot to cheak the outliers

sns.scatterplot(x=pdata['Price'],y=pdata['Rooms'])
plt.show()

#out=[]
#def detect_out(pdata):
 #   threshold=3
  #  mean=np.mean(pdata)
   # std=np.std(pdata)
    #for i in data:
     #   z_score = (i-mean)/std
      #  if np.abs(z_score)>threshold:
       #     out.append(i)
        #    return out
        #outlier_pt=detect_out(dataset)

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=.3)


x_train.shape

x_test.shape

from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import mean_absolute_error
lof = LocalOutlierFactor()
yhat = lof.fit_predict(x_train)

mask = yhat != -1
x_train, y_train = x_train[mask, :], y_train[mask]
# summarize the shape of the updated training dataset
print(x_train.shape, y_train.shape)

#LogisticRegression

l =LogisticRegression()
l.fit(x_train,y_train)

p = l.predict(x_test)

print(p)

accuracy_score(y_test,p)

classification_report(y_test,p)


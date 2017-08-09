import numpy as np
import pandas as pd
import sklearn
nam=[
'Alcohol',
'Malic acid',
'Ash',
'Alcalinity of ash',
'Magnesium',
'Total phenols',
'Flavanoids',
'Nonflavanoid phenols',
'Proanthocyanins',
'Color intensity',
'Hue',
'OD280/OD315 of diluted wines',
'Proline'
]

data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',
                 names=nam)
targ=np.array(data.index)
x=np.array(data)


sklearn.model_selection.KFold()
from sklearn.model_selection import KFold
kf = KFold(n_splits=5,shuffle=True,random_state=42)
for train_index, test_index in kf.split(data):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=5)

from sklearn.model_selection import cross_val_score
scores = cross_val_score(neigh,x,targ,cv=kf)

ls1=[]

for i in range (1,51):
    neigh = KNeighborsClassifier(n_neighbors=i)
    scs = cross_val_score(neigh,x,targ,cv=kf)
    ls1.append(scs.mean())
    print(scs)
    print(scs.mean())

from sklearn import preprocessing
X_scaled = preprocessing.scale(x)
ls=[]
ls.index(max(ls))

obj=sklearn.datasets.load_boston()

from sklearn import preprocessing
X_sc = preprocessing.scale(obj.data)
targ=obj.target
ls=np.linspace(1,10,200)
from sklearn.model_selection import KFold
kf = KFold(n_splits=5,shuffle=True,random_state=42)
from sklearn.neighbors import KNeighborsRegressor
for i in ls:
    neigh = KNeighborsRegressor(n_neighbors=5,weights='distance',p=i)
    scs = cross_val_score(neigh,X_sc,targ,cv=kf,scoring='neg_mean_squared_error')
    ls1.append(scs.mean())
    print(scs)
    print(scs.mean())


([  2.73100000e-02,
    0.00000000e+00,
    7.07000000e+00,
    0.00000000e+00,
    4.69000000e-01,
    6.42100000e+00,
    7.89000000e+01,
    4.96710000e+00,
    2.00000000e+00,
    2.42000000e+02,
    1.78000000e+01,
    3.96900000e+02,
    9.14000000e+00])

data=pd.read_csv('cours_ML/perceptron-train.csv',header=None)

import numpy as np
from sklearn.linear_model import Perceptron
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])
clf = Perceptron(random_state=241)
clf.fit(X, y)
predictions = clf.predict(X)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,predictions)
x=np.array(data[[1,2]])
y=np.array(data[0])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_t = np.array([[100.0, 2.0], [50.0, 4.0], [70.0, 6.0]])
X_te = np.array([[90.0, 1], [40.0, 3], [60.0, 4]])
X_train_scaled = scaler.fit_transform(X_t)
X_test_scaled = scaler.transform(X_te)

0.65500000000000003
accuracy_score(yt,clf.predict(X_test_scaled))

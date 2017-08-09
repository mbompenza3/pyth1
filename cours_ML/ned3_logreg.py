import numpy as np
import pandas as pd
import seaborn as sns
data=pd.read_csv('data-logistic.csv',header=None)
X=np.array(data[[1,2]])
y=np.array(data[0])

w=np.array([0,0])
k=0.1
er=1e-5
l=y.shape[0]
n=10000
st=0
C=10

import numpy as np
from sklearn.metrics import roc_auc_score
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
roc_auc_score(y_true, y_scores)
w=np.array([0,0])
n=10000
st=0
C=1
k=1
while True:
    st+=1
    z=np.exp(-y*w.dot(X.T))
    z1=1-1/(1+z)
    dw=(k/l)*(y*z1).dot(X)
    w=w+dw
    if (np.linalg.norm(dw)<er) or (st>=n):
        break

p=1/(1+np.exp(-w.dot(X.T)))
roc_auc_score(y, p)

w=np.array([0,0])
n=10000
st=0
C=1
while True:
    st+=1
    z=np.exp(-y*w.dot(X.T))
    z1=1-1/(1+z)
    dw=(k/l)*(y*z1).dot(X)-k*C*w
    w=w+dw
    if (np.linalg.norm(dw)<er) or (st>=n):
        break

k=1
array([ 0.28808965,  0.09172625])
c=1;k=0.1
array([ 0.12328347,  0.08684528])

from sklearn.linear_model import LinearRegression
lr2 = LinearRegression()
lr2.fit(X,y)
y2 = lr2.predict(X)
p=1/(1+np.exp(-w.dot(X.T)))
print(roc_auc_score(y, p))
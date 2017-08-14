import numpy as np
import pandas as pd


from sklearn.ensemble import RandomForestRegressor
# X = np.array([[1, 2], [3, 4], [5, 6]])
# y = np.array([-3, 1, 10])
# clf = RandomForestRegressor(n_estimators=100,random_state=1)
# clf.fit(X, y)
# predictions = clf.predict(X)

from sklearn.metrics import r2_score
# print(r2_score([10, 11, 12], [9, 11, 12.1]))

data=pd.read_csv('abalone.csv')

data['Sex'] = data['Sex'].map(lambda x: 1 if x == 'M' else (-1 if x == 'F' else 0))
y=np.array(data['Rings'])
X1=np.array(data.loc['Sex':'ShellWeight'])

from sklearn.model_selection import KFold
kf = KFold(shuffle=True,random_state=1,n_splits=5)
for i in range(1,10):

    l=[]
    for train_index,test_ind in kf.split(X):
            # print("TRAIN:", train_index, "TEST:", test_index)
            X_train = X1[train_index]
            y_train = y[train_index]
            X_test=X1[test_ind]
            y_test = y[test_ind]
            clf = RandomForestRegressor(n_estimators=i, random_state=1)
            clf.fit(X_test, y_test)
            predictions = clf.predict(X_train)
            # print(r2_score(y_train, predictions))
            l.append(r2_score(y_train, predictions))
    print(l)
    print(np.mean(l))

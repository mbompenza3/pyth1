import numpy as np
import pandas as pd
# X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
# y = np.array([1, 1, 2, 2])

data=pd.read_csv('svm-data.csv',header=None)
# print(data.head())
# print(data.shape)
X=np.array(data[[1,2]])
y=np.array(data[0])

from sklearn.svm import SVC
clf = SVC(C=100000,kernel='linear',random_state=241)
clf.fit(X, y)

# print(clf.predict([[-0.8, -1]]))
print(y)
predictions = clf.predict(X)
print(predictions)
from sklearn.metrics import accuracy_score
acc=accuracy_score(y,predictions)
print(acc)
print(clf.score(X,y))
print(clf.support_)
print(clf.support_vectors_)
print(clf.coef_)
print(clf.dual_coef_)
print(clf.decision_function(X))
# print(clf.get_params())

# dataar=np.array(data)
# from matplotlib import pyplot as plt
# for t in range(2):
#     if t==0:
#         c='r'
#         marker='>'
#     elif t==1:
#         c='g'
#         marker='o'
#
#
#     plt.scatter(dataar[dataar[:,0]==t,1],
#                     dataar[dataar[:,0]==t,2],marker=marker,c=c
#                     )
#
# plt.show()
import numpy as np
import pandas as pd

data=pd.read_csv('gbm-data.csv')
ar=data.values
X=ar[:,1:]
y=ar[:,0]
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test =train_test_split(X, y,test_size=0.8,random_state=241)

# X1, y1 = np.arange(10).reshape((5, 2)), range(5)
# X_train, X_test, y_train, y_test = train_test_split(
#     X1, y1, test_size=0.33, random_state=42)

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import log_loss
# X, y = make_hastie_10_2(random_state=0)
# X_train, X_test = X[:2000], X[2000:]
# y_train, y_test = y[:2000], y[2000:]
learning= [1, 0.5, 0.3, 0.2, 0.1]
train_loss=[]
test_loss=[]
for ll in learning:
    clf = GradientBoostingClassifier(n_estimators=250, learning_rate=ll,
        random_state=241,verbose=True).fit(X_train, y_train)
    # clf.score(X_test, y_test)

    pred=clf.staged_decision_function(X_train)
    predt=clf.staged_decision_function(X_test)
    lpr=list(pred)
    lprt=list(predt)

    apr=np.array(lpr)
    aprt=np.array(lprt)

    sgm=1/(1+np.exp(-apr))
    print(sgm.shape)
    sgmt = 1 / (1 + np.exp(-aprt))
    print(sgmt.shape)
    # predpr = clf.predict_proba(X_test)
    # predprt = clf.predict_proba(X_train)
    for kk in range(1,250):

        train_loss.append(log_loss(y_train,sgm[kk]))
        test_loss.append(log_loss(y_test,sgmt[kk]))


plt.figure()
plt.plot(test_loss, 'r', linewidth=2)
plt.plot(train_loss, 'g', linewidth=2)
plt.legend(['test', 'train'])
# plt.legend([ 'train'])

plt.show()


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=37, random_state=241)
clf.fit(X_train, y_train)
predf=clf.predict_proba(X_test)
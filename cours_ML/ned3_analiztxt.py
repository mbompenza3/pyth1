from sklearn import datasets
import numpy as np
newsgroups = datasets.fetch_20newsgroups(
                    subset='all',
                    categories=['alt.atheism', 'sci.space']
             )

from sklearn.feature_extraction.text import TfidfVectorizer
vect=TfidfVectorizer(newsgroups.data)

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
grid = {'C': np.power(10.0, np.arange(-5, 6))}
cv = KFold(n_splits=5, shuffle=True, random_state=241)
clf = SVC(kernel='linear', random_state=241)
gs = GridSearchCV(clf, grid, scoring='accuracy', cv=cv)
x=vect.fit_transform(newsgroups.data)
y=newsgroups.target
gs.fit(x, y)

feat_map=vect.get_feature_names()

clf1 = SVC(C=1,kernel='linear',random_state=241)
clf1.fit(x, y)

wt=clf.coef_
wt1=wt.toarray()
wt2=wt1.__abs__()
l=[]
for i in range(10):
    m=wt2.argmax()
    l.append(m)
    wt2[0][m]=0
s=[]
for ll in l:
    s.append(feat_map[ll])


import numpy as np
import pandas as pd

data=pd.read_csv('salary-train.csv')
data_test=pd.read_csv('salary-test-mini.csv')
data.columns
data['FullDescription']=data['FullDescription'].str.lower()
data['FullDescription'] = data['FullDescription'].replace('[^a-zA-Z0-9]', ' ', regex = True)
data['LocationNormalized'].fillna('nan', inplace=True)
data['ContractTime'].fillna('nan', inplace=True)

data_test['FullDescription']=data_test['FullDescription'].str.lower()
data_test['FullDescription'] = data_test['FullDescription'].replace('[^a-zA-Z0-9]', ' ', regex = True)

from sklearn.feature_extraction.text import TfidfVectorizer
# vect=TfidfVectorizer(data['FullDescription'],min_df=5)
vect1=TfidfVectorizer(min_df=5)
x=vect1.fit_transform(data['FullDescription'])
feat_map=vect1.get_feature_names()
x2=vect1.transform(data_test['FullDescription'])


from sklearn.feature_extraction import DictVectorizer
enc = DictVectorizer()
X_train_categ = enc.fit_transform(data[['LocationNormalized', 'ContractTime']].to_dict('records'))
X_test_categ = enc.transform(data_test[['LocationNormalized', 'ContractTime']].to_dict('records'))

from scipy.sparse import  hstack
x1=hstack( [x,X_train_categ] )
xt=hstack( [x2,X_test_categ] )

from sklearn.linear_model import Ridge

n_samples, n_features = 10, 5
np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)
clf = Ridge(alpha=1.0,random_state=241)
clf.fit(X, y)

clf.fit(x1, data['SalaryNormalized'])
clf.predict(xt)


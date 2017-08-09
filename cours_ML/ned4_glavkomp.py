import pandas as pd
import numpy as np

data=pd.read_csv('close_prices.csv')
dd=pd.read_csv('djia_index.csv')
y1=np.array(dd['^DJI'])

from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
pca.fit(X)

pca.components_
print(pca.explained_variance_ratio_)

x=data.loc[:,'AXP':'XOM']
pca = PCA(n_components=10)
pca.fit(x)
l=pca.explained_variance_ratio_
l.cumsum()
[ 0.73897118,  0.84904287,  0.89899376,  0.92774295,  0.94989743,
        0.9692132 ,  0.97596173,  0.98210264,  0.98530858,  0.98836469]
xn=pca.transform(x)
x1=xn[:,0]
np.corrcoef(x1,y1)
cm=pca.components_
cm[0].argmax()

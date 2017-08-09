from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
data=load_iris()
feat=data.data
feat_names=data.feature_names
targ=data.target
targ_names=data.target_names

for t in range(3):
    if t==0:
        c='r'
        marker='>'
    elif t==1:
        c='g'
        marker='o'
    elif t==2:
        c='b'
        marker='x'

    plt.scatter(feat[targ==t,0],
                    feat[targ==t,1],marker=marker,c=c
                    )
plt.show()

lab=targ_names[targ]
plen=feat[:,2]
is_set=(lab=='setosa')
max_set=plen[is_set].max()
min_non_set=plen[~is_set].min()
print('Max of setosa: {}.'.format(max_set))

feat=feat[~is_set]
lab=lab[~is_set]
is_virg=(lab=='virginica')

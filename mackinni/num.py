import numpy as np
import pandas as pd
import sklearn

dt=np.array([[0.9526, -0.246 , -0.8856],
             [0.5639, 0.2379, 0.9104]])
dt.shape
dt.dtype
dt1=[6,7.5,8,0,1]
arr1=np.array(dt1)

ar2=np.arange(1,9)
ar3=ar2.reshape((2,3))
ar3.ndim

ar2.shape
np.zeros(10)
np.zeros((3,6))
np.empty((2,3,2))

np.eye(3,4)

ar3*ar3

import numpy.random as rnd
dat=rnd.randn(7,4)
names=np.array(['Bob', 'Joe', 'Will', 'ВоЬ', 'Will', 'Joe', 'Joe'])

names=='Bob'
dat[names=='Bob']
dat[names=='Bob',2:]
dat[~(names=='Bob')]
mask=(names=='Bob')|(names=='Will')
dat[mask]
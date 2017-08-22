from skimage.io import imread
image = imread('parrots.jpg')

import pylab
pylab.imshow(image)

from skimage import img_as_float
imf=img_as_float(image)

matr=imf.reshape(474*713,3)

from sklearn.cluster import KMeans
import numpy as np
# X = np.array([[1, 2], [1, 4], [1, 0],
#               [4, 2], [4, 4], [4, 0]])
# kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
# kmeans.labels_
#
# kmeans.predict([[0, 0], [4, 4]])
#
# kmeans.cluster_centers_
for ii in range(1,10):
    kmeans = KMeans(init='k-means++', random_state=241,n_clusters=ii).fit(matr)
    lm=[]
    for k in range(ii):

        lm.append(matr[kmeans.labels_==k])

    lmm=[]
    lmmd=[]
    for k in range(ii):

        lmm.append(np.mean(lm[k],0))
        lmmd.append(np.median(lm[k],0))

    almmd = np.array(lmmd)
    almm = np.array(lmm)
    newimfd = almmd[kmeans.labels_]
    newimf3d = newimfd.reshape(474, 713, 3)
    newimf = almm[kmeans.labels_]
    newimf3 = newimf.reshape(474, 713, 3)
    mse = np.linalg.norm(matr - newimf)
    # mse = 120.5462231417401
    mn = (3*337962) ** 0.5
    mse = mse / mn
    msed = np.linalg.norm(matr - newimfd)
    # mse = 120.5462231417401

    msed = msed / mn
    max1 = 1

    psnr = 20 * np.log10(max1 / mse)
    psnrd = 20 * np.log10(max1 / msed)
    print(ii,psnr,psnrd)

almmd=np.array(lmmd)

newimf=kmeans.cluster_centers_[kmeans.labels_]
newimf3=newimf.reshape(474, 713, 3)

np.linalg.norm(3,4)

import numpy.random as rnd
dat=rnd.randn(2,2)
dat0=np.zeros((2,2))

np.linalg.norm(matr-newimf)
mse=120.5462231417401
mn=337962**0.5
mse=mse/mn
max1=255

psnr=20*np.log10(max1/mse)

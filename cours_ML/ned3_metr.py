import numpy as np
import pandas as pd

data=pd.read_csv('cours_ML/classification.csv')
x=np.array(data['true'])
y=np.array(data['pred'])

from sklearn.metrics import accuracy_score
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
accuracy_score(y_true, y_pred)
0.53500000000000003

from sklearn.metrics import precision_score
0.55844155844155841

from sklearn.metrics import recall_score
0.42156862745098039

from sklearn.metrics import f1_score
0.48044692737430167
tp=43
fn=59
fp=34
tn=64

dt=pd.read_csv('cours_ML/scores.csv')
x=np.array(dt['true'])
ylg=np.array(dt['score_logreg'])
0.71918767507002801

ykn=np.array(dt['score_knn'])
0.63515406162464982

ytr=np.array(dt['score_tree'])
0.69192677070828335

ysvm=(np.array(dt['score_svm'])+1)/2
0.70868347338935567

from sklearn.metrics import roc_auc_score
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
roc_auc_score(y_true, y_scores)

from sklearn.metrics import precision_recall_curve
y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8])
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
recall[precision>=0.7].max()
precision[recall>=0.7].max()
0.63025210084033612
yy=[ylg,ykn,ytr,ysvm]
for y1 in yy:
    precision, recall, thresholds = precision_recall_curve(x, y1)
    print(precision[recall>=0.7].max())

tp=900
fp=100


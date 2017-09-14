import numpy as np

import pandas as pd
import os
print(os.getcwd())
adver_data = pd.read_csv('advertising.csv')
x=np.array(adver_data[['TV','Radio','Newspaper']].values)
y=np.array(adver_data['Sales'].values)
means=x.mean(axis=0)
std=x.std(axis=0)
x1=(x-means)/std
ed=np.ones((200,1))
x2=np.hstack((ed,x1))

def mserror(y, y_pred):
    return sum((y-y_pred)**2)/len(y)

def linear_prediction(X, w):
    return X.dot(w)

def stochastic_gradient_step(X, y, w, train_ind, eta=0.01):
    grad0 = (linear_prediction(X,w)[train_ind]-y[train_ind])*2/len(y)
    grad1 = X[train_ind,1]*(linear_prediction(X,w)[train_ind]-y[train_ind])*2/len(y)
    grad2 = X[train_ind,2]*(linear_prediction(X,w)[train_ind]-y[train_ind])*2/len(y)# Ваш код здесь
    grad3 = X[train_ind,3]*(linear_prediction(X,w)[train_ind]-y[train_ind])*2/len(y)# Ваш код здесь
    return  w - eta * np.array([grad0, grad1, grad2, grad3])

def stochastic_gradient_descent(X, y, w_init, eta=1e-2, max_iter=1e4,
                                min_weight_dist=1e-8, seed=42, verbose=False):
    # Инициализируем расстояние между векторами весов на соседних
    # итерациях большим числом.
    weight_dist = np.inf
    # Инициализируем вектор весов
    w = w_init
    # Сюда будем записывать ошибки на каждой итерации
    errors = []
    # Счетчик итераций
    iter_num = 0
    # Будем порождать псевдослучайные числа
    # (номер объекта, который будет менять веса), а для воспроизводимости
    # этой последовательности псевдослучайных чисел используем seed.
    np.random.seed(seed)

    # Основной цикл
    while weight_dist > min_weight_dist and iter_num < max_iter:
        # порождаем псевдослучайный
        # индекс объекта обучающей выборки
        iter_num = iter_num + 1
        wold = w
        random_ind = np.random.randint(X.shape[0])
        w = stochastic_gradient_step(X, y, w, random_ind, eta)
        errors.append(mserror(y, linear_prediction(X, w)))  # Ваш код здесь
        weight_dist = np.linalg.norm(w - wold)
    return w, errors

w0=np.zeros(4)
stoch_grad_desc_weights, stoch_errors_by_iter = stochastic_gradient_descent(x2,y,w0,max_iter=1e2)
print(stoch_grad_desc_weights)
print(stoch_errors_by_iter)
print(len(stoch_errors_by_iter))

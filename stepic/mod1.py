# def foo():
#     print('foo')

# a = [i + 1 for i in range(4)]
# a = [i for i in range(4)]
# a = [i for i in range(5)][1:]
# a = list(i + 1 for i in range(4))
# print(a)

#
# from math import ceil,sqrt
# import itertools
# def pr(x):
#     n=sqrt(x)
#     n=ceil(n)
#     t=True
#     for i in range(2,n+1):
#         if x%i==0:
#             t=False
#             break
#
#     return  t
# def primes():
#     i=1
#     yield 2
#     while True:
#         i+=1
#         if pr(i):
#             # print(i)
#             yield (i)
#
#
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# lines=[]
# f = open("dataset_24465_4.txt")
# for line in f:
#     line = line.rstrip()
#     lines.append(line)
# f.close()
# lines.reverse()
# # print(lines)
#
# f = open("test1.txt", "w")
#
# contents = "\n".join(lines)
# f.write(contents)
# f.close()

# import os.path
# for current_dir,dirs, files in os.walk("C:\main"):
#     for f in files:
#         if f.endswith('.py'):
#             print(current_dir[3:])
#             break

# s=str(input())
# t=str(input())
# i=0
# while t in s:
#     ind=s.index(t)
#     s=s[ind+1:]
#     # print(s)
#     i+=1
# print(i)

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(-10,10.01,0.01) #Массив значений аргумента
# plt.plot(x,x**2) #Построение графика
# plt.xlabel(r'$x$') #Метка по оси x в формате TeX
# plt.ylabel(r'$f(x)$') #Метка по оси y в формате TeX
# plt.title(r'$y=x^2$') #Заголовок в формате TeX
# plt.grid(True) #Сетка
# plt.show() #Показать график

# s=''
# spam=['a','b','t','c']
# for ss in range(len(spam)-1):
#     s+=spam[ss]+', '
# s+='and '+spam[-1]
# print(s)
# 'B : A'.split(': ').strip()
n=int(input())
a=[input() for i in range(n)]
# print(a)
d={}
for aa in a:
    k=aa.split(':')
    if(len(k)>1):
        d[k[0].strip()]=k[1].split()
    else:
        d[k[0].strip()]=''
print(d)
# for dd in d.values():





























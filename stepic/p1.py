# print(2+2)
# print (2+3)

# a=float(input())
# b=float(input())
# op=str(input())
#
# if(b==0 and ((op =='/' )| (op =='mod') | (op=='div'))):
#     print('Деление на 0!')
# elif (op=="+"):
#     print(a+b)
# elif (op == "-"):
#     print(a - b)
# elif (op == "/"):
#     print(a / b)
# elif (op == "*"):
#     print(a * b)
# elif (op == "mod"):
#     print(a % b)
# elif (op == "pow"):
#     print(pow(a,b))
# elif (op=="div"):
#     print(a//b)
#
# a=int(input())
# b=int(input())
# c=int(input())
# ar=[a,b,c]
# max1=max(a,b,c)
# min1=min(a,b,c)
# ar.remove(max1)
# ar.remove(min1)
# print(max1)
# print(min1)
# print(ar[0])

# n=int(input())
# if((n%10==1) and ((n//10)%10!=1)):
#     print(n,'программист')
# elif((n%10>=2) and (n%10<=4) and ((n//10)%10!=1)):
#     print(n, 'программиста')
# else:
#     print(n,'программистов')
# i = 0
# while i <= 6:
#     print('*'*i)
#     i+=1

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# n=int(input())
# i=1
# s=0
# while(i<=n):
#     s1=int(input())
#     s+=s1
#     i+=1
# print(s)
# id

# obj=[1,2,1,2,3]
# ans = 0
# obj1=[]
# for ob in obj: # доступная переменная objects
#     if (ob not in obj1):
#         obj1.append(ob)
#         ans += 1
# print(ans)
# print(obj1)

# def fn(a1,a2):
#     return a1+a2
# # x=fn('q',4)
# # print(x)
# type(fn)

# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     return x-x%5+5
# print(closest_mod_5(21))

# inf=open('1.txt','r')
#
# s1=inf.readline()
# s2=inf.readline()
# inf.close()
#
# with open('1.txt') as inf:
#     s1=inf.readline()
#     s2=inf.readline()
#     s=inf.readline().strip()

# with open('C:\\Users\\MokhnachevskiyAN\\Desktop\\Новый текстовый документ (3).txt') as inf:
#     for li in inf:
#         # li=li.strip()
#         print(li)

# ouf=open('1.txt','w')
# ouf.write('txt1\n')
# ouf.write(str(24))
# ouf.close()
#
# with open('1.txt','w') as ouf:
#     ouf.write('text2\n')
#     ouf.write(str(25))

# inf=open('dataset_.txt','r')
# a=inf.readline()
# i=0
# s=0
# b=''
# p=''
# for i in range(0,len(a)):
#     if a[i].isnumeric():
#
#         s=10*s+int(a[i])
#     else:
#         b+=p*s
#         s=0
#         p=a[i]
# b+=p*s
#
# print(b)

# b=[]
# d={}
# a=[]
# # a=[str(i).lower() for i in input().split()]
# with open('dataset_3363_3.txt') as inf:
#     for li in inf:
#         a+=li.lower().split()
# for aa in set(a):
#     d[aa]=a.count(aa)
# mm=max(d.values())
#
# for key in d:
#     if d[key]==mm:
#         b.append(key)
# b.sort()
# print(b[0],mm)
# print(d)
a=[]

# s=0
# s1=0
# s2=0
# s3=0
# with open('dataset_3363_4.txt') as inf:
#      for li in inf:
#          a.append(li.strip().split(';'))
#          # a=[str(i) for i in input().split(';')]
#
# for aa in a:
#     s=0
#     for i in range(1,len(aa)):
#         s+=int(aa[i])
#     print(s/3)
#     s1+=int(aa[1])
#     s2+=int(aa[2])
#     s3+=int(aa[3])
# l=len(a)
# print(s1/l,s2/l,s3/l)
# d={}
#
# def f(x):
#     return x*x-x+1
#
# n =int(input())
#
# for i in range(n):
#     x=int(input())
#     if x in d:
#         print(d[x])
#     else:
#         d[x]=f(x)
#         print(d[x])

# import mod1
# mod1.foo()

# r=float(input())
# import math
#
# print(2*math.pi*r)

# import subprocess
# subprocess.call(['cmd'])

# import sys
# for i in sys.argv:
#     if sys.argv.index(i)!=0:
#         print(i)
#
# import
# d={}
# with open('C:\\Users\\MokhnachevskiyAN\\Desktop\\dataset_3380_5.txt') as inf:
#     for li in inf:
#         a=[str(i) for i in li.split()]
#         k=a[0]
#         v=float(a[2])
#         if k not in d:
#             d[k] = [v]
#         else:
#             d[k]+=[v]
#
# for kk in range(1,12):
#     k=str(kk)
#     if k in d:
#         print(k,sum(d[k])/len(d[k]))
#     else:
#         print(kk,'-')
# d={"север":0,"юг":0,"восток":0,"запад":0}
# n=int(input())
# for i in range(n):
#     a=input().split()
#     if a[0] not in d:
#         d[a[0]] = int(a[1])
#     else:
#         d[a[0]]+=int(a[1])
# # print(d)
#
# print(d['восток']-d['запад'],d['север']-d['юг'])
# 'r'.lower()
# a=[]
# b={}
#
# n=int(input())
# for i in range(n):
#     a.append(input().lower())
#
# m=int(input())
# for k in range(m):
#     for ss in (input().lower().split()):
#
#         if ss not in a:
#             b[ss] = ss
#
# for k in b:
#     print(b[k])
# d={}
# e={}
# a=input()
# b=input()
# x=''
# y=''
# for i in range(len(a)):
#     d[a[i]]=b[i]
#     e[b[i]]=a[i]
# # print(d)
# # print(e)
# a1=input()
# a2=input()
# for b1 in a1:
#     x+=d[b1]
# print(x)
# for b1 in a2:
#     y+=e[b1]
# print(y)
#

import re
# m=re.match('foo','on the table foo')
# print(m)
# if m is not None:
#     m.group()
#
# m1=re.search('foo','seafood')
# print(m1)

# bt='bat|bet|bit'
# m=re.match(bt,'bat')
# if m is not None:print(m.group())
#
# m=re.match(bt,'blt')
# if m is not None:print(m.group())
#
# m=re.match(bt,'He bit me')
# if m is not None:print(m.group())
#
# m=re.search(bt,'He bit me')
# if m is not None:print(m.group())

# anye='.end'
# m=re.match(anye,'bend')
# if m is not None:print(m.group())
#
# m=re.match(anye,'end')
# if m is not None:print(m.group())
#
# m=re.match(anye,'\nend')
# if m is not None:print(m.group())
#
# m=re.search(anye,'The end')
# if m is not None:print(m.group())

# pat='3.14'
# pi='3\.14'
# m=re.match(pi,'3.14')
# if m is not None:print(m.group())
# m=re.match(pat,'3014')
# if m is not None:print(m.group())
# m=re.match(pat,'3.14')
# if m is not None:print(m.group())

# patt='\w+@(\w+\.)?\w+\.com'
# print(re.match(patt,'nobody@xxx.com').group())
# print(re.match(patt,'nobody121@www.xyz1.com').group())
#
# import sys
# patt=''
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search()

# put your python code here
# import  re,sys
# ss=r'cat'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.findall(ss,line)
#     if len(res)>1:
#         print(line)
#
# import re, sys
#
# ss = r'\bcat\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     res = re.findall(ss, line)
#     if len(res) >= 1:
#         print(line)
#
# import re,sys
# ss=r'z.{3}z'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.findall(ss,line)
#     if len(res)>=1:
#
#         print(line)
#
# import re,sys
# ss=r'\\'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.search(ss,line)
#     if res:
#         print(line)

# import sys,re
# ss=r'\b(\w+)\1\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.search(ss,line)
#     if res:
#         print(line)

# import sys,re
# ss=r'\b[Aa]+\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.sub(ss,'argh',line,1)
#     print(res)
#     # print(line)

# import sys,re
# ss=r'\b(\w)(\w)'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.sub(ss,r'\2\1',line)
#     print(res)
    # print(line)

# import sys,re
# ss=r'(\w)\1+'
# for line in sys.stdin:
#     line = line.rstrip()
#     res=re.sub(ss,r'\1',line)
#     print(res)

import requests,re

u1=input()
u2=input()
res=requests.get(u1)
txt=res.text
s=r'(<a[^>]+href=")(.+)(".*>)'
# s=r'=\".+>'

# for line in txt:
#     print(line)
ss='No'
ls=re.findall(s,txt)
for ur in ls:
    print('url1='+ur[1])
    res1=requests.get(ur[1])
    txt1 = res1.text
    ls1 = re.findall(s, txt1)
    print(ls1)
    for ur1 in ls1:
        if u2 in ur1:
            ss='Yes'
            break
print(ss)


















import os
di=os.path.join('c','files','android')

myFiles=['acc.txt','det.csv','inv.doc']
for fname in myFiles:
    print(os.path.join('c:\\users\\asweig',fname))

os.getcwd()

os.makedirs('c:\\scripts\\pyth\\test')

os.path.abspath('.')

os.path.relpath('c:\\scripts','.')

path='c:\\windows\\system32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)

os.path.getsize(path)
os.path.split(path)
path.split(os.path.sep)

os.listdir('c:\\scripts')

totSize=0
for fn in os.listdir('c:\\scripts'):
    totSize=totSize+os.path.getsize(os.path.join('c:\\scripts',fn))
    print(fn,os.path.getsize(os.path.join('c:\\scripts',fn)))
print(totSize)

hFile=open('c:\\scripts\\res.txt')
hCont=hFile.read()

bacF=open('bacon.txt','w')
bacF.write('Hello , w!')
bacF.close()

bacF=open('bacon.txt')
cont=bacF.read()
bacF.close()
print(cont)

import shelve
shF=shelve.open('mydata')
cats=['zop','pook','sim']
shF['cats']=cats
shF.close()

shF=shelve.open('mydata')
print(type(shF))
print(shF['cats'])
shF.close()













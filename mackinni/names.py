import pandas as pd
nam1880=pd.read_csv('ch02/names/yob1880.txt',names=['name','sex','births'])
# print(nam1880.head())
namgr=nam1880.groupby('sex').births
print(type(namgr))
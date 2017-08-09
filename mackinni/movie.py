import pandas as pd
import os
# print(os.getcwd())
unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('ch02/movielens/users.dat',sep='::',header=None,names=unames,engine='python')
# print(users[:3])
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('ch02/movielens/ratings.dat',sep='::',header=None,names=rnames,engine='python')
mnames=['movie_id','title','genres']
movies=pd.read_table('ch02/movielens/movies.dat',sep='::',header=None,names=mnames,engine='python')
# print(ratings[:5])
# print(movies[:5])
# print(type(ratings))
# print(type(rnames))
data=pd.merge(pd.merge(ratings,users),movies)
# print(data.ix[0])

# print(data.groupby('title').size())
dat1=data.pivot_table(data,rows='title',cols='gender',aggfunc='mean')
print(dat1[:5])
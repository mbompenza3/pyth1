path='ch02/usagov_bitly_data2012-03-16-1331923249.txt'

# print(open(path).readline())
import json
rec=[json.loads(line) for line in open(path)]
# for r in rec[0]:
#     print(r +": "+str(rec[0][r]))
# print(rec[0]['tz'])
tzon=[rectz['tz'] for rectz in rec if 'tz' in rectz]
# print(tzon[:10])

def get_counts(seq):
    cnts={}
    for x in seq:
        if x in cnts:
            cnts[x]+=1
        else:
            cnts[x]=1
    return cnts

cnts=get_counts(tzon)
# print((cnts))
# print(len(tzon))

def top_cnts(cnt_dict,n=10):
    valkp=[(cnt,tz) for tz,cnt in cnt_dict.items()]
    valkp.sort()
    return valkp[-n:]

# print(top_cnts(cnts))

from collections import Counter
cnts=Counter(tzon)
# print(cnts.most_common(10))

from pandas import DataFrame,Series
import pandas as pd
frame=DataFrame(rec)
# print(frame)
# print(frame['tz'][:10])

tz_cnts=frame['tz'].value_counts()
# print(tz_cnts[:10])

cln_tz=frame['tz'].fillna('missing')
cln_tz[cln_tz=='']='unknown'
tz_cnts=cln_tz.value_counts()
# print(tz_cnts[:10])

# pl= tz_cnts.plot(kind='barh',rot=0)

# import matplotlib.pyplot as plt
# plt.hist(tz_cnts[:10])
# plt.show()

# print(frame['a'][1])
reslts=Series([x.split()[0] for x in frame.a.dropna()])
print(reslts[:5])
print(reslts.value_counts()[:8])

cfr=frame[frame.a.notnull()]

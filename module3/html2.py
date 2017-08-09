import requests, re

u1 = input()
# u2 = input()
res = requests.get(u1)
# res = requests.get('http://pastebin.com/raw/hfMThaGb')
txt = res.text
s = r'(<a[^>]+href=[\"\'])(\w*?://)?(\w[\w\.\-]+)'
aa=[]
ss = 'No'
ls = re.findall(s, txt)
for ur in ls:
    aa.append(ur[2])

aa=set(aa)
aa=list(aa)
aa.sort()
for li in aa:
    print(li)
    # res1 = requests.get(ur[1])
    # txt1 = res1.text
    # ls1 = re.findall(s, txt1)
    #
    # for ur1 in ls1:
    #     if u2 in ur1:
    #         ss = 'Yes'
    #         break

# ss=input()
# print(ss[2])
# print(ss[-2])
# print(ss[:5])
# print(ss[:-2])
# print(ss[0::2])
# print(ss[1::2])
# print(ss[::-1])
# print(ss[::-2])
# print(len(ss))

# st = input()
# i = st.rfind('f')
# i1 = st[::-1].find('f')
#
# if i > -1:
#     print(i, end=' ')
# if i1 > -1 and i1 != i:
#     i1 = len(st) - i1 - 1
#     print(i1)

st = input()
print(st[:st.find('h')],st[st.rfind('h')+1:],sep='')

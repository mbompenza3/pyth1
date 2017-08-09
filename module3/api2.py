# import requests
#
# api_url0 = "http://numbersapi.com/"
# params = {
#     'json': 'true',
# }
# # city = input().split('\n')
# inf=open('dataset_24476_3.txt','r')
# for li in inf:
#     li = li.strip()
#     # print(li)
#     api_url = api_url0 + li + "/math"
#     res = requests.get(api_url, params=params)
#     data = res.json()
#     if data['found']:
#         print('Interesting')
#     else:
#         print('Boring')
import requests
import json

client_id = 'c6653f078651c24b6427'
client_secret = '6056893ccad7ac809ccbf5b57958e22c'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
sp=[]
# инициируем запрос с заголовком
inf=open('dataset_24476_3.txt','r')
for li in inf:
    li = li.strip()
    r = requests.get("https://api.artsy.net/api/artists/"+li, headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    # print(j['sortable_name'],j['birthday'])
    sp.append((j['birthday'],j['sortable_name']))
sp.sort()
for ss in sp:
    print(ss[1])
#
# template = 'Current temperature in {} is {}'
# print(template.format(city, data["main"]["temp"]))

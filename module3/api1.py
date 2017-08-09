import requests

api_url0 = "http://numbersapi.com/"
params = {
    'json': 'true',
}
# city = input().split('\n')
inf=open('dataset_24476_3.txt','r')
for li in inf:
    li = li.strip()
    # print(li)
    api_url = api_url0 + li + "/math"
    res = requests.get(api_url, params=params)
    data = res.json()
    if data['found']:
        print('Interesting')
    else:
        print('Boring')
# returns json.loads(res.text) :)




#
# template = 'Current temperature in {} is {}'
# print(template.format(city, data["main"]["temp"]))

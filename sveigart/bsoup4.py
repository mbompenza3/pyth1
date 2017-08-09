
import requests, bs4
# res=requests.get('http://nostarch.com/automatestuff')
# res.raise_for_status()
# noSoup=bs4.BeautifulSoup(res.text)
# type(noSoup)
exFile=open('example.html')
exSoup=bs4.BeautifulSoup(exFile,"html5lib")
elems=exSoup.select('#author')
elems[0].getText()
pEl=exSoup.select('p')
pEl[0]
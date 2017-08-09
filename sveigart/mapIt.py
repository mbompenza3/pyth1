#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


import requests
res=requests.get('http://gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)
# res.status_code
# len(res.text)
# print(res.text[:200])
res.raise_for_status()
plFile=open('RandJ1.txt','w')
plFile.write(res.text)
plFile.close()

import requests, bs4
res=requests.get('http://nostarch.com/automatestuff')
res.raise_for_status()
noSoup=bs4.BeautifulSoup(res.text)
type(noSoup)
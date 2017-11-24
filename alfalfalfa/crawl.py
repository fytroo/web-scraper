import os
import glob
import urllib.request
import codecs
import csv
from bs4 import BeautifulSoup
import time
import re
from datetime import datetime
access = 'implement'
print('here')
def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

fname = 'docs/item_list.txt'
open(fname,'w').write('')
f = open(fname,'a',encoding='utf8')
print(fname)
for n in range(190000,1,-1):
    url = 'http://alfalfalfa.com/articles/{}.html'.format(n)
    try:
        url_html(url)
        f.write(url+'\n')
        print(url)
    except:
        print('404')
#        pass

#    time.sleep(2)
#

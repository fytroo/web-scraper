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



def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html


url = 'http://hayabusa.open2ch.net/test/read.cgi/livejupiter/1498437699/'
html = url_html(url)
soup = BeautifulSoup(html,'html.parser')
t = [ a.extract() for a in soup.select('ares')]
line = '\t'.join(['res','alias','text', 'anchor','since', 'url','access'])+'\n'
lines = [line]


a = soup.select('dt')[0].text
a = a[a.find('おーぷん：'):a.find('ID')][:-1].replace('おーぷん：','')
YYYY, mm, DD = a.split('(')[0].split('/')
HH, MM, SS = a.split(')')[1].split(':')
when = YYYY+mm+DD+'T'+HH+MM+SS+'+0900'

res0 = soup.select('h1')[0].get_text()
now = datetime.now().strftime('%Y%m%dT%H%M%S+0900')
line = '\t'.join([str(0),'tamako',res0,'-1',when,url,access])+'\n'
lines.append(line)

for (dt,dd) in zip(soup.select('dt'),soup.select('dd')):
    res = dt.get('res')
    anchor = dd.select('a[href^="/test/read.cgi"]')
    if len(anchor)==0:
        anchor = 0
    else:
        anchor = anchor[0].text[2:]
        for a in dd.select('a[href^="/test/read.cgi"]'):
            a.extract()
    text = re.sub(r'\n+','',dd.text)
    line = '\t'.join([res,'tamako',text,str(anchor),when,url,access])+'\n'
    lines.append(line)

fname = open('docs/1498437699.tsv','w',encoding='utf8')
for line in lines:
    fname.write(line)

import os
import glob
import urllib.request
from bs4 import BeautifulSoup
import time
from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)
from datetime import datetime


def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html


narou_root_url = 'http://ncode.syosetu.com/'
work_id = 'n9735cv'

url = narou_root_url+work_id
html = url_html(url)
soup = BeautifulSoup(html,'html.parser')

tsv_fname = 'narou_docs/narou.'+work_id+'.tsv'
tsv = open(tsv_fname,'w')
tsv.write('name\tsince\tuser_note\ttext\turl\twhen\taccess\tcard_note\n')

pretext_id = 0
who = soup.select('.novel_writername')[0].a.text
access = 'public'
note = 'corpus narou dev oz'
for sub in soup.select('.novel_sublist2'):
    url = 'http://ncode.syosetu.com'+sub.a.get('href')
    date = sub.select('.long_update')[0]\
        .get_text().split('\n')[1].split(' ')
    when = ''.join(date[0].split('/'))+'T'+''.join(date[1].split(':'))+'00+0900'
    work_fname = 'narou_docs/narou.'+'.'.join(url.split('/')[3:5])+'.doc.txt'
    lines = open(work_fname).readlines()   
    for line in lines:
        if len(line.rsplit())==0:
            continue
        text = line[:-1].replace('　',' ')
        now = datetime.now().strftime("%Y%m%dT%H%M%S+0900")
        tsv.write('\t'.join([who, now, note, text, url, when, access, note])+'\n')


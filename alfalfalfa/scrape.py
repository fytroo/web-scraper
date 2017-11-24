import os
import urllib.request
from bs4 import BeautifulSoup
import re
from datetime import datetime
from pytz import timezone
import pandas as pd
import csv
import time

def iso2utc(iso):
    try:
        return timezone('UTC').localize(pd.to_datetime(iso))
    except:
        return None

def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

def br2ln(soup):
    text = str(soup)
    text = re.sub('^(.+?)&gt;&gt;([0-9]+)<br>(.+?)$','\\1<anchor>\\2</anchor><text>\\3</text>',text)
    text = re.sub('<br\s*?>', '\n', text)
    text = re.sub('\n+', '\n', text)
    return BeautifulSoup(text,'html.parser')

def url_csv(url):
    max_col_nb = 6
    
    html = url_html(url)
    soup = BeautifulSoup(html,'html.parser')
    t = [ a.extract() for a in soup.select('ares')]
    t = [ e.extract() for e in soup.select('aside')]

    lines = []

    a = soup.select('.article_time')[0].text.split()
    YYYY, mm, dd = a[0].split('-')
    HH, MM, SS = a[1].split(':')
    iso = YYYY+mm+dd+'T'+HH+MM+SS
    since = iso2utc(iso).isoformat()

    res0 = soup.select('.main_article_title')[0].text.split()[0]
    img = soup.select('.main_article_thumb')[0].select('img')[0].get('src')
    
    line = [str(0),'-1',res0,since,url,img]
    lines.append(line)

    for block in soup.select('.res_block'):
        if len(block.select('.news_quote')):
            res = '1'
            since = since
            news_quote = br2ln(block.select('.news_quote')[0])
            text = news_quote.text
            anchor = '0'
            imgs = [ e.get('src') for e in news_quote.select('img') ]

        if len(block.select('.res_info')):
            if not 'id' in block.attrs:
                res_body = br2ln(block.find_all(class_=re.compile('^res_body*'))[0])
                imgs = [ e.get('src') for e in res_body.select('img') ]
                lines[-1]+=imgs
                continue
            
            res = block.get('id').split('_')[1]

            date = block.select('.res_date')[0].text
            YYYY, mm, DD = date.split('(')[0].split('/')
            HH, MM, SS = date.split(')')[1].split()[0].split('.')[0].split(':')
            iso = YYYY+mm+dd+'T'+HH+MM+SS
            since = iso2utc(iso).isoformat()

            res_body = br2ln(block.find_all(class_=re.compile('^res_body*'))[0]) 
            text = res_body.text
            
            anchor = '0'
            if len(res_body.select('anchor')):
                anchor = res_body.find('anchor').text
                text = res_body.find('text').text

            imgs = [ e.get('src') for e in res_body.select('img') ]
            
        line = [str(res),str(anchor),text,since,url]+imgs
        lines.append(line)
        max_col_nb = max(max_col_nb, len(line))

    header = ['res','anchor','text','since','url','img']
    header+= ['img' for _ in range( max_col_nb - 6 ) ]

    return [header] + lines

def main(url):
    lines = url_csv(url) 
    fname = 'docs/'+url.split('/')[-1].split('.')[0]+'.csv'
    with open(fname,'w', encoding='utf-8',errors='replace') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(lines)

f = open('item_list.txt','r',encoding='utf8')
url = f.readline()[:-1]
while url:
    try:
        main(url)
        print(url,'success to csv')
    except:
        print(url,'falied')
    url = f.readline()[:-1]
    time.sleep(7)

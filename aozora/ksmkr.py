import os
import glob
import urllib.request
import codecs
import csv
from bs4 import BeautifulSoup

def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

if __name__ == '__main__':
    url = 'http://www.aozora.gr.jp/cards/000148/files/776_14941.html'
    html = url_html(url)
    soup = BeautifulSoup(html,'html.parser')
    soup = soup.select(".main_text")[0]
    #for i in range(100):
    for ruby in soup.select("ruby"):
        ruby.replace_with(ruby.find('rb'))
    text = soup.get_text()
    with open('aozaora.776_14941.doc.txt','w') as f:
        f.write(text)

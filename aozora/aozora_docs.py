import urllib.request
from bs4 import BeautifulSoup
import time

work_urls = open('_aozora_works.txt','r').read().split('\n')

def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

for work_url in work_urls:
    try:
        html = url_html(work_url)
        soup = BeautifulSoup(html,'html.parser')
        soup = soup.select('.main_text')[0]
        
        for ruby in soup.select('ruby'):
            ruby.replace_with(ruby.find('rb'))
        text = soup.get_text()
        fname = 'aozora_doc/aozaora.'+work_url.split('/')[-1].split('.')[0]+'.doc.txt'
        with open(fname,'w') as f:
            f.write(work_url)
            f.write(text)

        text = text.replace('。','。\n')
        fname = 'aozora_doc/aozaora.'+work_url.split('/')[-1].split('.')[0]+'.ln.txt'
        with open(fname,'w') as f:
            f.write(work_url)
            f.write(text)
        print(fname)

    except:
        print('ouch',work_url)
        pass

    time.sleep(7)


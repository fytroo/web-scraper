import os
import glob
import urllib.request
import codecs
import csv
from bs4 import BeautifulSoup
import time

def url_html(url):
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()
    return html

if __name__ == '__main__':
    root_url = 'http://www.aozora.gr.jp/'
    open('aozora_urls.txt','w').write('')

    html = url_html(root_url)
    soup = BeautifulSoup(html,'html.parser')
    aiueo = [ a.get('href') for a in soup.select('a[href^="index_pages/sakuhin_"]')]

    for aiu in aiueo:
        html = url_html(root_url+aiu)
        soup = BeautifulSoup(html,'html.parser')
        cards = [ a.get('href') for a in soup.select('a[href^=../cards""]')]

        for card in cards:
            tyr:
                card_url = root_url+'/'.join(card.split('/')[1:])
                html = url_html(card_url)
                soup = BeautifulSoup(html,'html.parser')
                text_url = '/'.join(card_url.split('/')[:-1])+'/'+'/'.join(soup.select('a[href^=./files/""]')[0].get('href').split('/')[1:])
                fname = text_url.split('/')[-1].split('.')[0]
                print(text_url)

                with open('aozora_urls.txt','a') as f:
                    f.write(text_url+'\n')
            except:
                pass

            time.sleep(10)

        print('complete '+aiu)

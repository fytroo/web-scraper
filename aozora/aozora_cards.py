from bs4 import BeautifulSoup
import time

root_url = 'http://www.aozora.gr.jp/'

open('aozora_works.txt','w').write('')
aiueo = open('aozora_aiueo.txt','r').read().split('\n')[:-1]

for ai in aiueo:
    html = url_html(ai)
    soup = BeautifulSoup(html,'html.parser')

    card_urls = [ root_url+'/'.join(a.get('href').split('/')[1:]) for a in soup.select('a[href^=../cards]')]
    for card_url in card_urls:
        try:
            html = url_html(card_url)
            soup = BeautifulSoup(html,'html.parser')
            text_url = '/'.join(card_url.split('/')[:-1])+'/'+'/'.join(soup.select('a[href^=./files/]')[0].get('href').split('/')[1:])

            with open('aozora_works.txt','a') as f:
                f.write(text_url+'\n')
        except:
            pass

        time.sleep(10)

    print('###complete ',ai,'###')


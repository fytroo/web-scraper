import os
import sys
import traceback
from mimetypes import guess_extension
from time import time, sleep
from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup
import json
import subprocess

MY_EMAIL_ADDR = 'sktnkysh@gmail.com'

import argparse
parse = argparse.ArgumentParser(description='...')
parse.add_argument('query', type=str)
parse.add_argument('--number', '-n', default=10, type=int)
args = parse.parse_args()


class Fetcher:
    def __init__(self, ua=''):
        self.ua = ua

    def fetch(self, url):
        req = Request(url, headers={'User-Agent': self.ua})
        try:
            with urlopen(req, timeout=3) as p:
                b_content = p.read()
                mime = p.getheader('Content-Type')
        except:
            sys.stderr.write('Error in fetching {}\n'.format(url))
            sys.stderr.write(traceback.format_exc())
            return None, None
        return b_content, mime


fetcher = Fetcher(MY_EMAIL_ADDR)


def fetch_and_save_img(query):
    data_dir = 'data/{}/'.format(query.replace(' ', '_'))
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    for i, img_url in enumerate(img_url_list(query)):
        sleep(0.1)
        img, mime = fetcher.fetch(img_url)
        if not mime or not img:
            continue
        ext = guess_extension(mime.split(';')[0])
        if ext in ('.jpe', '.jpeg'):
            ext = '.jpg'
        if not ext:
            continue
        result_file = os.path.join(data_dir, str(i) + ext)
        with open(result_file, mode='wb') as f:
            f.write(img)
        print('fetched', img_url)


def img_url_list(query):
    res = subprocess.run(
        ['node', 'banana.js', '-q', query, '-n', str(args.number)],
        stdout=subprocess.PIPE).stdout
    img_urls = [e['url'] for e in json.loads(res)]
    return img_urls


if __name__ == '__main__':
    fetch_and_save_img(args.query)

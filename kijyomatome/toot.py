import os

from datetime import datetime
from pytz import timezone
import pandas as pd
now = lambda: datetime.now(timezone('UTC')).isoformat()
url = lambda n: 'http://alfalfalfa.com/articles/{}.html'.format(n)
iso2utc = lambda iso: timezone('UTC').localize(pd.to_datetime(iso))

import time

from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)

alias = 'tamako'
access = 'implement'

def main(fname):
    df = pd.read_csv(fname)

    res2id = {}
    for i in range(len(df)):
        res = int(df.ix[i]['res'])
        anchor = int(df.ix[i]['anchor'])
        text = str(df.ix[i]['text'])
        since = str(df.ix[i]['since'])
        url = str(df.ix[i]['url'])
        imgs = list(df.ix[i,5:].dropna())
        
        if anchor == -1:
            note_id = gdb.query('''
MATCH (a:Account) WHERE a.alias="%s"
CREATE (a)-[r:Toot {when:"%s"}]->
(b:Note:Implement {text:"%s",url:"%s",since:"%s",access:"%s",imgs:%s})
RETURN ID(b)
'''%( alias, now(), text, url, since, access, imgs ), data_contents=True)[0][0]
            res2id[res]=note_id
        else:
            note_id = gdb.query('''
MATCH (a:Account),(c:Note) WHERE a.alias="%s" AND ID(c)=%s
CREATE (a)-[r:Toot {when:"%s"}]->
(b:Note:Implement {text:"%s",url:"%s",since:"%s",access:"%s",imgs:%s})-
[:Anchor]->(c)
RETURN ID(b)
'''%( alias, res2id[anchor], now(), text, url, since, access, imgs ), data_contents=True)[0][0]
            res2id[res]=note_id

docs = os.listdir('docs')
docs.sort()
for doc in docs[::-1]:
    fname = 'docs/'+doc
    try:
        main(fname)
        print(fname,'tooted')
    except:
        print(fname,'falied')
    time.sleep(1)

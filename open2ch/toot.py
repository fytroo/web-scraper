from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)
from datetime import datetime
import os

for fname in os.listdir('docs'):
    
    lines = open('docs/'+fname).readlines()
    
    # skip header
    lines = lines[1:]
    pre_card_id = 0
    res2id = {}
    for line in lines:
        # cut \n terminal
        line = line[:-1]
        res, alias, text, anchor, since, url, access = line.split('\t') 
        now = datetime.now().strftime("%Y%m%dT%H%M%S+0900")
        
        res = int(res)
        anchor = int(anchor)
        if anchor == -1:
            card_id = gdb.query('\
                MATCH (a:Account) WHERE a.alias="%s"\
                CREATE (a)-[r:Toot {when:"%s"}]->(b:Card:Dev {text:"%s", url:"%s", since:"%s", access:"%s"})\
                RETURN ID(b)\
                '%( alias, now, text, url, since, access ), data_contents=True)[0][0]
            res2id[res]=card_id    
        else:
            card_id = gdb.query('\
                MATCH (a:Account),(c:Card) WHERE a.alias="%s" AND ID(c)=%s\
                CREATE (a)-[r:Toot {when:"%s"}]->(b:Card:Dev {text:"%s", url:"%s", since:"%s", access:"%s"})-[:Anchor]->(c)\
                RETURN ID(b)\
                '%( alias, res2id[anchor], now, text, url, since, access ), data_contents=True).elements[0][0]
            res2id[res]=card_id    

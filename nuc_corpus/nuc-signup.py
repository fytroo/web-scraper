from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)
from datetime import datetime
import random

with open('nuc-accounts.txt') as f:
    line = f.readline()
    while line:
        account_handle, account_bio = line.split('#')
        account_alias = 'nuc_'+account_handle
        account_bio = account_bio.rsplit()[0]
        now = datetime.now().strftime("%Y%m%dT%H%M%S+0900")
        color = '#'+str(random.randint(0,16777215))#ffffff
        now = datetime.now().strftime("%Y%m%dT%H%M%S+0900")
        gdb.query('MERGE (a:Account:Implement {handle:"%s"})'%(account_handle), data_contents=True)
        gdb.query('''
            MATCH (a:Account) WHERE a.name="%s"
            SET a+={alias:"%s",bio:"%s",since:"%s",color:"%s"}
        '''%(account_handle, account_alias, account_bio, now, color), data_contents=True)
        line = f.readline()

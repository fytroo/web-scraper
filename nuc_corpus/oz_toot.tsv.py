from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)
from datetime import datetime

work_id = 'n9735cv'
tsv_fname = 'narou_docs/narou.'+work_id+'.tsv'
lines = open(tsv_fname).readlines()

# skip header
lines = lines[1:]
pre_card_id = 0
for line in lines:
    # cut \n terminal
    line = line[:-1]
    who, since, user_note, text, url, when, access, card_note = line.split('\t') 
    now = datetime.now().strftime("%Y%m%dT%H%M%S+0900")
    card_id = gdb.query('\
        MATCH (a:User) WHERE a.name="%s"\
        CREATE (a)-[r:Toot {when:"%s", note:"%s"}]->(b:Card {text:"%s", url:"%s", since:"%s", access:"%s", note:"%s"})\
        RETURN ID(b)\
        '%( who, now, user_note, text, url, when, access, card_note ), data_contents=True).elements[0][0]
    if( pre_card_id ):
        gdb.query('\
            MATCH (a:Card),(b:Card)\
            WHERE ID(a)=%s AND ID(b)=%s\
            CREATE (a)-[r:Anchor {when:"%s", note:"%s"}]->(b)'\
            %( card_id, pre_card_id, now, card_note ), data_contents=True)

    pre_card_id = card_id

from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)


with open('nuc-accounts.txt') as f:
    line = f.readline()
    while line:
        account_name, account_bio = line.split('#')

        gdb.query('MERGE (a:Account:Dev {name:"%s"})'%(account_name), data_contents=True)
        gdb.query('MATCH (a:Account:Dev) WHERE a.name="%s" SET a.bio="%s"'\
            %(account_name,account_bio), data_contents=True)
        line = f.readline()

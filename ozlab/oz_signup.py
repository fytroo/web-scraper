from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)
from datetime import datetime
import random
account_name = '松 恭平'
account_alias = 'narou_490401'
account_bio = \
'''　はじめまして。松恭平という者です。『宝石世界クロニクル』という小説を投稿しています。人との出会いや繋がりを、大事に描いていきたいと思っています。俺TUEEEモノになる予定ですが、ストーリーの展開が少し遅いかもしれません。
　小説を書くのは初めての経験なので、至らない点も多々あるかと思いますが、よろしくお願いいたします。'''
color = '#'+str(random.randint(0,16777215))#ffffff
now = datetime.now().strftime("%Y%m%dT%H%M%S+0900")
note = 'corpus narou dev oz'
gdb.query('MERGE (a:Account:Dev {name:"%s"})'%(account_name), data_contents=True)
gdb.query('\
    MATCH (a:Account:Dev) WHERE a.name="%s"\
    SET a+={alias:"%s",bio:"%s",since:"%s",color:"%s",note:"%s"}'\
    %(account_name, account_alias, account_bio, now, color, note), data_contents=True)

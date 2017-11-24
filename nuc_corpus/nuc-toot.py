import mojimoji
from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)
from datetime import datetime
from datetime import datetime
from pytz import timezone
now = lambda: datetime.now(timezone('UTC')).isoformat()
url = lambda n: 'http://alfalfalfa.com/articles/{}.html'.format(n)
iso2utc = lambda iso: timezone('UTC').localize(pd.to_datetime(iso))


for i in range(1,130):

    when = '20170609T000000+0900'
    access = 'public'    
    try:
        when = open('nuc-headers/data.'+str(i)+'.header.txt').read()\
            .split('\n')[1]
        when = '２０'.join(when.split('２０')[1:])
        YYYY = '２０'+when.split('年')[0]
        MM = when.split('年')[1].split('月')[0]
        while len(MM)<2:
            MM = '０'+MM
        DD = when.split('月')[1].split('日')[0]
        while len(DD)<2:
            DD = '０'+DD

        when = mojimoji.zen_to_han(YYYY+MM+DD)+'T000000+0900'
    except:
        pass

    try:
        fname = 'nuc-docs/data.{}.doc.txt'.format(i)
        with open(fname) as f:
            line = f.readline()
            pre_card_id = 0

            while line:
                who, text = line.split('#')
                text = text.rsplit()[0]
                gdb.query('''
                    MATCH (a:Account) WHERE a.name="%s"
                    CREATE (a)-[r:Toot {when:"%s"}]->
                    (b:Note:Implement {text:"%s", since:"%s", access:"%s"})
                    RETURN ID(b)
                    '''%( who, now(), text, when, access ), data_contents=True)[0][0]
                if( pre_card_id ):
                    gdb.query('''
                        MATCH (a:Note),(b:Note)
                        WHERE ID(a)=%s AND ID(b)=%s
                        CREATE (a)-[r:Anchor {when:"%s"}]->(b)
                    '''%( card_id, pre_card_id, now() ), data_contents=True)

                line = f.readline()
                pre_card_id = card_id
    except:
        pass

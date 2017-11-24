import mojimoji
from neo4jrestclient.client import GraphDatabase
url = "http://neo4j:}apTap{ov3@localhost:7474/db/data/"
gdb = GraphDatabase(url)

for i in range(1,130):

    when = '20170609T______'
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

        when = mojimoji.zen_to_han(YYYY+MM+DD)+'T______'
    except:
        pass

    try:
        fname = 'nuc-docs/data.{}.doc.txt'.format(i)
        with open(fname) as f:
            line = f.readline()
            pretext_id = 0

            while line:
                who, text = line.split('#')
                text = text.rsplit()[0]
                text_id = gdb.query('\
                    CREATE (a:Card {text:"%s"})\
                    RETURN ID(a)'\
                    %( text ), data_contents=True)[0][0]
                gdb.query('\
                    MATCH (a:Account),(b:Card)\
                    WHERE a.name="%s" AND ID(b)=%s\
                    CREATE (a)-[r:Toot {when:"%s"}]->(b)'\
                    %( who, text_id, when ), data_contents=True)
                if( pretext_id ):
                    gdb.query('\
                        MATCH (a:Card),(b:Card)\
                        WHERE ID(a)=%s AND ID(b)=%s\
                        CREATE (a)-[r:Anchor {when:"%s"}]->(b)'\
                        %( text_id, pretext_id, when ), data_contents=True)

                line = f.readline()
                pretext_id = text_id
    except:
        pass

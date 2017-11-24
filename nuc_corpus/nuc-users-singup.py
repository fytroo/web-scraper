import secure 

url = secure.url
gdb = GraphDatabase(url)


gdb.nodes.create(text=toot_text, when=now, who="test_user")

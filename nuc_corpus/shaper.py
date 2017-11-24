for i in range(1,130):
    ii = str(i)
    while len(ii)<3:
        ii = '0'+ii

    fname = 'nuc-utf8/data'+ii+'.utf8.txt'
    gname = 'nuc-docs/data'+ii+'.doc.txt'
    text = open(fname,'r').read()
    with open(gname,'w') as f:
        f.write(text)

for i in range(1,130):
    ii = str(i)
    while len(ii)<3:
        ii = '0'+ii

    fname = 'nuc-utf8/data'+ii+'.utf8.txt'
    gname = 'nuc-docs/data.'+str(int(ii))+'.doc.txt'
    print(fname)
    try:
        lines = open(fname).read().split('###\n')[1].split('\n')
    except:
        continue

    with open(gname,'w') as f:
        who = ''
        for line in lines:
            if line.find('＠')!=-1:
                break

            if line.find('：')==-1:
                line = who +'：'+ line
            who = line.split('：')[0]
            f.write(line.replace('：','#')+'\n')

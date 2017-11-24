gname = 'nuc-users.txt'
open(gname,'w').write('')
for i in range(1,130):
    ii = str(i)
    while len(ii)<3:
        ii = '0'+ii

    fname = 'nuc-utf8/data'+ii+'.utf8.txt'
    try:
        lines = open(fname).read().split('###\n')[0].split('\n')
    except:
        continue

    with open(gname,'a') as f:
        who = ''
        for line in lines:
            if line.find('#')!=-1:
                continue
            if line.find('％ｃｏｍ')!=-1:
                continue
            if line.find('０代')==-1:
                continue
            line = line.replace('＠参加者','')
            who = line.split('：')
            out = '#'.join(who)+'\n'
            f.write(out)

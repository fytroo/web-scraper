import os

for eucJP_file in os.listdir('nuc/'):
    utf8_file = 'nuc-utf8/'+'.utf8.'.join(eucJP_file.split('.'))
    with open(utf8_file,'w') as f:
        try:
            text = open('nuc/'+eucJP_file, encoding='euc-jp').read()
            f.write(text)
        except:
            pass


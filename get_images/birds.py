import subprocess
import itertools
import sys


n = sys.argv[1]
for words in itertools.product(['green', 'white', 'yellow'],
                               ['finch', 'parro']):
    query = ' '.join(words)
    print(query)
    subprocess.run(['python', 'get_images.py', query, '-n', str(n)])

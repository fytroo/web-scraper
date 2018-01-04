import subprocess
import itertools

for words in itertools.product(['green', 'white', 'yellow'],
                               ['finch', 'parro']):
    query = ' '.join(words)
    print(query)
    subprocess.run(['python', 'get_images_yahoo.py', query])

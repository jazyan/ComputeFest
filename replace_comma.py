# python split_data.py ORIG NEW

import csv
import sys
import re

orig = open(sys.argv[1], 'rb')
new = open(sys.argv[2], 'w')

for line in orig:
    line = re.sub(r'(\[\w+\.*\w*); (\w+\.*\w*)', r'\1, \2', line)
    new.write(line)

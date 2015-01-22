# python num2cat.py NUMFILE CATFILE

import csv
import sys

num = open(sys.argv[1], 'r')
cat = open(sys.argv[2], 'w')

# file with mappings
mapread = open('mapping.txt', 'r')

attr = num.readline()
mapping = {}
line = mapread.readline()
while(line != attr):
    line = mapread.readline()

categ = mapread.readline().rstrip('\n').split(';')
numb = mapread.readline().rstrip('\n').split(';')
mapping = {categ[i]:int(numb[i]) for i in range(len(categ))}
print mapping

cat.write(attr)
for n in num:
    for key in mapping:
        if mapping[key] == int(n):
            cat.write(key + '\n')

# python cat2num.py MAPPING ORIG NEW
# mapping.txt will contain the mappings

import csv
import sys
import re

mapping = open(sys.argv[1], 'r')
orig = open(sys.argv[2], 'r')
origreader = csv.DictReader(orig)
new = open(sys.argv[3], 'w')

dictkey = {}
for line in mapping:
    for i in range(len(line)):
        if line[i] == ':':
            key = line[0:i]
            range_to_rep = re.search(r': \d+-\d+', line[i:len(line)])
            if range_to_rep:
                num_find = re.compile('(\d+)')
                range_num = num_find.findall(line[i+2:len(line)])
                if len(range_num) == 2:
                    range_num = map(int, range_num)
                    dictkey[key] = [str(i) for i in range(range_num[0], range_num[1]+1)]
            else:
                dictkey[key] = line[i+2:len(line)].split(',')
                dictkey[key] = [elt.strip().strip('\"') for elt in dictkey[key]]
            break;

spam = []
for row in origreader:
    spam.append(row)

for row in spam:
    for key in dictkey:
        row[key] = dictkey[key].index(row[key])

new.write(','.join(spam[0]) + "\n")
for row in spam:
    new.write(','.join(map(str, row.values())) + "\n")

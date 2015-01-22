#!/usr/bin/env python

# python mapping.py ORIGFILE OUTPUTFILE
# mapping.txt will contain the mappings

import csv
import sys

# file with number output
fwrite = open(sys.argv[2], 'w')

# file with mappings
fwrite2 = open('mapping.txt', 'w')

# file with categories
orig = open(sys.argv[1], 'rb')
spamreader = csv.DictReader(orig)

# file to convert back to cat
f_num2cat = open('out.csv', 'r')
f_num = open('out_cat.csv', 'w')

spam = []
for row in spamreader:
    spam.append(row)

origdict = {key:[] for key in spam[0]}
for i in range(len(spam)):
    for key in origdict:
        origdict[key].append(spam[i][key])

# dictkeys contains the mappings
dictkeys = {}
for key in origdict:
    keyli = list(set(origdict[key]))
    mapping = {keyli[i]:i for i in range(len(keyli))}
    dictkeys[key] = mapping

for key in dictkeys:
    fwrite2.write(key + "\n")
    fwrite2.write(';'.join(dictkeys[key]) + "\n")
    fwrite2.write(';'.join(map(str, dictkeys[key].values())) + "\n")

for row in spam:
    for key in origdict:
        row[key] = dictkeys[key][row[key]]

fwrite.write(','.join(spam[0]) + "\n")
for row in spam:
    fwrite.write(','.join(map(str, row.values())) + "\n")

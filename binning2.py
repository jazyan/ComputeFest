#!/usr/bin/env python

# Usage: ./binning.py TRAIN_FILE TEST_FILE OUT_FILE
# Converts the categories in TRAIN_FILE to the corresponding bins
# and prints the result in OUTFILE

import csv
import sys

bins = {}
train = open(sys.argv[1], 'rb')
test = open(sys.argv[2], 'rb')
fwrite = open(sys.argv[3], 'w')

spamreader = csv.DictReader(train)
spamreader2 = csv.DictReader(test)
spam1 = []
spam2 = []
for row in spamreader:
    spam1.append(row)

for row in spamreader2:
    spam2.append(row)

for j in range(len(spam1)):
    row = spam1[j]
    row2 = spam2[j]

    for key in row:
        bins[row[key]] = row2[key]

for x in range(len(spam1)):
    row = spam1[x]
    for key in row:
        row[key] = bins[row[key]]

fwrite.write(",".join(spam1[0]) + "\n")
for row in spam1:
    fwrite.write(",".join(row.values()) + "\n")

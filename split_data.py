#!/usr/bin/env python

# python split_data.py ORIG TEST TRAINING

import csv
import sys
import random

orig = open(sys.argv[1], 'rb')
test = open(sys.argv[2], 'w')
training = open(sys.argv[3], 'w')

origreader = csv.DictReader(orig)
total = 0
ctr = 0
for row in origreader:
    total += 1
    if total == 1:
        training.write(','.join(row) + "\n")
        test.write(','.join(row) + "\n")
    x = random.randint(1, 100)
    if x == 1:
        ctr += 1
        training.write(','.join(map(str, row.values())) + "\n")
    else:
        test.write(','.join(map(str, row.values())) + "\n")
        continue;

print "% CHOSEN", str(float(ctr)/float(total))

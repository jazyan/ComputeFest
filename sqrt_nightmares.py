#!/usr/bin/env python

# Usage: ./binning.py TRAIN_FILE TEST_FILE OUT_FILE
# Converts the categories in TRAIN_FILE to the corresponding bins
# and prints the result in OUTFILE

from binning import bin
import sys

#dicts = bin(sys.argv[1], sys.argv[2], sys.argv[3])

dicts = bin('CC_test1_clean.csv', 'CC_test1_anon.csv', 'test.csv')

corr = {}
count = 0

for i in range(len(dicts)):
    dict = dicts[i]
    for key in dict:
        for key2 in dict:
            if key != key2:
                tuple = (dict[key], dict[key2])
                tuple2 = (dict[key2], dict[key])
                if tuple in corr.keys():
                    corr[tuple] += 1
                elif tuple2 in corr.keys():
                    corr[tuple2] += 1
                else:
                    corr[tuple] = 1
    count += 1

for key in corr:
    print key, corr[key]
#!/usr/bin/env python

import csv

attributes = ['sex', 'age', 'race', 'marital-status', 'education', 'native-country', 'workclass', 'occupation', 'salary-class']

testdict = dict(zip(attributes, [[] for i in xrange(len(attributes))]))
origdict = dict(zip(attributes, [[] for i in xrange(len(attributes))]))

with open('CC_test1.csv', 'rb') as csvreader:
    with open('CC_test_orig.csv', 'rb') as csvreader2:
        test = csv.DictReader(csvreader, delimiter=';')
        orig = csv.DictReader(csvreader2, delimiter=';')
        for row in test:
            for a in attributes:
                testdict[a].append(row[a])
        for row in orig:
            for a in attributes:
                origdict[a].append(row[a])

for a in attributes:
    print a
    print set(testdict[a]), set(origdict[a])

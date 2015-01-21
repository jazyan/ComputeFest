#!/usr/bin/env python

# Usage:
# ./nearest_neigh.py TARGET_ATTRIBUTE TRAIN_FILE TEST_FILE
# Trains on TRAIN_FILE and outputs TEST_FILE with desired TARGET_ATTRIBUTE
# replaced by nearest neighbor predictions
# TARGET_ATTRIBUTE must be one of: sex, age, race, marital-status, education,
# education, native-country, workclass, occupation, salary-class

import csv, sys
import matplotlib.pyplot as plt

attributes = ['sex', 'age', 'race', 'marital-status', 'education', 'native-country', 'workclass', 'occupation', 'salary-class']

target = sys.argv[1]

train = dict(zip(attributes, [[] for i in xrange(len(attributes))]))
with open(sys.argv[2], 'rb') as csvreader:
    c = csv.DictReader(csvreader, delimiter=';')
    for row in c:
        for a in attributes:
            train[a].append(row[a])
n_train = len(train['sex'])

test = dict(zip(attributes, [[] for i in xrange(len(attributes))]))
with open(sys.argv[3], 'rb') as csvreader:
    c = csv.DictReader(csvreader, delimiter=';')
    for row in c:
        for a in attributes:
            test[a].append(row[a])
n_test = len(test['sex'])


# Discrete distance metric: number of non-target attributes in which i-th test disagrees with j-th train
def ddist(i, j):
    dist = 0
    for a in attributes:
        if a == target:
            continue
        if test[a][i] != train[a][j]:
            dist += 1

    return dist

for i in xrange(n_test):
    min_dist = len(attributes)
    cur_near = 0
    for j in xrange(n_train):
        d = ddist(i, j)
        if d < min_dist:
            cur_near = j
            min_dist = d

    test[target][i] = train[target][cur_near]

print ';'.join(attributes)
for i in xrange(n_test):
    line = []
    for a in attributes:
        line.append(test[a][i])
    print ';'.join(line)


#!/usr/bin/env python

# Usage: import bin and use it as a function

import csv

def bin(train, test, out):
    bins = {}
    fwrite = open(out, 'w')

    with open(train, 'rb') as csvfile:
        with open(test, 'rb') as csvfile2:
            spamreader = csv.DictReader(csvfile, dialect=csv.excel_tab)
            spamreader2 = csv.DictReader(csvfile2, dialect=csv.excel_tab)
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

            for y in range(len(spam1)):
                fwrite.write(",".join(spam1[y].values()) + "\n")
            return spam1

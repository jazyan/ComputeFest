import csv
import sys

fwrite = open(sys.argv[2], 'w')

with open(sys.argv[1], 'rb') as csvfile:
    spamreader = csv.DictReader(csvfile)
    spam = []
    for row in spamreader:
        spam.append(row)

    origdict = {key:[] for key in spam[0]}
    for i in range(len(spam)):
        for key in origdict:
            origdict[key].append(spam[i][key])

dictkeys = {}
for key in origdict:
    keyli = list(set(origdict[key]))
    mapping = {keyli[i]:i for i in range(len(keyli))}
    dictkeys[key] = mapping
    print key
    print dictkeys[key]

for row in spam:
    for key in origdict:
        row[key] = dictkeys[key][row[key]]

fwrite.write(','.join(spam[0]) + "\n")
for row in spam:
    fwrite.write(','.join(map(str, row.values())) + "\n")

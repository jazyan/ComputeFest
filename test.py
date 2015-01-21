#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt

fwrite = open("num_categories.csv", "w")

attributes = ['sex', 'age', 'race', 'marital-status', 'education', 'native-country', 'workclass', 'occupation', 'salary-class']

testdict = dict(zip(attributes, [[] for i in xrange(len(attributes))]))
origdict = dict(zip(attributes, [[] for i in xrange(len(attributes))]))

fwrite.write("sex;age;race;marital-status;education;native-country;workclass;occupation;salary-class\n")

with open('CC_test1.csv', 'rb') as csvreader:
    with open('CC_test_orig.csv', 'rb') as csvreader2:
        test = csv.DictReader(csvreader, delimiter=';')
        orig = csv.DictReader(csvreader2, delimiter=';')

        for row in orig:
            if row['sex'] == "Female":
                row['sex'] = 0
            else:
                row['sex'] = 1

            row['age'] = int(row['age']) - 48
            if row['race'] == 'Amer-Indian-Eskimo':
                row['race'] = 0
            elif row['race'] == 'Asian-Pac-Islander':
                row['race'] = 1
            elif row['race'] == 'White':
                row['race'] = 2
            else:
                row['race'] = 3

            if (row['marital-status'] == 'Married-civ-spouse'):
                row['marital-status'] = 0
            else:
                row['marital-status'] = 1

            if (row['education'] == '9th' or row['education'] == '10th' or row['education'] == '11th' or row['education'] == '12th' or row['education'] == 'HS-grad'):
                row['education'] = 1
            elif (row['education'] == '1st-4th' or row['education'] == '5th-6th' or row['education'] == '7th-8th' or row['education'] == 'Preschool'):
                row['education'] = 0
            else:
                row['education'] = 2

            if (row['native-country'] == 'Canada' or row['native-country'] == 'Dominican-Republic' or row['native-country'] == 'Outlying-US(Guam-USVI-etc)' or row['native-country'] == 'Cuba' or row['native-country'] == 'Guatemala' or row['native-country'] == 'Haiti' or row['native-country'] == 'South' or row['native-country'] == 'Mexico' or row['native-country'] == 'El-Salvador' or row['native-country'] == 'Puerto-Rico' or row['native-country'] == 'United-States' or
                    row['native-country'] == 'Trinadad&Tobago' or row['native-country'] == 'Nicaragua'):
                row['native-country'] = 0
            elif (row['native-country'] == 'Hong' or row['native-country'] == 'Cambodia' or row['native-country'] == 'Laos' or row['native-country'] == 'Thailand' or row['native-country'] == 'China' or row['native-country'] == 'Philippines' or row['native-country'] == 'Vietnam' or row['native-country'] == 'India' or row['native-country'] == 'Japan' or row['native-country'] == 'Taiwan'):
                row['native-country'] = 2
            else:
                row['native-country'] = 1

            if (row['workclass'] == 'State-gov' or row['workclass'] == 'Local-gov' or row['workclass'] == 'Federal-gov'):
                row['workclass'] = 2
            elif (row['workclass'] == 'Without-pay'):
                row['workclass'] = 0
            else:
                row['workclass'] = 1

            if (row['occupation'] == 'Other-service'):
                row['occupation'] = 2
            elif (row['occupation'] == 'Tech-support' or row['occupation'] == 'Machine-op-inspct'):
                row['occupation'] = 1
            else:
                row['occupation'] = 0

            if (row['salary-class'] == '<=50K'):
                row['salary-class'] = 0
            else:
                row['salary-class'] = 1

            fwrite.write(str(row['sex']) + ";" + str(row['age']) + ";" + str(row['race']) + ";" + str(row['marital-status']) + ';' + str(row['education']) + ";" + str(row['native-country']) + ';' + str(row['workclass']) + ';' + str(row['occupation']) + ";" + str(row['salary-class']) + '\n')

            for a in attributes:
                origdict[a].append(row[a])

        for row in test:
            for a in attributes:
                testdict[a].append(row[a])


#!/usr/bin/env python

import csv


sex = []
age = []
race = []
maritalstatus= []
education = []
nativecountry = []
workclass = []
occupation = []
salaryclass = []

i = 0
with open('CC_test1.csv', 'rb') as csvreader:
    with open('CC_test_orig.csv', 'rb') as csvreader2:
        spamreader = csv.DictReader(csvreader, delimiter=';')
        spamreader2 = csv.DictReader(csvreader2, delimiter=';')
        spam1 = []
        spam2 = []
        for row in spamreader:
            spam1.append(row)
            i += 1
            if (i == 800):
                break;
        i = 0
        for row in spamreader2:
            spam2.append(row)
            i += 1
            if (i == 800):
                break;

for j in range(800):
    sex.append(spam1[j]['sex'] + spam2[j]['sex'])
    age.append(spam1[j]['age'] + spam2[j]['age'])
    maritalstatus.append(spam1[j]['marital-status'] + spam2[j]['marital-status'])
    education.append(spam1[j]['education']+spam2[j]['education'])
    nativecountry.append(spam1[j]['native-country'] + spam2[j]['native-country'])
    workclass.append(spam1[j]['workclass'] + spam2[j]['workclass'])
    occupation.append(spam1[j]['occupation'] + spam2[j]['occupation'])
    salaryclass.append(spam1[j]['salary-class'] + spam2[j]['salary-class'])

print set(age)
print set(maritalstatus)
print set(education)
print set(nativecountry)
print set(workclass)
print set(occupation)
print set(salaryclass)

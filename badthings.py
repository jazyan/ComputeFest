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

with open('CC_test_orig.csv', 'rb') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=';')
    for row in spamreader:
        sex.insert(i, row['sex'])
        age.insert(i, row['age'])
        maritalstatus.insert(i, row['marital-status'])
        education.insert(i, row['education'])
        nativecountry.insert(i, row['native-country'])
        workclass.insert(i,row['workclass'])
        occupation.insert(i, row['occupation'])
        salaryclass.insert(i, row['salary-class'])


        i += 1

print set(age)
print set(maritalstatus)
print set(education)
print set(nativecountry)
print set(workclass)
print set(occupation)
print set(salaryclass)

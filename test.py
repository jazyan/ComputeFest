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

sex_o = []
age_o = []
race_o = []
maritalstatus_o = []
education_o = []
nativecountry_o = []
workclass_o = []
occupation_o = []
salaryclass_o = []

with open('CC_test1.csv', 'rb') as csvreader:
    with open('CC_test_orig.csv', 'rb') as csvreader2:
        test = csv.DictReader(csvreader, delimiter=';')
        orig = csv.DictReader(csvreader2, delimiter=';')
        for row in test:
            sex.append(row['sex'])
            age.append(row['age'])
            race.append(row['race'])
            maritalstatus.append(row['marital-status'])
            education.append(row['education'])
            nativecountry.append(row['native-country'])
            workclass.append(row['workclass'])
            occupation.append(row['occupation'])
            salaryclass.append(row['salary-class'])
        for row in orig:
            sex_o.append(row['sex'])
            age_o.append(row['age'])
            race_o.append(row['race'])
            maritalstatus_o.append(row['marital-status'])
            education_o.append(row['education'])
            nativecountry_o.append(row['native-country'])
            workclass_o.append(row['workclass'])
            occupation_o.append(row['occupation'])
            salaryclass_o.append(row['salary-class'])

print "AGE"
print set(age), set(age_o)
print "MARITAL STATUS"
print set(maritalstatus), set(maritalstatus_o)
print "RACE"
print set(race), set(race_o)
print "EDUCATION"
print set(education), set(education_o)
print "NATIVE COUNTRY"
print set(nativecountry), set(nativecountry_o)
print "WORKCLASS"
print set(workclass), set(workclass_o)
print "OCCUPATION"
print set(occupation), set(occupation_o)
print "SALARY CLASS"
print set(salaryclass), set(salaryclass_o)

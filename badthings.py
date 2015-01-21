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
error = 0

with open('CC_test_orig.csv', 'rb') as csvfile:
    with open('CC_test1.csv', 'rb') as csvfile2:
        spamreader = csv.DictReader(csvfile, delimiter=';')
        spamreader2 = csv.DictReader(csvfile2, delimiter=';')
        spam1 = []
        spam2 = []
        for row in spamreader:
            spam1.append(row)
            if i > 800:
                break;
            i += 1
        i = 0

        for row in spamreader2:
            spam2.append(row)
            if i > 800:
                break;
            i += 1

        for j in range(800):
            row = spam1[j]
            row2 = spam2[j]

            if row['age'] != row2['age']:
                print "error! %d \n", error
            sex.insert(j, row['sex'] + " /"  +row2['sex'])
            age.insert(j, row['age'] + " /" + row2['age'])
            maritalstatus.insert(j, row['marital-status']+ " /"  + row2['marital-status'])
            education.insert(j, row['education'] + " " + row2['education'])
            nativecountry.insert(j, row['native-country'] + " /" + row2['native-country'])
            workclass.insert(j,row['workclass'] + " " + row2['workclass'])
            occupation.insert(j, row['occupation'] + " /" + row2['occupation'])
            salaryclass.insert(j, row['salary-class'] + " /" + row2['salary-class'])


print set(age)
print set(maritalstatus)
print set(education)
print set(nativecountry)
print set(workclass)
print set(occupation)
print set(salaryclass)
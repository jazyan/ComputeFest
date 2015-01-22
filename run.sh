#!/bin/bash

echo "Training File: " $1
echo "Test File: " $2
echo "Target Attribute: " $3

echo "Converting to numbers..."
./cat2num.py $1 num_train.csv
cat mapping.txt > mapping_train.txt
./cat2num.py $2 num_test.csv
cat mapping.txt > mapping_test.txt

echo "Running SVM Classifier..."
./svm.py $3 num_train.csv num_test.csv num_out.csv

echo "Converting back to categories..."
./num2cat.py num_out.csv out.csv

echo "All done! Results in out.csv."

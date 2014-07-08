#!/usr/bin/env python3

__author__ = 'ivaylo spasov'


import os
import csv

filename = 'budget.csv'
dataDir = 'data'


def get_file_path(filename):
#   Get the current working directory
    currenDirPath = os.getcwd()
#   Get the full path of the file budget.csv by joining paths
    filepath = os.path.join(currenDirPath, dataDir, filename)
    return filepath


def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cBudget = row[0]
            return cBudget
    f.close()

path = get_file_path(filename)

currentBudget = float(read_csv(path))

if '__name__' == '__main__':
    read_csv(path)
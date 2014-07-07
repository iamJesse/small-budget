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


def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
#       print(reader)
        for row in reader:
            currentBudget = float(row[0])
            return currentBudget


path = get_file_path(filename)

currentBudget = float(read_csv(path))

if __name__ == '__main__':
    get_file_path(filename)
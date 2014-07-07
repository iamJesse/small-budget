#!/usr/bin/env python3

__author__ = 'ivaylo spasov'

import os
import csv
import random
import string

filename = 'budget.csv'
dataDir = 'data'


def get_file_path(filename):
    currenDirPath = os.getcwd()
#   print(currenDirPath)
    file_path = os.path.join(currenDirPath, dataDir, filename)
#   print(file_path)
    return file_path


path = get_file_path(filename)


def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
#       print(reader)
        for row in reader:
            print(row[0])
#           print(float(row[0]))
#           print(type(float(row[0])))


read_csv(path)
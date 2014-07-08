#!/usr/bin/env python3

__author__ = 'ivaylo spasov'


import os
import csv
from getBudget import path

filename = 'budget.csv'
dataDir = 'data'

def write_csv():
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)

    csvfile.close()
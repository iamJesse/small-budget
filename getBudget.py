#!/usr/bin/env python3

__author__ = 'ivaylo'


def getBudget():
    openBudget = open('budget', 'w')
    addToBudget = float(input('enter float: '))
    currentBudget = openBudget.write(str(addToBudget))
    openBudget.close()


getBudget()
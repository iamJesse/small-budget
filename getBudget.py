#!/usr/bin/env python3

__author__ = 'ivaylo'


def getBudget():
    openBudget = open('budget.txt', 'w')
    addToBudget = float(input('enter float: '))
    currentBudget = openBudget.write(str(addToBudget))
    print('Current budget is {0}'.format(addToBudget))
    openBudget.close()


getBudget()
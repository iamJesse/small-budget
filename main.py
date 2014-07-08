#!/usr/bin/env python3

__author__ = 'ivaylo spasov'

import os
import csv
from getBudget import currentBudget, path

def main():
    endProgram = 'no'
    totalBudget = currentBudget
    while endProgram == 'no':
        print('Welcome to the Personal Budget Program')
        print('Menu Selections: ')
        print('1-Add an Expense: ')
        print('2-Add Revenue: ')
        print('3-Check Budget Balance: ')
        print('4-Save progress')
        print('5-Exit without saving')

        choice = int(input('enter your selection: '))
        if choice == 1:
            totalBudget = addExpense(totalBudget)
        elif choice == 2:
            totalBudget = addRevenue(totalBudget)
        elif choice == 3:
            print('Your balance is {0}'.format(totalBudget))
        elif choice == 4:
#           saveBudget(totalBudget)
            print('Thanks for saving your progress')
        elif choice == 5:
            endProgram = 'yes'
            print('Thank you for using "Small budget" program, Goodbye')
        else:
            print('Invalid selection, please try again')



def addExpense(totalBudget):
    expense = float(input('Enter your expense amount: $'))
    timesPerMonth = int(input('How many times per month: '))
    totalExpense = expense * timesPerMonth
    totalBudget = totalBudget - totalExpense
    if totalExpense <= totalBudget:
        print ('The expenses was accepted, your remaining budget is: ${0}'.format(totalBudget))
        return totalBudget
    else:
        print ('The expenses was rejected because the budget exceeded.')
        totalBudget = totalBudget
        return totalBudget


def addRevenue(totalBudget):
    revenue = float(input('Enter new monthly income: $'))
    totalBudget = totalBudget + revenue
    print('your new budget is: ${0}'.format(totalBudget))
    return totalBudget


def saveBudget(totalBudget):
    with open(path, 'w') as f:
        writer = csv.writer(f)
    f.close()

main()
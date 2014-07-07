#!/usr/bin/env python3

__author__ = 'ivaylo spasov'

from getBudget import *


def main():
    endProgram = 'no'
    totalBudget = currentBudget
    while endProgram == 'no':
        print('Welcome to the Personal Budget Program')
        print('Menu Selections: ')
        print('1-Add an Expense: ')
        print('2-Add Revenue: ')
        print('3-Check Budget Balance: ')
        print('4-Exit')

        choice = int(input('enter your selection: '))
        if choice == 1:
            totalBudget = addExpense(totalBudget)
        elif choice == 2:
            totalBudget = addRevenue(totalBudget)
        elif choice == 3:
            print('Your balance is', totalBudget)
        elif choice == 4:
            endProgram = 'yes'
            print('Thank you for using my budget program, Goodbye')
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


def addRevenue(totalBudget):
    print(totalBudget)
    revenue = float(input('Enter new monthly income: $'))
    totalBudget = totalBudget + revenue
    print('your new budget is: ${0}'.format(totalBudget))
    return totalBudget

main()
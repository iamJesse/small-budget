#!/usr/bin/env python3

__author__ = 'ivaylo spasov'


def main():
    endprogram = 'no'
    totalbudget = float(4000)
    while endprogram == 'no':
        print('Welcome to the Personal Budget Program')
        print('Menu Selections: ')
        print('1-Add an Expense: ')
        print('2-Add Revenue: ')
        print('3-Check Budget Balance: ')
        print('4-Exit')

        choice = int(input('enter your selection: '))
        if choice == 1:
            totalbudget = addexpense(totalbudget)
        elif choice == 2:
            totalbudget = addRevenue(totalbudget)
        elif choice == 3:
            print('Your balance is', totalbudget)
        elif choice == 4:
            endprogram = 'yes'
            print('Thank you for using my budget program, Goodbye')
        else:
            print('Invalid selection, please try again')


def addexpense(totalbudget):
    expense = float(input('Enter your expense amount: $'))
    monthly = int(input('How many times per month: '))
    totalexpense = expense * monthly
    totalbudget = totalbudget - totalexpense
    if totalexpense <= totalbudget:
        print ('The expenses was accepted, your remaining budget is: ${0}'.format(totalbudget))
        return totalbudget
    else:
        print ('The expenses was rejected because the budget exceeded.')


def addRevenue(totalbudget):
    print(totalbudget)
    revenue = float(input('Enter new monthly income: $'))
    totalbudget = totalbudget + revenue
    print('your new budget is: ${0}'.format(totalbudget))
    return totalbudget

main()
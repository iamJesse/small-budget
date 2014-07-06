#!/usr/bin/env python3

__author__ = 'ivaylo spasov'

def budget_modifier():
    editBudget = open('budget.txt', 'w')
    primaryBudget = input('Enter your primary budget: ')
    editBudget.write(primaryBudget)
    editBudget.close()

budget_modifier()


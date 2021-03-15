# -*- coding: utf-8 -*-
"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off
a credit card balance within 12 months. By a fixed monthly payment, we mean a single number
which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year,
for example:

Lowest Payment: 180 
Assume that the interest is compounded monthly according to the balance at the end of the month 
(after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using this payment scheme, which is okay. 
A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
@author: epits
"""




balance = 3329
annualInterestRate = 0.2

# Checks if with a given guess the balance of the card at the end of the year will be covered.
def balanceAcc(balance,month,guess):
    if month==12:
        if balance<=0:
            return True
            
        
        return False
            
         
    return balanceAcc((balance-guess) * (1+monthlyInterestRate),month+1,guess)

monthlyInterestRate= annualInterestRate/12

for guess in range(0,balance,10):
    dsa=balanceAcc(balance,0,guess)
    if balanceAcc(balance,0,guess):
        print(str(guess))
        break
    
def balanceAcc(balance,month,guess):


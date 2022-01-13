'''
Full Name: Rahique Mirza
ID: 912715741
Date: 01/13/2022
Filename: L1_Mirza_Rahique_rmm6798.py
Purpose: The purpose of this code is to calculate the balance based on a given interest rate
         with a given number of years, and the frequency at which interest is compounded.
'''

P = 10000
i = .14
n = 12 
t = 10 
F=(P*(1+(i/n))**(n*t))
print(F)

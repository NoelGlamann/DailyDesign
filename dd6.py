#!usr/bin/python3
#Noel Glamann
#10/14/19

""" Daily Design #6
       Generate random number from 1-30.
       Create loop that will print a number until 
       the number generated is 12.
"""

import random as rd

number = rd.randint(1, 31)


while True:
    if number != 12:
        print(number)
        number = rd.randint(1, 31)
    else:
        break
    
#!usr/bin/python3
#Noel Glamann
#30 October 2019

""" 

Daily Design #9
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
(Not sure why we need abs() because it wants negatives to be false)

"""

def near_hundred(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False
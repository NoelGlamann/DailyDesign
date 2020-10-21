#!/usr/bin/python3
#29 October 2019
#Noel Glamann

""" 

Daily Design #8

Given an int n, return the absolute difference between 
n and 21, except return double the absolute difference 
if n is over 21.

"""

def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return abs(21 -n) * 2
    
num = input("Number: ")
num = float(num)

print(diff21(num)) 



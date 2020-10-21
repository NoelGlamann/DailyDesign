#!usr/bin/python3
#Noel Glamann
#11/19/2019

''' 
Daily Design #13
Go to Codingbat, to section Logic-1 and do problem sorta_sum. 
Copy your code into a python file called dd13.py and turn it in to Google Classroom. 
'''

def sorta_sum(a, b):
    c = a +b
    if c in range(10,20):
        return 20
    else: 
        return c
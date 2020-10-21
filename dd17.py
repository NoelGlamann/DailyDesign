#!usr/bin/python3
#Noel Glamann
#December 11, 2019

'''
             Daily Design #17
Create a program that asks for two integers from the user, 
stores them in variables and then tries to divide the first 
one by the second one. If successful, print the result, but 
if not (say by trying to divide by zero) print the error 
message "What a Terrible Fail." instead. save the file as 
dd17.py and turn it in.
'''

int1 = input("First Number: ")
int2 = input("Second Number: ")
answer = 0.0

int1 = int(int1)
int2 = int(int2)

try:
    answer = int1/int2
    print(answer)
except:
    print("What a terrible fail!")
    


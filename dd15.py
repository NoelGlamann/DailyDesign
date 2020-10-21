#!usr/bin/python3
#Noel Glamann
#December 05, 2019

'''
Create a dictionary called phonebook that contains the following key : definition pairs:
James : 555-1234
Courtney : 555-4398
Alvin : 555-9276
Kim :555-7859

then, ask the user for a name. If the name is in the phonebook, print the number,
otherwise, print a message that gives the name and says it wasn't found.
save your program as dd15.py and turn it in.
'''

name = ""
number = ""
phonebook = {"James" : "555-1234", "Courtney" : "555-4398", "Alvin" : "555-9276", "Kim" : "555-7859"}


name = input("What name would you like to find in the Phone Book? ")

if name in phonebook:
    number = phonebook[name]
    print("Their phone number is:", number)
else:
    print("I'm sorry! The name,", name + ", was not found in our Phone Book.")
    
    
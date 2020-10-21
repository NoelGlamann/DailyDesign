#!/usr/bin/python3
#Noel Glamann
#December 10, 2019

'''
daily design #16
'''

my_file = open("design_file.txt", "w")
my_file.write("This is some text.")
my_file.close()

my_file = open("design_file.txt", "r")
the_text = my_file.read()
print(the_text)
my_file.close()
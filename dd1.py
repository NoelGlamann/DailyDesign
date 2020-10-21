#!/usr/bin/python3
#Noel Glamann
#September 4, 2019

''' The purpose of this program is to calculate the area of a triangle.
This is done with numbers input by the user for the base and height. 
The final calculation will then be printed out. '''

#Greeting and Explanation
print("               Area of a Triangle")
print("              --------------------")
print(" ")
print(" ")
print("To calcuate the area of a triangle, two values are needed.")
print("1. Base Length")
print("2. Height")
print("Please input the values below.")
print(" ")
print(" ")

#Input Base Length
B = input("Base: ")
B = float(B)

#Input Height
H = input("Height: ")
H = float(H)

#Calculations
A = (.5)*(B)*(H)

#Final Result
print(" ")
print(" ")
print("The area equals", A)


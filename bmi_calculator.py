# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:52:40 2023

@author: franc
"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float("{:.2f}".format(weight/(height**2)))
print(f"your bmi is {bmi}.")

if bmi < 18.5:
    print("you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print("you have a normal weight.")
elif bmi > 25 and bmi < 30:
    print("you are overweight.")
elif bmi > 30 and bmi < 35:
    print("you are obese.")
elif bmi > 35:
    print("you are clinically obese.")
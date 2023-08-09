# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:28:12 2023

@author: franc
"""
year = int(input("which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"the year {year} is a leap year.")
    elif year % 400 == 0:
        print(f"the year {year} is a leap year.")
else:
    print(f"the year {year} is not a leap year.")
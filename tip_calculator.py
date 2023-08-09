# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
bill_with_tip = percentage/100 * bill + bill
result = "{:.2f}".format(bill_with_tip/number_of_people)
     
print(f"Each person should pay: ${result}")
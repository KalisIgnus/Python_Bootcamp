# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:05:11 2023

@author: franc
"""

name_1 = input("What is your name? \n")
name_2 = input("What is their name? \n")

lname_1 = name_1.lower()
lname_2 = name_2.lower()

combined_name = name_1.lower() + name_2.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
    
love = l + o + v + e

total_score = int(str(true) + str(love))
  
if total_score > 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.") 
    
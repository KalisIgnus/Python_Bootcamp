# -*- coding: utf-8 -*-
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. "))

com_choice = int(random.randint(0,2))

print(f"You picked {user_choice}. The computer picked {com_choice}.")

if user_choice == com_choice:
    print("It's a draw.")
if user_choice == 0 and com_choice == 2:
    print("You win.")
if user_choice == 0 and com_choice == 1:
    print("The computer wins.")
if user_choice == 1 and com_choice == 2:
    print("You win.")    
if user_choice == 1 and com_choice == 0:
    print("The computer wins.")   
if user_choice == 2 and com_choice == 1:
    print("You win.")    
if user_choice == 2 and com_choice == 0:
    print("The computer wins.")
if user_choice == 2 and com_choice == 1:
    print("You win.")    
       
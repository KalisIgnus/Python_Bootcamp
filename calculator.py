# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:48:56 2023

@author: franc
"""
def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    number_1 = float(input("What's the first number? "))
    
    should_continue = True
    
    while should_continue: 
        for symbol in operations:
            print(symbol)
            
        operation = input("Pick an operation from the list above: ")
        number_2 = float(input("What's the next number? "))
    
        if operation == "+":
            answer = addition(number_1, number_2)
        elif operation == "-":
            answer = subtraction(number_1, number_2)
        elif operation == "*":
            answer = multiplication(number_1, number_2)
        elif operation == "/":
            answer = division(number_1, number_2)
        print(f"{number_1} {operation} {number_2} = {answer}")
        
        question = input(f"Type 'y' to continue calculating with {answer}, 's' to start a new calculation or 'n' to quit. ") 
        if question == 'y':
            number_1 = answer
        elif question == 's':
            should_continue = False
            calculator()
        elif question == 'n':
            should_continue = False
            
calculator()

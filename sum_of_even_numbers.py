# -*- coding: utf-8 -*-

total = 0
#first solution
#for number in range(2,101,2):
#    total += number

#second solution
for number in range(1,101):
    if number % 2 == 0:
        total += number
        
print(total)
    
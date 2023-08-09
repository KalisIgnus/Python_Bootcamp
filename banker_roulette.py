# -*- coding: utf-8 -*-

import random

names_string = input("Give me everybody's name, separated by a comma. ")
names = names_string.split(", ")

in_name = random.randint(0,len(names))
name = names[in_name]

print(f"{name} is going to buy the meal today!")
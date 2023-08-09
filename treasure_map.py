# -*- coding: utf-8 -*-
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontalc = int(position[0])
verticalc = int(position[1])

map[verticalc - 1][horizontalc - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

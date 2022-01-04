
import random
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure, row,column. e.g, 31? ")

row_value = int(position[0])
column_value = int(position[1])

map[row_value-1][column_value-1] = "🧈"

print(f"{row1}\n{row2}\n{row3}")
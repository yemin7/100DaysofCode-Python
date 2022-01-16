#import variables
#from turtle import Turtle, Screen
#
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color('red', 'green')
#timmy.forward(100)
#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
#table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
#table.add_column("Type", ['Electric', 'Water', 'Fire'])


table.field_names = ["Pokemon Name", "Type"]
#table.add_row(["Pikachu", "Electric"])
#table.add_row(["Squirtle", "Water"])
#table.add_row(["Charmander", "Fire"])

table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])

table.align = 'l'
table.align['Pokemon Name', 'Type'] = 'c' 

print(table)
from sys import argv
import string
from ship_class import *

def pvt(the_var):
    print(the_var)
    print(type(the_var))

# check if the user has input an argument in cmd for grid dimension if not, ask for input
if len(argv) == 1:
    grid_dimension = int(input('Input size of board [number must be less than 26]: '))
else:
    grid_dimension = int(argv[1])

if grid_dimension > 26:
    grid_dimension = int(input('Why did you input a number > 26. Input size of board: '))

x_axis = list(string.ascii_uppercase)[:grid_dimension]
y_axis = list(range(grid_dimension + 1))[1:]


grid = [[False for i in range(grid_dimension)] for i in range(grid_dimension)]

def print_grid_as_grid():
    print('   ', ' '.join(x_axis),'\n') #prints(x_axis index [A-Z])
    fg_format = '\033[3{fg_index}mo\033[0m'
    for row_index, row in enumerate(grid):
        print(f"{str(row_index+1):2}  {' '.join([fg_format.format(fg_index = 1 if cell else 4) for cell in row])}") #prints(x_axis index [A-Z])

ship_list = []
def create_and_add_ship(*the_coordinates):
    a_ship = SmallShip(*the_coordinates) if len(the_coordinates) == 2 else BigShip(*the_coordinates) 
    ship_list.append(a_ship)
    # truth_list.append(True)

# Placing ships on grid
create_and_add_ship(('A', 1), ('A', 2))
create_and_add_ship(('A', 3), ('A', 4), ('A', 5), ('A', 6))


# grid[4][-1] = True

# while not len(ship_list) == sum([ship.determine_if_ship_destroyed for ship in ship_list]):
while not all([ship.determine_if_ship_destroyed() for ship in ship_list]):
    print_grid_as_grid()
    guess = input('Guess and Enter a coordinate as 2 values separated by a space: ')
    x, y = guess.split()
    # FOR HOMEWORKKKKKKKKKKKK - get index once - not each time - factor out - get index before entering the loop
    x_int = x_axis.index(x)

    # FOR HOMEWORKKKKKKKKKKKK - write the below for loop in one line of code using a list comprehension 
    # for ship in ship_list: 
    #     if ship.determine_if_hit_or_not((x, int(y))):
    #         grid[x_int][int(y)] = True
    grid[x_int][int(y)] = len([True for ship in ship_list if ship.determine_if_hit_or_not((x, int(y)))]) == 1 

print_grid_as_grid()



# while ship_list.determine_if_ship_destroyed():
# show grid
# ask for a move
# repeat steps 1 and 2 inside of while loop   
# until game is finished - i.e. all ships destroyed


# one_ship = SmallShip(('A', 1), ('A', 2))
# two_ship = SmallShip(('A', 3), ('A', 4))
# ship_list = [one_ship, two_ship]

# print(one_ship.determine_if_hit_or_not(('A', 1)))
# print(one_ship.determine_if_hit_or_not(('A', 2)))
# print(one_ship.determine_if_ship_destroyed())

# print_grid_as_grid()



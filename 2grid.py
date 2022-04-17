#!usr/bin/env python

import string

# battleship equal 8x8
y_axis = list(string.ascii_uppercase)[:8]
def pvt(the_var):
    print(the_var)
    print(type(the_var))

def create_one_based_index_coordinate_list(a_number):
    return list(range(a_number + 1))[1:]

grid_width = int(input('How wide do you want the grid? '))
grid_height = int(input('How high do you want the grid? '))
coordinates_width = create_one_based_index_coordinate_list(grid_width)
coordinates_height = create_one_based_index_coordinate_list(grid_height)

grid = []
for coordinate_w in coordinates_width:
    for coordinate_h in coordinates_height:
        grid.append(str(coordinate_w) + '-' + str(coordinate_h) + '-')
        # grid.append([coordinate_w, coordinate_h])

print(grid)
print(len(grid))

exit()
print(coordinates_height)

def create_one_based_index_coordinate_list(a_number):
    return list(range(a_number + 1))[1:]

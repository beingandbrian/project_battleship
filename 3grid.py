from sys import argv
import string

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

# # l = ['   '.join(x_axis) for i in x_axis]
# print(['   '+i for i in x_axis])
# print('   '.join(x_axis))
# exit()
y_axis = list(range(grid_dimension + 1))[1:]

numbers_to_letters_dict = dict(zip(y_axis, x_axis))

grid = [[False for i in range(grid_dimension)] for i in range(grid_dimension)]

def print_grid_as_grid():
    print(x_axis)
    fg_format = '\033[3{fg_index}mo\033[0m'
    for row_index, row,  in enumerate(grid):
        # print(row_index+1, row)
        print(' '.join([fg_format.format(fg_index = 1 if cell else 4) for cell in row]))

grid[1][-1] = True
print_grid_as_grid()


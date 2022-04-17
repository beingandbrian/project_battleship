guess = input('Guess and Enter a coordinate as 2 values separated by a space: ')

'string_split'.split('_')

# from sys import argv
# import string

# def pvt(the_var):
#     print(the_var)
#     print(type(the_var))

# def check_grid_dimension(a_dimension):
#     a_dimension = int(input('Input number < 26 ')) if a_dimension > 26 else a_dimension
#     return a_dimension 



# # check if the user has input an argument in cmd for grid dimension if not, ask for input
# if len(argv) == 1:
#     grid_dimension = int(input('Input size of board [number must be less than 26]: '))
#     if grid_dimension > 26:
#         grid_dimension = int(input('Why did you input a number > 26. Input size of board: '))
# else:
#     grid_dimension = int(argv[1])
#     if grid_dimension > 26:
#         grid_dimension = int(input('Why did you input a number > 26. Input size of board: '))
# letters = list(string.ascii_uppercase)[:grid_dimension]
# print(letters, len(letters))
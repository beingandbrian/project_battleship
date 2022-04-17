#!usr/bin/env python

# one possibility:
# https://betterprogramming.pub/making-grids-in-python-7cf62c95f413


# source for below: https://stackoverflow.com/questions/41910947/how-do-i-make-a-grid-in-python
# width by height (width x height)
width = int(input('How wide do you want the grid? '))
height = int(input('How high do you want the grid? '))

row = []
grid = []
placeholder = '++'

for _ in range(width):
    row.append(placeholder)

for _ in range(height):
    grid.append(list(row))

# print(row)
print(grid)

grid[0][0] = "occupied"

print(grid)


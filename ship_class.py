
class Ship:
# attributes:
# takes up space - will have a few coordinates on the grid - Lshape 3 x 1, 4 in a line, 2 in a line

    def __init__(self, *ship_coordinates):
        self.coordinates = ship_coordinates
        # should be the same length of ship
        self.hit_list = []
    
    def __str__(self):
        return f'The ship coordinates = {self.coordinates}'

    def determine_if_hit_or_not(self, the_coordinate):
        # its_a_hit = False
        # for coordinate in self.coordinates:
        #     if coordinate == the_coordinate:
        #         its_a_hit = True
        
        # return its_a_hit
        # return the_coordinate in self.coordinates

        if the_coordinate in self.coordinates:
            self.hit_list.append(the_coordinate)
            return True
        else:
            return False
    
    def determine_if_ship_destroyed(self):
        return len(self.coordinates) == len(self.hit_list)

class BigShip(Ship):

    def __init__(self, point1, point2, point3, point4):
        super(BigShip, self).__init__(point1, point2, point3, point4)

class SmallShip(Ship):

    def __init__(self, point1, point2):
        super(SmallShip, self).__init__(point1, point2)
    

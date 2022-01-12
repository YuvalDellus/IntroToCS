############################################################
# FILE : ex8.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION :  ships game, ship class
############################################################


############################################################
# Helper class
############################################################
import ship_helper as sh
from copy import deepcopy

class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """
    UP = "up"  # Choose your own value
    DOWN = "down"  # Choose your own value
    LEFT = "left"  # Choose your own value
    RIGHT = "right"  # Choose your own value

    NOT_MOVING = "not moving"  # Choose your own value

    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

############################################################
# Class definition
############################################################


class Ship:
    """
    A class representing a ship in Battleship game.
    A ship is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A ship sails on its vertical\horizontal axis back and
    forth until reaching the board's boarders and then changes its direction to
    the opposite (left <--> right, up <--> down).
    If a ship is hit in one of its coordinates, it ceases its movement in all
    future turns.
    A ship that had all her coordinates hit is considered terminated.
    """

    def __init__(self, pos, length, direction, board_size):
        """
        A constructor for a Ship object
        :param pos: A tuple representing The ship's head's (x, y) position
        :param length: Ship's length
        :param direction: Initial direction in which the ship is sailing
        :param board_size: Board size in which the ship is sailing
        """
        self.__pos = pos
        self.__length = length
        self.__direction = direction
        self.__board_size = board_size
        self.__hits = list()  # will contain the places the ship was hit
        self.__ship_place = self.coordinates()

    def __repr__(self):
        """
        Return a string representation of the ship.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)).
        The tuple's content should be (in the exact following order):
            1. A list of all the ship's coordinates.
            2. A list of all the ship's hit coordinates.
            3. Last sailing direction.
            4. The size of the board in which the ship is located.
        """
        ship_status = list()
        self.coordinates()  # updates the ship's coordinates into ship_place

        ship_status.append(self.__ship_place)  # ship's coordinates
        ship_status.append(self.__hits)  # ship's hit coordinates
        ship_status.append(sh.direction_repr_str(Direction, self.__direction))
        ship_status.append(self.__board_size)

        return str(tuple(ship_status))

    def move(self):
        """
        Make the ship move one board unit.
        Movement is in the current sailing direction, unless such movement would
        take the ship outside of the board, in which case the ship switches
        direction and sails one board unit in the new direction.
        :return: A direction object representing the current movement direction.
        """
        if not Ship.damaged_cells(self):
            y = self.__pos[1]
            x = self.__pos[0]
            last_y_cell = y + self.__length
            last_x_cell = x + self.__length
            boarder = self.__board_size

            if self.__direction == Direction.UP:
                if 0 < y:  # first cell in boarders
                    self.__pos = (x, y - 1)  # go up
                    return Direction.UP

                else:  # first cell out of borders
                    self.__pos = (x, y + 1)  # go down
                    self.__direction = Direction.DOWN
                    return Direction.DOWN

            elif self.__direction == Direction.DOWN:
                if last_y_cell < boarder:  # last cell in boarders
                    self.__pos = (x, y + 1)  # go down
                    return Direction.DOWN

                else:  # last cell out of boarders
                    self.__pos = (x, y - 1)  # go up
                    self.__direction = Direction.UP
                    return Direction.UP

            if self.__direction == Direction.LEFT:
                if 0 < x:  # first cell in boarders
                    self.__pos = (x - 1, y)  # go left
                    return Direction.LEFT

                else:  # first cell out of boarders
                    self.__pos = (x + 1, y)  # go right
                    self.__direction = Direction.RIGHT
                    return Direction.RIGHT

            elif self.__direction == Direction.RIGHT:
                if last_x_cell < boarder:  # last cell in boarders
                    self.__pos = (x + 1, y)  # go right
                    return Direction.RIGHT

                else:  # last cell out of boarders
                    self.__pos = (x - 1, y)  # go left
                    self.__direction = Direction.LEFT
                    return Direction.LEFT

        return Direction.NOT_MOVING

    def hit(self, pos):
        """
        Inform the ship that a bomb hit a specific coordinate. The ship updates
         its state accordingly.
        If one of the ship's body's coordinate is hit, the ship does not move
         in future turns. If all ship's body's coordinate are hit, the ship is
         terminated and removed from the board.
        :param pos: A tuple representing the (x, y) position of the hit.
        :return: True if the bomb generated a new hit in the ship, False
         otherwise.
        """
        if pos in self.coordinates():
            hit = pos[:]
            if hit not in self.__hits:
                self.__hits.append(hit)
                self.__direction = Direction.NOT_MOVING
                return True
        return False

    def terminated(self):
        """
        :return: True if all ship's coordinates were hit in previous turns, False
        otherwise.
        """
        if len(self.__hits) == self.__length:  # all coordinates of the ship was hit
            return True
        return False

    def __contains__(self, pos):
        """
        Check whether the ship is found in a specific coordinate.
        :param pos: A tuple representing the coordinate for check.
        :return: True if one of the ship's coordinates is found in the given
        (x, y) coordinate, False otherwise.
        """

        return pos in self.coordinates()

    def coordinates(self):
        """
        Return ship's current coordinates on board.
        :return: A list of (x, y) tuples representing the ship's current
        occupying coordinates.
        """
        ship_place = list()

        if self.__direction in Direction.VERTICAL:
            for y in range(self.__length):
                ship_place.append((self.__pos[0], self.__pos[1] + y))

        elif self.__direction in Direction.HORIZONTAL:
            for x in range(self.__length):
                ship_place.append((self.__pos[0] + x, self.__pos[1]))

        else:  # ship not moving, return itself place
            return self.__ship_place

        self.__ship_place = ship_place

        return ship_place

    def damaged_cells(self):
        """
        Return the ship's hit positions.
        :return: A list of tuples representing the (x, y) coordinates of the
         ship which were hit in past turns (If there are no hit coordinates,
         return an empty list). There is no importance to the order of the
         values in the returned list.
        """
        damaged_cells = deepcopy(list(self.__hits))
        #  self.__hits updates and generated in "hit" function

        return damaged_cells

    def direction(self):
        """
        Return the ship's current sailing direction.
        :return: One of the constants of Direction class :
         [UP, DOWN, LEFT, RIGHT] according to current sailing direction or
         NOT_MOVING if the ship is hit and not moving.
        """
        return self.__direction

    def cell_status(self, pos):
        """
        Return the status of the given coordinate (hit\not hit) in current ship.
        :param pos: A tuple representing the coordinate to query.
        :return:
            if the given coordinate is not hit : False
            if the given coordinate is hit : True
            if the coordinate is not part of the ship's body : None 
        """
        if pos in self.__hits:  # if the cell was hit
            return True

        elif pos not in self.__hits and pos in self.coordinates():
            # if the cell both belong to the ship and wasn't hit
            return False

        return None

    def get_hits(self):
        """
        API function
        :return: the damaged cells of a ship
        """
        return self.__hits

    def get_place(self):
        """
        API function
        :return: the place coordinates of the shp
        """
        return self.__ship_place

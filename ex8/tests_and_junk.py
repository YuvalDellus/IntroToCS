# def move(self):
#     """
#     Make the ship move one board unit.
#     Movement is in the current sailing direction, unless such movement would
#     take the ship outside of the board, in which case the ship switches
#     direction and sails one board unit in the new direction.
#     :return: A direction object representing the current movement direction.
#     """
#     if not Ship.damaged_cells(self):
#         new_location = self.__pos[:]
#         if self.__direction == Direction.VERTICAL:
#             if Ship.direction(self) == Direction.UP:
#                 new_location[0] += 1
#                 if 0 < new_location[0] + self.__length < self.__board_size:
#                     self.__pos = new_location
#                     return Direction.UP
#
#                 else:  # went out of the board, change direction
#                     new_location[0] -= 2
#                     self.__pos = new_location
#                     return Direction.DOWN
#
#             else:  # the direction is vertical but down
#                 new_location[0] -= 1
#                 if 0 < new_location[0] - self.__length < self.__board_size:
#                     self.__pos = new_location
#                     return Direction.DOWN
#
#                 else:  # went out of the board, change direction
#                     new_location[0] += 2
#                     self.__pos = new_location
#                     return Direction.UP
#
#         else:  # the direction is horizontal
#             if Ship.direction(self) == Direction.RIGHT:
#                 new_location[1] += 1
#                 if 0 < new_location[1] + self.__length < self.__board_size:
#                     self.__pos = new_location
#                     return Direction.RIGHT
#
#                 else:  # went out of the board, change direction
#                     new_location[1] -= 2
#                     self.__pos = new_location
#                     return Direction.LEFT
#
#             else:  # the direction is horizontal but left
#                 new_location[1] -= 1
#                 if 0 < new_location[1] - self.__length < self.__board_size:
#                     self.__pos = new_location
#                     return Direction.LEFT
#
#                 else:  # went out of the board, change direction
#                     new_location[1] += 2
#                     self.__pos = new_location
#                     return Direction.RIGHT
#
#     return Direction.NOT_MOVING


# t = (0,1)
# places = list()
#
# for x in range(3):
#     places.append((t[0],t[1]+x))
#
# print(places)
#
# print(str(t))
# temp_bombs = {}
# bombs = {(0,1): 3, (2,0): 5, (3,5): 1, (0,3): 2, (0,3): 3}
# print(bombs)
# for bomb in bombs:
#     bombs[bomb] -= 1
#     if bombs[bomb] != 0:
#         print(bomb)
#         temp_bombs[bomb] = bombs[bomb]
# bombs = temp_bombs
# temp_bombs = {}
# print(str(tuple(bombs)))


# def move(self):
#     """
#     Make the ship move one board unit.
#     Movement is in the current sailing direction, unless such movement would
#     take the ship outside of the board, in which case the ship switches
#     direction and sails one board unit in the new direction.
#     :return: A direction object representing the current movement direction.
#     """
#     if not Ship.damaged_cells(self):
#         new_location = list(self.__pos[:])
#         direction = self.__direction
#         if direction == Direction.UP:
#             new_location[1] += 1
#         elif direction == Direction.DOWN:
#             new_location[1] -= 1
#         elif direction == Direction.RIGHT:
#             new_location[0] += 1
#         elif direction == Direction.LEFT:
#             new_location[0] -= 1
#         print("direction from move:", self.__direction)
#         return Ship.help_move(self, direction, new_location)
#
#     return Direction.NOT_MOVING
#
#
# def help_move(self, direction, location):
#     """
#     checks if the ship went out of the board and if so turn it around and
#     updates the location
#     """
#     if direction == Direction.DOWN:
#         axis = 1
#         opp_direction = Direction.UP
#     elif direction == Direction.UP:
#         axis = 1
#         opp_direction = Direction.DOWN
#     elif direction == Direction.RIGHT:
#         axis = 0
#         opp_direction = Direction.LEFT
#     elif direction == Direction.LEFT:
#         axis = 0
#         opp_direction = Direction.RIGHT
#     # print("direct from help:", direction)
#     if (0 <= location[axis] + self.__length - 1 < self.__board_size) and \
#             (0 <= location[axis] <= self.__board_size - 1):  # both ends of the
#         # ship are in the board game
#         print("ship_begin:", location, "ship_end:",
#               (1, location[axis] + self.__length - 1))
#         # print("board size:", self.__board_size)
#         self.__pos = tuple(location)[:]  # update new position
#         self.__direction = direction[:]
#         return direction
#
#     else:  # ship is out of the board
#         location[axis] += 2 * (self.__pos[axis] - location[axis])  # will
#         self.__pos = tuple(location)[:]
#         self.__direction = opp_direction[:]
#         print("ship_begin:", location, "ship_end:",
#               (1, location[axis] + self.__length - 1), "turned!")
#         # print("board size:", self.__board_size)
#         # print("direction from hel_move:", self.__direction)
#         # print("ghjghjbjhbhj")
#         return opp_direction


list1 = list()
r = [4,4,4,4]
t= set((8,5))
a = [1,2,3,4,5]

list1.append(r)
list1.append(t)
print(list1)


def move(self):
    """
    Make the ship move one board unit.
    Movement is in the current sailing direction, unless such movement would
    take the ship outside of the board, in which case the ship switches
    direction and sails one board unit in the new direction.
    :return: A direction object representing the current movement direction.
    """
    if not Ship.damaged_cells(self):  # while ship wasn't hit
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
            if x < 0:  # first cell in boarders
                self.__pos = (x - 1, y)  # go left
                return Direction.LEFT

            else:
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

    return Direction.NOT_MOVING  # while ship wasn't hit


    # game.play()
    # game = Game(5, [ship.Ship((1, 1), 1, "left", 5), ship.Ship((1,3), 3, "right", 5)])
    # game.play()
    # game = Game(5, [ship.Ship((0, 2), 3, "down", 5)])
    # game = Game(5, [ship.Ship((1, 0), 3, "down", 5),ship.Ship((3, 1), 2, "down", 5)])
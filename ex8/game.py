############################################################
# FILE : ex8.py
# WRITER : Yuval Dellus , yuval_dellus, 305211880
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION :  ships game, game class
############################################################


############################################################
# Imports
############################################################
import game_helper as gh
from copy import deepcopy
############################################################
# Class definition
############################################################

TURNS_TO_EXPLODE = 4

class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board.
        :param ships: A list of ships (of type Ship) that participate in the
            game.
        :return: A new Game object.
        """
        self.__board_size = board_size
        self.__ships = ships
        self.__bombs = dict()  # here the game will keep track on the bombs

    def __play_one_round(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits and
             terminated ships)
        :return:
            (some constant you may want implement which represents) Game status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """
        new_bomb = gh.get_target(self.__board_size)
        self.__bombs[new_bomb] = TURNS_TO_EXPLODE  # add new bomb to the game
        self.ships_update()  # moves all the ships
        self.bombs_update()  # checks all bombs status
        hit_ships_list = self.hit_ships_list()  # all damaged cells of ships
        hit_list, hit_counter = self.hit_list()  # list of all the coordinates
        # that was hit in the last turn, number of hits
        unhit_ships_list = self.unhit_ships_list()  # all the unhit coordinates
        print(gh.board_to_string(self.__board_size, hit_list, self.__bombs, hit_ships_list, unhit_ships_list))
        self.remove_bombs(hit_list)  # all the bombs that need to be removed
        ships_terminated_count = self.remove_terminated_ships()
        gh.report_turn(hit_counter, ships_terminated_count)

    def hit_list(self):
        """
        checks for all the ships if any of the bomb hit it, if so, will update
        the ship status, add the relevant coordinate to the hits of the turn
         and count it
        :return: the coordinate that was hit, how many hits
        """
        hit_list = list()
        hit_counter = 0
        for ship in self.__ships:
            for bomb in self.__bombs:
                if ship.hit(bomb):  # if was hit returns True and updates ship
                    hit_list.append(bomb)  # save coordinate of detonated bomb
                    hit_counter += 1  # count the hit

        return hit_list, hit_counter

    def bombs_update(self):
        """
        update all the bombs that a turn was passed, if the bomb is still
        relevant will keep  it.
        :return:
        """
        temp_bombs = {}
        for bomb in self.__bombs:
            self.__bombs[bomb] -= 1  # updates bomb
            if self.__bombs[bomb] != 0:  # if bomb still relevant
                temp_bombs[bomb] = self.__bombs[bomb]

        self.__bombs = temp_bombs

    def remove_bombs(self, hit_list):
        """
        removes any bomb that hit a ship.
        :param hit_list: the coordinates that was hit in the past turn
        :return:
        """
        temp_bombs = deepcopy(self.__bombs)

        for bomb in self.__bombs:
            for ship in self.__ships:
                if bomb in hit_list:  # if the bomb explode in the last turn
                    if bomb in temp_bombs:
                        del temp_bombs[bomb]

        self.__bombs = temp_bombs

    def ships_update(self):
        """
        moves all the ships in the game
        :return:
        """
        for ship in self.__ships:
            ship.move()

    def hit_ships_list(self):
        """
        collete all the coordinates that was hit anytime
        :return: list with all the coordinates
        """
        ships_hit_list = list()

        for ship in self.__ships:
            ships_hit_list += ship.get_hits()

        return ships_hit_list

    def unhit_ships_list(self):
        """
        collect all the coordinates of ships that wasn't hit at all
        :return:  list of coordinates
        """
        unhit_list = list()

        for ship in self.__ships:
            hit_list = ship.get_hits()
            for coordinate in ship.get_place():
                if coordinate not in hit_list:  # the coordinate wasn't hit
                    unhit_list.append(coordinate)
        return unhit_list

    def remove_terminated_ships(self):
        """
        removes any ship that was terminated and count those which does
        :return: number of ships which was terminated
        """
        temp_ships_list = list()

        for ship in self.__ships:
            if not ship.terminated():
                temp_ships_list.append(ship)
        ships_terminated_count = len(self.__ships) - len(temp_ships_list)

        self.__ships = temp_ships_list

        return ships_terminated_count

    def __repr__(self):
        """
        Return a string representation of the board's game.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)). The tuple should contain (maintain
        the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board, mapping their
                coordinates to the number of remaining turns:
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """
        repr_status = (self.__board_size, self.__bombs, self.__ships)
        return str(repr_status)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        gh.report_legend()
        print(gh.board_to_string(self.__board_size, [], self.__bombs, [], self.unhit_ships_list()))
        while len(self.__ships):  # len 0 is False, no more ships
            self.__play_one_round()
        gh.report_gameover()

############################################################
# An example usage of the game
############################################################
import ship
if __name__=="__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()

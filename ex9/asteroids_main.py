from screen import Screen
import sys
from random import randint
import asteroid
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import math

COLLISION_MSG = 'Your ship crushed with an asteroid!'
GAMEOVER_MSG = "You're Dead!!"
WINNING_MSG = 'You won !!'
DEFAULT_ASTEROIDS_NUM = 5
LIMIT = 15
SIZE_1 = 1
SIZE_2 = 2
SIZE_3 = 3
SCORE_3 = 20
SCORE_2 = 50
SCORE_1 = 100



class GameRunner:

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.__ship = self.start_ship()
        self.__asteroids = []
        self.start_asteroids(asteroids_amnt)
        self.__torpedos_list = []
        self.__value = 0


    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

    def move_object(self, obj):
        if type(obj) is Ship:
            location, speed, heading = Ship.get_ship_info(obj)
        elif type(obj) is Torpedo:
            location, speed, heading = Torpedo.get_torpedo_info(obj)
        else:
            location, speed = asteroid.Asteroid.get_asteroid_info(obj)

        x, y = location
        x_speed, y_speed = speed
        x_delta = Screen.SCREEN_MAX_X - Screen.SCREEN_MIN_X
        y_delta = Screen.SCREEN_MAX_Y - Screen.SCREEN_MIN_Y

        new_x = (x_speed + x - Screen.SCREEN_MIN_X) % x_delta + Screen.SCREEN_MIN_X
        new_y = (y_speed + y - Screen.SCREEN_MIN_Y) % y_delta + Screen.SCREEN_MIN_Y
        obj.move_forward(new_x, new_y)

    def turn_ship(self):
        if self._screen.is_left_pressed():
            self.__ship.move_ship_left()
            # print(self.__ship)
        elif self._screen.is_right_pressed():
            Ship.move_ship_right(self.__ship)
            # print(self.__ship)
        if self._screen.is_up_pressed():
            Ship.ex_ship(self.__ship)
            # print(self.__ship)

    def start_asteroids(self, amount):
        for num in range(amount):
            ast = Asteroid.create_asteroid(self)
            while ast.get_asteroid_info()[0] == self.__ship.get_ship_info()[0]:
                ast = Asteroid.create_asteroid(self)
            self.__asteroids.append(ast)
            self._screen.register_asteroid(ast, 3)

    def _game_loop(self):
        '''
        Your code goes here!
        '''
        self.turn_ship()
        self.move_object(self.__ship)
        self._screen.draw_ship(self.__ship.get_ship_info()[0][0], self.__ship.get_ship_info()[0][1], self.__ship.get_ship_info()[2])
        self.mange_asteroids()
        self.generate_torpedo()
        self.manage_torpedoes()
        if not self.__asteroids:
            title = "You Won!"
            self._screen.show_message(title,WINNING_MSG)
            self._screen.end_game()
            sys.exit()

    def start_ship(self):
        x = randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y = randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)

        self._screen.draw_ship(x, y, 0)
        return Ship(x,0,y,0)

    def is_dead(self, ast, ship):
        """function that removes life from a ship while crushing an asteroid"""
        if ast.has_intersection(ship):
            # self.__asteroids.remove(ast)
            # self._screen.unregister_asteroid(ast)
            life = ship.ship_life()
            if life > 0:
                self._screen.remove_life()
                title = 'collision'
                self._screen.show_message(title, COLLISION_MSG)
            if life == 0:
                self._screen.remove_life()
                title = 'Game Over'
                self._screen.show_message(title, GAMEOVER_MSG)
                self._screen.end_game()
                sys.exit()

    def remove_ast(self, ast, ship):
        """function that removes an asteroid after the collision with the ship"""
        if ast.has_intersection(ship):
            self.__asteroids.remove(ast)
            self._screen.unregister_asteroid(ast)

    def mange_asteroids(self):
        for ast in self.__asteroids:
            # print(ast)
            # print(type(ast))
            self.move_object(ast)
            self._screen.draw_asteroid(ast,ast.get_asteroid_info()[0][0],ast.get_asteroid_info()[0][1])
            self.is_dead(ast, self.__ship)
            self.remove_ast(ast, self.__ship)

    def generate_torpedo(self):
        if self._screen.is_space_pressed():
            if len(self.__torpedos_list) < LIMIT:
                torpedo = Torpedo(self.__ship.get_ship_info())
                self.__torpedos_list.append(torpedo)
                self._screen.register_torpedo(torpedo)
                cord, speed, heading = torpedo.get_torpedo_info()
                x, y = cord
                self._screen.draw_torpedo(torpedo, x, y, heading)
        return

    def manage_torpedoes(self):
        if self.__torpedos_list:
            for torpedo in self.__torpedos_list:
                cord, speed, heading = torpedo.get_torpedo_info()
                x, y = cord
                self.move_object(torpedo)
                self._screen.draw_torpedo(torpedo, x, y, heading)
                self.points_manager(torpedo)
                self.torpedo_time_out(torpedo)
                for ast in self.__asteroids:
                    if ast.has_intersection(torpedo):
                        self.__asteroids.remove(ast)
                        self._screen.unregister_asteroid(ast)
                        self._screen.unregister_torpedo(torpedo)
                        self.__torpedos_list.remove(torpedo)
                        ast_info = ast.get_asteroid_info()
                        size = ast.get_size()
                        torpedo_info = torpedo.get_torpedo_info()[1]
                        if size > 1:
                            self.split_asteroid(ast_info, torpedo_info, size - 1)
                        break

    def split_asteroid(self, ast_info, torpedo_info, size):
        cord, speed = ast_info
        x, y = cord
        x_speed, y_speed = speed
        torpedo_x_speed, torpedo_y_speed = torpedo_info
        down_formula = math.sqrt(x_speed**2 + y_speed**2)

        x_speed = (torpedo_x_speed + x_speed) / down_formula
        y_speed = (torpedo_y_speed + y_speed) / down_formula

        ast_1, ast_2 = Asteroid(x, x_speed, y, y_speed, size), Asteroid(x, -x_speed, y, -y_speed, size)
        self.__asteroids.append(ast_1)
        self.__asteroids.append(ast_2)
        self._screen.register_asteroid(ast_1, size)
        self._screen.register_asteroid(ast_2, size)

    def points_manager(self, torpedo):
        """function that adds points if an asteroid was shoot"""
        for ast in self.__asteroids:
            if ast.has_intersection(torpedo):
                size = ast.get_size()
                if size == SIZE_3:
                    self.__value += SCORE_3
                    val = self.__value
                    self._screen.set_score(val)
                elif size == SIZE_2:
                    self.__value += SCORE_2
                    val = self.__value
                    self._screen.set_score(val)
                elif size == SIZE_1:
                    self.__value += SCORE_1
                    val = self.__value
                    self._screen.set_score(val)

    def torpedo_time_out(self, torpedo):
        life_time = Torpedo.get_life_time(torpedo)
        if life_time == 0:
            self.__torpedos_list.remove(torpedo)
            self._screen.unregister_torpedo(torpedo)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )

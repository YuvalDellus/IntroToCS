from screen import Screen
from random import randint
import math



class Ship:

    def __init__(self, x_location, x_speed , y_location, y_speed, heading = 0):
        self.__x_location = x_location
        self.__x_speed = x_speed
        self.__y_location = y_location
        self.__y_speed = y_speed
        self.__heading = heading
        self.__radius = 1
        self.__life = 3

    # def start_ship(self):
    #     x = randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
    #     y = randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
    #
    #     self._screen.draw_ship(x, y, 0)
    #     return Ship(x,0,y,0)

    def get_ship_info(self):
        cord_info = (self.__x_location, self.__y_location)
        speed_info = (self.__x_speed, self.__y_speed)
        return cord_info, speed_info, self.__heading

    def move_ship_left(self):
        self.__heading += 7

    def move_ship_right(self):
        self.__heading -= 7

    def ex_ship(self):
        rad_heading = math.radians(self.__heading)
        self.__x_speed += math.cos(rad_heading)
        self.__y_speed += math.sin(rad_heading)

    def move_forward(self, x, y):
        self.__x_location = x
        self.__y_location = y

    def get_radius(self):
        return self.__radius

    def ship_life(self):
        self.__life -= 1
        return self.__life

    def __str__(self):
        return str((self.__x_location, self.__y_location, self.__x_speed, self.__y_speed, self.__heading))



# x = Ship(0,0,0,0)
# x.start_ship()
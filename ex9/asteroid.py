from random import randint
from screen import Screen
import ship
import math
from torpedo import Torpedo


class Asteroid:

    def __init__(self, x_location, x_speed, y_location, y_speed, size = 3):
        self.__x_location = x_location
        self.__x_speed = x_speed
        self.__y_location = y_location
        self.__y_speed = y_speed
        self.__size = size
        self.__radius = (self.__size*10 - 5)

    def create_asteroid(self):
        x = randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y = randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        x_speed = randint(1, 3)
        y_speed = randint(1, 3)
        return Asteroid(x,x_speed, y, y_speed)

    def get_asteroid_info(self):
        cord_info = (self.__x_location, self.__y_location)
        speed_info = (self.__x_speed, self.__y_speed)
        return cord_info, speed_info

    def move_forward(self, x, y):
        self.__x_location = x
        self.__y_location = y

    def __str__(self):
        return str((self.__x_location, self.__y_location, self.__x_speed,
                    self.__y_speed,self.__size))

    def get_size(self):
        return self.__size

    def has_intersection(self, obj):
        if type(obj) is ship.Ship:
            cord, speed, heading = obj.get_ship_info()
            x, y = cord
            radius = obj.get_radius()
        elif type(obj) is Torpedo:
            cord, speed, heading = Torpedo.get_torpedo_info(obj)
            x, y = cord
            radius = obj.get_radius()
        else:
            cord, speed = obj.get_asteroid_info()
            x, y = cord

        distance = math.sqrt((x - self.__x_location)**2 + (y - self.__y_location)**2)
        if distance <= self.__radius + radius:
            return True
        return False

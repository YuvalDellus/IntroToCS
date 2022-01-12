from ship import Ship
import math

class Torpedo:

    def __init__(self, orientation_info):
        cord, speed, heading = orientation_info
        x, y = cord
        x_speed, y_speed = speed
        torpedo_x_speed = x_speed + 2 * math.cos(math.radians(heading))
        torpedo_y_speed = y_speed + 2 * math.sin(math.radians(heading))

        self.__x_location = x
        self.__x_speed = torpedo_x_speed
        self.__y_location = y
        self.__y_speed = torpedo_y_speed
        self.__heading = heading
        self.__radius = 4
        self.__life_time = 200

    def get_torpedo_info(self):
        cord_info = (self.__x_location, self.__y_location)
        speed_info = (self.__x_speed, self.__y_speed)
        return cord_info, speed_info, self.__heading

    def move_forward(self, x, y):
        self.__x_location = x
        self.__y_location = y

    def get_radius(self):
        return self.__radius

    def get_life_time(self):
        """
        function that reduce life time of an torpedo and returns its new value
        """
        self.__life_time -= 1
        new_lt = self.__life_time
        return new_lt




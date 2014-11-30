import colorsys

__author__ = 'anton'

import math


class Car:
    SAFE_DISTANCE = 80
    CRASH_DISTANCE = 10
    SPEED_LIMIT = 0.01

    def __init__(self, radius=0, alpha=0, speed=0, speed_limit=1, number=0, color=(1, 1, 1)):
        self.laps = 0
        self.radius = radius
        self.alpha = alpha
        self.speed = speed
        self.SPEED_LIMIT = speed_limit
        self.number = number
        self.color = self.__hsv_to_html(color)
        self.__previousCar = None
        self.__acceleration = self.speed / 5

    def move(self):
        if self.__previousCar is not None and self.distance_to_previous_car < self.SAFE_DISTANCE:
            self.speed -= self.__acceleration
        if self.__previousCar is not None and self.distance_to_previous_car > self.SAFE_DISTANCE:
            self.speed += self.__acceleration
        if self.__previousCar is not None and self.distance_to_previous_car < self.CRASH_DISTANCE:
            self.speed = 0
        if self.speed < 0:
            self.speed = 0
        if self.speed > self.SPEED_LIMIT:
            self.speed = self.SPEED_LIMIT

        self.alpha += self.speed
        if self.alpha > 2 * math.pi:
            self.laps += 1
            self.alpha -= 2 * math.pi

    @property
    def x(self):
        return self.radius * math.cos(self.alpha)

    @property
    def y(self):
        return self.radius * math.sin(self.alpha)

    @property
    def previous_car(self):
        return self.__previousCar

    @previous_car.setter
    def previous_car(self, value):
        self.__previousCar = value

    @property
    def distance_to_previous_car(self):
        return math.sqrt((self.x - self.previous_car.x) ** 2 + (self.y - self.previous_car.y) ** 2)

    def __hsv_to_html(self, hsv):
        rgb = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        return "#{:02x}{:02x}{:02x}".format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

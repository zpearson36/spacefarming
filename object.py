import math
from abc import abstractmethod

from utils import Vector, Position

GRAVITAIONAL_CONSTANT = .001

class Object:
    def __init__(self, radius, density, position, velocity=Vector(), colour=(0,0,255)):
        self.__radius = radius
        self.__density = density
        self.position = position
        self.velocity = velocity
        self.colour = colour

    @property
    def area(self):
        return 2 * math.pi * (self.__radius ** 2)

    @property
    def mass(self):
        return self.__density * self.area

    @property
    def radius(self):
        return self.__radius

    def update_pos(self):
        pass

    def update_velocity(self, v2):
        self.velocity += v2

    @abstractmethod
    def display(self, screen):
        pass

    @staticmethod
    def gravitational_force(obj1, obj2):
        magnitude = (GRAVITAIONAL_CONSTANT * obj1.mass * obj2.mass) / obj1.position.distance(obj2.position)
        dx = obj1.position.x_pos - obj2.position.x_pos
        dy = obj1.position.y_pos - obj2.position.y_pos
        angle = math.atan2(-dy, dx)
        return Vector(magnitude, angle)

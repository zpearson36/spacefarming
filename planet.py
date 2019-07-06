import math
import pygame
from utils import Position
from object import Object

class Planet(Object):
    def __init__(self, radius, density, position):
        Object.__init__(self, radius, density, position)

    def display(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.position.x_pos),
            int(self.position.y_pos)), self.radius, 0)

    def update_pos(self):
        new_x = self.velocity.magnitude*math.sin(self.velocity.angle)
        new_y = self.velocity.magnitude*math.cos(self.velocity.angle)
        self.position = Position(self.position.x_pos + new_x,
                                 self.position.y_pos + new_y)

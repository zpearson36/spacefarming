import pygame
from object import Object

class Planet(Object):
    def __init__(self, radius, density, position):
        Object.__init__(self, radius, density, position)

    def display(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.position.x_pos),
            int(self.position.y_pos)), self.radius, 0)

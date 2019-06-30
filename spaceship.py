import pygame
from object import Object

class Spaceship(Object):
    def __init__(self, radius, density, position):
        Object.__init__(self, radius, density, position, colour=(255,0,0))

    def display(self, screen):
        pygame.draw.rect(screen, self.colour, self.__get_rect_from_pos(), 0)

    def __get_rect_from_pos(self):
        return[self.position.x_pos - self.radius,
               self.position.y_pos - self.radius,
               self.radius * 2, self.radius * 2]

import pygame
import tkinter
from planet import Planet
from spaceship import Spaceship
from object import Object
from utils import Position, Vector, collide
pygame.init()
x = 10
y = 35
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen = pygame.display.set_mode((width-50, height-50))
pygame.display.set_caption("what it do, bitches!")

objs = []
objs.append(Planet(radius=300, density=.5, position=Position(width/2, height/2)))
objs.append(Spaceship(radius=25, density=.001, position=Position(width/2, 100)))

green = (0, 255, 0)
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 24)
force2 = font.render('Force:', True, green, blue)
angle = font.render('Angle:', True, green, blue)
# create a rectangular object for the
# text surface object
forceRect = force2.get_rect()
angleRect = angle.get_rect()

# set the center of the rectangular object.
forceRect.center = (100, 100)
angleRect.center = (100, 150)

running = True
while running:
    screen.fill((255,255,255))
    screen.blit(force2, forceRect)
    screen.blit(angle, angleRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i, obj in enumerate(objs):
        obj.update_pos()
        obj.display(screen)
        for obj2 in objs[i+1:]:
            force = Object.gravitational_force(obj, obj2)
            force2 = font.render(f'Gravity: {force.magnitude}', True, green, blue)
            angle = font.render(f'Angle: {force.angle}', True, green, blue)
            force_opp = -force
            obj.update_velocity(Vector(force.magnitude/obj.mass, force_opp.angle))
            obj2.update_velocity(Vector(force.magnitude/obj2.mass, force.angle))
            collide(obj, obj2)
    pygame.display.flip()

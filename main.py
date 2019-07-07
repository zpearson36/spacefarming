import pygame
import random
import tkinter
import math
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
ss = Spaceship(radius=25, density=.1, position=Position(width/2, height/2 - 25))
objs.append(Planet(radius=25000, density=.001, position=Position(width/2, 25500 + height/25)))
#for _ in range(random.randint(1,10)):
#    radius = random.randint(5,150)
#    objs.append(Planet(radius=radius, density=random.random(), position=Position(random.randint(radius, width-radius),random.randint(radius, height-radius))))

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
    ss.display(screen)
    for i, obj in enumerate(objs):
        obj.update_pos()
        obj.display(screen)
        for obj2 in objs[i+1:]:
            force = Object.gravitational_force(obj, obj2)
            force2 = font.render(f'Gravity: {objs[0].velocity.magnitude}', True, green, blue)
            angle = font.render(f'Angle: {objs[1].velocity.magnitude}', True, green, blue)
            obj.update_velocity(Vector(force.magnitude/obj.mass, force.angle - .5 * math.pi))
            obj2.update_velocity(Vector(force.magnitude/obj2.mass, force.angle + .5 * math.pi))
            collide(obj, obj2)
    pygame.display.flip()

import pygame

width = 640
height = 360
captions = "Game"

clock:pygame.time.Clock = pygame.time.Clock() 

ballangle:float = 0
ballspeed:float = 0.2

ballx:float = (width / 2)
bally:float = (height / 2)
ballw:float = 32
ballh:float = 32

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(captions)

pygame.display.update()
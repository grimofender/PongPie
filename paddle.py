import globalvar
import pygame, random, math


def PlayerScored(player:int):
        globalvar.ballx = (globalvar.width / 2)
        globalvar.bally = (globalvar.height / 2)
        if player == 1:
            globalvar.ballangle = random.randrange(155, 205) / (180/math.pi)
        else:
            if player == 2:
                globalvar.ballangle = random.randrange(-25, 25) / (180/math.pi)
        print("Player "+ str(player) + " scored!!!")
        return

# TODO Implement Paddles
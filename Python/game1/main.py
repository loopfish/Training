import pygame
import sys
import os

'''
Variables
'''

# put variables here
worldx = 960
worldy = 720
fps    = 40  # frame rate
ani    = 4   # animation cycles



'''
Objects
'''

# put Python classes and functions here


'''
Setup
'''

# put run-once code here
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','background.png'))

'''
Main Loop
'''

# put game loop here
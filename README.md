import pygame
import random
import sys

pygame.init()

# Screen settings 
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
# colors

WHITE =(255,255,255)
BLACK = (30, 30, 30)
GREEN = (40, 160, 60)

#GROUN 
dino = pygame.Rect(80, GROUND_Y -50, 40,50)
velocity_y =0
gravity = 0.8
jump_power = -15
on_ground = True
# Dinosaur-game

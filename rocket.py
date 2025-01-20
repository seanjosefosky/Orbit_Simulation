import pygame, random
import pygame.gfxdraw

class Rocket():
    m = 0
    vel = 0
    pos = 0


def DrawRocket(screen, x, y):
    color = pygame.Color(156, 141, 240)
    pygame.gfxdraw.aacircle(screen, x, y, 10, color)
    pygame.gfxdraw.filled_circle(screen, x, y, 10, color)
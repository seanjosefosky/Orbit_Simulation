import pygame, random as r
from pygame import gfxdraw
import pygame.gfxdraw
import rocket, simulation
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
screen_w = screen.get_width
screen_h = screen.get_height
clock = pygame.time.Clock()
running = True
dt = 0

# TODO: Drag screen with mouse
def MoveScreen():
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    if key[pygame.MOUSEBUTTONDOWN]:
        print(Mouse_x,Mouse_y)


# Background Handling
stars = []
class Stars:
    def __init__(self, name, pos, radius):
        self.name = name
        self.pos = pos
        self.radius = radius

def DrawStars():
    limit = 100
    if len(stars) < limit:
        radius = r.uniform(0.1,3)
        spawn = pygame.Vector2(r.uniform(0,screen.get_width()), r.uniform(0,screen.get_height()))
        newstar = Stars(len(stars), spawn, radius)
        stars.append(newstar)

    # Draw all stars in 'stars' list after all of their information is created
    if len(stars) == limit:
        for body in stars:
            pygame.draw.circle(screen, "white", body.pos, body.radius)

    # TODO: Prevent stars overlapping when spawning


# Draw it antialiased
class MainBody:
    m = 100
    rad = 60
    pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def DrawMainBody():
    body = MainBody()
    color = pygame.Color(48,41,191)
    x = int(body.pos.x)
    y = int(body.pos.y)
    pygame.gfxdraw.aacircle(screen, x, y, body.rad, color)
    pygame.gfxdraw.filled_circle(screen, x, y, body.rad, color)

    #TODO: Make circle look like sphere
    # pygame.gfxdraw.arc(screen, 300, 100, 60, 45, 180, color)



# TODO #
# Newtonian gravity simulation
# mass, distance, scale, velocity
# zone of influence (2 body simulation)
# 


# TODO: Draw orbit path behind thing



# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    simulation.Simulation(MainBody,rocket.Rocket())

    screen.fill("black")

    DrawStars()
    # MoveScreen()
    DrawMainBody()
    rocket.DrawRocket(screen, 600, 500)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000




pygame.quit()
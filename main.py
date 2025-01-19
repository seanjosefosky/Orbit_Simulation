# Example file showing a circle moving on screen
import pygame, random as r

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Bodies Handling

bodies = []

class Bodies:
    def __init__(self, name, pos, radius):
        self.name = name
        self.pos = pos
        self.radius = radius


def DrawBodies():
    limit = 100
    if len(bodies) < limit:
        radius = r.uniform(0.1,3)
        bodyspawn = pygame.Vector2(r.uniform(0,screen.get_width()), r.uniform(0,screen.get_height()))
        newbody = Bodies(len(bodies), bodyspawn, radius)
        bodies.append(newbody)

    # Draw "bodies" list after all of their information is generated
    if len(bodies) == limit:
        for body in bodies:
            pygame.draw.circle(screen, "white", body.pos, body.radius)


# TODO: Prevent body collision when spawning


# TODO: Drag screen with mouse
def MoveScreen():
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    if key[pygame.MOUSEBUTTONDOWN]:
        print(Mouse_x,Mouse_y)



# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        screen.fill("black")

        DrawBodies()
        MoveScreen()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000




pygame.quit()
from pgzero.builtins import *

WIDTH = 800
HEIGHT = 600

playerx = 100;
playery = 200;

def draw():
    screen.blit(images.backdrop, (0,0))
    screen.blit(images.mars ,(50,50))
    screen.blit(images.astronaut, (playerx, playery))
    screen.blit(images.ship, (550, 300))

def game_loop():
    global playerx, playery

    if keyboard.right:
        playerx += 5
    elif keyboard.left:
        playerx -= 5
    elif keyboard.up:
        playery -= 5
    elif keyboard.down:
        playery += 5


clock.schedule_interval(game_loop, 0.03)
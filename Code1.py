WIDTH=800
HEIGHT=600

playerx=100
playery=100

def draw():
    screen.blit(images.backdrop,(0,0))
    screen.blit(images.mars,(50,50))
    screen.blit(images.astronaut,(100,200))
    screen.blit(images.ship,(playerx,playery))
    
def gameloop():
    global playerx,playery
    if keyboard.right:
        playerx+=5
    elif keyboard.left:
        playerx-=5
    elif keyboard.up:
        playery-=5
    elif keyboard.down:
        playery+=5

clock.schedule_interval(gameloop,0.03)
room=[
[1,1,0,1,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,0],
[1,0,0,0,1],
[1,0,0,0,1],
[1,1,1,1,1],
]
    
WIDTH=800
LENGTH=600

topleftx=100
toplefty=150

OBJECT_LIST=[images.floor, images.pillar]

roomheight=7
roomwidth=5

def draw():    
    for y in range (roomheight):
        for x in range (roomwidth):
            item=room[y][x]
            drawing=OBJECT_LIST[item]
            
            screen.blit(drawing, (topleftx+x*30, toplefty+y*30-drawing.get_height()))
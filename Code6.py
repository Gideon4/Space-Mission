from pgzero.builtins import *

WIDTH=800
LENGTH=600

topleftx=100
toplefty=150

OBJECT_LIST=[images.floor, images.pillar]

PLAYER_NAME = "Gideon"
FRIEND1_NAME = "Holt"
FRIEND2_NAME = "Heltzer"

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [ ["Room 0 - where unused objects are kept", 0, 0, False, False] ]

outdoor_rooms = range(1, 26)
for planetsectors in range(1, 26): #rooms 1 to 25 are generated here
    GAME_MAP.append( ["The dusty planet surface", 13, 13, True, True] )

GAME_MAP  += [
        #["Room name", height, width, Top exit?, Right exit?]
        ["The airlock", 13, 5, True, False], # room 26
        ["The engineering lab", 13, 13, False, False], # room 27
        ["Poodle Mission Control", 9, 13, False, True], # room 28
        ["The viewing gallery", 9, 15, False, False], # room 29
        ["The crew's bathroom", 5, 5, False, False], # room 30
        ["The airlock entry bay", 7, 11, True, True], # room 31
        ["Left elbow room", 9, 7, True, False], # room 32
        ["Right elbow room", 7, 13, True, True], # room 33
        ["The science lab", 13, 13, False, True], # room 34
        ["The greenhouse", 13, 13, True, False], # room 35
        [PLAYER_NAME + "'s sleeping quarters", 9, 11, False, False], # room 36
        ["West corridor", 15, 5, True, True], # room 37
        ["The briefing room", 7, 13, False, True], # room 38
        ["The crew's community room", 11, 13, True, False], # room 39
        ["Main Mission Control", 14, 14, False, False], # room 40
        ["The sick bay", 12, 7, True, False], # room 41
        ["West corridor", 9, 7, True, False], # room 42
        ["Utilities control room", 9, 9, False, True], # room 43
        ["Systems engineering bay", 9, 11, False, False], # room 44
        ["Security portal to Mission Control", 7, 7, True, False], # room 45
        [FRIEND1_NAME + "'s sleeping quarters", 9, 11, True, True], # room 46
        [FRIEND2_NAME + "'s sleeping quarters", 9, 11, True, True], # room 47
        ["The pipeworks", 13, 11, True, False], # room 48
        ["The chief scientist's office", 9, 7, True, True], # room 49
        ["The robot workshop", 9, 11, True, False] # room 50
        ]

#simple sanity check on map above to check data entry
assert len(GAME_MAP)-1 == MAP_SIZE, "Map size and GAME_MAP don't match"

def comproom(height, width, exittop, exitright):

    fakerow=[1]
    room=[]

    room.append([1]*width)

    for i in range (height-2):
        for j in range (width-2):
            fakerow.append(0)
        fakerow.append(1)
        room.append(fakerow)
        fakerow=[1]

    room.append([1]*width)

    if exittop:
        room[0][round(int(width/2),0)]=0
    if exitright:
        room[round(int(height/2),0)][width-1]=0

    return(room)

'''def draw():
    for y in range (roomheight):
        for x in range (roomwidth):
            item=room[y][x]
            drawing=OBJECT_LIST[item]

            screen.blit(drawing, (topleftx+x*30, toplefty+y*30-drawing.get_height()))'''

roomnumber=31

roomname=GAME_MAP[roomnumber][0]
roomheight=GAME_MAP[roomnumber][1]
roomwidth=GAME_MAP[roomnumber][2]
roomtopexit=GAME_MAP[roomnumber][3]
roomrightexit=GAME_MAP[roomnumber][4]

comproom(roomheight,roomwidth,roomtopexit,roomrightexit)
from scenery import *
from objects import *
from player import *
import time

room_height = 5
room_width = 5
TILE_SIZE = 30

room_map = []

WIDTH = 800
HEIGHT = 600

top_left_x = 100
top_left_y = 150

OBJECT_LIST = objects

PLAYER_NAME = "Adam"
FRIEND1_NAME = "Yeet"
FRIEND2_NAME = "Yote"

#variables for the player
player_x, player_y = 5, 2
player_direction = "down"
player_frame = 0
player_image = PLAYER[player_direction][player_frame]
player_offset_x, player_offset_y = 0, 0
player_old_x, player_old_y = 0,0

#This is the section for setting up the scenery.
for coord in range (13):
    for room_num in range (1,6):
        scenery[room_num] +=[[31,0,coord]]
#This is the section for the start of making the map.

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

def autogen_room():
    global room_number,room_height,room_width
    room_map=[]
    temprow=[]

    room_name = GAME_MAP[room_number][0]
    height=GAME_MAP[room_number][1]
    width=GAME_MAP[room_number][2]
    exit_top=GAME_MAP[room_number][3]
    exit_right=GAME_MAP[room_number][4]

    room_height=height
    room_width=width

    floor_object = 0
    bottom_edge=1
    side_edge = 1
    if room_number<26:
        floor_object =2
    if room_number<21:
        bottom_edge = 2
        side_edge = 2
    if room_number>20 and room_number<26:
        bottom_edge = 1
        side_edge = 2

    temprow=[side_edge]*width
    room_map.append(temprow)


    for j in range(height-2):
        temprow=[]
        temprow.append(side_edge)

        for i in range(width-2):
            temprow.append(floor_object)


        temprow.append(side_edge)

        room_map.append(temprow)

    temprow=[]
    temprow=[bottom_edge]*width
    room_map.append(temprow)


    if exit_top:

        room_map[0][int(width/2)] = floor_object
    if exit_right:
        room_map[int(height/2)][width-1] = floor_object

    #insert scenery
    if room_number in scenery:
        for scenery_item in scenery[room_number]:
            scenery_num = scenery_item[0]
            scenery_y = scenery_item[1]
            scenery_x = scenery_item[2]
            room_map[scenery_y][scenery_x]= scenery_num

            image_here = objects[scenery_num][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int (image_width / TILE_SIZE)

            for tile_num in range (1, image_width_in_tiles):
                room_map[scenery_y][scenery_x + tile_num] = 255
    return room_map

def draw_player():
    player_image = PLAYER[player_direction][player_frame]
    tempx = top_left_x + player_x * TILE_SIZE + player_offset_x * TILE_SIZE
    tempy = top_left_y + player_y * TILE_SIZE + player_offset_y * TILE_SIZE - player_image.get_height()
    screen.blit(player_image,(tempx, tempy))


def draw():
    global room_map
    global room_height
    global room_width

    for y in range(room_height):
        for x in range(room_width):
            item=room_map[y][x]
            if item != 255:
                drawing = OBJECT_LIST[item][0]
                screen.blit(drawing, (top_left_x + x*30, top_left_y + y*30 - drawing.get_height()))
        #if player_y == y:
    draw_player()



def game_loop():
    global player_x, player_y, player_offset_x, player_offset_y
    global player_direction, player_frame
    global room_number, player_old_x, player_old_y

    #before moving, store the current position in the old variables
    player_old_x = player_x
    player_old_y = player_y

    #print(player_x, player_y)
    if player_frame == 0:
        if keyboard.right:
            player_x += 1
            player_direction = "right"
            player_frame = 1
        elif keyboard.left:
            player_x -= 1
            player_direction = "left"
            player_frame = 1
        elif keyboard.down:
            player_y += 1
            player_direction = "down"
            player_frame = 1
        elif keyboard.up:
            player_y -= 1
            player_direction = "up"
            player_frame = 1
    if player_frame > 0:
        player_frame += 1
        time.sleep(0.05)
        #adjust the offsets
        if player_direction == "right":
            player_offset_x = -1 + (0.25 * player_frame)
        if player_direction == "left":
            player_offset_x = 1 - (0.25 * player_frame)
        if player_direction == "up":
            player_offset_y = -1 + (0.25 * player_frame)
        if player_direction == "down":
            player_offset_y = 1 - (0.25 * player_frame)

        #loop back around to frame 0
        if player_frame == 5:
            player_frame = 0
            player_offset_x = 0
            player_offset_y = 0

    #right
    if player_x == room_width:
        room_number += 1
        autogen_room()
        player_x=0
        player_y=int(room_height/2)
        player_frame=0
        return

    #left
    if player_x == 0:
        room_number -= 1
        autogen()
        player_x=room_width-1
        player_y=int(room_height/2)
        player_frame=0
        return

    #up
    if player_y == 0g:
        room_number -= MAP_WIDTH
        autogen()
        player_y=room_height-1
        player_x=int(room_height/2)
        player_frame=0
        return

    #down
    if player_y == room_height:
        room_number += MAP_WIDTH
        autogen()
        player_y=0
        player_x=int(room_height/2)
        player_frame=0
        return

    if room_map[player_y][player_x] not in items_player_may_stand_on:
        player_x = player_old_x
        player_y = player_old_y

clock.schedule_interval(game_loop, 0.03)

room_number =31

room_map = autogen_room()
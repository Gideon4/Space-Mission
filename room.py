from pgzero.builtins import *
from Code6 import *
from Objects import *
from Scenery import *
from Player import *

TILE_SIZE=30

def autogen_room(height, width, exit_top, exit_right):
    global room_map
    global room_number
    room_map = []

    #check tile
    floor_object = 0
    bottom_edge = 1
    side_edge = 1
    if room_number < 26:
        floor_object  =2
    if room_number in range(1,21):
        bottom_edge=2
        side_edge=2
    if room_number in range(21,26):
        side_edge=2


    #everything else that i forgot to organize
    room_map = []
    temprow = []

    temprow=[side_edge]*width
    room_map.append(temprow)

    for j in range(height-2):
        temprow = []
        temprow.append(side_edge)

        for i in range(width-2):
            temprow.append(floor_object)

        temprow.append(side_edge)
        room_map.append(temprow)

    temprow = []
    temprow = [bottom_edge]*width
    room_map.append(temprow)


    if exit_top:

        room_map[0][int(width/2)] = floor_object

    if exit_right:
        print(room_map)
        room_map[int(height/2)][width-1] = floor_object

    #insert scenery
    if room_number in scenery:
        for sceneryitem in  scenery[room_number]:
            scenerynum=sceneryitem[0]
            sceneryy=sceneryitem[1]
            sceneryx=sceneryitem[2]
            room_map[sceneryy][sceneryx]=scenerynum

            image_here=objects[scenerynum][0]
            image_width=image_here.get_width()
            image_width_in_tiles=int(image_width/TILE_SIZE)

            for tilenumber in range(1,image_width_in_tiles):
                room_map[sceneryy][sceneryx+tilenumber]=255

    print (room_map)
    return room_map

#TEST

temprow=""



roommap = []

WIDTH = 800
HEIGHT = 600

top_left_x = 100
top_left_y = 150

OBJECT_LIST = objects

room_height = 0
room_width = 0

room_number = 31
room_height  = GAME_MAP[room_number][1]
room_width = GAME_MAP[room_number][2]
room_topExit = GAME_MAP[room_number][3]
room_rightExit = GAME_MAP[room_number][4]
roommap = autogen_room(room_height, room_width, room_topExit, room_rightExit)

def draw():
    for y in range(room_height):
        for x in range(room_width):
            item = roommap[y][x]
            if item !=255:

                drawimg = OBJECT_LIST[item][0]

                screen.blit(drawimg, (top_left_x + x*30, top_left_y  + y*30 - drawimg.get_height()))
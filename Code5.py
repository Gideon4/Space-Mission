def comproom(height, width, exittop, exitright):
    
    fakerow=[1]
    room=[]
    
    room.append([1]*width)
    
    for i in range (height-2):
        room.append(for j in range (width-2):
            fakerow.append(0))
    
    print(room)
    
comproom(7,5,3,4)
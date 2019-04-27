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
    
x=comproom(7,5,True,True)
print(x)
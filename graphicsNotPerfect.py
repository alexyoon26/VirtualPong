from vpython import *
import time
import math

scene = canvas(width=1425, height=775,
     center=vector(0,0,0), background=color.black)

cup1Loc=[-0.6,1,9.4]
cup2Loc=[0.6,1,9.4]
cup3Loc=[-1.8,1,9.4]
cup4Loc=[1.8,1,9.4]
cup5Loc=[0,1,8.2]
cup6Loc=[-1.2,1,8.2]
cup7Loc=[1.2,1,8.2]
cup8Loc=[-0.6,1,7]
cup9Loc=[0.6,1,7]
cup10Loc=[0,1,5.8]
cupLocations=[cup1Loc,cup2Loc,cup3Loc,cup4Loc,
    cup5Loc,cup6Loc,cup7Loc,cup8Loc
    ,cup9Loc,cup10Loc]

def drawTableBorder():
    tableBorderMiddle=box(pos=vector(0,0.41,0),color=color.black,length=0.1, width=20, height=0)
    tableBorderLeft=box(pos=vector(-4.1,0,0),color=color.red,length=0.2, width=20, height=.8)
    tableBorderLeft=box(pos=vector(4.1,0,0),color=color.red,length=0.2, width=20, height=.8)

def drawPongTable():
    pongTable=box(pos=vector(0,0,0),color=color.white,length=8, width=20, height=.8)

def drawBall():
    ball=sphere (color=color.orange, radius=.4)
    ddy=-0.00098
    dy=0
    dz=-0.15
    xPos=0
    yPos=7
    zPos=10
    
    while True:
        rate(40)
        dy=dy+ddy
        yPos=yPos+dy
        zPos=zPos+dz
        ball.pos=vector(xPos,yPos,zPos)
        if yPos<=0:
            break
        

def drawCupHelper(x,z):
    #https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/program/Extrusions/edit
    tube = extrusion(path=[vec(0,0,0), vec(1.5,0,0)], shape=shapes.circle(radius=0.6, thickness=0.1),
                    pos=vec(x,1,-z), axis=vec(0,2,0), color=color.red, end_face_color=color.white)

###### MOVE CODE TO RUN WHEN OPENCV CODE GETS VALS ######

# cupHit = cupCollision(v, l, dx, 7, 1, g) #v,l,dx determined from opencv
#                                         # g number - needs to be calcd
# if cupHit != None:
#     time.sleep(.45) #whatever time it takes to hit is
#             cupLocations.pop(cupHit)
# v = l = dx = g = 10
def cupCollision(v, l, dx, y, h, g):
    t = math.sqrt((2*y-2*h)/g) #time
    posx = ((v*t)/(math.sqrt(l**2+dx**2))+1)*dx
    posy = ((v*t)/(math.sqrt(l**2+dx**2))+1)*l
    cups = cupLocations()

    for i in range(len(cups)):
        center = (cups[i][0], cups[i][2])
        distance = math.sqrt((center[0]-posx)**2 + (center[1]-posy)**2)
        if distance < 0.6:
            return i
    
    return None

def drawCup():
    time.sleep(3)
    cupLocations.pop()
    for row in range(len(cupLocations)):
        drawCupHelper(cupLocations[row][0],cupLocations[row][2])


def virtualPong():
    while True:
        print('run')
        drawCup()
        drawPongTable()
        drawTableBorder()
        drawBall()
    


scene.camera.pos = vector(0, 6.52134, 4)
    

virtualPong()

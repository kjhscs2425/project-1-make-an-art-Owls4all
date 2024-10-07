import turtle
import math
# ---------Setting up variables ---------#
#stuff to mess with 
sides = 6 #number of sides. (default 6) Changing this not yet fully supported
s = 100 #side length variable (default 100)
triCount = 3 #number of triangles  (default 3)       
triScale = 0.8 #Relative scale of triangle sides (default 0.85)

#important stuff- best not to change
t = turtle  # typing shortcut
t.speed(10)
theta = 720/sides # angle to turn for triangle edges
phi = 360/sides    # angle to turn for hexagon edges
alpha = phi/2  # angle from edge to center of gap
radius = s
#----------------------------------------#

#math notes 
'''
it works for a hexagon because distance center-to-corner is the same as corner-to-corner 
due to hexagons being made from equilateral triangles.
This is why it does not work for other shapes inherently: they are made from isoscoles triangles. 
For the side length variable to be accurate, I must use trig to determine the center distance and angles 
(whch the existing math does not work properly for.)

Inner length as a function of side lenghth:
[tbd]

Initial angle should be 1 section above horizontal,
= 360/sides
'''


#---------setting up functions-----------#
def shape(side,sideCount): # function count 1
    t.left(360/sideCount)
    t.forward(radius) #draw line to corner
    ''' ^^^ Need to change this line ^^^ '''
    t.left(theta) #turn to draw the first side
    for i in range(1,sideCount): # loop count 1
        t.forward(side) #draw a side 
        t.left(phi) #turn to draw next side
    t.left(phi) #turn to center
    t.forward(radius) #finish shape

def travel(distance): # function count 2
    t.up() #stop drawing
    t.left(phi-alpha) #point to center of gap
    t.forward(distance) #create distance from center
    t.right(alpha) #point in correct direction for triangle drawing
    t.down() #start drawing again
    

def triangle(whichOne): # function count 3
        fullSide=s*triScale**whichOne
        gap = math.sqrt((4/3)*((math.sqrt((((s*(triScale**whichOne))**2)-((s*triScale**(whichOne))**2)*(3/4)))))**2) #right now it only works properly with 3 triangles. will fix.
        t.forward(fullSide) #draw triangle side, scaled by appropriate factor
        t.left(theta)  #turn appropriate angle
        t.forward((fullSide-gap)/2) #go partway#
        t.up() #stop drawing
        t.forward(gap) #keep going without leaving a mark (this is so triangles don't overlap)
        t.down() #start drawing again
        t.forward((fullSide-gap)/2) #finish the side
        t.left(theta)
        t.forward(fullSide)
        t.left(theta)
#-------------------------------------#

#-----------begin executing-----------#

shape(s,sides) #draw the hexagon
t.left(180) #point opposite direction
travel(3*s/8) #move to start point for first triangle
triangle(1)
travel(math.sqrt((((s*(triScale))**2)-((s*triScale)**2)*(3/4))))

for i in range(2,triCount): # loop count 2
    triangle(i) #draw a triangle. Use loop variable to specify which size
    travel(math.sqrt((((s*(triScale**i))**2)-((s*triScale**(i))**2)*(3/4)))) #prepare for next triangle


for i in range(3): # loop count 3
        t.forward(s*triScale**(triCount+1)) #draw side of final triangle
        t.left(theta) #turn to draw next side
#-------------------------------------#

#--------Make the image persist-------#
turtle.hideturtle()
turtle.exitonclick()
#-------------------------------------#
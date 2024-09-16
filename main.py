import turtle
# ---------Setting up variables ---------#
#stuff to mess with 
sides = 6 #number of sides. (default 6) Changing this not yet fully supported
s = 100 #side length variable (default 100)
triCount = 3 #number of triangles  (default 3)       
triScale = 0.85 #Relative scale of triangle sides (default 0.85)
triSpread = 0.75 #affects distance of triangles (default 0.75)

#important stuff- best not to change
t = turtle  # typing shortcut
theta = 720/sides # angle to turn for triangle edges
phi = theta/2    # angle to turn for hexagon edges
alpha = phi/2  # angle from edge to center of gap
#----------------------------------------#

#---------setting up functions-----------#
def shape(side,sideCount): # function count 1
    t.forward(side) #draw line to edge of hexagon
    t.left(theta) #turn to draw the first side
    for i in range(1,sideCount): # loop count 1
        t.forward(side) #draw a side 
        t.left(phi) #turn to draw next side
    t.right(theta+180) #turn to center
    t.forward(side) #finish shape

def travel(): # function count 2
    t.up() #stop drawing
    t.left(phi-alpha) #point to center of gap
    t.forward(s*(triSpread/triCount)) #create distance from center
    t.right(alpha) #point in correct direction for triangle drawing
    t.down() #start drawing again
    

def triangle(whichOne): # function count 3
        fullSide=s*triScale**whichOne
        gap = (s*(triSpread/triCount))*2.65*triScale**whichOne #right now it only works properly with 3 triangles. will fix.
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
t.left(phi) #prepare initial angle
shape(s,sides) #draw the hexagon
t.left(180) #point opposite direction
travel() #move to start point for first triangle

for i in range(1,triCount): # loop count 2
    triangle(i) #draw a triangle. Use loop variable to specify which size
    travel() #prepare for next triangle

for i in range(3): # loop count 3
        t.forward(s*triScale**triCount+1) #draw side of final triangle
        t.left(theta) #turn to draw next side
#-------------------------------------#

#--------Make the image persist-------#
turtle.hideturtle()
turtle.exitonclick()
#-------------------------------------#
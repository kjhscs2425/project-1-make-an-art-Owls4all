import turtle
# ---------Setting up variables ---------#
t = turtle #typing shortcut
theta = 120 # 
phi = 60    #   angles- these shouldn't be changed
alpha = 30  # 

s = 100 #side length variable 
triCount = 3 #number of triangles               these can change!
triScale = 0.75 #Relative scale of triangle sides
triSpread = 0.5 #affects distance of triangles
#----------------------------------------#

#---------setting up functions-----------#
def hexagon(side):
    t.forward(side)
    t.left(theta)
    for i in range(5):
        t.forward(side)
        t.left(phi)
    t.right(theta+180)
    t.forward(side)

def travel():
    t.up()
    t.left(phi-alpha)
    t.forward(s*(triSpread/triCount))
    t.right(alpha)
    t.down()
    

def triangle(whichOne):
    for i in range(3):
        t.forward(s*triScale**whichOne)
        t.left(theta)
#-------------------------------------#

#-----------begin executing-----------#
t.left(phi)
hexagon(s)
t.left(180)
travel()

for i in range(1,triCount):
    travel()
    triangle(i)
#-------------------------------------#

#--------Make the image persist-------#
turtle.exitonclick()
#-------------------------------------#
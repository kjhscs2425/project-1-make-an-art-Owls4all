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
    t.right(theta)
    for i in range(5):
        t.forward(side)
        t.right(phi)
    t.left(theta)
    t.forward(side)

def travel():
    t.up()
    t.left(180-theta+alpha)
    t.forward(s*(triSpread/triCount))
    t.left(alpha)
    t.down()

def triangle(whichOne):
    for i in range(3):
        t.forward(s*triScale**whichOne)
        t.left(theta)

turtle.exitonclick()
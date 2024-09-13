import turtle
# ---------Setting up variables ---------#
t = turtle #typing shortcut
theta = 120 # 
phi = 60    #   angles- these shouldn't be changed
alpha = 30  # 

s = 100 #side length variable 
triCount = 3 #number of triangles               these can change!
triScale = 0.5 #Relative scale of triangle sides
#----------------------------------------#

#---------setting up functions-----------#
def hexagon(side):
    t.forward(side)
    t.left(theta)
    for i in range(5):
        t.forward(side)
        



turtle.exitonclick()
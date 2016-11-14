import turtle


def draw_square():
    windows = turtle.Screen()#create the background screen for the drawing
    windows.bgcolor("red") # create an instance from a Class Screen
    
    brad = turtle.Turtle() #move around, def __init__ stand for initialize
    # brad is an instance of class Turtle
    
    brad.shape("turtle")#https://docs.python.org/2/library/turtle.html#turtle.shape
    brad.color("white","blue")#two color, first outline, second filled; can't do three colors
    brad.speed(5)

    #don't repeat too much
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90) #repeat 4 squares

    angie = turtle.Turtle()
    angie.circle(100) #create circle
    angie.color("blue")
    angie.shape("arrow")
    
    windows.exitonclick()
    
draw_square()

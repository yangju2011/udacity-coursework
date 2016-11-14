import turtle


def draw_square(some_turtle):
    i = 0
    while i<4: # repeat for squares
        some_turtle.forward(100)
        some_turtle.right(90)
        i=i+1
        
def draw_shape():#n stands for the number of edge
    windows = turtle.Screen()#create the background screen for the drawing
    windows.bgcolor("red")
    
    brad = turtle.Turtle() #move around, def __init__ stand for initialize
    
    brad.shape("turtle")#https://docs.python.org/2/library/turtle.html#turtle.shape
    brad.color("white","blue")#two color, first outline, second filled; can't do three colors
    brad.speed(5)

    for i in range(0,36):
        brad.right(10)
        draw_square(brad)

    windows.exitonclick()

draw_shape()

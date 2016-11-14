import turtle

def draw_diamond(some_turtle):
    for i in range (0,2):
        some_turtle.forward(100)
        some_turtle.right(40)
        some_turtle.forward(100)
        some_turtle.right(140)

def draw_flower():

    #create screen with turtle.Screen
    windows = turtle.Screen()
    windows.bgcolor("pink")

    #initialize a turtle
    judy =  turtle.Turtle()

    #property of this instance
    judy.shape("arrow")
    judy.color("black")
    judy.speed(50)

    for i in range(0,72):
        draw_diamond(judy)
        judy.right(5)

    judy.right(90)
    judy.forward(200)
    
draw_flower()

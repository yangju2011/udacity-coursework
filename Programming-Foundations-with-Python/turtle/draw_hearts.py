import turtle

def draw_heart(size,color_fill):
    #initialize a turtle
    heart =  turtle.Turtle()

    #property of this instance
    heart.shape("turtle")
    heart.color("white",color_fill)
    heart.speed(5)
    
    heart.begin_fill()

    heart.left(45)
    heart.forward(size)
    heart.right(180)
    heart.circle(-size/2,-180)
    heart.right(90)
    heart.circle(-size/2,-180)
    heart.backward(size)

    heart.end_fill()
    
def draw_hearts():
    windows = turtle.Screen()
    windows.bgcolor("lavender")

    i = 250
    k = 0
    colors = ["darkred","firebrick","magenta","mediumorchid","crimson","hotpink","violet","plum","lightpink","pink"]
    while i > 0 and k < 10:
        draw_heart(i,colors[k])
        k = k + 1
        i = i - 25
        
    windows.exitonclick()


draw_hearts()

from turtle import *

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor(0,0,0)
screen.title("Henry Window")

turty = Turtle()
turty.shape("turtle")
turty.color(1,0,0)
turty.pensize(5)

# H
turty.penup()
turty.goto(-450,-200)
turty.setheading(90)
turty.pendown()
turty.forward(400)
turty.backward(200)
turty.setheading(0)
turty.forward(100)
turty.setheading(90)
turty.forward(200)
turty.backward(400)

# e
turty.pencolor(1,0.5,0)
turty.penup()
turty.goto(-250,-150)
turty.pendown()
turty.goto(-150,-150)
turty.setheading(90)
turty.circle(50, 315)

# n
turty.pencolor(1,1,0)
turty.penup()
turty.setheading(90)
turty.goto(-50,-200)
turty.pendown()
turty.goto(-50,-100)
turty.goto(-50,-150)
turty.circle(-50,180)
turty.goto(50,-200)

# r
turty.pencolor(0,1,0)
turty.penup()
turty.setheading(90)
turty.goto(150,-200)
turty.pendown()
turty.goto(150,-100)
turty.goto(150,-150)
turty.circle(-50,135)

# y
turty.pencolor(0,0,1)
turty.penup()
turty.setheading(-45)
turty.goto(350,-100)
turty.pendown()
turty.goto(400,-150)
turty.setheading(45)
turty.goto(450,-100)
turty.setheading(-135)
turty.goto(350,-200)
turty.circle(-50,45)
turty.goto(-450,-225)
turty.circle(-50,45)

screen.exitonclick()
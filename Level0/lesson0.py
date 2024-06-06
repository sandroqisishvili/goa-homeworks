from turtle import *


#we want to paint a house
begin_fill()
speed(10)
#step one draw a square
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)        #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color("cyan")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

begin_fill()
color("pink")
penup()
goto(0,200)
pendown()

left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

begin_fill()
right(90)
forward(150)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

color("blue")
forward(150)
right(180)
forward(200)
right(90)
forward(50)
left(180)
forward(50)
left(90)
forward(200)
left(90)
forward(50)


exitonclick()


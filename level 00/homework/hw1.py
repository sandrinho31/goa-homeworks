from turtle import * 
#we want to paint a house

#step1: create a square
width(5)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#step2: drawing a door


forward(80)

left(90)

color("blue")
begin_fill()
forward(100)
right(90)

forward(50)
right(90)

forward(100)
end_fill()
color("brown")

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(140)
forward(150)

left(98)
forward(155)
end_fill()

penup()
goto(70,150)
pendown()

left(42)
forward(50)
right(90)
forward(50)

right(90)

forward(50)

right(90)

forward(50)

right(90)

forward(25)

right(90)
forward(50)

right(90)
forward(25)

right(90)
forward(25)

right(90)
forward(50)




penup()

goto(140,150)
pendown()

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(25)
left(90)

forward(50)
left(90)

forward(25)
left(90)

forward(25)
left(90)

forward(50)

exitonclick()
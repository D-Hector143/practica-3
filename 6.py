# Este programa hace un paisaje
# Hector Pinto Calle
# 1.0 26/04/2025

import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("midnight blue")

t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.hideturtle()

# luna

t.penup()
t.goto(-250, 150)
t.pendown()
t.color("light yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# estrellas
 
t.color("white")

estrellas = [
    (-250, 180), (-220, 140), (-190, 170), (-160, 130), 
    (-130, 190), (-100, 160), (-70, 200), (-40, 150),
    (0, 180), (30, 160), (60, 190), (90, 140), 
    (120, 200), (150, 170), (180, 190), (210, 130), 
    (240, 180), (270, 150)
]

for x, y in estrellas:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(2)
    t.end_fill()

# montañas

t.color("dim gray")
t.penup()
t.goto(-400, -100)
t.pendown()
t.begin_fill()
t.goto(-200, 100)
t.goto(0, -100)
t.goto(-400, -100)
t.end_fill()

t.color("slate gray")
t.penup()
t.goto(-200, -100)
t.pendown()
t.begin_fill()
t.goto(0, 120)
t.goto(200, -100)
t.goto(-200, -100)
t.end_fill()

# suelo

t.penup()
t.goto(-400, -100)
t.pendown()
t.color("forest green")
t.begin_fill()
t.forward(800)
t.left(90)
t.forward(100)
t.left(90)
t.forward(800)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

# arboles

# arbol 1
t.penup()
t.goto(-300, -100)
t.pendown()
t.color("saddle brown")
t.begin_fill()
t.forward(10)
t.left(90)
t.forward(30)
t.left(90)
t.forward(10)
t.left(90)
t.forward(30)
t.left(90)
t.end_fill()

t.penup()
t.goto(-310, -70)
t.pendown()
t.color("dark green")
t.begin_fill()
t.goto(-295, -30)
t.goto(-280, -70)
t.goto(-310, -70)
t.end_fill()

# arbol 2

t.penup()
t.goto(150, -100)
t.pendown()
t.color("saddle brown")
t.begin_fill()
t.forward(10)
t.left(90)
t.forward(30)
t.left(90)
t.forward(10)
t.left(90)
t.forward(30)
t.left(90)
t.end_fill()

t.penup()
t.goto(140, -70)
t.pendown()
t.color("dark green")
t.begin_fill()
t.goto(155, -30)
t.goto(170, -70)
t.goto(140, -70)
t.end_fill()

# casa

t.penup()
t.goto(-80, -100)
t.pendown()
t.color("firebrick")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-80, 0)
t.pendown()
t.color("maroon")
t.begin_fill()
t.goto(-30, 50)
t.goto(20, 0)
t.goto(-80, 0)
t.end_fill()

t.penup()
t.goto(-45, -100)
t.pendown()
t.color("sienna")
t.begin_fill()
t.forward(30)
t.left(90)
t.forward(50)
t.left(90)
t.forward(30)
t.left(90)
t.forward(50)
t.left(90)
t.end_fill()

t.penup()
t.goto(-70, -30)
t.pendown()
t.color("light blue")
t.begin_fill()
for _ in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()

turtle.done()

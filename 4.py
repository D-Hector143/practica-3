# Este programa dibuja las iniciales de mi nombre
# Hector Pinto Calle
# 1.0 26/04/2025


import turtle
v = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.pensize(4)

#Cuadro
tortuga.color("red")
tortuga.fillcolor("yellow")
tortuga.begin_fill()

tortuga.forward(300)
tortuga.left(90)
tortuga.forward(200)
tortuga.left(90)
tortuga.forward(300)
tortuga.left(90)
tortuga.forward(200)

tortuga.end_fill()

#H
tortuga.color("green")

tortuga.left(90)
tortuga.up()
tortuga.forward(50)
tortuga.left(90)
tortuga.forward(50)
tortuga.down()
tortuga.forward(100)
tortuga.left(180)
tortuga.forward(50)
tortuga.left(90)
tortuga.forward(50)
tortuga.left(90)
tortuga.forward(50)
tortuga.left(180)
tortuga.forward(100)

#P
tortuga.color("lime")
tortuga.left(90)
tortuga.forward(50)
tortuga.down()
tortuga.left(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(50)
tortuga.right(90)
tortuga.forward(50)
tortuga.right(90)
tortuga.forward(50)


v.exitonclick()

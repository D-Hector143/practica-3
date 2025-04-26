# Este programa dibuja un cuadro sin esquinas
# Hector Pinto Calle
# 1.0 26/04/2025

import turtle
v = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.pensize(10)

# abajo
tortuga.color("red")
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.fd(50)

# flecha
tortuga.left(135)
tortuga.forward(11.18)
tortuga.left(135)
tortuga.forward(15)
tortuga.left(135)
tortuga.forward(11.18)
tortuga.right(45)
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.left(90)

# derecha
tortuga.color("turquoise")
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.fd(50)

# flecha
tortuga.left(135)
tortuga.forward(11.18)
tortuga.left(135)
tortuga.forward(15)
tortuga.left(135)
tortuga.forward(11.18)
tortuga.right(45)
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.left(90)

# arria
tortuga.color("lime")
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.fd(50)

# flecha
tortuga.left(135)
tortuga.forward(11.18)
tortuga.left(135)
tortuga.forward(15)
tortuga.left(135)
tortuga.forward(11.18)
tortuga.right(45)
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.left(90)

# izquierda
tortuga.color("fuchsia")
tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.fd(50)

# flecha
tortuga.left(135)
tortuga.forward(11.18)
tortuga.left(135)
tortuga.forward(15)
tortuga.left(135)
tortuga.forward(11.18)
tortuga.right(45)

tortuga.up()
tortuga.forward(30)
tortuga.down()
tortuga.left(90)


v.exitonclick()

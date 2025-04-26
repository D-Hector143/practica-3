# Este programa dibuja un triangulo 
# Hector Pinto Calle
# 1.0 27/03/2025

import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("green")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(2)

tortuga.forward(100)
tortuga.left(110)
tortuga.forward(150)
tortuga.left(140)
tortuga.forward(150)

tortuga.hideturtle()
pantalla.mainloop()
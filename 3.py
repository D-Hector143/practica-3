# Este programa dibuja un circulo
# Hector Pinto Calle
# 1.0 26/04/2025

import turtle
import math

def dibujar_circulo(x, y, radio):
    tortuga.penup()
    tortuga.goto(x, y - radio)
    tortuga.pendown()
    tortuga.circle(radio)

x = float(input("Ingresa la coordenada x del centro del circulo: "))
y = float(input("Ingresa la coordenada y del centro del circulo: "))
radio = float(input("Ingresa el radio del circulo: "))

area = math.pi * radio**2
print(f"El área del círculo es: {area:.2f}")

# tortuga

pantalla = turtle.Screen()
pantalla.bgcolor("orange")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(2)

dibujar_circulo(x, y, radio)

tortuga.penup()
tortuga.goto(x, y - radio + 40.)
tortuga.write(f". {area:.2f}", align="center", font=("Arial", 10, "normal"))

tortuga.hideturtle()
pantalla.mainloop()

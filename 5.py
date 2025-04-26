# Este programa 
# Hector Pinto Calle
# 1.0 27/03/2025

import turtle

# Dibujar triangulo
pantalla = turtle.Screen()
pantalla.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(3)

tortuga.color("blue")
tortuga.fillcolor("blue")
tortuga.begin_fill()

tortuga.penup()  
tortuga.goto(-400, 0) 
tortuga.setheading(0)
tortuga.pendown()

tortuga.forward(100)
tortuga.left(110)
tortuga.forward(150)
tortuga.left(140)
tortuga.forward(150)

tortuga.end_fill()

# Dibujar Cuadro
pantalla = turtle.Screen()
pantalla.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(3)

tortuga.color("red")
tortuga.fillcolor("red")
tortuga.begin_fill()

lado = 100

tortuga.penup()  
tortuga.goto(-200, 0)
tortuga.setheading(0)
tortuga.pendown() 

for _ in range(4):
    tortuga.forward(lado)
    tortuga.left(90) 

tortuga.end_fill()

# Dibujar rectángulo
pantalla = turtle.Screen()
pantalla.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(3)

tortuga.color("yellow")
tortuga.fillcolor("yellow")
tortuga.begin_fill()

tortuga.penup()  
tortuga.goto(0, 0) 
tortuga.setheading(0)
tortuga.pendown()  

ancho = 200
altura = 100

for _ in range(2):
    tortuga.forward(ancho)  
    tortuga.left(90)        
    tortuga.forward(altura) 
    tortuga.left(90)

tortuga.end_fill()

# Dibujar circulo

pantalla = turtle.Screen()
pantalla.bgcolor("white")

tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(3)

tortuga.color("green")
tortuga.fillcolor("green")

tortuga.penup()
tortuga.goto(300, 0)
tortuga.setheading(0)
tortuga.pendown()

radio = 60

tortuga.begin_fill()
tortuga.circle(radio)
tortuga.end_fill()


# Dibujar rombo
pantalla = turtle.Screen()
pantalla.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(3)

tortuga.color("yellow")
tortuga.fillcolor("yellow")
tortuga.begin_fill()

tortuga.penup()  
tortuga.goto(-450, -200)
tortuga.setheading(0)
tortuga.pendown() 
tortuga.right(30)

lado = 100

for _ in range(4):
    tortuga.forward(lado)
    tortuga.left(90) 

tortuga.end_fill()

# Dibuja paralelogramo

pantalla = turtle.Screen()
pantalla.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(3)

tortuga.color("blue")
tortuga.fillcolor("blue")
tortuga.begin_fill()

tortuga.penup()  
tortuga.goto(-200, -100) 
tortuga.setheading(0) 
tortuga.pendown() 

lado_base = 140  
lado_altura = 160 
angulo = -50

tortuga.forward(lado_base)
tortuga.left(180 - angulo)
tortuga.forward(lado_altura)
tortuga.left(angulo)
tortuga.forward(lado_base)
tortuga.left(180 - angulo)
tortuga.forward(lado_altura)
tortuga.left(angulo)

tortuga.end_fill()

# Dibuja un trapesoide

ventana = turtle.Screen()
ventana.bgcolor("white")


t = turtle.Turtle()
t.shape("turtle")        
t.color("black")
t.fillcolor("green")     
t.pensize(1)             


t.penup()
t.goto(120, -130)
t.pendown()
t.begin_fill()

t.forward(50)
t.right(120)
t.forward(100)
t.right(60)
t.forward(90)
t.right(60)
t.forward(100)

t.right(120)

t.end_fill()


# Dibuja un obalo 

ventana = turtle.Screen()
ventana.bgcolor("white")

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.fillcolor("red")
t.pensize(1)

t.setheading(0)

t.penup()
t.goto(300, -220)
t.pendown()

t.begin_fill()

for _ in range(2):
    t.circle(80, 90)   
    t.circle(40, 90)   

t.end_fill()

# Finalizar
turtle.done()

tortuga.hideturtle()
pantalla.mainloop()
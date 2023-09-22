import math
import turtle

# Configuración inicial
turtle.setup(1000, 800)
turtle.bgcolor("pink")
turtle.shape("turtle")
turtle.speed(-100)
turtle.fillcolor("brown")

# Dibuja el tallo
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green")  # Cambia el color del tallo a verde
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()


# Código de la hoja 
turtle.penup()
turtle.goto(-20, -250)
turtle.setheading(1 * 137.508)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.right(10)
turtle.forward(70)
turtle.left(40)
turtle.forward(70)
turtle.left(140)
turtle.forward(70)
turtle.left(40)
turtle.forward(70)
turtle.end_fill()


# Código de la hoja 
turtle.penup()
turtle.goto(0, -200)
turtle.setheading(1 * 137.508)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
turtle.right(-80)
turtle.forward(-70)
turtle.left(-40)
turtle.forward(-70)
turtle.left(-140)
turtle.forward(-70)
turtle.left(-40)
turtle.forward(-70)
turtle.end_fill()

# Cambia el color del centro del girasol a café más claro (RGB: 139, 69, 19)
turtle.penup()
turtle.goto(0,-180)
turtle.fillcolor("#8B4513")  # Café más claro
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()
#este es un regalo para mi princesa usando lo que me gusta para dedicartelo
# Código del girasol (el que proporcionaste)
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()

# Escribe "Te Quiero" en la parte superior del girasol
turtle.penup()
turtle.goto(0, 200)  # Ajusta la posición vertical según sea necesario
turtle.color("Red")  # Color del texto
turtle.write("TE AMO MI PRINCESA", align="center", font=("Arial", 24, "bold"))


turtle.penup()
turtle.goto(0, -350)  # Ajusta la posición vertical según sea necesario
turtle.color("Red")  # Color del texto
turtle.write("YEANNELY CAROLINA 🐋", align="center", font=("Arial", 24, "bold"))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()

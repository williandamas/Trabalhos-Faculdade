# Bibliotecas
import turtle

#Variaveis
click = turtle.Screen()

#FUNÇÕES

# Aponta a Localização
def local(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

# Desenha Triangulo
def Triangulo():
    for i in range(3):
        turtle.delay(5)
        turtle.forward(100)
        turtle.left(120)
        
    
# Desenha Quadrado
def Quadrado():
    for i in range(4):
        turtle.delay(5)
        turtle.forward(100)
        turtle.right(90)

# Desenha Circulo
def Circulo():
    for i in range(0, 360):
        turtle.delay(1)
        turtle.forward(1)
        turtle.right(1)

#Chamadas
click.onkey(Quadrado,"B")
click.onkey(Triangulo,"A")
click.onkey(Circulo,"C")
click.listen()
click.onclick(local) 
click.mainloop() 


#Bibliotecas
import turtle

#Variáveis
click = turtle.Screen()

#Função do Exercício 1
def Triangulo(lado):
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)

#Função do Exercício 2
def Casa(lado):
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)

# Função do Exercício 3
def Triforce(lado):
    for i in range(lado):
        turtle.forward(200)
        turtle.left(120)
    for i in range(1):
        turtle.forward(100)
        turtle.left(30)
        turtle.left(30)
        turtle.forward(100)
    for i in range(2):
        turtle.left(120)
        turtle.forward(100)

# Função do Exercício 4
def Estrela():
    lado = 1
    while lado <= 5:
        turtle.forward(300)
        turtle.right(144)
        lado = lado + 1

# Função do Exercício 5
def  Poligono(n, lado):
    if n >= 3:
        for i in range(n):
            turtle.forward(lado)
            turtle.left(360/n)
    else:
        print(f'O número de lados deve ser maior que {n}')

# Função do Exercício 6
def Friso(n, lado):
    for i in range(n):
        for i in range(2):
            turtle.forward(lado)
            turtle.left(90)
        for i in range(1):
            turtle.left(180)
            turtle.forward(lado)
            turtle.right(90)
            turtle.forward(lado)
            turtle.left(90)

#Triangulo(70)                   # Passe um argumento (tamanho do lado)
#Casa(70)                        # Passe um argumento (tamanho do lado)
#Triforce(3)                     # Passe um argumento (lado)
#Estrela()                       # Não tem necessidade de argumento
#Poligono(8, 50)                 # Passe dois argumento (qtd de lados, tamanho dos lados)
#Friso(3,50)                      # Passe dois argumento (quantidade, tamanho dos lados)
click.exitonclick()






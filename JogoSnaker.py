# Bibliotecas e Pacotes
import turtle
import time
import random



# Variáveis (pontuação, velocidade e tamanaho)
velocidade = 0.1
pontos = 0
pontos_maximos = 0
tamanhos = []

# Tela de configurações
tc = turtle.Screen()
tc.title("Jogo da cobrinha")
tc.bgcolor('yellow')
tc.setup(width=600, height=600)
tc.tracer(0)

# Cobra
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("black")
cobra.penup()
cobra.goto(0, 0)
cobra.direcao = "stop"

# comida 
comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("red")
comida.penup()
comida.goto(0, 100)


# Placares
pl = turtle.Turtle()
pl.speed(0)
pl.shape("square")
pl.color = ("black")
pl.penup()
pl.hideturtle()
pl.goto(0, 260)
pl.write("Placar: 0    Placar Recorde: 0", align= "center", font=("ds-digital", 24, "normal"))

# Funções de direcionamento
def cima():
    if cobra.direcao != "down":
        cobra.direcao = "up"
def baixo():
    if cobra.direcao != "up":
        cobra.direcao = "down"
def esquerda():
    if cobra.direcao != "right":
        cobra.direcao = "left"
def direita():
    if cobra.direcao != "left":
        cobra.direcao = "right"
def move():
    if cobra.direcao == "up":
        y = cobra.ycor()
        cobra.sety(y + 20)
    if cobra.direcao == "down":
        y = cobra.ycor()
        cobra.sety(y - 20)
    if cobra.direcao == "left":
        x = cobra.xcor()
        cobra.setx(x - 20)
    if cobra.direcao == "right":
        x = cobra.xcor()
        cobra.setx(x + 20)

# teclas de controle
tc.listen()
tc.onkeypress(cima, "w")
tc.onkeypress(baixo, "s")
tc.onkeypress(esquerda, "a")
tc.onkeypress(direita, "d")

#  Logica do jogo
while True:
    tc.update()

    # verificar colisão com as bordas da área
    if cobra.xcor()>290 or cobra.xcor()<-290 or cobra.ycor()>290 or cobra.ycor()<-290:
        time.sleep(1)
        cobra.goto(0, 0)
        cobra.direcao = "stop"

        # Tamanho do corpo
        for tamanho in tamanhos:
            tamanho.goto(1000, 1000) #fora de alcance
        #limpar tamanhos
        tamanhos.clear()

        #resetar pontos
        pontos = 0

        #resetar velocidade
        velocidade = 0.1

        pl.clear()
        pl.write(f"Placar: {pontos}  Placar Recorde: {pontos_maximos}", align="center", font=("ds-digital", 24, "normal"))
    
    # velificar colisão com comida
    if cobra.distance(comida) <20:
        # mover a comida para lugar aleatório
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

        # add um novo tamanho na cobra
        novo_tamanho = turtle.Turtle()
        novo_tamanho.speed(0)
        novo_tamanho.shape("square")
        novo_tamanho.color("black")
        novo_tamanho.penup()
        tamanhos.append(novo_tamanho)

        # diminua o velocidade
        velocidade -= 0.001
        # aumenta os pontos em:
        pontos += 10

        if pontos > pontos_maximos:
            pontos_maximos = pontos
        pl.clear()
        pl.write(f"Placar: {pontos}    Placar Recorde: {pontos_maximos}", align="center", font=("ds-digital", 24, "normal"))
    
    # mover o tamanho em ordem reversa
    for index in range(len(tamanhos)-1, 0, -1):
        x = tamanhos[index-1].xcor()
        y = tamanhos[index-1].ycor()
        tamanhos[index].goto(x, y)
    # movimento do tamanho 0 da cobra
    if len(tamanhos)>0:
        x = cobra.xcor()
        y = cobra.ycor()
        tamanhos[0].goto(x, y)
    
    move()

    # colisão com o corpo
    for tamanho in tamanhos:
        if tamanho.distance(cobra) <20:
            time.sleep(1)
            cobra.goto(0, 0)
            cobra.direcao = "stop"

            # ocultar tamanhos
            for tamanho in tamanhos:
                tamanho.goto(1000, 1000)
            tamanhos.clear()
            pontos = 0
            velocidade = 0.1

            #atualize os pontos
            pl.clear()
            pl.write(f"Placar: {pontos}    Placar Recorde: {pontos_maximos}", align="center", font=("ds-digital", 24, "normal"))
    time.sleep(velocidade)
tc.mainloop()





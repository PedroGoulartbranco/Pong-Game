import pygame
from random import choice

pygame.init()
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando = True

gerar_bola = True

def recolocar_bola():
    cord_x, cord_y = (640, 360)
    return cord_x, cord_y

def lado_bola():
    direta_esqurda = ["direita", "esquerda"]
    direita_ou_esqurda = choice(direta_esqurda)
    diagonais = ["cima", "baixo", "reta"]
    direcao = choice(diagonais)

    if direita_ou_esqurda == "direita":
        velocidade_x = 5
    else:
        velocidade_x = -5
    
    if direcao == "cima":
        velocidade_y = -5
    elif direcao == "baixo":
        velocidade_y = 5
    else:
        velocidade_y = 0

    return velocidade_x, velocidade_y

def aleatorizar_velocidade_bate():
    lista_velocidade = [1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    velocidade_x = choice(lista_velocidade)
    velocidade_y = choice(lista_velocidade)
    return velocidade_x, velocidade_y
  


cordenada_x_bola = 0
coordenada_y_bola = 0
velocidade_bola_x = 10
velocidade_bola_y = 5

velocidade_jogadores = 7

jogador_1_coordenada_x = 15
jogador_1_coordenada_y = 290

jogador_2_coordenada_x = 1255
jogador_2_coordenada_y = 290

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill("white")

    pygame.draw.rect(tela, "black", (640, 0, 1, 720)) # Desenha uma linha reta

    pygame.draw.rect(tela, "black", (0, 0, 1, 720)) # Desenha uma linha reta

    pygame.draw.circle(tela, "black", (cordenada_x_bola, coordenada_y_bola), 25) #Circulo

    pygame.draw.rect(tela, "black", (jogador_1_coordenada_x, jogador_1_coordenada_y, 10, 120)) #Jogador 1 desenho

    pygame.draw.rect(tela, "black", (jogador_2_coordenada_x, jogador_2_coordenada_y, 10, 120)) #Jogador 2 desenho


    cordenada_x_bola += velocidade_bola_x
    coordenada_y_bola += velocidade_bola_y

    if gerar_bola:
        cordenada_x_bola, coordenada_y_bola = recolocar_bola()
        velocidade_bola_x, velocidade_bola_y = lado_bola()
        gerar_bola = False


    #Verificar se foi gol
    if cordenada_x_bola >= 1280:
        gerar_bola = True
    if cordenada_x_bola <= 0:
        gerar_bola = True

    #Verificar se bateu na parede
    if coordenada_y_bola >= 695 or coordenada_y_bola <= 25:
        multiplicador_vel_x, multiplicador_vel_y = aleatorizar_velocidade_bate()
        velocidade_bola_x *= (multiplicador_vel_x)
        velocidade_bola_y *= -(multiplicador_vel_y)
        print(velocidade_bola_x, velocidade_bola_y)

    if velocidade_bola_x >= 17:
        velocidade_bola_x = 10
    elif velocidade_bola_x <= -17:
        velocidade_bola_x = -10
    if velocidade_bola_y >= 17:
        velocidade_bola_x = 10
    elif velocidade_bola_y <= -17:
        velocidade_bola_y = -10

    #Teclado
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w]:
        jogador_1_coordenada_y -= velocidade_jogadores
    if tecla[pygame.K_s]:
        jogador_1_coordenada_y += velocidade_jogadores
    if tecla[pygame.K_UP]:
        jogador_2_coordenada_y -= velocidade_jogadores
    if tecla[pygame.K_DOWN]:
        jogador_2_coordenada_y += velocidade_jogadores

    #Limite dos jogadores
    if jogador_1_coordenada_y >= 600:
        jogador_1_coordenada_y = 600
    if jogador_1_coordenada_y <= 0:
        jogador_1_coordenada_y = 0
    
    if jogador_2_coordenada_y >= 600:
        jogador_2_coordenada_y = 600
    if jogador_2_coordenada_y <= 0:
        jogador_2_coordenada_y = 0

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
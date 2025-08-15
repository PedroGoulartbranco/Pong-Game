import pygame
from random import choice

pygame.init()
pygame.mixer.init() #Faz as musicas funcionarem
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando = True

pygame.display.set_caption("Pong Game") 

icone = pygame.image.load("imagens/bola.png")
pygame.display.set_icon(icone)

font_pontuacao = pygame.font.Font(None, 900)
font_botao = pygame.font.Font("fontes/PressStart2P-Regular.ttf", 25)

pontuacao_jogador_1 = 0
pontuacao_jogador_2 = 0

pygame.mixer.music.load("audio/musica.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

som_gol = pygame.mixer.Sound("audio/gol.mp3")
som_gol.set_volume(0.5)

bola = pygame.image.load("imagens/bola.png").convert_alpha()
bola_parte_visivel = bola.get_bounding_rect()
bola = bola.subsurface(bola_parte_visivel).copy()
bola= pygame.transform.scale(bola, (50, 50))

botao_R = pygame.image.load("imagens/R.png").convert_alpha()
botao_R_visivel= botao_R.get_bounding_rect()
botao_R = botao_R.subsurface(botao_R_visivel).copy()
botao_R = pygame.transform.scale(botao_R, (100, 100))

botao_Z = pygame.image.load("imagens/Z.png").convert_alpha()
botao_Z_visivel= botao_Z.get_bounding_rect()
botao_Z= botao_Z.subsurface(botao_R_visivel).copy()
botao_Z= pygame.transform.scale(botao_Z, (100, 100))

coordenada_botao_R = (300, 250)
coordenada_botao_Z = (300, 450)

fundo = pygame.image.load("imagens/gramado.png")
fundo = pygame.transform.scale(fundo, (1280, 720))

def recolocar_bola():
    cord_x, cord_y = (640, 360)
    return cord_x, cord_y

def lado_bola():
    direta_esqurda = ["direita", "esquerda"]
    direita_ou_esqurda = choice(direta_esqurda)
    diagonais = ["cima", "baixo"]
    direcao = choice(diagonais)

    if direita_ou_esqurda == "direita":
        velocidade_x = 5
    else:
        velocidade_x = -5
    
    if direcao == "cima":
        velocidade_y = -5
    elif direcao == "baixo":
        velocidade_y = 5

    return velocidade_x, velocidade_y

def aleatorizar_velocidade_bate():
    lista_velocidade = [1, 1.2, 1.3]
    velocidade_x = choice(lista_velocidade)
    velocidade_y = choice(lista_velocidade)
    return velocidade_x, velocidade_y

def gerar_bola(cordenada_x_bola, coordenada_y_bola):
    cordenada_x_bola, coordenada_y_bola = recolocar_bola()
    velocidade_bola_x, velocidade_bola_y = lado_bola()
    return cordenada_x_bola, coordenada_y_bola, velocidade_bola_x, velocidade_bola_y
  
coordenada_pont_jogador_1 = (150, 100)
coordenada_pont_jogador_2 = (800, 100)

cordenada_x_bola = 0
coordenada_y_bola = 0
velocidade_bola_x = 12
velocidade_bola_y = 8

velocidade_jogadores = 7

jogador_1_coordenada_x = 15
jogador_1_coordenada_y = 290

jogador_2_coordenada_x = 1255
jogador_2_coordenada_y = 290

tem_que_gerar_bola = True

partida_rodando = True

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    if partida_rodando:

        tela.blit(fundo, (0, 0))

        pygame.draw.rect(tela, "black", (640, 0, 1, 720)) # Desenha uma linha reta

        pygame.draw.rect(tela, "black", (0, 0, 1, 720)) # Desenha uma linha reta

        if tem_que_gerar_bola:
            cordenada_x_bola, coordenada_y_bola, velocidade_bola_x, velocidade_bola_y = gerar_bola(cordenada_x_bola, coordenada_y_bola)
            tem_que_gerar_bola = False

        pygame.draw.rect(tela, "black", (jogador_1_coordenada_x, jogador_1_coordenada_y, 10, 120)) #Jogador 1 desenho

        pygame.draw.rect(tela, "black", (jogador_2_coordenada_x, jogador_2_coordenada_y, 10, 120)) #Jogador 2 desenho

        jogador_1_colisao = pygame.Rect(jogador_1_coordenada_x, jogador_1_coordenada_y, 10, 120)
        jogador_2_colisao = pygame.Rect(jogador_2_coordenada_x, jogador_2_coordenada_y, 10, 120)


        cordenada_x_bola += velocidade_bola_x
        coordenada_y_bola += velocidade_bola_y

        colisao_bola = pygame.Rect(cordenada_x_bola, coordenada_y_bola, bola.get_width(), bola.get_height())

        #Verificar se foi gol
        if cordenada_x_bola >= 1280:
            pontuacao_jogador_1 += 1
            som_gol.play()
            cordenada_x_bola, coordenada_y_bola = recolocar_bola()
            velocidade_bola_x, velocidade_bola_y = lado_bola()
            continue
        elif cordenada_x_bola <= 0:
            pontuacao_jogador_2 += 1
            som_gol.play()
            cordenada_x_bola, coordenada_y_bola = recolocar_bola()
            velocidade_bola_x, velocidade_bola_y = lado_bola()
            continue
        else:
            #Verificar se colide com os jogadores
            if jogador_1_colisao.colliderect(colisao_bola):
                multiplicador_vel_x, multiplicador_vel_y = aleatorizar_velocidade_bate()
                velocidade_bola_x *= -(multiplicador_vel_x)
                cordenada_x_bola  = jogador_1_coordenada_x + 10
        
            if jogador_2_colisao.colliderect(colisao_bola):
                multiplicador_vel_x, multiplicador_vel_y = aleatorizar_velocidade_bate()
                velocidade_bola_x *= -(multiplicador_vel_x)
                cordenada_x_bola = jogador_2_coordenada_x - bola.get_width()

        if velocidade_bola_x >= 15:
            velocidade_bola_x = 11
        elif velocidade_bola_x <= -15:
            velocidade_bola_x = -11
        if velocidade_bola_y >= 15:
            velocidade_bola_y = 11
        elif velocidade_bola_y <= -15:
            velocidade_bola_y = -11

        #Verificar se bateu na parede
        if coordenada_y_bola >= 695 or coordenada_y_bola <= 0:
            multiplicador_vel_x, multiplicador_vel_y = aleatorizar_velocidade_bate()
            

            velocidade_bola_y *= -(multiplicador_vel_y)
            print(velocidade_bola_x, velocidade_bola_y)


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


            
        pontuacao_string_jogador_1 = str(pontuacao_jogador_1)
        pontuacao_string_jogador_2 = str(pontuacao_jogador_2)

        converter_jogador_1 = font_pontuacao.render(pontuacao_string_jogador_1, True, "#666666")
        converter_jogador_2 = font_pontuacao.render(pontuacao_string_jogador_2, True, "#666666")

        converter_jogador_1.set_alpha(128)
        converter_jogador_2.set_alpha(128)

        tela.blit(converter_jogador_1, coordenada_pont_jogador_1)
        tela.blit(converter_jogador_2, coordenada_pont_jogador_2)

        tela.blit(bola, (cordenada_x_bola, coordenada_y_bola))

        if pontuacao_jogador_1 == 3 or pontuacao_jogador_2 == 3:
            pontuacao_jogador_1 = 0
            pontuacao_jogador_2 = 0
            partida_rodando = False
    else:
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_r]:
            partida_rodando = True
        if tecla[pygame.K_z]:
            rodando = False
        tela.blit(botao_R, coordenada_botao_R)
        tela.blit(botao_Z, coordenada_botao_Z)

        texto_r = "Aperte R para uma nova partida"
        texto_z = "Aperte Z para sair"

        coordenada_texto_r = (420, 300)
        coordenada_texto_z = (420, 500)

        converter_texto_r = font_botao.render(texto_r, True, "white")
        converter_texto_z = font_botao.render(texto_z, True, "white")

        tela.blit(converter_texto_r, coordenada_texto_r)
        tela.blit(converter_texto_z, coordenada_texto_z)

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
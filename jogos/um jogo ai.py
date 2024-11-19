import pygame
 
# iniciando o pygame

pygame.init()

tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("brick breaker")

tamanho_bola = 20
bola = pygame.Rect(100,500,tamanho_bola,tamanho_bola)

tamanho_jogador = 100
jogador = pygame.Rect(0,730,tamanho_jogador,30)


blocos_col = 5
blocos_lin = 8
blocos_total = blocos_col * blocos_lin

def criar_blocos(blocos_col,blocos_lin):
    blocos = []
    return blocos

cores = {
    "branco": (255,255,255),
    "preto": (0,0,0),
    "azul": (0,0,255),
    "verde": (0,255,0),
    "vermelho": (255,0,0),
    "amarelo": (255,255,0)
}

fim_jogo = False
pontuação = 0
movimento_bola = [1,1]
# funções


# loop
tela.fill(cores["branco"])

pygame.draw.rect(tela, cores["azul"],jogador)
pygame.draw.rect(tela, cores["amarelo"],bola)

while fim_jogo == False:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT():
            fim_jogo = True



    pygame.time.wait(1)
    pygame.display.flip()

quit()
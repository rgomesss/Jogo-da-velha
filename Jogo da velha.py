import pygame

# Inicialização do Pygame
pygame.init()

# Definição das cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Definição das dimensões da janela do jogo
largura_janela = 400
altura_janela = 400
tamanho_quadrado = largura_janela // 3

# Criação da janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo da Velha")

# Matriz para representar o tabuleiro
tabuleiro = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# Variável para controlar o jogador atual
jogador_atual = 1

# Função para desenhar o tabuleiro na janela
def desenhar_tabuleiro():
    janela.fill(BRANCO)
    pygame.draw.line(janela, PRETO, (0, tamanho_quadrado), (largura_janela, tamanho_quadrado), 5)
    pygame.draw.line(janela, PRETO, (0, 2 * tamanho_quadrado), (largura_janela, 2 * tamanho_quadrado), 5)
    pygame.draw.line(janela, PRETO, (tamanho_quadrado, 0), (tamanho_quadrado, altura_janela), 5)
    pygame.draw.line(janela, PRETO, (2 * tamanho_quadrado, 0), (2 * tamanho_quadrado, altura_janela), 5)
    
    for linha in range(3):
        for coluna in range(3):
            jogador = tabuleiro[linha][coluna]
            if jogador == 1:
                pygame.draw.line(janela, PRETO, (coluna * tamanho_quadrado + 15, linha * tamanho_quadrado + 15), 
                                 ((coluna + 1) * tamanho_quadrado - 15, (linha + 1) * tamanho_quadrado - 15), 5)
                pygame.draw.line(janela, PRETO, ((coluna + 1) * tamanho_quadrado - 15, linha * tamanho_quadrado + 15),
                                 (coluna * tamanho_quadrado + 15, (linha + 1) * tamanho_quadrado - 15), 5)
            elif jogador == -1:
                pygame.draw.circle(janela, PRETO, (coluna * tamanho_quadrado + tamanho_quadrado // 2,
                                                   linha * tamanho_quadrado + tamanho_quadrado // 2), tamanho_quadrado // 2 - 15, 5)

# Função para verificar se há um vencedor
def verificar_vencedor():
    # Verificar linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != 0:
            return tabuleiro[linha][0]
    
    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != 0:
            return tabuleiro[0][coluna]
    
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 0:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 0:
        return tabuleiro[0][2]
    
    # Verificar empate
    empate = True
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == 0:
                empate = False
                break
    if empate:
        return 0
    
    return None

# Função principal do jogo
def game():
    # Variável para controlar o jogador atual
    jogador_atual = 1

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
            if event.type == pygame.MOUSEBUTTONDOWN and not verificar_vencedor():
                # Obter a posição do clique do mouse
                pos = pygame.mouse.get_pos()
                coluna = pos[0] // tamanho_quadrado
                linha = pos[1] // tamanho_quadrado
                
                # Verificar se a posição está vazia
                if tabuleiro[linha][coluna] == 0:
                    tabuleiro[linha][coluna] = jogador_atual
                    
                    # Alternar o jogador atual
                    jogador_atual *= -1

        # Desenhar o tabuleiro na janela
        desenhar_tabuleiro()
        
        # Verificar se há um vencedor
        vencedor = verificar_vencedor()
        if vencedor is not None:
            if vencedor == 0:
                mensagem = "Empate!"
            else:
                mensagem = f"Jogador {vencedor} venceu!"
            
            fonte = pygame.font.Font(None, 36)
            texto = fonte.render(mensagem, True, PRETO)
            janela.blit(texto, (largura_janela // 2 - texto.get_width() // 2, altura_janela // 2 - texto.get_height() // 2))
        
        # Atualizar a janela
        pygame.display.flip()

# Função de menu
def menu():
    continuar = True
    while continuar:
        continuar = int(input("\nSEJA BEM VINDO AO JOGO DA VELHA!\nEscolha uma opção desejada:\n0. Sair\n1. Jogar novamente\n"))
        if continuar == 1:
            # Limpar o tabuleiro
            for linha in range(3):
                for coluna in range(3):
                    tabuleiro[linha][coluna] = 0
            
            # Iniciar o jogo
            game()
        else:
            print("Saindo...")

# Executar o menu
menu()


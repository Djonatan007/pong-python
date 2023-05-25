# Ping Pong com Pygames

### - Exemplo de como o jogo fica ao final do desenvolvimento.
<img type="gif" src="audios\Ping-Pong.gif">

### - Criar um executável
```python
# Instalar o pacote pyInstaller
pyinstaller --onefile ping-pong.py
```

# Set das variáveis
```python
import pygame
from pygame import mixer
import sys

Para iniciar, deve ser feito o init dos pacotes abaixo:

  pygame.init()
  mixer.init()

Em resumo, essas duas linhas de código são utilizadas no início do programa que utiliza a biblioteca Pygame e a funcionalidade de reprodução de áudio do Mixer. Elas configuram o ambiente necessário para o desenvolvimento do jogo, incluindo o gerenciamento de janelas, eventos, gráficos e áudio.

Depois será necessário configurar os aspectos especificos do jogo:

  SCREEN_WIDTH = 800
  SCREEN_HEIGHT = 600
  PADDLE_WIDTH = 10
  PADDLE_HEIGHT = 60
  BALL_SIZE = 10
  PADDLE_SPEED = 4
  BALL_SPEED = 5

Essas constantes são utilizadas para configurar o tamanho e o comportamento de elementos-chave do jogo, como a tela, raquetes e bola. Ao definir essas constantes, o programador pode facilmente ajustar esses valores em um único lugar para personalizar o jogo ou aplicativo de acordo com suas necessidades.

E abaixo será necessário realizar algumas outras configurações como, estilo de fonte, cores, e sons que serão utilizados no jogo:

  WHITE = (255,255,255)
  BLACK = (0,0,0)
  font_file = "C:\Windows\Fonts\GARA.TTF"
  font = pygame.font.Font(font_file, 36)
  score_a = 0
  score_b = 0

  mixer.music.load("C:/Users/djona/Desktop/pong/audios/music_game.mp3")
  mixer.music.set_volume(0.3)
  collision_sound_A = mixer.Sound("C:/Users/djona/Desktop/pong/audios/Sound_A.wav")
  collision_sound_B = mixer.Sound("C:/Users/djona/Desktop/pong/audios/Sound_B.wav")
  point_sound = mixer.Sound("C:/Users/djona/Desktop/pong/audios/hoohooo.wav")

  mixer.music.play(-1) # Reproduz música ou som escolhido em um loop infinito
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Cria uma janela de exibição com largura e altura definidas
  pygame.display.set_caption("Pong") # Define o título da janela do jogo como "Pong"

# O código abaixo cria objetos retangulares para representar as raquetes (paddle_a e paddle_b) e a bola (ball) no nosso jogo. Além disso, é definido as velocidades iniciais da bola (ball_dx e ball_dy) com base na constante BALL_SPEED
  paddle_a = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
  paddle_b = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
  ball =  pygame.Rect(SCREEN_WIDTH //2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
  ball_dx, ball_dy = BALL_SPEED, BALL_SPEED
```

# Renderização do Menu

```python
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Renderização do menu principal
        screen.fill(BLACK)
        title_font = pygame.font.Font(font_file, 36)  # Configuração da Fonte
        title_text = title_font.render("Pong", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))

        screen.blit(title_text, title_rect) # Desenha o texto escolhido na posição definida pelo retângulo na tela do jogo

        title_font = pygame.font.Font(font_file, 16)
        current_time = pygame.time.get_ticks() # Obtém o tempo decorrido em milissegundos desde o início do programa. A variável current_time armazena esse valor, que pode ser usado para medir a passagem do tempo, controlar animações, temporizadores ou eventos baseados no tempo no jogo ou aplicativo

        if current_time % 2000 < 1000:
            title_text1 = title_font.render("Pressione espaço para iniciar", True, WHITE)
            title_rect1 = title_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4 + 60)) # Cria um objeto retangular que contém um texto e define sua posição na tela
            screen.blit(title_text1, title_rect1) # Desenha o texto escolhido na posição definida pelo retângulo na tela do jogo
        
        pygame.display.flip()
```

#### Explicação da Estrutura a seguir:

```python
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
```
<blockquote style="background-color: #E6F0F7;">

Trata-se de uma estrutura práticada por desenvolvedores de jogos utilizando essa biblioteca.

A estrutura envolve a criação de um loop principal *(while True)* que continua executando indefinidamente até que uma condição de término seja encontrada. Dentro desse loop principal, os eventos são verificados em um loop *for* para capturar as interações do jogador, como o fechamento da janela ou pressionar teclas específicas.

</blockquote>

<blockquote style="background-color: #E6F0F7;">

Podemos ver que esse bloco funciona da seguinte forma:

```python
current_time = pygame.time.get_ticks()
```
A função é chamada para obter o tempo em milissegundos desde que o jogo começou.

```python
if current_time % 2000 < 1000:
```
O trecho de código verifica se o resto da divisão da variável *current_time* por 2000 é menor que 1000. Se essa condição for verdadeira, significa que *current_time* está dentro do intervalo de 0 a 999 milissegundos após cada múltiplo de 2000 milissegundos. Essa verificação é usada para criar um efeito piscante.

Por exemplo, se *current_time* for 2500, o resto da divisão por 2000 é 500. Como 500 é menor que 1000, a condição é verdadeira e o código dentro do bloco if será executado. Isso resultará na renderização do texto desejado. Esse efeito piscante é criado porque o texto só será mostrado durante a primeira metade do intervalo de 2000 milissegundos.

</blockquote>

# Game

```python
def game_loop():
    global ball_dx, ball_dy, score_a, score_b, ball # Define as variáveis como globais. Essas variáveis podem ser acessadas e modificadas em qualquer parte do programa

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(BLACK) 
        pygame.draw.rect(screen, WHITE, paddle_a)
        pygame.draw.rect(screen, WHITE, paddle_b)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Obtém o estado atual do teclado no momento em que é executado
        keys = pygame.key.get_pressed()

        #Movimento Vertical Raquete A
        if keys[pygame.K_w] and paddle_a.top > 0:
            paddle_a.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_a.bottom < SCREEN_HEIGHT:
            paddle_a.y += PADDLE_SPEED

        #Movimento Vertical Raquete B
        if keys[pygame.K_UP] and paddle_b.top > 0:
            paddle_b.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_b.bottom < SCREEN_HEIGHT:
            paddle_b.y += PADDLE_SPEED

        #Movimento Horizontal Raquete A
        if keys[pygame.K_a] and paddle_a.left > 0:
            paddle_a.x -= PADDLE_SPEED
        if keys[pygame.K_d] and paddle_a.right < SCREEN_WIDTH // 2 - 70:
            paddle_a.x += PADDLE_SPEED

        #Movimento Horizontal Raquete B
        if keys[pygame.K_UP] and paddle_b.left > 0:
            paddle_b.x -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_b.right < SCREEN_WIDTH // 2 - 70:
            paddle_b.x += PADDLE_SPEED
      
        # Atualização da posição da bola
        ball.x += ball_dx
        ball.y += ball_dy


        if ball.colliderect(paddle_a):
            ball.left = paddle_a.right
            ball_dx = -ball_dx
            collision_sound_A.play()

        elif ball.colliderect(paddle_b):
            ball.right = paddle_b.left
            ball_dx = -ball_dx
            collision_sound_B.play()

       if ball.colliderect(paddle_a):
            ball.bottom = paddle_a.top
            ball_dx = -ball_dx
            collision_sound_A.play()

        elif ball.colliderect(paddle_b):
            ball.top = paddle_b.bottom
            ball_dx = -ball_dx
            collision_sound_B.play()


        #Bola quando bate na extremidade da tela
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_dy = -ball_dy

        #Ponto para o Time B
        if ball.left <= 0:
            score_b += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            point_sound.play()

            if score_b == 10: # Quando o placar alcançar a 10 então ele chama um método de finalização da partida
                end_game(False)

        #Ponto para o Time A
        elif ball.right >= SCREEN_WIDTH:
            score_a += 1
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_dx = -ball_dx
            point_sound.play()
            # print(score_a)
            if score_a == 10: # Quando o placar alcançar a 10 então ele chama um método de finalização da partida
                end_game(True)

        # Placar na Tela
        score_text = font.render(f"{score_a}  {score_b}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
        screen.blit(score_text, score_rect)

        # Atualizar a tela
        pygame.display.flip()

        # Controlar FPS
        clock = pygame.time.Clock()
        clock.tick(60)
```

#Fim de Jogo

```python
def end_game(winner): 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

       
        mixer.music.stop()
        screen.fill(BLACK)
        # Se a variavel Winner que vem por parâmetro do método end_game vier verdadeira, significa que o Jogador 2 ganhou e se vier falsa, o jogador 1 ganhou
        if winner:
            winner_text = "Player 2 Wins!"
        else:
            winner_text = "Player 1 Wins!"

        # Renderização da tela de fim de jogo
        winner_font = pygame.font.Font(font_file, 36)
        winner_render = winner_font.render(winner_text, True, WHITE)
        winner_rect = winner_render.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(winner_render, winner_rect)
        pygame.display.flip()
```

# Reiniciando o Jogo
```python
def reset_game():
    global paddle_a, paddle_b, ball, ball_dx, ball_dy, score_a, score_b # Define as variaveis como global e elas podem ser utilizadas em qualquer local do código

    paddle_a = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_b = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_dx, ball_dy = BALL_SPEED, BALL_SPEED
    score_a, score_b = 0, 0
```
O código apresentado define uma função chamada reset_game() que é responsável por reiniciar as variáveis relacionadas ao jogo Pong.

- FSM

<img type="img" src="audios\fsm.jpg">





import sys

import pygame

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255,255,255)
BLACK = (0,0,0)
font_file = "C:\Windows\Fonts\8514fix.fon"
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#running  = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # running = False


    #GAME
    screen.fill(BLACK)
    title_font = pygame.font.Font(font_file, 36)
    title_text = title_font.render("Dj pong", True, WHITE)
    title_rect = title_text.get_rect (center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(title_text, title_rect)

    pygame.display.flip()






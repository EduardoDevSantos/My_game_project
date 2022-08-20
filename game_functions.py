import sys
import pygame
def check_events():
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen(ai_settings, screen, sprite):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    sprite.blitme()
    # Deixa a tela mais recente visivel
    pygame.display.flip()
    
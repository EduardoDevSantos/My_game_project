from settings import Settings
from sprite import Sprite
import game_functions as gf
import pygame
def run_game():
    ai_settings = Settings()
    # Seta o tamanho da tela
    screen = pygame.display.set_mode((ai_settings.screen_widht,
    ai_settings.screen_height))
    pygame.display.set_caption("Mario doidão")
    sprite = Sprite(screen)
    # Seta a cor de fundo
    # Inicia o laço de repetição principal
    while True:
        gf.check_events()
        # Mantém a tela mais recente visível
        gf.update_screen(ai_settings, screen, sprite)
        
run_game()
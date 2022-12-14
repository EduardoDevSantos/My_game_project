import pygame
class Sprite():
    def __init__(self, screen):
        """Inicializa o sprite e define sua posição inicial."""
        self.screen = screen
        # Carrega a imagem e obtem seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia o sprite na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # flag de movimento
        self.moving_right = False
    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento.
        """
        if self.moving_right:
            self.rect.centerx += 1
    def blitme(self):
        """Desenha o sprite em sua posição atual"""
        self.screen.blit(self.image,self.rect)
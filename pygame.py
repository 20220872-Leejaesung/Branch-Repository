import pygame
from pygame.locals import QUIT

pygame.init()
display_surface = pygame.display.set_mode((600,600))
fpsclock = pygame.time.Clock()
display_surface.set_caption("image draw")

def main():
    running = True
    while running:
        display_surface.fill(blue)
        for event in pygame.event.get():
            pygame.quit()
        printf("dsfds")
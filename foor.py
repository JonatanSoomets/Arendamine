'''Jonatan Soomets'''

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Foor – Jonatan Soomets")

MUST = (0, 0, 0)
VALGE = (255, 255, 255)
PUNANE = (255, 0, 0)
KOLLANE = (255, 255, 0)
ROHELINE = (0, 255, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(MUST)

    # Kast
    pygame.draw.rect(screen, VALGE, (100, 20, 100, 260), 2)

    # Punane tuli
    pygame.draw.circle(screen, PUNANE, (150, 75), 35)

    # Kollane tuli
    pygame.draw.circle(screen, KOLLANE, (150, 150), 35)

    # Roheline tuli
    pygame.draw.circle(screen, ROHELINE, (150, 225), 35)

    pygame.display.flip()
    clock.tick(60)
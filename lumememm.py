'''Jonatan Soomets'''

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumememm – Jonatan Soomets")

# Värvid
TAEVAS = (135, 206, 235)
VALGE = (255, 255, 255)
MUST = (20, 20, 20)
ORANZ = (255, 140, 0)
PUNANE = (200, 30, 30)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(MUST)

    # Keha osad
    pygame.draw.circle(screen, VALGE, (150, 230), 65)
    pygame.draw.circle(screen, VALGE, (150, 140), 45)
    pygame.draw.circle(screen, VALGE, (150, 65), 32)

    # Silmad
    pygame.draw.circle(screen, MUST, (141, 57), 5)
    pygame.draw.circle(screen, MUST, (159, 57), 5)

    # Nina
    pygame.draw.polygon(screen, PUNANE, [(150, 80), (143, 63), (157, 63)])

    pygame.display.flip()
    clock.tick(60)
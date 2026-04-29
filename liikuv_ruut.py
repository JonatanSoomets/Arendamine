'''Jonatan Soomets'''

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Liikuv ruut - Jonatan Soomets")

MUST = (0, 0, 0)
VALGE = (255, 255, 255)

x = WIDTH // 2
y = HEIGHT // 2
RUUT = 50
KIIRUS = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Nooleklahvid
    klahvid = pygame.key.get_pressed()
    if klahvid[pygame.K_LEFT]:  x -= KIIRUS
    if klahvid[pygame.K_RIGHT]: x += KIIRUS
    if klahvid[pygame.K_UP]:    y -= KIIRUS
    if klahvid[pygame.K_DOWN]:  y += KIIRUS

    screen.fill(VALGE)

    # Ruut
    pygame.draw.rect(screen, MUST, (x, y, RUUT, RUUT))

    pygame.display.flip()
    clock.tick(60)

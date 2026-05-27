'''Jonatan Soomets'''

import pygame
import sys

pygame.init()

# ekraan
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("yl 2")
# pildid
bg = pygame.image.load("bg_shop.jpg")
bg = pygame.transform.smoothscale(bg, (640, 480))#taust

müüja = pygame.image.load("seller.png")
müüja = pygame.transform.smoothscale(müüja, (260, 310))  # müüja

vestlus = pygame.image.load("chat.png")
vestlus = pygame.transform.smoothscale(vestlus, (252, 200))  # vestlus

# Teksti funktsioonid
font = pygame.font.SysFont("arial", 28)
tekst = font.render("Tere, mina olen Jonatan Soomets", True, (255, 255, 255))

# loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Taustapilt
    screen.blit(bg, (0, 0))

    # Poemüüa
    screen.blit(müüja, (105, 155))

    # Rääkimis kast
    screen.blit(vestlus, (250, 65))

    # Tekst
    screen.blit(tekst, (290, 145))

    pygame.display.flip()
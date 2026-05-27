'''Jonatan Soomets'''

import pygame
import sys
import math

pygame.init()

# Ekraani seadistus
ekraan = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ülesanne 2")

# Piltide laadimine ja skaleerimine
def lae_pilt(fail, suurus):
    pilt = pygame.image.load(fail)
    return pygame.transform.smoothscale(pilt, suurus)

taust = lae_pilt("bg_shop.jpg", (640, 480))  # taust
muüja = lae_pilt("seller.png", (260, 310))   # poemüüja
jutumull = lae_pilt("chat.png", (252, 200))  # jutumull

# Teksti seadistus
font = pygame.font.SysFont("arial", 20)
tekst = font.render("Tere, olen Jonatan Soomets", True, (255, 255, 255))

logo = lae_pilt("VIKK logo.png", (280, 70))
mõõk = lae_pilt("mook.png", (120, 160)) 
tort = lae_pilt("cake.png", (120, 120)) 

# Kaare teksti seadistus
font3 = pygame.font.SysFont("arial", 22, bold=True)
kaare_tekst = "0502 KIVELUT"

# Kaare seadistus
kesk_x, kesk_y = 240, 10
raadius = 100
algus_nurk = 0.1

# Põhitsükkel
while True:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Taust
    ekraan.blit(taust, (0, 0))
    # Müüja
    ekraan.blit(muüja, (105, 155))
    # Jutumull
    ekraan.blit(jutumull, (250, 65))
    # Tekst jutumulli sisse
    ekraan.blit(tekst, (280, 145))
    # Logo
    ekraan.blit(logo, (25, 10))

    # Kaare teksti joonistamine
    for i, täht in enumerate(kaare_tekst):
        nurk = algus_nurk + i * 0.13
        x = kesk_x + raadius * math.cos(nurk)
        y = kesk_y + raadius * math.sin(nurk)
        täht_pind = font3.render(täht, True, (0, 150, 200))
        täht_pind = pygame.transform.rotate(täht_pind, -math.degrees(nurk) + 90)
        ristkülik = täht_pind.get_rect(center=(x, y))
        ekraan.blit(täht_pind, ristkülik)

    # Mõõk
    ekraan.blit(mõõk, (510, 140))
    # Tort
    ekraan.blit(tort, (400, 200))

    pygame.display.flip()
'''Jonatan Soomets'''

import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rally – Jonatan Soomets")

# Värvid
VALGE = (255, 255, 255)
MUST = (0, 0, 0)

# Pildid
bg = pygame.image.load("bg_rally.jpg")
bg = pygame.transform.smoothscale(bg, (WIDTH, HEIGHT))

punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

# Punane auto – ekraani alla keskele
punane_x = WIDTH // 2 - punane_auto.get_width() // 2
punane_y = HEIGHT - punane_auto.get_height() - 10

# Tee vahemik
tee_vasak = 150
tee_parem = 490

# Sinised autod [x, y, kiirus]
autod = []
for i in range(5):
    x = random.randint(tee_vasak, tee_parem - sinine_auto.get_width())
    y = random.randint(-300, -50)
    kiirus = random.randint(3, 7)
    autod.append([x, y, kiirus])

# Skoor ja font
skoor = 0
font = pygame.font.SysFont("arial", 28, bold=True)

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Taust
    screen.blit(bg, (0, 0))

    # Punane auto
    screen.blit(punane_auto, (punane_x, punane_y))

    # Sinised autod
    for i in range(len(autod)):
        screen.blit(sinine_auto, (autod[i][0], autod[i][1]))
        autod[i][1] += autod[i][2]

        # Kui auto jõuab alla, alustab uuesti ülevalt
        if autod[i][1] > HEIGHT:
            skoor += 10
            autod[i][1] = random.randint(-300, -50)
            autod[i][0] = random.randint(tee_vasak, tee_parem - sinine_auto.get_width())
            autod[i][2] = random.randint(3, 7)

    # Skoor
    skoor_tekst = font.render("Skoor: " + str(skoor), True, VALGE, MUST)
    screen.blit(skoor_tekst, (10, 10))

    pygame.display.flip()
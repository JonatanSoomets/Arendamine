'''Jonatan Soomets'''

import pygame, sys, math

pygame.init()

WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumemees – Jonatan Soomets")

TAEVAS = (135, 206, 235);
VALGE = (255, 255, 255);
MUST = (20, 20, 20)
PUNANE = (200, 30, 30);
KOLLANE = (255, 220, 0);
PRUUN = (101, 67, 33)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(TAEVAS)

    # Päike
    px, py = 255, 38
    pygame.draw.circle(screen, KOLLANE, (px, py), 20)
    for i in range(8):
        a = math.radians(i * 45)
        pygame.draw.line(screen, KOLLANE,
                         (int(px + 23 * math.cos(a)), int(py + 23 * math.sin(a))),
                         (int(px + 33 * math.cos(a)), int(py + 33 * math.sin(a))), 3)


    # 3 Pilve
    def cloud(cx, cy, s=1.0):
        for dx, dy, r in [(-18, 4, 13), (0, 0, 16), (18, 4, 13), (0, 10, 13)]:
            pygame.draw.circle(screen, VALGE, (cx + int(dx * s), cy + int(dy * s)), int(r * s))


    cloud(55, 30, 1.0)
    cloud(145, 18, 0.85)
    cloud(203, 52, 0.75)

    # Kehad
    pygame.draw.circle(screen, VALGE, (150, 228), 62)
    pygame.draw.circle(screen, VALGE, (150, 145), 44)
    pygame.draw.circle(screen, VALGE, (150, 72), 30)

    # Kübar
    pygame.draw.rect(screen, MUST, (126, 41, 48, 5))
    pygame.draw.rect(screen, MUST, (134, 14, 32, 30))

    # Silmad
    pygame.draw.circle(screen, MUST, (142, 65), 5)
    pygame.draw.circle(screen, MUST, (158, 65), 5)

    # Nina
    pygame.draw.polygon(screen, PUNANE, [(150, 86), (143, 72), (157, 72)])

    # Nööbid
    pygame.draw.circle(screen, MUST, (150, 130), 5)
    pygame.draw.circle(screen, MUST, (150, 147), 5)
    pygame.draw.circle(screen, MUST, (150, 164), 5)

    # Vasak käsi
    pygame.draw.line(screen, PRUUN, (106, 148), (60, 118), 4)
    pygame.draw.line(screen, PRUUN, (75, 127), (60, 108), 3)
    pygame.draw.line(screen, PRUUN, (75, 127), (56, 133), 3)

    # Parem käsi
    pygame.draw.line(screen, PRUUN, (194, 148), (240, 118), 4)
    pygame.draw.line(screen, PRUUN, (225, 127), (240, 108), 3)
    pygame.draw.line(screen, PRUUN, (225, 127), (244, 133), 3)

    pygame.display.flip()
    clock.tick(60)
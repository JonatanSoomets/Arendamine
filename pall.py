import pygame, sys
pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Põrkav pall")
screen.fill(lBlue)
clock = pygame.time.Clock()

# palli joonistamine (kuna meil pole pilti, joonistame ringi)
ballRadius = 30
posX, posY = 100, 100
speedX, speedY = 3, 4

gameover = False
# loop
while not gameover:
    clock.tick(60)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    # palli joonistamine
    pygame.draw.circle(screen, red, (posX, posY), ballRadius)

    posX += speedX
    posY += speedY

    # kui puudub ääri, siis muudab suunda
    if posX + ballRadius > screenX or posX - ballRadius < 0:
        speedX = -speedX

    if posY + ballRadius > screenY or posY - ballRadius < 0:
        speedY = -speedY

    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()

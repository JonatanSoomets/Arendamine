import pygame, sys
pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Harjutamine")
clock = pygame.time.Clock()

font      = pygame.font.SysFont("arial", 22)
font_väik = pygame.font.SysFont("arial", 16)

# Algseaded (nagu originaalpildil)
TAUST  = (144, 238, 144)  # hele roheline
JOON   = (255,   0,   0)  # punane
READ   = 10
VEERUD = 16

VÄRVID = {
    "punane":   (255,   0,   0),
    "roheline": (  0, 255,   0),
    "sinine":   (  0,   0, 255),
    "kollane":  (255, 255,   0),
    "valge":    (255, 255, 255),
    "must":     (  0,   0,   0),
    "oranž":    (255, 165,   0),
    "lilla":    (160,  32, 240),
    "roosa":    (255, 105, 180),
    "hall":     (128, 128, 128),
}

väljad = [
    {"silt": "Joone värv:",  "väärtus": ""},
    {"silt": "Ridade arv:",  "väärtus": ""},
    {"silt": "Veergude arv:","väärtus": ""},
]
aktiivne = 0

menüü = True
viga = ""

while menüü:
    screen.fill((30, 30, 30))

    t = font.render("Sisesta seaded:", True, (255, 255, 255))
    screen.blit(t, (30, 20))

    for i, väli in enumerate(väljad):
        y = 70 + i * 80
        silt = font_väik.render(väli["silt"], True, (180, 180, 180))
        screen.blit(silt, (30, y))
        ääris = (255, 215, 0) if i == aktiivne else (100, 100, 100)
        pygame.draw.rect(screen, (50, 50, 50), (30, y+22, 300, 36), border_radius=6)
        pygame.draw.rect(screen, ääris, (30, y+22, 300, 36), 2, border_radius=6)
        screen.blit(font.render(väli["väärtus"], True, (255, 255, 255)), (40, y+28))

    if viga:
        screen.blit(font_väik.render(viga, True, (255, 80, 80)), (30, 318))

    pygame.draw.rect(screen, (60, 160, 60), (30, 360, 140, 44), border_radius=8)
    bt = font.render("Alusta", True, (255, 255, 255))
    screen.blit(bt, (100 - bt.get_width()//2, 370))

    hint = font_väik.render("Värvid: punane, sinine, roheline, kollane, valge, must, oranž, lilla, roosa, hall", True, (100, 100, 100))
    screen.blit(hint, (30, 435))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for i in range(len(väljad)):
                y = 70 + i * 80
                if 30 <= mx <= 330 and y+22 <= my <= y+58:
                    aktiivne = i
            if 30 <= mx <= 170 and 360 <= my <= 404:
                aktiivne = -1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                aktiivne = (aktiivne + 1) % len(väljad)
            elif event.key == pygame.K_BACKSPACE:
                väljad[aktiivne]["väärtus"] = väljad[aktiivne]["väärtus"][:-1]
            elif event.key == pygame.K_RETURN:
                aktiivne = -1
            else:
                väljad[aktiivne]["väärtus"] += event.unicode

    if aktiivne == -1:
        joon_nimi = väljad[0]["väärtus"].strip().lower()
        try:
            read   = max(1, int(väljad[1]["väärtus"].strip()))
            veerud = max(1, int(väljad[2]["väärtus"].strip()))
        except:
            read, veerud = None, None

        if joon_nimi in VÄRVID and read and veerud:
            JOON   = VÄRVID[joon_nimi]
            READ   = read
            VEERUD = veerud
            menüü  = False
        else:
            viga = "Kontrolli sisestust! Värvinimi peab olema eesti keeles."
            aktiivne = 0

    pygame.display.flip()
    clock.tick(60)

# ── Ruudustik ──────────────────────────────────────────────────────────────
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(TAUST)

    rw = WIDTH  // VEERUD
    rh = HEIGHT // READ
    for r in range(READ):
        for v in range(VEERUD):
            pygame.draw.rect(screen, JOON, (v*rw, r*rh, rw, rh), 2)

    pygame.display.flip()
    clock.tick(60)
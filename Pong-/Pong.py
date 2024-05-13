import pygame, sys, random, time
from pygame.locals import *

# Rinaldi Iván / DNI:42235627

pygame.init()

tamaño = (800, 800)
ventana = pygame.display.set_mode(tamaño)
reloj = pygame.time.Clock()
pygame.display.set_caption("Ping Pong con 6to")

GREY = (175, 175, 175)
RED = (255, 0, 0)
DARK_PINK = (255, 0, 100)
PINK = (255, 0, 255)
ORANGE = (255, 100, 0)
RED_PINK = (255, 100, 100)
MAGENT = (255, 100, 255)
YELLOW = (255, 255, 0)
LIGHT_YELLOW = (255, 255, 100)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)

historial = "historial.txt"


def agregar(a, winner, score1, score2):  # Agrega datos al final del archivo
    a1 = open(a, "a")
    a1.write(f"El ganador fue el jugador: {winner} ({score1}-{score2}) \n")
    a1.close()


def print_text(text, position, font_size, color):
    font = pygame.font.SysFont("Times New Roman", font_size, True, False)
    superficie = font.render(text, True, (color))
    ventana.blit(superficie, position)


def tiempo(sec):
    time.sleep(sec)


def showrecord(a):
    a1 = open(a, "r")
    posy = 100
    print_text("HISTORIAL", (250, 10), 50, WHITE)
    for record in a1:
        position = (10, posy)
        print_text(record, position, 20, WHITE)
        posy += 20
    a1.close()


def dificult():
    # logo = pygame.image.load("C:\\Users\\Ivan\\Documents\\Pong\\logo.png").convert()
    logo = pygame.image.load("logo.png").convert()
    mousepos = pygame.mouse.get_pos()
    menuover = False
    while not menuover:
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = mousepos[0]
                y = mousepos[1]
                if x >= 50 and x <= 250 and y >= 400 and y <= 500:
                    juego(100)
                if x >= 550 and x <= 750 and y >= 400 and y <= 500:
                    juego(200)
                if x >= 50 and x <= 250 and y >= 600 and y <= 700:
                    juego(300)
                if x >= 550 and x <= 750 and y >= 600 and y <= 700:
                    juego(400)
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.MOUSEBUTTONDOWN:
                    pass

        ventana.fill(BLACK)
        ventana.blit(logo, [70, 20])

        pygame.draw.rect(ventana, MAGENT, (50, 400, 200, 100))
        pygame.draw.rect(ventana, MAGENT, (550, 400, 200, 100))
        pygame.draw.rect(ventana, MAGENT, (50, 600, 200, 100))
        pygame.draw.rect(ventana, MAGENT, (550, 600, 200, 100))
        print_text(f"DIF 1", (80, 420), 50, YELLOW)
        print_text(f"DIF 2", (590, 420), 50, YELLOW)
        print_text(f"DIF 3", (80, 620), 50, YELLOW)
        print_text(f"DIF 4", (590, 620), 50, YELLOW)

        pygame.display.flip()
        reloj.tick(60)


def record():
    mousepos = pygame.mouse.get_pos()
    menuover = False
    while not menuover:
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = mousepos[0]
                y = mousepos[1]
                if x >= 550 and x <= 750 and y >= 400 and y <= 500:
                    menu()

            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.MOUSEBUTTONDOWN:
                    pass

        ventana.fill(BLACK)

        showrecord(historial)
        pygame.draw.rect(ventana, GREY, (550, 400, 200, 100))
        print_text(f"Volver", (575, 420), 50, YELLOW)

        pygame.display.flip()
        reloj.tick(60)


def juego(tamaño_j_y):
    limit = 600 - tamaño_j_y
    j1_Pos = 245  # Es solo Y
    j2_Pos = 245  # Por que solo se mueven de arriba a abajo

    j1_Vel = 0
    j2_Vel = 0

    tamaño_j_x = 20
    # tamaño_j_y = 110

    pelota_pos_x = 390
    pelota_pos_y = 300

    randombin = random.randint(0, 1)
    randombin2 = random.randint(0, 1)

    pelota_vel_x = 0
    pelota_vel_y = 0
    pelota_radio = 10

    puntos_j1 = 0
    puntos_j2 = 0
    max_point = 3
    gameover = False

    sonidopelota = pygame.mixer.Sound("sonidopelota.mp3")
    sonidovictoria = pygame.mixer.Sound("victoria.mp3")
    sonidopunto = pygame.mixer.Sound("punto.mp3")

    fondo = pygame.image.load("galaxia.jpg").convert()
    pelota2 = pygame.image.load("pelota.png").convert()

    if randombin == 1:
        pelota_vel_x = 7
    else:
        pelota_vel_x = -7

    if randombin2 == 0:
        pelota_vel_y = 7
    else:
        pelota_vel_y = -7

    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    j1_Vel = -10
                if event.key == pygame.K_s:
                    j1_Vel = +10
                if event.key == pygame.K_UP:
                    j2_Vel = -10
                if event.key == pygame.K_DOWN:
                    j2_Vel = +10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    j1_Vel = 0
                if event.key == pygame.K_s:
                    j1_Vel = 0
                if event.key == pygame.K_UP:
                    j2_Vel = 0
                if event.key == pygame.K_DOWN:
                    j2_Vel = 0

        if pelota_pos_x > 750:
            puntos_j1 += 1
            sonidopunto.play()
            tiempo(1)

        elif pelota_pos_x < 50:
            puntos_j2 += 1
            sonidopunto.play()
            tiempo(1)

        if pelota_pos_x > 750 or pelota_pos_x < 50:
            pelota_pos_x = 390
            pelota_pos_y = 300

        if pelota_pos_y > 590 or pelota_pos_y < 10:
            pelota_vel_y *= -1

        if j2_Pos > limit - 10:
            j2_Pos = limit
        if j2_Pos < 10:
            j2_Pos = 0
        if j1_Pos > limit - 10:
            j1_Pos = limit
        if j1_Pos < 10:
            j1_Pos = 0

        pelota_pos_x += pelota_vel_x
        pelota_pos_y += pelota_vel_y

        j2_Pos += j2_Vel
        j1_Pos += j1_Vel

        if puntos_j1 == max_point or puntos_j2 == max_point:
            gameover = True

        # ventana.fill(GREEN)
        ventana.blit(fondo, [0, 0])

        j1 = pygame.draw.rect(ventana, RED, (28, j1_Pos, tamaño_j_x, tamaño_j_y))
        j2 = pygame.draw.rect(ventana, RED, (752, j2_Pos, tamaño_j_x, tamaño_j_y))
        tablero = pygame.draw.rect(ventana, BLACK, (0, 600, 800, 200))

        linea1 = pygame.draw.line(ventana, WHITE, (50, 0), (50, 600), 1)
        linea2 = pygame.draw.line(ventana, WHITE, (749, 0), (749, 600), 1)
        linea3 = pygame.draw.line(ventana, WHITE, (0, 1), (800, 1), 1)
        linea4 = pygame.draw.line(ventana, WHITE, (0, 599), (800, 599), 1)

        linea5 = pygame.draw.line(ventana, WHITE, (400, 0), (400, 600), 1)

        pelota = pygame.draw.circle(
            ventana, GREEN, (pelota_pos_x, pelota_pos_y), pelota_radio
        )

        print_text(f"Jugador 1: {puntos_j1}", (50, 670), 50, WHITE)
        print_text(f"Jugador 2: {puntos_j2}", (460, 670), 50, WHITE)

        if pelota.colliderect(j1) or pelota.colliderect(j2):
            pelota_vel_x *= -1
            sonidopelota.play()

        if puntos_j1 == max_point:
            print_text("¡GANA JUGADOR 1!", (150, 320), 50, WHITE)
            sonidovictoria.play()
            ganador = 1
            agregar(historial, ganador, puntos_j1, puntos_j2)

        elif puntos_j2 == max_point:
            print_text("¡GANA JUGADOR 2!", (150, 320), 50, WHITE)
            sonidovictoria.play()
            ganador = 2
            agregar(historial, ganador, puntos_j2, puntos_j1)

        ##-----------
        # if j1.colliderect(pelota) or j2.colliderect(pelota):
        #    pelota_vel_x *= -1
        ##-----------
        pygame.display.flip()
        reloj.tick(50)
    tiempo(3)
    menu()


def menu():
    musicmenu = pygame.mixer.Sound("ALIBI.mp3")
    # logo = pygame.image.load("C:\\Users\\Ivan\\Documents\\Pong\\logo.png").convert()
    logo = pygame.image.load("logo.png").convert()
    mousepos = pygame.mouse.get_pos()
    menuover = False
    while not menuover:
        musicmenu.play()
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = mousepos[0]
                y = mousepos[1]
                if x >= 50 and x <= 250 and y >= 400 and y <= 500:
                    musicmenu.stop()
                    dificult()
                if x >= 550 and x <= 750 and y >= 400 and y <= 500:
                    musicmenu.stop()
                    record()
                if x >= 300 and x <= 500 and y >= 600 and y <= 700:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.MOUSEBUTTONDOWN:
                    pass

        ventana.fill(BLACK)
        ventana.blit(logo, [70, 20])

        pygame.draw.rect(ventana, GREY, (50, 400, 200, 100))
        pygame.draw.rect(ventana, GREY, (550, 400, 200, 100))
        pygame.draw.rect(ventana, RED, (300, 600, 200, 100))
        print_text(f"Jugar", (80, 420), 50, GREEN)
        print_text(f"Historial", (555, 420), 50, YELLOW)
        print_text(f"Salir", (345, 620), 50, WHITE)

        pygame.display.flip()
        reloj.tick(60)
    sys.exit()


menu()

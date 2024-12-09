import pygame
import random
import math
from pygame import mixer
#inicar pygame
pygame.init()
#crear pantalla
pantalla = pygame.display.set_mode((800,600))

#titulo e iconos
pygame.display.set_caption('INVASIÓN ESPACIAL')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

# agregrar musica

mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)
#variables jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugadorx=368
jugadory=500
jugarox_cambio = 0

#variables enemigo
img_enemigo = []
enemigox=[]
enemigoy=[]
enemigox_cambio = []
enemigoy_cambio = []
cantidad_enemigos = 8
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigox.append(random.randint(0, 736))
    enemigoy.append(random.randint(50,200))
    enemigox_cambio.append(3.5)
    enemigoy_cambio.append(50)

#variables bala
img_bala = pygame.image.load('bala.png')
balax= 0
balay= 500
balax_cambio = 0
balay_cambio = 14
bala_visible = False

#variable puntuaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
textox = 10
textoy = 10


#texto GAMEOVER

fuente_final = pygame.font.Font('freesansbold.ttf', 40)

#funcion textofinal

def textofinal():
    mi_fuentefinal = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuentefinal, (60,200))


#funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f'PUNTAJE: {puntaje}', True, (255,255,255))
    pantalla.blit(texto,(x,y))
#Funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))
#Funcion enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene], (x,y))

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16,y +10))
#funcion calcular colision
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_2 - y_1,2))
    if distancia <  27:
        return True
    else:
        return False



#loop del juego
se_ejecuta = True
while se_ejecuta:
    #pantalla color
    pantalla.blit(fondo,(0,0))


    #Iterar eventos
    for evento in pygame.event.get():
        #evento cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #evento presionar tecla
        if evento.type ==  pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugarox_cambio = -6.9
            if evento.key == pygame.K_RIGHT:
                jugarox_cambio = +6.9
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('Laser Gun.mp3')
                sonido_bala.play()
                if bala_visible == False:
                    balax = jugadorx
                    disparar_bala(balax, balay)

        #evento soltar flecha
        if  evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugarox_cambio = 0

    #modificar ubicacion del jugador
    jugadorx += jugarox_cambio

    #mantener dentro de bordes al jugador
    if jugadorx <= 0:
        jugadorx = 0
    elif jugadorx >= 736:
        jugadorx = 736




    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):

        #GAME OVER
        if enemigoy[e] > 500:
            for k in range(cantidad_enemigos):
                enemigoy[k] = 1000
            textofinal()
            break


        enemigox[e] += enemigox_cambio[e]
        # mantener dentro de bordes al enemigo
        if enemigox[e] <= 0:
            enemigox_cambio[e] = 2
            enemigoy[e] += enemigoy_cambio[e]
        elif enemigox[e] >= 736:
            enemigox_cambio[e] = -2
            enemigoy[e] += enemigoy_cambio[e]

        colision = hay_colision(enemigox[e], enemigoy[e], balax, balay)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            balay = 500
            bala_visible = False
            puntaje += 1


            enemigox[e] = random.randint(0, 736)
            enemigoy[e] = random.randint(50, 200)

        enemigo(enemigox[e], enemigoy[e], e)

    #movimiento bala
    if balay <= -64:
        balay= 500
        bala_visible = False

    if bala_visible:
        disparar_bala(balax,balay)
        balay -= balay_cambio





    jugador(jugadorx,jugadory)

    mostrar_puntaje(textox,textoy)

    #actualizar
    pygame.display.update()





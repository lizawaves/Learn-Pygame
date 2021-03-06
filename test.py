import pygame
import random

from spacethingsfunc import *


pygame.init()

crash_sound = pygame.mixer.Sound('Big_Explosion_Cut_Off.wav')
pygame.mixer.music.load('Ether_Oar.wav')




def space_ship_teste(x,y,r,s,d):


    toppoint = (x,y-s)
    lpoint = (x-s,y)
    rpoint = (x+s,y)

    if 0 < d < 2:
        #both go up
        toppoint = (x+r, (y-s)+r)
        lpoint = ((x-s, y)
        rpoint = (x+s, y)


    pygame.draw.polygon(gameDisplay, green, ((toppoint,lpoint,rpoint)))

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((display_w/2), (display_h/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 150, 450, 100, 50, green, bright_green,unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('You Crased', largeText)
        TextRect.center = ((display_w/2), (display_h/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play Again", 150, 450, 100, 50, green, bright_green,game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():


    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects('Space Things', largeText)
        TextRect.center = ((display_w/2), (display_h/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start!", 250, 450, 100, 50, green, bright_green,game_loop)
        button("Quit", 450, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():

    pygame.mixer.music.play(-1)

    global pause

    ship_x = display_w / 2
    ship_y = display_h / 2
    ship_r = 3
    ship_s = 6
    ship_d = 0

    ship_x_change = 0
    ship_y_change = 0

    space_ship(ship_x, ship_y)

    number_of_things = 1
    thing_speed = 1
    dodged = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship_d += -1
                    if ship_d == -8:
                        ship_d = 0
                if event.key == pygame.K_RIGHT:
                    ship_d += 1
                    if ship_d == 8:
                        ship_d = 0

                if event.key == pygame.K_UP:
                    ship_y_change += -1
                if event.key == pygame.K_DOWN:
                    ship_y_change += 1
                if event.key == pygame.K_p:
                    pause = True
                    paused()

        ship_x += ship_x_change
        ship_y += ship_y_change

            #print(str(thing[i].x) + " " + str(thing[i].y))


        gameDisplay.fill(black)

        space_ship_teste(ship_x, ship_y,ship_r,ship_s,ship_d)


        if ship_x < 0 or ship_x > display_w or ship_y < 0 or ship_y > display_h:
            crash()


        pygame.display.update()
        clock.tick(60)

game_intro()
#game_loop()

#arrumar a colisão das bolas
#melhorar a progessão
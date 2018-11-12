import pygame
import random

from spacethingsfunc import *


pygame.init()

crash_sound = pygame.mixer.Sound('Big_Explosion_Cut_Off.wav')
pygame.mixer.music.load('Ether_Oar.wav')

shipImg = pygame.image.load('car.png')

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    pygame.mouse.set_visible(False)

def paused():

    pygame.mouse.set_visible(True)

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

    pygame.mouse.set_visible(True)

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

    pygame.mouse.set_visible(True)
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
    pygame.mouse.set_visible(False)

    global pause

    ship_x = display_w / 2
    ship_y = display_h / 2

    ship_x_change = 0
    ship_y_change = 0

    space_ship(ship_x, ship_y)

    number_of_things = 1
    thing_speed = 1
    dodged = 0

    inicial_r = 20

    thing = []

    milestone = 5

    aimposition = (0,0)

    for i in range(number_of_things):
        thing.append(Thing(0, 0, 0, 0, 0, 0))

        thing[i].x_orientation = random.randrange(0, 100)
        thing[i].x = random.randrange(0, display_w)

        thing[i].y_orientation = random.randrange(0,100)
        if thing[i].y_orientation < 50:
            thing[i].y = display_h
        else:
            thing[i].y = 0

        thing[i].r = random.randrange(inicial_r, inicial_r+20)


    bullC = 0
    bullet = []
    #bullet.append(Bullet(0,0,0,0))
    #bullet_x = 0
    #bullet_y = 0
    #bullet_vx = 0
    #bullet_vy = 0
    #bullet_c = blue







    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship_x_change += -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship_x_change += 1
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    ship_y_change += -1
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    ship_y_change += 1
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.MOUSEMOTION:
                aimposition = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    bullet.append(Bullet(0, 0, 0, 0))
                    bullet[bullC].x = ship_x
                    bullet[bullC].y = ship_y
                    bullet[bullC].vx = (aimposition[0] - ship_x)/100
                    bullet[bullC].vy = (aimposition[1] - ship_y)/100
                    bullC += 1
                    print('mouse clicked')



        for i in range(bullC):
            bullet[i].x += bullet[i].vx
            bullet[i].y += bullet[i].vy

        ship_x += ship_x_change
        ship_y += ship_y_change

        for i in range(number_of_things):
            if thing[i].x_orientation > 50:
                thing[i].x += -thing_speed
            else:
                thing[i].x += thing_speed
            if thing[i].y_orientation < 50:
                thing[i].y += -thing_speed
            else:
                thing[i].y += thing_speed
            #print(str(thing[i].x) + " " + str(thing[i].y))



        gameDisplay.fill(black)

        space_ship(ship_x, ship_y)
        aim(aimposition[0],aimposition[1],red)

        for i in range(number_of_things):
            space_things(thing[i].x,thing[i].y,thing[i].r,white)

        for i in range(bullC):
            bullets(int(bullet[i].x),int(bullet[i].y),blue)


        things_dodged(dodged)

        if ship_x < 0 or ship_x > display_w or ship_y < 0 or ship_y > display_h:
            crash()

        for i in range(number_of_things):
            if abs((((ship_x - thing[i].x)*(ship_x - thing[i].x))+((ship_y - thing[i].y)*(ship_y - thing[i].y))) < thing[i].r * thing[i].r):
                crash()

        for i in range(number_of_things):
            if thing[i].y > display_h or thing[i].x > display_w or thing[i].x < 0 or thing[i].y < 0:
                dodged += 1
                if dodged <= 13:
                    inicial_r += dodged

                if dodged == milestone:
                    thing.append(Thing(0, 0, 0, 0, 0, 0))
                    number_of_things += 1
                    milestone += milestone


                thing[i].x_orientation = random.randrange(0, 100)
                thing[i].x = random.randrange(0, display_w)
                thing[i].y_orientation = random.randrange(0, 100)
                if thing[i].y_orientation < 50:
                    thing[i].y = display_h
                else:
                    thing[i].y = 0
                thing[i].r = random.randrange(inicial_r, inicial_r + 20)
                #print(str(thing[i].x) + " " + str(thing[i].y))


        pygame.display.update()
        clock.tick(60)

game_intro()
#game_loop()

#melhorar a progessão
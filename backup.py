import pygame
import random

from spacethingsfunc import *


pygame.init()

def crash():

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

    things_count = 1

    ship_x = display_w / 2
    ship_y = display_h / 2

    ship_x_change = 0
    ship_y_change = 0

    space_ship(ship_x, ship_y)

    number_of_things = 1
    thing_speed = 1
    dodged = 0

    thing = []

    for i in range(number_of_things):
        thing.append(Thing(0, 0, 0, 0, 0, 0))

        inicial_r = 20
        thing[i].x_orientation = random.randrange(0, 100)
        thing[i].x = random.randrange(0, display_w)

        thing[i].y_orientation = random.randrange(0,100)
        if thing[i].y_orientation < 50:
            thing[i].y = display_h
        else:
            thing[i].y = 0

        thing[i].r = random.randrange(inicial_r, inicial_r+20)

        print(thing[i].x)





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship_x_change += -1
                if event.key == pygame.K_RIGHT:
                    ship_x_change += 1
                if event.key == pygame.K_UP:
                    ship_y_change += -1
                if event.key == pygame.K_DOWN:
                    ship_y_change += 1


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
            print(str(thing[i].x) + " " + str(thing[i].y))


        gameDisplay.fill(black)

        space_ship(ship_x, ship_y)

        for i in range(number_of_things):
            space_things(thing[i].x,thing[i].y,thing[i].r)


        things_dodged(dodged)

        if ship_x < 0 or ship_x > display_w or ship_y < 0 or ship_y > display_h:
            crash()

        for i in range(number_of_things):
            if ship_y < thing[i].y+thing[i].r and ship_y > thing[i].y-thing[i].r:
                if ship_x < thing[i].x+thing[i].r and ship_x > thing[i].x-thing[i].r:
                    crash()

        for i in range(number_of_things):
            if thing[i].y > display_h or thing[i].x > display_w or thing[i].x < 0 or thing[i].y < 0:
                dodged += 1
                inicial_r += dodged

                if dodged == 5 or dodged == 10 or dodged == 15 or dodged == 20:
                    thing.append(Thing(0, 0, 0, 0, 0, 0))
                    number_of_things += 1


                thing[i].x_orientation = random.randrange(0, 100)
                thing[i].x = random.randrange(0, display_w)
                thing[i].y_orientation = random.randrange(0, 100)
                if thing[i].y_orientation < 50:
                    thing[i].y = display_h
                else:
                    thing[i].y = 0
                thing[i].r = random.randrange(inicial_r, inicial_r + dodged)
                print(str(thing[i].x) + " " + str(thing[i].y))


        pygame.display.update()
        clock.tick(60)

game_intro()
#game_loop()

#arrumar a colisão das bolas
#melhorar a progessão
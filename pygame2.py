import pygame
import random


pygame.init()


black = (0,0,0)
white = (255,255,255)
red = (190,0,0)
green = (0,190,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

display_w = 800
display_h = 600

gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Space stuff')
clock = pygame.time.Clock()


###

class Thing:
  def __init__(self, x, y, r, speed):
    self.x = x
    self.y = y
    self.r = r
    self.speed = speed

###



#gameDisplay.fill(black)

#pixAr = pygame.PixelArray(gameDisplay)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)

def things_dodged(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Dodged: "+str(count), True, red)
    gameDisplay.blit(text, (0,0))

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

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

def space_ship(x,y):
    pygame.draw.polygon(gameDisplay, green, ((x,y),(x+10,y),(x+5,y-15)))


def space_things(tx, ty, tr):
    pygame.draw.circle(gameDisplay, white, (tx, ty), tr, 0)


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

    thing = []
    thing.append(Thing)

    inicial_r = 20
    thing_x_orientation = random.randrange(0, 100)
    thing[0].x = random.randrange(0, display_w)

    thing_u_or_d = random.randrange(0,100)
    if thing_u_or_d < 50:
        thing[0].y = display_h
    else:
        thing[0].y = 0

    thing[0].r = random.randrange(inicial_r, inicial_r+20)

    thing_speed = 1

    dodged = 0

    number_of_things = 1

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
            if thing_x_orientation > 50:
                thing[i].x += int(-(thing_speed+dodged*0.5))
            else:
                thing[i].x += int(thing_speed+dodged*0.5)
            if thing_u_or_d < 50:
                thing[i].y += int(-(thing_speed+dodged*0.5))
            else:
                thing[i].y += int(thing_speed+dodged*0.5)


        #print(str(ship_x) + " " + str(ship_y) + " " + str(thing_x) + " " + str(thing_y) + " " + str(thing_r))
        gameDisplay.fill(black)

        space_ship(ship_x, ship_y)

        for i in range(number_of_things):
            space_things(thing[i].x,thing[i].y,thing[i].r)
            #print(thing[i].x)

        things_dodged(dodged)

        if ship_x < 0 or ship_x > display_w or ship_y < 0 or ship_y > display_h:
            crash()

        if ship_y < thing[0].y+thing[0].r and ship_y > thing[0].y-thing[0].r:
            if ship_x < thing[0].x+thing[0].r and ship_x > thing[0].x-thing[0].r:
                crash()

        if thing[0].y > display_h or thing[0].x > display_w or thing[0].x < 0 or thing[0].y < 0:
            dodged += 1
            inicial_r += dodged

            if dodged == 3 or dodged == 6:
                thing.append(Thing)
                number_of_things += 1

            for i in range(number_of_things):
                thing_x_orientation = random.randrange(0, 100)
                thing[i].x = random.randrange(0, display_w)
                thing_u_or_d = random.randrange(0, 100)
                if thing_u_or_d < 50:
                    thing[i].y = display_h
                else:
                    thing[i].y = 0
                thing[i].r = random.randrange(inicial_r, inicial_r + dodged)
                #print(thing[i].x)


        pygame.display.update()
        clock.tick(60)

game_intro()
#game_loop()
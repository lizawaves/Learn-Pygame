import pygame
import random



black = (0,0,0)
white = (255,255,255)
red = (190,0,0)
green = (0,190,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

colors = [white, red, green]

display_w = 800
display_h = 600

gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Space stuff')
clock = pygame.time.Clock()

pause = False

class Thing:
  def __init__(self, x, y, r, speed,x_orientation, y_orientation):
    self.x = x
    self.y = y
    self.r = r
    self.speed = speed
    self.x_orientation = x_orientation
    self.y_orientation = y_orientation


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


def space_ship(x,y):
    pygame.draw.polygon(gameDisplay, green, ((x,y),(x+10,y),(x+5,y-15)))


def space_things(tx, ty, tr,color):
    pygame.draw.circle(gameDisplay, color, (tx, ty), tr, 0)
from config import *
import pygame
import time

done = False

def startHome():
  pygame.quit()
  pygame.init()
  pygame.display.set_caption('StoneBoard Home')
  (width, height) = (1500, 1000)
  screen = pygame.display.set_mode((width, height))
  home_background_colour = (41,60,57)
  screen.fill(home_background_colour)
  print("Launched Home")
  done = False
  
  stoneBoard_logo = pygame.image.load('stable/StoneBoardPackagesstable/assets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (250, 250))
  screen.blit(stoneBoard_logo,(1240,-105))
  pygame.display.flip()

  #Add It To Load New Stuff

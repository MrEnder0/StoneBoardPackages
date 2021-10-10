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
  home_background_colour = (255,171,252)
  screen.fill(home_background_colour)
  print("Launched Home")
  done = False

  #Test if launcher opened before

  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load('artAssets/stoneBoard_experimentalRelease.png').convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (120, 120))
    screen.blit(stoneBoard_experimentalRelease,(0,-35))

  stoneBoard_logo = pygame.image.load('artAssets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (250, 250))
  screen.blit(stoneBoard_logo,(1240,-105))
  pygame.display.flip()

  #Add It To Load New Stuff

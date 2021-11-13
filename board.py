from experimental.StoneBoardPackagesexperimental.soundManager import *
from experimental.StoneBoardPackagesexperimental.home import *
from config import *
import pygame
import time
import os

def launchLoadedServer():
  pygame.quit()
  pygame.init()
  pygame.display.set_caption("StoneBoard")
  (width, height) = (1920, 1080)
  screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
  board_background_colour = (250,250,250)
  screen.fill(board_background_colour)
  userFilePath = "storage/user.txt"
  menuSelectLine = 1
  run = True
  print("Opened Board")
  
  music()

  #Experimental indicator
  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/stoneBoard_experimentalRelease.png").convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (120, 120))
    
  stoneBoard_logo = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo.png").convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (288, 28))
  stoneBoard_logo_rectangle = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo_rectangle.png').convert_alpha()
  stoneBoard_logo_rectangle = pygame.transform.scale(stoneBoard_logo_rectangle, (400, 200))
  exitButton = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/exit.png").convert_alpha()
  boldFont = pygame.font.Font("experimental/StoneBoardPackagesexperimental/assets/fonts/Silkscreen/slkscr.ttf", 22)
  bottomBar = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/bottom_bar.png").convert_alpha()
  
  class Button():
    def __init__(self, x, y, image, scale):
      width = image.get_width()
      height = image.get_height()
      self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
      self.rect = self.image.get_rect()
      self.rect.topleft = (x, y)
      self.clicked = False
    def draw(self):
      action = False
      pos = pygame.mouse.get_pos()
      if self.rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
          self.clicked = True
          action = True
      if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False
      
      screen.blit(self.image, (self.rect.x, self.rect.y))
      return action
    
  bottomBar = Button(-5, 1000, bottomBar, 0.34)
  exitButton = Button(1828, 1008, exitButton, 0.13)
  
  while run:
    screen.fill(board_background_colour)
    screen.blit(stoneBoard_experimentalRelease,(0,-35))
    screen.blit(stoneBoard_logo_rectangle,(1600,-135))
    screen.blit(stoneBoard_logo,(1620,10))
    bottomBar.draw()
    
    if exitButton.draw():
        clickSound()
        time.sleep(0.6)
        run = False
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
  
  pygame.quit()
  quit()

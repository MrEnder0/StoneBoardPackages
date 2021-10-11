from config import *
import pygame
import time

def startHome():
  pygame.quit()
  pygame.init()
  pygame.display.set_caption('StoneBoard Home')
  (width, height) = (1500, 1000)
  screen = pygame.display.set_mode((width, height))
  home_background_colour = (41,60,57)
  screen.fill(home_background_colour)
  print("Launched Home")
  run = True

  #Test if launcher opened before

  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_experimentalRelease.png').convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (120, 120))
    screen.blit(stoneBoard_experimentalRelease,(0,-35))

  stoneBoard_logo = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (250, 250))
  screen.blit(stoneBoard_logo,(1240,-105))
  pygame.display.flip()

  #Add It To Load New Stuff

  button_img = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/bottom_bar.png').convert_alpha()

  class Button():
    def __init__(self, x, y, image, scale):
      width = image.get_width()
      height = image.get_height()
      self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
      self.rect = self.image.get_rect()
      self.rect.topleft = (x, y)

    def draw(self):
      screen.blit(self.image, (self.rect.x, self.rect.y))


  start_button = Button(0, 920, button_img, 1)

  while run:
    screen.fill(home_background_colour)
    screen.blit(stoneBoard_experimentalRelease,(0,-35))
    screen.blit(stoneBoard_logo,(1240,-105))
    start_button.draw()
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

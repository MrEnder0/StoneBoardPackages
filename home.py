from config import *
import pygame
import time

def startHome():
  pygame.quit()
  pygame.init()
  pygame.display.set_caption('StoneBoard Home')
  (width, height) = (1500, 1000)
  screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
  home_background_colour = (250,250,250)
  screen.fill(home_background_colour)
  print("Launched Home")
  run = True

  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_experimentalRelease.png').convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (120, 120))
    screen.blit(stoneBoard_experimentalRelease,(0,-35))

  stoneBoard_logo = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (288, 28))
  screen.blit(stoneBoard_logo,(1200,10))
  
  stoneBoard_logo_rectangle = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo_rectangle.png').convert_alpha()
  stoneBoard_logo_rectangle = pygame.transform.scale(stoneBoard_logo_rectangle, (400, 200))
  screen.blit(stoneBoard_logo_rectangle,(1180,-130))

  #Buttons

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


  start_button = Button(-5, 920, button_img, 0.266)

  while run:
    screen.fill(home_background_colour)
    screen.blit(stoneBoard_logo_rectangle,(1180,-135))
    screen.blit(stoneBoard_experimentalRelease,(0,-35))
    screen.blit(stoneBoard_logo,(1200,10))
    start_button.draw()
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

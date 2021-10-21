from stable.StoneBoardPackagesstable.soundManager import *
from getmac import get_mac_address as gma
from config import *
import pygame
import time
import uuid
import os

def startHome():
  pygame.quit()
  pygame.init()
  pygame.display.set_caption('StoneBoard Home')
  (width, height) = (1500, 1000)
  screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
  home_background_colour = (250,250,250)
  screen.fill(home_background_colour)
  print("Launched Home")
  #print(gma())
  run = True
  
  music()

  #Test if existing user
  oldUser = os.path.isfile('storage/user.txt')

  if oldUser:
    newUserWindow = False
    print("Logged In!")
  else:
    print("No useraccount found creating new.")
    newUserWindow = True
    userFilePath = 'storage/user.txt'
    useruuid = uuid.uuid4()
    with open(userFilePath, 'w') as user:
      user.write(str(useruuid))

  stoneBoard_logo = pygame.image.load('stable/StoneBoardPackagesstable/assets/stoneBoard_logo.png').convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (288, 28))
  screen.blit(stoneBoard_logo,(1200,10))
  
  stoneBoard_logo_rectangle = pygame.image.load('stable/StoneBoardPackagesstable/assets/stoneBoard_logo_rectangle.png').convert_alpha()
  stoneBoard_logo_rectangle = pygame.transform.scale(stoneBoard_logo_rectangle, (400, 200))
  screen.blit(stoneBoard_logo_rectangle,(1180,-130))

  boldFont = pygame.font.Font('stable/StoneBoardPackagesstable/assets/fonts/Silkscreen/slkscr.ttf', 22)
  bottomBar = pygame.image.load('stable/StoneBoardPackagesstable/assets/bottom_bar.png').convert_alpha()
  exitButton = pygame.image.load('stable/StoneBoardPackagesstable/assets/exit.png').convert_alpha()
  newUserScreen = pygame.image.load('stable/StoneBoardPackagesstable/assets/newUserScreen.png').convert_alpha()

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

  newUserScreen = Button(466, 60, newUserScreen, 1)
  bottomBar = Button(-5, 920, bottomBar, 0.266)
  exitButton = Button(1420, 928, exitButton, 0.13)

  while run:
    screen.fill(home_background_colour)
    screen.blit(stoneBoard_logo_rectangle,(1180,-135))
    screen.blit(stoneBoard_experimentalRelease,(0,-35))
    screen.blit(stoneBoard_logo,(1200,10))

    if bottomBar.draw():
        caveManSound()
        print("Cave Man Secret Sound")

    if exitButton.draw():
        clickSound()
        time.sleep(0.6)
        run = False
        
    if newUserWindow:
      if newUserScreen.draw():
        newUserWindow = False
        clickSound()
      screen.blit(boldFont.render(str(useruuid), 0, (200, 200, 240)), (475, 565))

    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
  pygame.quit()
  quit()

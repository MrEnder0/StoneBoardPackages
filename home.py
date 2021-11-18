from experimental.StoneBoardPackagesexperimental.serverManager import *
from experimental.StoneBoardPackagesexperimental.soundManager import *
from experimental.StoneBoardPackagesexperimental.board import *
from config import *
import pygame
import time
import uuid
import os

import webbrowser

def startHome():
  pygame.quit()
  pygame.init()
  pygame.display.set_caption("StoneBoard Home")
  (width, height) = (1500, 1000)
  screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
  home_background_colour = (250,250,250)
  screen.fill(home_background_colour)
  userFilePath = "storage/user.txt"
  menuSelectLine = 1
  run = True
  menu = 0
  print("Launched Home")
  #webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)
  
  music()
  
  #Test if existing user
  oldUser = os.path.isfile("storage/user.txt")
  if oldUser:
    newUserWindow = False
    print("Logged In!")
  else:
    print("No useraccount found creating new.")
    newUserWindow = True
    useruuid = uuid.uuid4()
    with open(userFilePath, "w") as user:
      user.write(str(useruuid))
      
  #Experimental indicator
  if Experintal == True:
    stoneBoard_experimentalRelease = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/stoneBoard_experimentalRelease.png").convert_alpha()
    stoneBoard_experimentalRelease = pygame.transform.scale(stoneBoard_experimentalRelease, (120, 120))
    
  stoneBoard_logo = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo.png").convert_alpha()
  stoneBoard_logo = pygame.transform.scale(stoneBoard_logo, (288, 28))
  stoneBoard_logo_rectangle = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/stoneBoard_logo_rectangle.png').convert_alpha()
  stoneBoard_logo_rectangle = pygame.transform.scale(stoneBoard_logo_rectangle, (400, 200))
  stoneBoard_server_ui = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/serverUi.png').convert_alpha()
  stoneBoard_server_ui = pygame.transform.scale(stoneBoard_server_ui, (800, 500))
  menuSelectionBox = pygame.image.load('experimental/StoneBoardPackagesexperimental/assets/selectionBox.png').convert_alpha()
  menuSelectionBox = pygame.transform.scale(menuSelectionBox, (660, 40))
  exitButton = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/exit.png").convert_alpha()
  joinButton = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/join.png").convert_alpha()
  acceptButton = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/accept.png").convert_alpha()
  boldFont = pygame.font.Font("experimental/StoneBoardPackagesexperimental/assets/fonts/Silkscreen/slkscr.ttf", 22)
  bottomBar = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/bottom_bar.png").convert_alpha()
  newUserScreen = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/newUserScreen.png").convert_alpha()
  minimizeButton = pygame.image.load("experimental/StoneBoardPackagesexperimental/assets/menu_minimize.png").convert_alpha()
  
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
    
  serverUiExit = Button(1060, 626, minimizeButton, 0.13)
  serverUiOpen = Button(10, 928, joinButton, 0.13)
  serverUiCreate = Button(370, 626, joinButton, 0.13)
  serverUiAccept = Button(445, 626, acceptButton, 0.13)
  newUserScreen = Button(466, 60, newUserScreen, 1)
  bottomBar = Button(-5, 920, bottomBar, 0.266)
  exitButton = Button(1420, 928, exitButton, 0.13)
  
  while run:
    screen.fill(home_background_colour)
    screen.blit(stoneBoard_experimentalRelease,(0,-35))
    screen.blit(stoneBoard_logo_rectangle,(1180,-135))
    screen.blit(stoneBoard_logo,(1200,10))
    bottomBar.draw()
    
    if exitButton.draw():
        clickSound()
        time.sleep(0.6)
        run = False
    if serverUiOpen.draw():
        clickSound()
        menu = 1
    if menu == 1:
      readServers()
      lineDistance = 0
      lineCount = 0
      screen.blit(stoneBoard_server_ui,(350,200))
      
      with open('storage/serversList.txt', 'r') as serversList:
        for line in serversList:
           lineDistance += 40
           lineCount += 1
           lineText = line
           lineText = lineText[:-1]
           screen.blit(boldFont.render(str(lineText), 0, (200, 200, 240)), (450, 260 + lineDistance))

      screen.blit(menuSelectionBox,(400,250 + menuSelectLine * 40))
      key_input = pygame.key.get_pressed()   
      if key_input[pygame.K_UP]:
        if not menuSelectLine == 1:
          menuSelectLine += -1
          time.sleep(0.2)
      if key_input[pygame.K_DOWN]:
        if not menuSelectLine == lineCount:
          menuSelectLine += 1
          time.sleep(0.2)

      with open("storage/selectedLine.txt", "w") as selectedLine:
        selectedLine.write(str(menuSelectLine))
      #with open("storage/lineCount.txt", "w") as lineCountFile:
      #  lineCountFile.write(str(lineCount))

      if serverUiCreate.draw():
        clickSound()
        createServer()

      if serverUiAccept.draw():
        clickSound()
        loadServer()
        time.sleep(0.4)
        launchLoadedServer()

      if serverUiExit.draw():
        clickSound()
        time.sleep(0.6)
        menu = 0
        
    if newUserWindow:
      if newUserScreen.draw():
        newUserWindow = False
        clickSound()
      screen.blit(boldFont.render(str(useruuid), 0, (200, 200, 240)), (475, 565))
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
  
  #Working on instant quit thing
  pygame.quit()
  quit()

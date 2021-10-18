from config import *
import pygame
import random

def music():
    pygame.mixer.init()
    path = 'experimental/StoneBoardPackagesexperimental/assets/sounds/'
    music = pygame.mixer.Sound(path + "591665__erokia__sunburst.mp3")
    music.set_volume(0.1)

    if PlayMusic:
        pygame.mixer.music.load(path + "591665__erokia__sunburst.mp3") 
        pygame.mixer.music.play(-1,0.0)
        
def clickSound():
    pygame.mixer.init()
    path = 'experimental/StoneBoardPackagesexperimental/assets/sounds/'
    sound = pygame.mixer.Sound(path + "uiClick.mp3")
    sound.set_volume(0.3)
    pygame.mixer.music.load(path + "uiClick.mp3") 
    pygame.mixer.music.play(1,0.0)

def caveManSound():
    pygame.mixer.init()
    randomGrunt = random.randint(1,3)
    path = 'experimental/StoneBoardPackagesexperimental/assets/sounds/'
    if randomGrunt == 1:
        pygame.mixer.music.load(path + "cave_man1.mp3") 
        pygame.mixer.music.play(1,0.0)
    elif randomGrunt == 2:
        pygame.mixer.music.load(path + "cave_man2.mp3") 
        pygame.mixer.music.play(1,0.0)
    elif randomGrunt == 3:
        pygame.mixer.music.load(path + "cave_man3.mp3") 
        pygame.mixer.music.play(1,0.0)

from config import *
import pygame

def music():
    pygame.mixer.init()
    path = 'stable/StoneBoardPackagesstable/assets/sounds/'
    sound = pygame.mixer.Sound(path + "591665__erokia__sunburst.mp3")
    sound.set_volume(0.1)

    if PlayMusic:
        pygame.mixer.music.load(path + "591665__erokia__sunburst.mp3") 
        pygame.mixer.music.play(-1,0.0)
        
def clickSound():
    pygame.mixer.init()
    path = 'stable/StoneBoardPackagesstable/assets/sounds/'
    sound = pygame.mixer.Sound(path + "uiClick.mp3")
    sound.set_volume(0.3)
    pygame.mixer.music.load(path + "uiClick.mp3") 
    pygame.mixer.music.play(1,0.0)

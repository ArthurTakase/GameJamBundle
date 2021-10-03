import pygame
from pygame.locals import *

def splash():
    vsplash = pygame.mixer.Sound("sound/Splash.wav")
    vsplash.set_volume(0.5)
    vsplash.play()

def start():
    vstart = pygame.mixer.Sound("sound/Start.wav")
    vstart.set_volume(0.5)
    vstart.play()

def eat():
    veat = pygame.mixer.Sound("sound/Eat.wav")
    veat.set_volume(0.5)
    veat.play()

def wrong():
    vwrong = pygame.mixer.Sound("sound/wrong.wav")
    vwrong.set_volume(0.5)
    vwrong.play()

def select():
    vselect = pygame.mixer.Sound("sound/Blip_Select.wav")
    vselect.set_volume(0.3)
    vselect.play()

def select_back():
    vselect_back = pygame.mixer.Sound("sound/Blip_Select_back.wav")
    vselect_back.set_volume(0.3)
    vselect_back.play()

def food():
    vfood = pygame.mixer.Sound("sound/food.wav")
    vfood.set_volume(0.2)
    vfood.play()

def change():
    vchange = pygame.mixer.Sound("sound/change.wav")
    vchange.set_volume(0.2)
    vchange.play()

def pause():
    vpause = pygame.mixer.Sound("sound/pause.wav")
    vpause.set_volume(0.3)
    vpause.play()

def reverse_pause():
    vrpause = pygame.mixer.Sound("sound/reverse_pause.wav")
    vrpause.set_volume(0.3)
    vrpause.play()

def music():
    vmusic = pygame.mixer.Sound("sound/music.wav")
    #pygame.mixer.music.set_volume(0.8)
    vmusic.play(-1)
    pass

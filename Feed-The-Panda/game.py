#!/usr/bin/python

#Libraries import
import pygame
from pygame.locals import *
import sys
import time

#Local import
import ingredients
import inputOutput
import inputOutput
import requests
import sound

pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('Feed The Panda')
hat = False
hat_number = 0
fish = "0"
score = 0
score_update = False
size = 5
hauteur_bulle = 50
taille_bulle = 20

def text_draw(text, position, color, size):
    '''
        Création de texte à l'endroit que l'on souhaite.
    '''
    myfont = pygame.font.SysFont('Arial', size)
    textsurface = myfont.render(text, True, color)
    screen.blit(textsurface,position)

def drawSandwich(sandwich, x, y):
    '''
        Draw a sandwich at the specified coordonates
    '''
    global fish
    ingredientCount = len(sandwich)
    for i in range(ingredientCount - 1):
        imagePath = ingredients.getImage(sandwich[ingredientCount - 1 - i], fish)
        sprite = pygame.image.load(imagePath).convert_alpha()
        screen.blit(sprite, (x, y - i * 10))
    if ingredientCount > 0:
        imagePath = ingredients.getImage(sandwich[0], fish)
        sprite = pygame.image.load(imagePath).convert_alpha()
        screen.blit(sprite, (x, y - ingredientCount * 10))

# Partie drawing du panda

spritePanda=pygame.image.load('image/_3.png').convert_alpha()
lastChangedPanda=time.time()
wasHappy=False
def drawPanda():
    '''
        Draw the panda
    '''
    global spritePanda, lastChangedPanda, wasHappy
    screen.blit(spritePanda, (0,36))
    if int(time.time() - lastChangedPanda) > 0.5 and wasHappy:
        spritePanda=pygame.image.load('image/_miette.png').convert_alpha()
    if int(time.time() - lastChangedPanda) > 2:
        spritePanda=pygame.image.load('image/_3.png').convert_alpha()

def updatePanda(happy):
    '''
        Update panda sprite based on last result
    '''
    global spritePanda, lastChangedPanda, wasHappy
    wasHappy = happy
    if happy:
        spritePanda=pygame.image.load('image/_D.png').convert_alpha()
    else:
        spritePanda=pygame.image.load('image/_c.png').convert_alpha()
    lastChangedPanda=time.time()

def sadPanda():
    '''
        Update panda sprite to be sad (No please :'( )
    '''
    global spritePanda
    spritePanda=pygame.image.load('image/_sad.png').convert_alpha()


def affiche(time, xjauge, request, sandwich):
    '''
        Affiche les différentes images à l'écran.
        :time: temps du timer
    '''
    global hat, hat_number, score, spritePanda, taille_bulle, hauteur_bulle
    #screen.blit(jauge, (xjauge,0)) #Image de fond
    front_image = pygame.image.load('image/background'+fish+'.png').convert_alpha()
    screen.blit(front_image, (0,0)) #Image de fond
    pygame.draw.rect(screen, (95,225,156), (0,491,xjauge,9))

    #The panda
    drawPanda()

    if hat :
        hat_s = pygame.image.load('image/chapeau'+str(hat_number)+'.png').convert_alpha()
        screen.blit(hat_s, (0,36)) #Image de fond

    #The buble
    pygame.draw.rect(screen, (0,0,0), (245,hauteur_bulle+taille_bulle,155,taille_bulle))
    pygame.draw.rect(screen, (255,255,255), (248,hauteur_bulle+taille_bulle,149,taille_bulle))
    buble = pygame.image.load('image/bulleSolo.png').convert_alpha()
    screen.blit(buble, (245,110))
    buble2 = pygame.image.load('image/bulleSolo2.png').convert_alpha()
    if hauteur_bulle >= 0:
        screen.blit(buble2, (245,hauteur_bulle))
    else :
        pygame.draw.rect(screen, (0,0,0), (245,0,155,110))
        pygame.draw.rect(screen, (255,255,255), (248,0,149,110))

    #The plate
    plate = pygame.image.load('image/assiette.png').convert_alpha()
    screen.blit(plate, (230, 187))

    #The request in the buble
    drawSandwich(request, 255, 120)

    #The sandwich made
    drawSandwich(sandwich, 237, 310)

    #Timer
    s_timer = pygame.image.load('image/chrono.png').convert_alpha()
    screen.blit(s_timer, (0,0))
    text_draw(str(time), (15,17), (127,5,73), 20) #Timer
    text_draw(str(score), (115,17), (127,5,73), 20) #score

    #pygame.display.update()

#Array of the current made sandwich
currentHamburger=[]
request = 0
xjauge = 0

def add_ingredient(ingredient):
    global currentHamburger, request, xjauge, score, score_update, size
    currentHamburger.append(ingredient)
    if requests.isFinished(currentHamburger):
        correct = requests.isCorrect(request, currentHamburger)
        updatePanda(correct)
        if correct:
            sound.eat()
            #print("REUSSI")
            score_update = True
            xjauge += 50
            score += 10
            if xjauge > 400 :
                xjauge = 400
        else:
            #print("RATE")
            sound.wrong()
            if score != 0:
                score -= 10
        currentHamburger.clear()
        request = requests.getNew(size)
        #print(request)
    else :
        sound.food()

def tutorial():
    tuto_screen = 1
    current_time = 0
    xjauge = 400

    while tuto_screen <= 7:
        front_image = pygame.image.load('image/background'+fish+'.png').convert_alpha()
        screen.blit(front_image, (0,0)) #Image de fond
        pygame.draw.rect(screen, (95,225,156), (0,491,400,9))
        s_tuto = pygame.image.load('image/tuto'+str(tuto_screen)+'.png').convert_alpha()
        screen.blit(s_tuto, (0,0))
        pygame.display.update()

        if tuto_screen <= 3:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    tuto_screen += 1

        else :
            front_image = pygame.image.load('image/background'+fish+'.png').convert_alpha()
            screen.blit(front_image, (0,0)) #Image de fond
            pygame.draw.rect(screen, (95,225,156), (0,491,400,9))
            s_tuto = pygame.image.load('image/tuto'+str(tuto_screen)+'.png').convert_alpha()
            screen.blit(s_tuto, (0,0))
            pygame.display.update()
            tuto_screen += 1
            time.sleep(0.5)


def game():
    global currentHamburger, request, xjauge
    global taille_bulle, hauteur_bulle
    global hat, hat_number, fish, score_update, size, score

    size = 5
    #Requested sandwich
    request=requests.getNew(size)
    #print(request)

    #Variables
    current_time = -1 #Timer
    xjauge = 400 #position de la jauge
    time_difficultes = 0.5 #0.5 #Vitesse vide jauge
    time_on_pause = 0
    time_at_pause = 0
    nombre_skin = 6
    score = 0
    is_high = False
    hauteur_bulle = 50
    taille_bulle = 20

    start = int(time.time())
    click = False
    pause = False
    while xjauge > 0:
        mx, my = pygame.mouse.get_pos() #Position de la souris

        # Bouton
        b_top = pygame.Rect(0, 350, 180, 40)
        b_viande = pygame.Rect(0, 400, 180, 40)
        b_salade = pygame.Rect(0, 445, 180, 40)
        b_fromage = pygame.Rect(200, 350, 180, 40)
        b_tomate = pygame.Rect(200, 400, 180, 40)
        b_bottom = pygame.Rect(200, 445, 180, 40)

        if score % 100 == 0 and score != 0 and score_update:
            size += 1 #Vitesse vide jauge
            score_update = False
            taille_bulle += 20
            hauteur_bulle -= 15
            request=requests.getNew(size)

        if int(time.time()-start) != current_time and not pause: #Timer
            current_time = int(time.time()) - start - time_on_pause

        if int(time.time()-start) != current_time/2 and not pause: #Jauge toute les demis secondes
            xjauge -= time_difficultes

        # clique sur les boutons
        if b_top.collidepoint((mx, my)) : # Haut du pain
            if click :
                add_ingredient(0)
        if b_viande.collidepoint((mx, my)) : # Viande
            if click :
                add_ingredient(4)
        if b_salade.collidepoint((mx, my)) : # Salade
            if click :
                add_ingredient(3)
        if b_fromage.collidepoint((mx, my)) : # Fromage
            if click :
                add_ingredient(2)
        if b_tomate.collidepoint((mx, my)) : # Tomate
            if click :
                add_ingredient(5)
        if b_bottom.collidepoint((mx, my)) : # bas du pain
            if click :
                add_ingredient(1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not pause:
                if event.button == 1:
                    click = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE :
                    if pause :
                        sound.reverse_pause()
                        pause = False
                        time_on_pause += (int(time.time()) - time_at_pause)
                    else :
                        sound.pause()
                        pause = True
                        time_at_pause = int(time.time())
                        affiche(current_time, xjauge, request, currentHamburger)
                        front_image = pygame.image.load('image/pause.png').convert_alpha()
                        screen.blit(front_image, (0,0)) #Image de fond
                        pygame.display.update()

                # Skins
                elif event.key == K_UP :
                    sound.change()
                    hat = True
                    hat_number += 1
                    if hat_number > nombre_skin :
                        hat_number = 1
                elif event.key == K_DOWN :
                    sound.change()
                    hat = True
                    hat_number -= 1
                    if hat_number <= 0 :
                        hat_number = nombre_skin
                elif event.key == K_LEFT : # Remove all
                    sound.change()
                    hat = False
                    fish = "0"
                elif event.key == K_RIGHT : # Saumon
                    sound.change()
                    if fish == "1" :
                        fish = "0"
                    else :
                        fish = "1"

                elif not pause :
                    # ingredient/request gestion
                    ingredient=inputOutput.translateToIngredient(event)
                    #print(ingredients.getName(ingredient))
                    if ingredient != ingredients.UNKNOW_INGREDIENT:
                        add_ingredient(ingredient)

        if not pause :
            affiche(current_time, xjauge, request, currentHamburger)
            pygame.display.update()

    sadPanda()
    affiche(current_time, xjauge, request, currentHamburger)

    # ouvrir fichier score, regarder si on est le meilleur
    # si meilleur -> True

    file_open = open("highscore.txt", "r")
    highscore = int(file_open.read())

    if highscore < score:
        is_high = True
        file_open = open("highscore.txt", "w")
        file_open.write(str(score))
    else :
        is_high = False

    pygame.display.update()

    return score, current_time, is_high

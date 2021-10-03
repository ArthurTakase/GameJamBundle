import pygame
from pygame.locals import *
import time
import sys
import game
import sound

pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('Feed The Panda')

def intro():
    splash = pygame.image.load('image/Splash.png').convert_alpha()
    screen.blit(splash, (0,0)) #Image de fond
    pygame.display.update()
    time.sleep(1)
    for i in range(0,30):
        pygame.draw.rect(screen, (36,35,35), (0,0,400,500))
        screen.blit(splash, (0,0)) #Image de fond
        pygame.draw.rect(screen, (36,35,35), (0,0,400,0+(i*20)))
        pygame.display.update()
        time.sleep(0.03)
    thanks = pygame.image.load('image/thanks.png').convert_alpha()
    screen.blit(thanks, (0,0)) #Image de fond
    sound.splash()
    pygame.display.update()
    time.sleep(1)

def anime_credit():
    nappe = pygame.image.load('image/credit.png').convert_alpha()
    for i in range(0,25):
        screen.blit(nappe, (0,500-(i*20))) #Image de fond
        pygame.display.update()
        time.sleep(0.02)

def anime_credit_back():
    nappe = pygame.image.load('image/credit.png').convert_alpha()
    start_menu = pygame.image.load('image/start_menu.png').convert_alpha()
    #screen.blit(nappe, (0,0)) #Image de fond
    for i in range(0,25):
        screen.blit(start_menu, (0,0)) #Image de fond
        screen.blit(nappe, (0,0+(i*20))) #Image de fond
        pygame.display.update()
        time.sleep(0.02)

def credit():
    anime_credit()

    while 1:
        mx, my = pygame.mouse.get_pos()

        nappe = pygame.image.load('image/credit.png').convert_alpha()
        screen.blit(nappe, (0,0)) #Image de fond

        button_retour = pygame.Rect(0, 0, 100, 60)

        if button_retour.collidepoint((mx, my)) :
            if click :
                sound.select()
                anime_credit_back()
                main()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def game_over(score, time_final, high):
    nappe = pygame.image.load('image/background_nappe.png').convert_alpha()
    time.sleep(2)
    for i in range(0,25):
        screen.blit(nappe, (0,500-(i*20))) #Image de fond
        pygame.display.update()
        time.sleep(0.03)

    while 1:
        mx, my = pygame.mouse.get_pos()

        nappe = pygame.image.load('image/background_nappe.png').convert_alpha()
        screen.blit(nappe, (0,0))
        if high :
            game_over = pygame.image.load('image/high.png').convert_alpha()
            screen.blit(game_over, (0,0)) #Image de fond
        else :
            game_over = pygame.image.load('image/gameover.png').convert_alpha()
            screen.blit(game_over, (0,0)) #Image de fond

        button_restart = pygame.Rect(60, 325, 135, 40)
        button_menu = pygame.Rect(207, 325, 135, 40)

        file_open = open("highscore.txt", "r")
        highscore = int(file_open.read())

        text_size = 40
        game.text_draw(str(time_final), (290-(len(str(time_final))*(text_size/2)),200), (127,5,73), text_size) #Timer
        game.text_draw(str(score), (150-(len(str(score))*(text_size/2)),200), (127,5,73), text_size) #Score
        game.text_draw(str(highscore), (220-(len(str(highscore))*(text_size/2)),275), (127,5,73), text_size) #HighScore

        if button_restart.collidepoint((mx, my)) :
            if click :
                for i in range(4,8):
                    front_image = pygame.image.load('image/background0.png').convert_alpha()
                    screen.blit(front_image, (0,0)) #Image de fond
                    s_tuto = pygame.image.load('image/tuto'+str(i)+'.png').convert_alpha()
                    screen.blit(s_tuto, (0,0))
                    pygame.display.update()
                    time.sleep(0.5)

                game.game()

        if button_menu.collidepoint((mx, my)) :
            if click :
                main()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def main():
    loop = True
    while loop:
        mx, my = pygame.mouse.get_pos()

        start_menu = pygame.image.load('image/start_menu.png').convert_alpha()
        screen.blit(start_menu, (0,0)) #Image de fond

        button_start = pygame.Rect(150,370, 100, 40)
        button_credit = pygame.Rect(135,430, 140, 40)

        if button_start.collidepoint((mx, my)) :
            if click :
                sound.start()
                game.tutorial()
                score, time_final, high = game.game()
                game_over(score, time_final, high)

        if button_credit.collidepoint((mx, my)) :
            if click :
                sound.select()
                credit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT :
                loop = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

    pygame.quit()
    sys.exit()

intro()
sound.music()
main()

import pygame
from pygame import *
import jeu

mixer.init()
pygame.init()

mixer.music.load("musique/menujeu2.ogg")
mixer.music.play()

blanc = (255,255,255)
size = width, height = 800, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("pendu xd")

bg = pygame.image.load('imagefond.jpg')
bg2 = pygame.image.load('menufond2.jpg')
bg3 = pygame.image.load('difficulterfond.jpg')
bg4 = pygame.image.load('gagner.jpg')
bg5 = pygame.image.load('perdu.jpg')

p0 = pygame.image.load("erreur0.png")
p1 = pygame.image.load('erreur1.png')
p2 = pygame.image.load('erreur2.png')
p3 = pygame.image.load('erreur3.png')
p4 = pygame.image.load('erreur4.png')
p5 = pygame.image.load('erreur5.png')
p6 = pygame.image.load('erreur6.png')
p7 = pygame.image.load('erreur7.png')

kk = [ p0, p1, p2, p3, p4, p5, p6, p7]

font = pygame.font.Font('BradBunR.ttf',180)
font1 = pygame.font.Font('BradBunR.ttf',55)
font3 = pygame.font.Font('BradBunR.ttf',100)
font6 = pygame.font.Font('BradBunR.ttf',25)
erreur = 0

class pendu:

    def rafraichir():
        erreur = 0
        bite = [""]


    def Perdu():
        jfoe

    def Gagner():
        screen.blit(bg4,[0,0])
        e = font1.render("Rejouer",1,blanc)
        pt3 = font6.render("(Push Echap)",1,blanc)
        screen.blit(e,(0,500))
        screen.blit(pt3,(160,525))

    def errorlettre(erreur) :
        screen.blit(kk[erreur],[0,0])

    def hard(erreur):
        screen.blit(bg3,[0,0])
        pendu.errorlettre(erreur)
        mC1 = font3.render(motCacher,1,blanc)
        screen.blit(mC1,(100,100))

    def medium(erreur):
        screen.blit(bg3,[0,0])
        pendu.errorlettre(erreur)
        mC2 = font3.render(motCacher,1,blanc)
        screen.blit(mC2,(200,200))


    def easy(erreur):
        screen.blit(bg3,[0,0])
        pendu.errorlettre(erreur)
        mC3 = font3.render(motCacher,1,blanc)
        screen.blit(mC3,(200,200))

    def accueil():
        Gt = font.render("PENDU",1,blanc)
        Pt = font1.render("Appuyer sur espace pour continuer",1,blanc)
        screen.blit(bg,[0,0])
        screen.blit(Gt,(200,-50))
        screen.blit(Pt,(40,500))

    def main():
        Gt1 = font.render("Main",1,blanc)
        Pt1 = font3.render("Easy",1,blanc)
        Pt2 = font3.render("Medium",1,blanc)
        Pt3 = font3.render("Hard",1,blanc)
        pt = font6.render("(Push 1)",1,blanc)
        pt1 = font6.render("(Push 2)",1,blanc)
        pt2 = font6.render("(Push 3)",1,blanc)
        screen.blit(bg2,[0,0])
        screen.blit(Gt1,(250,-50))
        screen.blit(Pt1,(50,250))
        screen.blit(Pt2,(50, 350))
        screen.blit(Pt3,(50, 450))
        screen.blit(pt,(220,300))
        screen.blit(pt1,(300,400))
        screen.blit(pt2,(220,500))

continuer = 1
partie = 'intro'
motCacher=""
motATrouver=""

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        if partie == 'intro' and event.type == pygame.KEYDOWN and event.key == K_SPACE:
            partie = 'menu'
        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP1:
            partie = 'easy'
            mot = jeu.motChoisi(1)
            motCacher = mot[0]
            motATrouver = mot[1]
        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP2:
            partie = 'medium'
            mot = jeu.motChoisi(2)
            motCacher = mot[0]
            motATrouver = mot[1]
        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP3:
            partie = 'hard'
            mot = jeu.motChoisi(3)
            motCacher = mot[0]
            motATrouver = mot[1]
        if partie == 'easy' or partie == 'medium' or partie == 'hard' or partie == 'Gagner' or partie == 'rafraichir':
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    partie = 'menu'
                lettre= event.dict['unicode']
                if 'a' <= lettre <= 'z':
                    lettre= event.dict['unicode']
                    bite = jeu.jeu(erreur,lettre,motATrouver,motCacher)
                    if type(bite) == bool:
                        print("perdu")
                    if type(bite) == tuple :
                        if len (bite) == 3 :
                            erreur = bite [0]
                            motCache = bite[2]
                            motCacher = "".join(motCache)
                        if len(bite) == 2:
                            partie = "Gagner"
                            motCache = bite[1]
                            motCacher = "".join(motCache)







    if partie == 'intro':
        pendu.accueil()
    elif partie == 'menu':
        pendu.main()
    elif partie == 'easy':
        pendu.easy(erreur)
    elif partie == 'medium':
        pendu.medium(erreur)
    elif partie == 'hard':
        pendu.hard(erreur)
    elif partie == 'Gagner':
        pendu.Gagner()
    elif partie == 'rafraichir':
        pendu.rafraichir()

    pygame.display.flip()

pygame.quit()
quit()
import pygame ##importation de la bibliothèque
from pygame.locals import *
pygame.init()##initialiser la bibliothèque pygame
blanc = (255,255,255)
fenetre= pygame.display.set_mode((640,480))##création de la fenêtre et ouveture de ka fenêtre pygame
font = pygame.font.Font('BradBunR.ttf',100)
Gt = font.render("Menu",1,blanc)
fond= pygame.image.load("background.jpg")##chargement et collage du fond
fenetre.blit(fond,[0,0])
fenetre.blit(Gt,(230,150)) ##collage du fond##rafraichissement de l'écran
pygame.display.flip()

class pipopipette:

    def accueil():
        Gt = font.render("Pipopette",1,blanc)
        Pt = font1.render("Appuyer sur espace pour continuer",1,blanc)
        screen.blit(bg,[0,0])
        screen.blit(Gt,(200,-50))
        screen.blit(Pt,(40,500))


pygame.display.flip()

continuer = 1

while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

pygame.display.flip()

import pygame ##importation de la bibliothèque
from pygame.locals import *
pygame.init()##initialiser la bibliothèque pygame
blanc = (255,255,255)
fenetre= pygame.display.set_mode((1280,720))##création de la fenêtre et ouveture de ka fenêtre pygame
font = pygame.font.Font('BradBunR.ttf',200)
Gt = font.render("Pipopette",1,blanc)
fond= pygame.image.load("background.jpeg")##chargement et collage du fond
fenetre.blit(fond,[0,0])
fenetre.blit(Gt,(360,100)) ##collage du fond##rafraichissement de l'écran
pygame.display.flip()

continuer = 1

while continuer:

	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

pygame.display.flip()



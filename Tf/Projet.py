import pygame                                                                       ##importation de la bibliothèque
from pygame.locals import *

pygame.init()
                                                                                  ##initialiser la bibliothèque pygame
blanc = (255,255,255)
vertdeau= (206,255,212)
jaune=(255,233,127)
bleu=(63,100,127)
bordeau=(124,47,73)

fenetre= pygame.display.set_mode((1280,720))
                                                                                        ##création de la fenêtre et ouveture de ka fenêtre pygame
ecriture = pygame.font.Font('BradBunR.ttf',200)
ecriture1 = pygame.font.Font('BradBunR.ttf',160)
ecriture2= pygame.font.Font('BradBunR.ttf',60)
ecriture3=pygame.font.Font('BradbunR.ttf',80)
ecriture4=pygame.font.Font('BradbunR.ttf',40)
ecriture5=pygame.font.Font('bradbunR.ttf',30)

fond= pygame.image.load("background.jpeg")                                              ##chargement et collage du fond
fond1=pygame.image.load("background2.jpeg")                                                        ##collage du fond##rafraichissement de l'écran
fond2=pygame.image.load("background3.jpeg")


def accueil():
        fenetre.blit(fond,[0,0])
        Gt = ecriture.render("Pipopipette",1,blanc)
        Pt = ecriture2.render("Appuyez sur espace pour continuer",1,blanc)
        fenetre.blit(Gt,(360,100))
        fenetre.blit(Pt,(400,580))


def menu():
        fenetre.blit(fond1,[0,0])
        Gt = ecriture1.render("Menu",1,blanc)
        Pt = ecriture2.render("Easy (push 1)",1,blanc)
        Ht=ecriture2.render("Medium (push 2)",1,blanc)
        Jt=ecriture2.render("Hard (push 3)",1,blanc)
        Kt=ecriture2.render("Règle du jeu (push 4)",1,blanc)
        fenetre.blit(Gt,(500,20))
        fenetre.blit(Pt,(150,250))
        fenetre.blit(Ht,(150,350))
        fenetre.blit (Jt,(150,450))
        fenetre.blit (Kt,(150,550))


def easy():
    fenetre.fill(vertdeau)



def medium():
    fenetre.fill(jaune)


def hard():
    fenetre.fill (bleu)


def regle():
    fenetre.fill(bordeau)
    Wt=ecriture4.render("Chacun votre tour, positionnez un trait de votre couleur sur la grille dans le",1,blanc)
    Xt=ecriture4.render("but d'obtenir un carré. Un carré = 1 point",1,blanc)

    Ct=ecriture1.render("Attention!!",1,blanc)
    Lt=ecriture4.render("Il faut mettre en place une stratégie afin d’obtenir le plus de carré. ",1,blanc)
    Mt=ecriture4.render("Ce n’est pas celui qui a le plus de trait qui obtient le carré ",1,blanc)
    Qt=ecriture4.render("mais celui qui arrive à le fermer en premier.",1,blanc)
    Vt=ecriture5.render("retour au menu (echap)",1,blanc)

    fenetre.blit(Ct,(70,150))
    fenetre.blit(Wt,(70,50))
    fenetre.blit(Xt,(70,100))
    fenetre.blit(Lt,(70,300))
    fenetre.blit(Mt,(70,350))
    fenetre.blit(Qt,(70,400))
    fenetre.blit(Vt,(1000,500))


continuer = 1
partie = 'intro'

while continuer:

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
        if partie == 'intro' and event.type == pygame.KEYDOWN and event.key == K_SPACE:
            partie = 'menu'
        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP1:
            partie = 'easy'

        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP2:
            partie = 'medium'

        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP3:
            partie = 'hard'

        if partie == 'menu' and event.type == pygame.KEYDOWN and event.key == K_KP4:
            partie = 'regle'

        if partie == 'easy' or partie == 'medium' or partie == 'hard' or partie == 'regle':
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    partie = 'menu'

        if partie == 'intro':
            accueil()
        elif partie == 'menu':
            menu()
        elif partie == 'easy':
            easy()
        elif partie == 'medium':
            medium()
        elif partie =='hard':
            hard()
        elif partie== 'regle':
            regle()


pygame.quit()
quit()



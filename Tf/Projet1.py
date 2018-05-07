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
        gt = ecriture.render("Pipopipette",1,blanc)
        pt = ecriture2.render("Appuyez sur espace pour continuer",1,blanc)
        fenetre.blit(gt,(360,100))
        fenetre.blit(pt,(400,580))


def menu():
        fenetre.blit(fond1,[0,0])
        gt = ecriture1.render("Menu",1,blanc)
        pt = ecriture2.render("Easy (push 1)",1,blanc)
        ht=ecriture2.render("Medium (push 2)",1,blanc)
        jt=ecriture2.render("Hard (push 3)",1,blanc)
        kt=ecriture2.render("Règle du jeu (push 4)",1,blanc)
        fenetre.blit(gt,(500,20))
        fenetre.blit(pt,(150,250))
        fenetre.blit(ht,(150,350))
        fenetre.blit (jt,(150,450))
        fenetre.blit (kt,(150,550))


def easy():
    fenetre.fill(vertdeau)
    at=ecriture3.render("Grille facile",1,blanc)
    vt=ecriture5.render("retour au menu (echap)",1,blanc)

    fenetre.blit(at,(500,50))
    fenetre.blit(vt,(550,150))



def medium():
    fenetre.fill(jaune)
    bt=ecriture3.render("Grille intermédiaire",1,blanc)
    vt=ecriture5.render("retour au menu (echap)",1,blanc)

    fenetre.blit(bt,(400,50))
    fenetre.blit(vt,(525,150))


def hard():
    fenetre.fill (bleu)
    zt=ecriture3.render("Grille difficile",1,blanc)
    vt=ecriture5.render("retour au menu (echap)",1,blanc)

    fenetre.blit(zt,(450,50))
    fenetre.blit(vt,(500,150))



def regle():
    fenetre.fill(bordeau)
    wt=ecriture4.render("Chacun votre tour, positionnez un trait de votre couleur sur la grille dans le",1,blanc)
    xt=ecriture4.render("but d'obtenir un carré. Un carré = 1 point",1,blanc)

    ct=ecriture1.render("Attention!!",1,blanc)
    lt=ecriture4.render("Il faut mettre en place une stratégie afin d’obtenir le plus de carré. ",1,blanc)
    mt=ecriture4.render("Ce n’est pas celui qui a le plus de trait qui obtient le carré ",1,blanc)
    qt=ecriture4.render("mais celui qui arrive à le fermer en premier.",1,blanc)
    vt=ecriture5.render("retour au menu (echap)",1,blanc)

    fenetre.blit(ct,(70,150))
    fenetre.blit(wt,(70,50))
    fenetre.blit(xt,(70,100))
    fenetre.blit(lt,(70,300))
    fenetre.blit(mt,(70,350))
    fenetre.blit(qt,(70,400))
    fenetre.blit(vt,(1000,500))


def nom():
    f = ecriture2.render("Joueur 1 entrer pseudo",2,blanc)
    e = ecriture2.render(pseudo[0],2,blanc)
    r =ecriture4.render('Appuyer sur "entrée"',2,blanc)

    p = ecriture2.render("Joueur 2 entrer votre pseudo ",2,blanc)
    z = ecriture2.render(pseudo[1],2,blanc)                                                          # # Défintion de l'écran pour entrer le pseudo


    fenetre.blit(r,(0,400))
    fenetre.blit(f,(0,250))
    fenetre.blit(e,(200,320))

    fenetre.blit(p,(0,370))
    fenetre.blit(z,(200,420))
    return pseudo



continuer = 1
partie = 'intro'
pseudo = ['', '']
currentPseudo = 0

while continuer:

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



        if partie == 'easy' or partie == 'medium' or partie == 'hard' :
            nom()
            if event.type == pygame.KEYDOWN :
                lettre = event.dict["unicode"]
                if 'a' <= lettre <= 'z' :
                    lettre = event.dict['unicode']      # Le joeur entre son pseudo
                    pseudo[currentPseudo]  = pseudo[currentPseudo] + lettre
                elif event.key == K_RETURN:
                    print("space")
                    if currentPseudo == 0:
                        currentPseudo = 1
                    elif currentPseudo == 1:
                        print("c'est gagné")

        pygame.display.flip()

pygame.quit()
quit()



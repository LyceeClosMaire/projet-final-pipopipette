import pygame,os
pygame.init()

QUIT = 1
size = width, height = 1024, 720
black = 0, 0, 0
white = (255,0,255)
gride = [((0,0),(720,720)),((725,0),(720,720)),((0,725),(720,720))]

screen = pygame.display.set_mode(size)

screen.fill((149, 191, 96))
gamezone=pygame.Rect((0,0),(720,720))
pygame.draw.rect(screen,white,gamezone)

feuille = pygame.image.load(os.path.abspath("P:\Pictures\spriteGride.png"))
img = feuille.subsurface(pygame.Rect(gride[1]))
rectangle = img.get_rect(topleft=(0,0))

screen.blit(img,rectangle)

while QUIT:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = 0



    pygame.display.flip()

pygame.quit()
import pygame,os
pygame.init()

QUIT = 1
size = width, height = 1280, 720
black = 0, 0, 0
white = (255,255,255)


screen = pygame.display.set_mode(size)

screen.fill((149, 191, 96))
rectangle=pygame.Rect((0,0),(720,720))
img = pygame.image.load(os.path.abspath("P:\Downloads\kani_sushi.png"))
screen.blit(img,rectangle)

while QUIT:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            QUIT = 0



    pygame.display.flip()

pygame.quit()
import pygame

WIDTH = 600
HEIGHT = 600

pygame.font.init()

SCREEN =  pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pygame matching game")

BLACK = (0,0,0)

SCREEN.fill("pink")
pygame.display.update()

img1_1 = pygame.image.load('Hd2 logo.jpg')
img2_1= pygame.image.load('assassins creedlogo.png')
img3_1 = pygame.image.load('krimlogo.png')
img4_1 = pygame.image.load('nmslogo.jpg')

img1 = pygame.transform.scale(img1_1,(75,75))
img2 = pygame.transform.scale(img2_1,(75,75))
img3 = pygame.transform.scale(img3_1,(75,75))
img4 = pygame.transform.scale(img4_1,(75,75))

SCREEN.blit(img1,(100,100))
SCREEN.blit(img2,(100,200))
SCREEN.blit(img3,(100,300))
SCREEN.blit(img4,(100,400))

font = pygame.font.SysFont("Times New Roman",36)

txt_1 = font.render("HellDivers 2",True,(0,0,0))
SCREEN.blit(txt_1,(350,125))

txt_2 = font.render("assasins creed",True,(0,0,0))
SCREEN.blit(txt_2,(350,225))

txt_3 = font.render("No Man's Sky",True,(0,0,0))
SCREEN.blit(txt_3,(350,325))

txt_4 = font.render("Skyrim",True,(0,0,0))
SCREEN.blit(txt_4,(350,425))

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN,(0,0,0),pos,10,0)

        if event.type == pygame.MOUSEBUTTONUP:
            pos_2 = pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN,(0,0,0),pos_2,10,0)
            pygame.draw.line(SCREEN,(0,0,0),pos,pos_2)
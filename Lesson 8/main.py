import pygame

WIDTH = 600
HEIGHT = 600

pygame.font.init()

SCREEN =  pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pygame matching game")

BLACK = (0,0,0)

SCREEN.fill("pink")
pygame.display.update()

candycrush_img = pygame.image.load('candycrush.jpg')
ludo_img = pygame.image.load('ludo.png')
subwayserfers_img = pygame.image.load('subwayserfers.png')
templerun_img = pygame.image.load('tmplerun.png')

SCREEN.blit(candycrush_img,(100,100))
SCREEN.blit(ludo_img,(100,200))
SCREEN.blit(subwayserfers_img,(100,300))
SCREEN.blit(templerun_img,(100,400))

font = pygame.font.SysFont("Times New Roman",36)

candycrush_txt = font.render("Ludo",True,(0,0,0))
SCREEN.blit(candycrush_txt,(350,125))

ludo_txt = font.render("temple run",True,(0,0,0))
SCREEN.blit(ludo_txt,(350,225))

subwayserfers_txt = font.render("Candy Crush",True,(0,0,0))
SCREEN.blit(subwayserfers_txt,(350,325))

templerun_txt = font.render("Subway Serfers",True,(0,0,0))
SCREEN.blit(templerun_txt,(350,425))






while True:
    pygame.display.update()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:        #mouse click down
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN,(0,0,0),pos,10,0)

        if event.type == pygame.MOUSEBUTTONUP:
            pos_2 = pygame.mouse.get_pos()
            pygame.draw.circle(SCREEN,(0,0,0),pos_2,10,0)
            pygame.draw.line(SCREEN,(0,0,0),pos,pos_2)

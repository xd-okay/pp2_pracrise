import pygame

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("plz 1 point")

x,y=100,100
running = True

square = pygame.Surface((1000,1000))
square.fill((255,255,255))

while running:
    
    screen.blit(square,(0,0))
    pygame.draw.circle(screen, 'red', (x,y), 25)
    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running =False
            pygame.quit() 
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if(y+45<=600):
                    y+=20
            elif event.key == pygame.K_UP:
                if(y-45>=0):
                    y-=20
            elif event.key == pygame.K_LEFT:
                if(x-45>=0):
                    x-=20
            elif event.key == pygame.K_RIGHT:
                if(x+45<=800):
                    x+=20
                    
                
            
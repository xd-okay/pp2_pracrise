import pygame
import datetime

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("plz 1 point")
mickey_img=pygame.image.load("mickeys_hand.png").convert_alpha()
face_img=pygame.image.load("images.png").convert_alpha()

square= square = pygame.Surface((1000,1000))
square.fill((0,0,0))


running = True

while running:
    
    screen.blit(square,(0,0))
    screen.blit(face_img, (130,0))
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    lh_angle=-6*seconds
    rh_angle=-6*minutes
    
    
    rotated_image = pygame.transform.rotate(mickey_img, lh_angle)    
    screen.blit(rotated_image, (90,105))
    
    rotated_image = pygame.transform.rotate(mickey_img, rh_angle)    
    screen.blit(rotated_image, (300,105))
    
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running =False
            pygame.quit()   
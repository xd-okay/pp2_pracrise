import pygame
import os



pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("My playlist plz 1 point")

os.chdir("pp2_pracrise/Practice9/music")
track_list=os.listdir()
tracks_counts=len(track_list)
current_index = 0
is_playing = False
total_length=1

square= square = pygame.Surface((1000,1000))
square.fill((0,0,0))

running = True
while running:
    current_time = pygame.mixer.music.get_pos() / 1000
    circle_position=(current_time*400)/total_length+50
    
    pygame.draw.line(screen, 'white', (50, 180), (450, 180), 3)
    pygame.draw.circle(screen, 'white', (int(circle_position), 180), 6 )
    if(is_playing==True):
        pygame.display.set_caption(track_list[current_index])
    else:
        pygame.display.set_caption(f"Paused {track_list[current_index]}")
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                pygame.mixer.music.load(track_list[current_index]) 
                pygame.mixer.music.play()
                is_playing=True
                sound = pygame.mixer.Sound(track_list[current_index])
                total_length = sound.get_length()
                screen.blit(square,(0,0))
            elif event.key==pygame.K_s:
                pygame.mixer.music.stop()
                is_playing=False
            elif event.key==pygame.K_n:
                if(current_index==tracks_counts-1):
                    current_index=0
                else:
                    current_index+=1
                pygame.mixer.music.load(track_list[current_index]) 
                pygame.mixer.music.play()
                is_playing=True
                screen.blit(square,(0,0))
            elif event.key==pygame.K_b:
                if(current_index==0):
                    current_index=tracks_counts-1
                else:
                    current_index-=1
                pygame.mixer.music.load(track_list[current_index]) 
                pygame.mixer.music.play()
                is_playing=True
                screen.blit(square,(0,0))
            elif event.key==pygame.K_q:
                running=False
                pygame.quit()
                
                
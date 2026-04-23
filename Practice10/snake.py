import random
import pygame 
from pygame import * 
pygame.init() 
#Прокомментировал
screen = pygame.display.set_mode((600,400)) 

lvl=1
running = True 
score=0
x = 50 
y = 50 

fruit_color = (200,120,0) 
snake_color = (50,200,50) 

segments = [[50,50],[60,50],[70,50],[80,50]]

dir = "r" 

fruit = [random.randint(0,59)*10,random.randint(0,39)*10] 
eaten = False 

image_lib = {} 

def load_image(path): 
    loaded_image = image_lib.get(path) 
    if loaded_image == None: 
        loaded_image = pygame.image.load(path) 
        image_lib[path] = loaded_image 
    return loaded_image 

# pygame.mixer.music.load("open-source-lab-dreamy-times-358804.mp3") 
# pygame.mixer.music.play() 

sfx_lib = {} 

def load_sfx(path): 
    sfx = sfx_lib.get(path) 
    if sfx == None: 
        sfx = pygame.mixer.Sound(path) 
        sfx_lib[path] = sfx 
    return sfx 

while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
            snake_color = (255,0,0) 
            # load_sfx("gc.wav").play() 

    klava = pygame.key.get_pressed() 

    

    if klava[K_UP] and dir !="d": 
        dir = "u" 
    elif klava[K_DOWN] and dir !="u": 
        dir = "d" 
    elif klava[K_LEFT] and dir !="r": 
        dir = "l" 
    elif klava[K_RIGHT] and dir !="l": 
        dir = "r" 

    x = segments[-1][0] 
    y = segments[-1][1] 

    if dir == "r": 
        segments[-1][0]+=10 
    if dir == "l": 
        segments[-1][0]-=10 
    if dir == "u": 
        segments[-1][1]-=10 
    if dir == "d": 
        segments[-1][1]+=10 

    if segments[-1][0] == fruit[0] and segments[-1][1] == fruit[1]: 
        eaten = True 
        fruit[0]=random.randint(0, 59) * 10
        fruit[1]=random.randint(0, 39) * 10
        score+=1
        lvl=int(score/4)
        segments.insert(0, [0,0])
    
    
    if segments[-1][0] == 0 or segments[-1][1] == 0 or segments[-1][0] == 600 or segments[-1][1] == 400:
           running = False
    for i in range(0,len(segments)-2): 
        if segments[-1][0] == segments[i][0] and segments[-1][1] == segments[i][1]:
            running = False

    # if running == False:
    #     font = pygame.font.SysFont("times new roman",20) 
    #     text = font.render("GAME OVER",True,(0,0,0)) 

    #     screen.blit(text,(200,200)) 
        
        




    for i in range(0,len(segments)-1): 
        segments[i][0] = segments[i+1][0] 
        segments[i][1] = segments[i+1][1] 

    segments[len(segments)-2][0] = x 
    segments[len(segments)-2][1] = y 

    screen.fill((255,255,255)) 

    # screen.blit(load_image("wall.png"),(200,200)) 

    for segment in segments: 
        pygame.draw.rect(screen,snake_color,pygame.Rect(segment[0],segment[1],9,9)) 

    # if not eaten: 
    pygame.draw.rect(screen,fruit_color,pygame.Rect(fruit[0],fruit[1],9,9)) 

    font = pygame.font.SysFont("times new roman",20) 
    text = font.render("Score: "+str(score),True,(0,0,0))
    screen.blit(text,(200,0))
    text = font.render("lvl: "+str(lvl),True,(0,0,0))
    screen.blit(text,(200,40))
    pygame.time.Clock().tick((lvl*3)+15) 
    pygame.display.flip()
import random
import pygame 
from pygame import * # Инициализация Pygame
pygame.init() 

# Настройка окна
screen = pygame.display.set_mode((600, 400)) 
clock = pygame.time.Clock()

# Глобальные переменные
lvl = 0
running = True 
score = 0
snake_color = (50, 200, 50) 
segments = [[50, 50], [60, 50], [70, 50], [80, 50]] # Начальное тело змейки
dir = "r" # Текущее направление

# --- Параметры еды ---
def spawn_fruit():
    """Функция для генерации новой еды с весом и таймером"""
    x = random.randint(0, 59) * 10
    y = random.randint(0, 39) * 10
    
    # Веса: 1 (обычный), 2 (редкий), 3 (супер)
    # 70% шанс - вес 1, 20% - вес 2, 10% - вес 3
    rand_val = random.random()
    if rand_val < 0.7:
        weight = 1
        color = (200, 120, 0) # Оранжевый
    elif rand_val < 0.9:
        weight = 2
        color = (255, 255, 0) # Желтый
    else:
        weight = 3
        color = (255, 0, 0)   # Красный
        
    # Таймер жизни еды (в кадрах). Например, 100 кадров.
    timer = 100 
    return [x, y, weight, color, timer]

# Инициализация первой еды: [x, y, weight, color, timer]
fruit = spawn_fruit()

# --- Основной цикл игры ---
while running: 
    # 1. Обработка событий
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
            snake_color = (255, 0, 0) 

    # 2. Управление (Клавиатура)
    klava = pygame.key.get_pressed() 
    if (klava[K_w] or klava[K_UP]) and dir != "d": 
        dir = "u" 
    elif (klava[K_s] or klava[K_DOWN]) and dir != "u": 
        dir = "d" 
    elif (klava[K_a] or klava[K_LEFT]) and dir != "r": 
        dir = "l" 
    elif (klava[K_d] or klava[K_RIGHT]) and dir != "l": 
        dir = "r" 

    # Сохраняем позицию головы перед движением
    head_x = segments[-1][0] 
    head_y = segments[-1][1] 

    # 3. Логика движения головы
    if dir == "r": head_x += 10 
    if dir == "l": head_x -= 10 
    if dir == "u": head_y -= 10 
    if dir == "d": head_y += 10 

    # Добавляем новую голову
    segments.append([head_x, head_y])

    # 4. Проверка столкновения с едой
    if head_x == fruit[0] and head_y == fruit[1]: 
        score += fruit[2]         # Увеличиваем счет на вес еды
        lvl = int(score / 10)     # Повышаем уровень
        # Удлиняем змейку на величину веса (один сегмент уже добавили, добавляем остальные)
        for _ in range(fruit[2] - 1):
            segments.insert(0, segments[0][:])
        fruit = spawn_fruit()     # Создаем новую еду
    else:
        # Если еду не съели, удаляем хвост (обычное движение)
        segments.pop(0)

    # 5. Логика таймера еды
    fruit[4] -= 1 # Уменьшаем таймер на каждом кадре
    if fruit[4] <= 0:
        fruit = spawn_fruit() # Еда исчезает и появляется в новом месте

    # 6. Проверка столкновений (стены и хвост)
    # Стены
    if head_x < 0 or head_x >= 600 or head_y < 0 or head_y >= 400:
        running = False
    
    # Самоедство (проверяем голову против всех сегментов кроме самой головы)
    for segment in segments[:-1]:
        if head_x == segment[0] and head_y == segment[1]:
            running = False

    # 7. Отрисовка
    screen.fill((255, 255, 255)) 

    # Рисуем еду (размер зависит от веса для наглядности)
    pygame.draw.rect(screen, fruit[3], pygame.Rect(fruit[0], fruit[1], 9, 9)) 

    # Рисуем змейку
    for segment in segments: 
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0], segment[1], 9, 9)) 

    # Интерфейс (Счет, Уровень, Таймер еды)
    font = pygame.font.SysFont("times new roman", 20) 
    score_text = font.render(f"Score: {score}  Lvl: {lvl}", True, (0, 0, 0))
    timer_text = font.render(f"Food Timer: {fruit[4]}", True, (150, 0, 0))
    
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (10, 30))

    # Настройка скорости игры (растет с уровнем)
    clock.tick(15 + lvl * 2) 
    pygame.display.flip()

pygame.quit()
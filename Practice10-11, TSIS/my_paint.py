import pygame
import math

# Определяем палитру
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []             # "Хвост" от мыши
    permanent_shapes = []   # Фигуры, которые живут вечно (до нажатия C)
    
    while True:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                
                # Смена цвета кисти (для линии)
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                
                # Очистка экрана
                if event.key == pygame.K_c:
                    points = []
                    permanent_shapes = []

                # --- ДОБАВЛЕНИЕ ЦВЕТНЫХ ФИГУР ---
                
                # A - Квадрат (Желтый)
                if event.key == pygame.K_a:
                    permanent_shapes.append({'type': 'square', 'pos': mouse_pos, 'color': YELLOW})
                
                # S - Прямоугольный треугольник (Зеленый)
                elif event.key == pygame.K_s:
                    permanent_shapes.append({'type': 'right_tri', 'pos': mouse_pos, 'color': GREEN})
                
                # D - Равносторонний треугольник (Циановый/Голубой)
                elif event.key == pygame.K_d:
                    permanent_shapes.append({'type': 'eq_tri', 'pos': mouse_pos, 'color': CYAN})
                
                # F - Ромб (Маджента/Фиолетовый)
                elif event.key == pygame.K_f:
                    permanent_shapes.append({'type': 'rhombus', 'pos': mouse_pos, 'color': MAGENTA})

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: radius += 1
                if event.button == 3: radius = max(1, radius - 1)
                
                # Доп. кнопки мыши (Красные фигуры)
                if event.button == 6:
                    permanent_shapes.append({'type': 'rect_special', 'pos': event.pos, 'color': RED})
                if event.button == 7:
                    permanent_shapes.append({'type': 'circle_special', 'pos': event.pos, 'color': RED})

            if event.type == pygame.MOUSEMOTION:
                points.append(mouse_pos)
                points = points[-256:]

        # 1. Отрисовка линии (кисти)
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        # 2. Отрисовка всех постоянных фигур
        for shape in permanent_shapes:
            pos = shape['pos']
            color = shape['color']
            size = 40 
            
            if shape['type'] == 'square':
                pygame.draw.rect(screen, color, (pos[0]-size//2, pos[1]-size//2, size, size), 2)
            
            elif shape['type'] == 'right_tri':
                pts = [pos, (pos[0], pos[1] + size), (pos[0] + size, pos[1] + size)]
                pygame.draw.polygon(screen, color, pts, 2)
                
            elif shape['type'] == 'eq_tri':
                h = size * math.sqrt(3) / 2
                pts = [(pos[0], pos[1] - size), 
                       (pos[0] - size, pos[1] + h/2), 
                       (pos[0] + size, pos[1] + h/2)]
                pygame.draw.polygon(screen, color, pts, 2)
                
            elif shape['type'] == 'rhombus':
                pts = [(pos[0], pos[1] - size), (pos[0] + size, pos[1]), 
                       (pos[0], pos[1] + size), (pos[0] - size, pos[1])]
                pygame.draw.polygon(screen, color, pts, 2)
                
            elif shape['type'] == 'rect_special':
                pygame.draw.rect(screen, color, (pos[0]-10, pos[1]-10, 20, 20))
                
            elif shape['type'] == 'circle_special':
                pygame.draw.circle(screen, color, pos, 20)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    # Цвет кисти меняется градиентом
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue': color = (c1, c1, c2)
    elif color_mode == 'red': color = (c2, c1, c1)
    elif color_mode == 'green': color = (c1, c2, c1)
    else: color = WHITE
    
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        prog = i / (iterations if iterations > 0 else 1)
        x = int((1 - prog) * start[0] + prog * end[0])
        y = int((1 - prog) * start[1] + prog * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

if __name__ == "__main__":
    main()
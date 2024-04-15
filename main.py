'''Игра «Тир».
Мишень находится в игровом окне в постоянном движении и ведется подсчет количества очков при каждом попадании по цели.
При нажатии на мишень мышкой: увеличение счета на 1, мишень перемещается на другую позицию и
увеличивает скорость движения на 5%.'''

# Импорт библиотек:
import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width, target_height = 80, 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_velocity_x = 0.1
target_velocity_y = 0.1

score = 0

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

font = pygame.font.Font(None, 36)

# Добавляем переменные для взрыва
explosion_active = False  # Активность взрыва
explosion_duration = 0  # Продолжительность взрыва
explosion_radius = 0  # Радиус взрыва
explosion_pos = (0, 0)  # Позиция взрыва

running = True
while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_velocity_x *= 1.05
                target_velocity_y *= 1.05
                score += 1
                # Активируем взрыв
                explosion_active = True
                explosion_duration = 50  # Время отображения взрыва
                explosion_radius = 20  # Начальный радиус взрыва
                explosion_pos = (mouse_x, mouse_y)

    target_x += target_velocity_x
    target_y += target_velocity_y

    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_velocity_x *= -1
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_velocity_y *= -1

    screen.blit(target_image, (target_x, target_y))

    if explosion_active:
        pygame.draw.circle(screen, (255, 69, 0), explosion_pos, explosion_radius)  # Рисуем "взрыв"
        explosion_radius += 6  # Увеличиваем радиус взрыва
        explosion_duration -= 1  # Уменьшаем время отображения взрыва
        if explosion_duration <= 0:
            explosion_active = False  # Заканчиваем отображение взрыва

    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
'''Игра «Тир».
Мишень находится в игровом окне в постоянном движении.
При нажатии на мишень мышкой: мишень перемещается на другую позицию и увеличивает скорость движения на 5%.'''

# Импорт библиотек: pygame и random
import pygame # Библиотека для создания видеоигр
import random  # Библиотека для генерирования случайных чисел
# Инициализация Pygame
pygame.init()

# Установка размеров окна игры
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Создание окна игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка названия окна игры
pygame.display.set_caption("Игра Тир")
# Загрузка и установка иконки окна игры
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения мишени и установка её размеров
target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Инициализация начальной позиции мишени в случайном месте
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Установка начальной скорости движения мишени
target_velocity_x = 0.1
target_velocity_y = 0.1

# Установка цвета фона в случайный цвет
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Основной цикл программы
running = True
while running:
    # Заполнение фона окна
    screen.fill(color)
    # Обработка событий
    for event in pygame.event.get():
        # Завершение работы при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат курсора мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещение мишени в случайную позицию
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Увеличение скорости мишени на 5% при попадании
                target_velocity_x *= 1.05
                target_velocity_y *= 1.05

    # Обновление позиции мишени
    target_x += target_velocity_x
    target_y += target_velocity_y

    # Проверка на столкновение с краями экрана и изменение направления движения
    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_velocity_x *= -1
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_velocity_y *= -1

    # Отображение мишени на экране
    screen.blit(target_image, (target_x, target_y))
    # Обновление содержимого окна игры
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()
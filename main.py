'''Игра «Тир».
Мишень находится в игровом окне в постоянном движении и ведется подсчет количества очков при каждом попадании по цели.
При нажатии на мишень мышкой: увеличение счета на 1, мишень перемещается на другую позицию и
увеличивает скорость движения на 5%.'''

# Импорт библиотек:
import pygame  # Импортируем библиотеку Pygame для создания игр
import random  # Импортируем модуль random для генерации случайных чисел

# Инициализация Pygame
pygame.init()

# Установка размеров окна игры
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Определяем константы для ширины и высоты экрана
# Создание окна игры с заданными размерами
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Установка названия и иконки окна
pygame.display.set_caption("Игра Тир")  # Устанавливаем заголовок окна
icon = pygame.image.load("img/icon.jpg")  # Загружаем иконку для окна
pygame.display.set_icon(icon)  # Устанавливаем иконку для окна

# Загрузка изображения мишени
target_image = pygame.image.load("img/target.png")  # Загрузка изображения мишени
target_width, target_height = 80, 80  # Установка размеров мишени

# Начальная позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Случайная начальная позиция X мишени
target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # Случайная начальная позиция Y мишени

# Начальная скорость мишени
target_velocity_x = 0.1 # Устанавливаем начальную скорость мишени по оси x
target_velocity_y = 0.1 # Устанавливаем начальную скорость мишени по оси y

# Начальный счет
score = 0  # Счет начинается с нуля

# Установка цвета фона (случайный цвет фона)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализация шрифта для отображения счета
font = pygame.font.Font(None, 36)

# Основной цикл игры
running = True
while running:
    screen.fill(color)  # Заполняем экран цветом фона
    # Обработка событий:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка на закрытие окна
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # СОбработка нажатия кнопки мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Получаем координаты курсора мыши
            # Проверяем попадание по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещение мишени в случайную позицию:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Новая случайная позиция X
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)  # Новая случайная позиция Y
                # Увеличение скорости мишени на 5% при попадании:
                target_velocity_x *= 1.05  # Увеличиваем скорость по оси X
                target_velocity_y *= 1.05  # Увеличиваем скорость по оси Y
                # Увеличение счета при попадании:
                score += 1  # Прибавляем один к счету при попадании

    # Движение мишени
    target_x += target_velocity_x
    target_y += target_velocity_y

    # Проверка выхода мишени за пределы экрана и изменение направления движения
    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_velocity_x *= -1
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_velocity_y *= -1

    screen.blit(target_image, (target_x, target_y))  # Отображение мишени на экране

    # Отображение счета
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))  # Формирование текста для отображения счета
    screen.blit(score_text, (10, 10))  # Вывод счета на экран

    pygame.display.update()  # Обновление содержимого всего экрана

pygame.quit()  # Выход из Pygame, закрытие всех окон и освобождение ресурсов
'''Игра «Тир».
Мишень находится в игровом окне в постоянном движении и ведется подсчет количества очков при каждом попадании по цели.
При нажатии на мишень мышкой: появляется визуальный эффект типа "взрыв", происходит увеличение счета на 1,
мишень перемещается на другую позицию и увеличивается скорость движения мишени на 5%.'''

# Импорт библиотек:
import pygame # Импортируем библиотеку Pygame для создания игр
import random # Импортируем модуль random для генерации случайных чисел
# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # Определяем константы для ширины и высоты экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Создание окна игры с заданными размерами

# Настройка заголовка окна и иконки
pygame.display.set_caption("Игра Тир") # Устанавливаем заголовок окна
icon = pygame.image.load("img/icon.jpg") # Загружаем иконку для окна
pygame.display.set_icon(icon) # Устанавливаем иконку для окна

# Загрузка изображения цели
target_image = pygame.image.load("img/target.png")
# Установка размеров цели
target_width, target_height = 80, 80

# Начальная позиция цели (случайное местоположение на экране)
target_x = random.randint(0, SCREEN_WIDTH - target_width) # Случайная начальная позиция X мишени
target_y = random.randint(0, SCREEN_HEIGHT - target_height) # Случайная начальная позиция Y мишени

# Начальная скорость цели
target_velocity_x = 0.1 # Установка начальной скорости мишени по оси x
target_velocity_y = 0.1 # Установка начальной скорости мишени по оси у

# Начальный счет игры
score = 0

# Цвет фона (случайный)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Шрифт текста для отображения счета
font = pygame.font.Font(None, 36)

# Добавляем переменные для взрыва
explosion_active = False  # Активность взрыва
explosion_duration = 0  # Продолжительность взрыва
explosion_radius = 0  # Радиус взрыва
explosion_pos = (0, 0)  # Позиция взрыва

# Основной цикл игры
running = True
while running:
    # Заполнение экрана цветом
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Проверка на закрытие окна
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # СОбработка нажатия кнопки мыши
            mouse_x, mouse_y = pygame.mouse.get_pos() # Получаем координаты курсора мыши
            # Проверка попадания по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещение цели на новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width) # Новая случайная позиция X
                target_y = random.randint(0, SCREEN_HEIGHT - target_height) # Новая случайная позиция Y
                # Увеличение скорости цели на 5% при попадании
                target_velocity_x *= 1.05 # Увеличение скорости по оси X
                target_velocity_y *= 1.05 # Увеличение скорости по оси У
                # Увеличение счёта (+1) при попадании по цели
                score += 1
                # Активация взрыва на месте попадания
                explosion_active = True
                explosion_duration = 50  # Время отображения взрыва
                explosion_radius = 20  # Начальный радиус взрыва
                explosion_pos = (mouse_x, mouse_y)

    # Обновление позиции цели
    target_x += target_velocity_x
    target_y += target_velocity_y

    # Проверка выхода мишени за пределы экрана и изменение направления движения
    if target_x + target_width > SCREEN_WIDTH or target_x < 0:
        target_velocity_x *= -1
    if target_y + target_height > SCREEN_HEIGHT or target_y < 0:
        target_velocity_y *= -1

    # Отображение мишени на экране
    screen.blit(target_image, (target_x, target_y))

    # Отрисовка взрыва, если он активирован
    if explosion_active:
        # Рисование "взрыва"
        pygame.draw.circle(screen, (255, 69, 0), explosion_pos, explosion_radius)
        # Увеличение радиуса взрыва
        explosion_radius += 6
        # Уменьшение времени отображения взрыва
        explosion_duration -= 1
        if explosion_duration <= 0:
            # Окончание отображения взрыва
            explosion_active = False

    # Отображение счёта
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255)) # Формирование текста для отображения счета
    screen.blit(score_text, (10, 10)) # Вывод счета на экран

    # # Обновление содержимого всего экрана
    pygame.display.update()

pygame.quit() # Выход из Pygame, закрытие всех окон и освобождение ресурсов
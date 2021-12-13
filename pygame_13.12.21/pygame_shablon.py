# Pygame шаблон - скелет для нового проекта Pygame

import random
import pygame

WIDTH = 360  # ширина игрового окна
HEIGHT = 480  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Задаем цвета RBG
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()  # это команда, которая запускает pygame
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # окно программы, которое создается,
# когда мы задаем его размер в настройках
pygame.display.set_caption('fools')
clock = pygame.time.Clock()  # Дальше необходимо создать clock, чтобы убедиться, что игра
# работает с заданной частотой кадров.

# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)   # Рендеринг

    pygame.display.flip()  # после отрисовки всего, переворачиваем экран

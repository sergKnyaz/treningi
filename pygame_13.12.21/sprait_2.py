# https://pythonru.com/uroki/biblioteka-pygame-chast-3-bolshe-o-sprajtah

import random
import pygame
import os

# Специальная переменная __file__ относится к папке, в которой сохранен код игры, а команда os.path.dirname 
# указывает путь к папке.
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,'img')
# Изображение загружается с помощью pygame.image.load(), а convert() ускорит прорисовку в Pygame, конвертируя 
# изображение в тот формат, который будет быстрее появляться на экране
player_img=pygame.image.load(os.path.join(img_folder,'img_1.png'))#.convert()

WIDTH = 800  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Задаем цвета RBG
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # запускает инициализатор встроенных классов Sprite
        self.image = player_img
        # set_colorkey() говорит Pygame игнорировать любые пиксели конкретного цвета.
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # Команда get_rect() оценивает изображение image и высчитывает прямоугольник,
        # способный окружить его, rect можно использовать для размещения спрайта в любом месте.
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # создание спрайта по центру

    def update(self):
        self.rect.x += 5  # при каждом игровом цикле x-координата спрайта будет увеличиваться на 5 пикселей
        if self.rect.left > WIDTH:
            self.rect.right = 0  # если левая сторона rect пропадает с экрана,
            # просто задаем значение правого края равное 0


# Создаем игру и окно
pygame.init()  # это команда, которая запускает pygame
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # окно программы, которое создается,
# когда мы задаем его размер в настройках
pygame.display.set_caption('fools')
clock = pygame.time.Clock()  # Дальше необходимо создать clock, чтобы убедиться, что игра
# работает с заданной частотой кадров.

all_sprites = pygame.sprite.Group()  # создавать группу спрайтов в игре
player = Player()
all_sprites.add(player)  # добавить спрайт в группу all_sprites.

# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()  # обновление спрайтов

    screen.fill(BLUE)  # Рендеринг  

    all_sprites.draw(screen)  # отрисовка спрайтов

    pygame.display.flip()  # после отрисовки всего, переворачиваем экран

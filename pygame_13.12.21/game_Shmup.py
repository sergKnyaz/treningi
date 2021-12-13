# https://pythonru.com/primery/streljalka-s-pygame-1-sprajt-igroka-i-upravlenie

import random
import pygame

WIDTH = 480  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
FPS = 60  # частота кадров в секунду

# Задаем цвета RBG
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # запускает инициализатор встроенных классов Sprite
        self.image = pygame.Surface((50, 40))  # создадим квадрат размером 50х50
        self.image.fill(GREEN)  # и заполним его зеленым цветом
        self.rect = self.image.get_rect()  # Команда get_rect() оценивает изображение image и высчитывает прямоугольник,
        # способный окружить его, rect можно использовать для размещения спрайта в любом месте.
        self.rect.centerx = WIDTH / 2  # создание спрайта по центру по Х
        self.rect.bottom = HEIGHT - 10 # нижняя часть спрайта на 10 выше нижнего края экрана
        self.speed = 0  # свойство speedx, которое будет отслеживать, с какой скоростью двигается игрок 
        # по оси x (со стороны в сторону)

    def update(self):
        self.speed=0
        # Этот код устанавливает скорость speedx на значении 0 для каждого кадра, а затем проверяет, 
        # не нажата ли кнопка.
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed=-8
        if keystate[pygame.K_RIGHT]:
            self.speed=8
        self.rect.x += self.speed
        # нужно сделать так, чтобы спрайт не пропадал с экрана.
        if self.rect.right > WIDTH: self.rect.right = WIDTH
        if self.rect.left < 0: self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))  # создадим квадрат размером 50х50
        self.image.fill(RED)  # и заполним его  цветом
        self.rect = self.image.get_rect()
        self.rect.x=random.randrange(WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speed=random.randrange(1,8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y+=self.speed
        if self.rect.top > HEIGHT+10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x=random.randrange(WIDTH-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speed=random.randrange(1,8)    

# Создаем игру и окно
pygame.init()  # это команда, которая запускает pygame
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # окно программы, которое создается,
# когда мы задаем его размер в настройках
pygame.display.set_caption('fools')
clock = pygame.time.Clock()  # Дальше необходимо создать clock, чтобы убедиться, что игра
# работает с заданной частотой кадров.

all_sprites = pygame.sprite.Group()  # создавать группу спрайтов в игре
mobs=pygame.sprite.Group()
player = Player()
all_sprites.add(player)  # добавить спрайт в группу all_sprites.
for i in range(8):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)


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

    screen.fill(BLACK)  # Рендеринг

    all_sprites.draw(screen)  # отрисовка спрайтов

    pygame.display.flip()  # после отрисовки всего, переворачиваем экран

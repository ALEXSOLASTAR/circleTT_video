import threading
import time

import pygame
import sys
from sprit import MyCircleSprite
from parameters import width, height, left_border, top_border, rith_border, dovn_border, object_width, color_list
from sprite_create import creat_sprite_list

# Ініціалізація Pygame
pygame.init()


# Створюємо вікно гри
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption("Моя перша гра")

sound_dict = {
    "0": pygame.mixer.Sound("music/do.mp3"),
    "1": pygame.mixer.Sound("music/re.mp3"),
    "2": pygame.mixer.Sound("music/zvuk-notyi-mi.mp3"),
    "3": pygame.mixer.Sound("music/zvuk-notyi-fa.mp3"),
    "4": pygame.mixer.Sound("music/zvuk-notyi-sol.mp3"),
    "5": pygame.mixer.Sound("music/zvuk-notyi-lya.mp3"),
    "6": pygame.mixer.Sound("music/zvuk-notyi-si.mp3"),
    "7": pygame.mixer.Sound("music/zvuk-notyi-do-vo-vtoroy-oktave-rastyanutyiy.mp3"),
    "8": pygame.mixer.Sound("music/zvuk-notyi-re (1).mp3"),
    "9": pygame.mixer.Sound("music/zvuk-notyi-mi-rastyanutyiy.mp3")
}



# Створення групи спрайтів
all_sprites = pygame.sprite.Group()

# Створення кругового спрайта і додавання його до групи
sound_key = -1
for i in creat_sprite_list(10, object_width, 50, 1.5, color_list):
    sound_key += 1
    circle_sprite = MyCircleSprite(i["color"], i["x"], i["y"], i["radius"], i["speed"], i["direction"], sound_dict[f"{sound_key}"])
    all_sprites.add(circle_sprite)


sprite_time = time.time()
border_time = time.time()
now_time = time.time()

stop = False

def update_sprits():
    time.sleep(0.5)
    while True:
        time.sleep(0.007)
        all_sprites.update(left_border, rith_border)
        if stop:
            break


def move_border():
    global left_border, rith_border, stop
    time.sleep(0.5)
    while True:
        time.sleep(0.12)
        left_border += 1
        rith_border -= 1
        if rith_border - left_border <= object_width-10:
            stop = True
            break


# Створюємо два потоки
thread1 = threading.Thread(target=update_sprits)
thread2 = threading.Thread(target=move_border)

# Запускаємо потоки
thread1.start()
thread2.start()
while True:

    # if now_time*1000 - sprite_time*1000 >= 10:
    #     all_sprites.update(left_border, width)
    #     sprite_time = time.time()
    # if now_time * 1000 - border_time * 1000 >= 100:
    #     print(width, left_border)
    #     left_border += 1
    #     width -= 1
    #     border_time = time.time()

    # Очистка екрану
    screen.fill((90, 90, 90))#!!!!!!!!!!!!!
    # pygame.draw.line(screen, (255, 255, 255), [left_border, 0], [left_border, height], 3)
    # pygame.draw.line(screen, (255, 255, 255), [width, 0], [width, height], 3)
    pygame.draw.rect(screen, (0, 0, 0), (left_border, top_border, rith_border - left_border, dovn_border-50))

    # Малювання всіх спрайтів у групі на екрані
    all_sprites.draw(screen)

    # Оновлення вікна
    pygame.display.update()
    if stop:
        break




# import threading
# import time
#
# import pygame
# import sys
# from sprit import MyCircleSprite
# from parameters import width, height, left_border, top_border
# from sprite_create import creat_sprite_list
#
# # Ініціалізація Pygame
# pygame.init()
#
#
# # Створюємо вікно гри
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Моя перша гра")
#
# # Створення групи спрайтів
# all_sprites = pygame.sprite.Group()
#
# # Створення кругового спрайта і додавання його до групи
# for i in creat_sprite_list(20, 20, 20, 1):
#     circle_sprite = MyCircleSprite(i["color"], i["x"], i["y"], i["radius"], i["speed"], i["direction"])
#     all_sprites.add(circle_sprite)
# sprite_time = time.time()
# border_time = time.time()
# now_time = time.time()
#
#
# def update_sprits():
#     time.sleep(0.5)
#     while True:
#         time.sleep(0.005)
#         all_sprites.update(left_border, width)
#
#
# def move_border():
#     global left_border, width
#     time.sleep(0.5)
#     while True:
#         time.sleep(0.08)
#         left_border += 1
#         width -= 1
#
#
# # Створюємо два потоки
# thread1 = threading.Thread(target=update_sprits)
# thread2 = threading.Thread(target=move_border)
#
# # Запускаємо потоки
# thread1.start()
# thread2.start()
# while True:
#
#     # if now_time*1000 - sprite_time*1000 >= 10:
#     #     all_sprites.update(left_border, width)
#     #     sprite_time = time.time()
#     # if now_time * 1000 - border_time * 1000 >= 100:
#     #     print(width, left_border)
#     #     left_border += 1
#     #     width -= 1
#     #     border_time = time.time()
#
#     # Очистка екрану
#     screen.fill((0, 0, 0))#!!!!!!!!!!!!!
#     pygame.draw.line(screen, (255, 255, 255), [left_border, 0], [left_border, height], 3)
#     pygame.draw.line(screen, (255, 255, 255), [width, 0], [width, height], 3)
#
#     # Малювання всіх спрайтів у групі на екрані
#     all_sprites.draw(screen)
#
#     # Оновлення вікна
#     pygame.display.update()

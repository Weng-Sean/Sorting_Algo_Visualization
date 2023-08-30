import pygame
import random
from threading import Thread
import time

BAR_NUMBER = 3000

pygame.font.init()
pygame.init()
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("quick sort")

run = True


def msg2screen(txt, x, y, color=(0, 0, 0), size=35):
    screen_txt = pygame.font.SysFont(None, size).render(txt, True, color)
    screen.blit(screen_txt, (int(x - size / 6 * len(txt)), int(y - size / 4)))


def draw_bars(surface, num_list):
    w = (WIDTH / (len(num_list) + 2))
    x = w
    for num in num_list:
        pygame.draw.rect(surface, (255, 125, 0), (x, HEIGHT - num, w, num))
        x += w


def quick_sort():
    global l, finish_sorting
    quick_sort_helper(0, len(l))
    finish_sorting = True

    return True


def quick_sort_helper(idx1, idx2):
    global l


    if idx2 - idx1 <= 1:
        return None


    pivot = l[idx2 - 1]
    idx = idx1
    boundary = idx1
    while idx < idx2 - 1:
        num = l[idx]
        if num < pivot:
            l[boundary], l[idx] = l[idx], l[boundary]
            boundary += 1
        idx += 1
    l[idx2 - 1], l[boundary] = l[boundary], pivot



    quick_sort_helper(idx1, boundary)
    quick_sort_helper(boundary + 1, idx2)


l = []
start_sorting = False
finish_sorting = False

for i in range(BAR_NUMBER):
    l.append(random.randint(20, HEIGHT))

a = -1
b = -1

quick_sort()




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    draw_bars(screen, l)

    if not start_sorting:
        start_sorting = True
        if a == -1:
            a = time.time()

        Thread(target=quick_sort).start()

    if not finish_sorting:
        b = time.time()

    msg2screen(f"{max(0, int(b - a))} seconds", 100, 100, color=(125, 255, 0), size=35)

    pygame.display.flip()


import pygame
import random
from threading import Thread
import time

BAR_NUMBER = 1000

pygame.font.init()
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("insertion sort")


def msg2screen(txt, x, y, color=(0, 0, 0), size=35):
    screen_txt = pygame.font.SysFont(None, size).render(txt, True, color)
    screen.blit(screen_txt, (int(x - size / 6 * len(txt)), int(y - size / 4)))

def draw_bars(surface, num_list):
    w = (WIDTH / (len(num_list) + 2))
    x = w
    for num in num_list:
        pygame.draw.rect(surface, (255,125,0), (x, HEIGHT - num, w, num))
        x += w + 1

def insertion_sort():
    global l, finish_sorting, boundary, start_sorting

    if boundary == len(l):
        finish_sorting = True
        return True

    num = l[boundary]
    i = boundary
    while i > 0 and num < l[i - 1]:
        l[i], l[i-1] = l[i-1], l[i]
        i -= 1

    boundary += 1

    start_sorting = False
    return False


l = []
start_sorting = False
finish_sorting = False

for i in range(BAR_NUMBER):
    l.append(random.randint(20, HEIGHT))


a = -1
b = -1

boundary = 0
run = True
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

        Thread(target=insertion_sort).start()

    if not finish_sorting:
        b = time.time()

    msg2screen(f"{int(b-a)} seconds", 100, 100, color=(125, 255, 0), size=35)

    pygame.display.flip()



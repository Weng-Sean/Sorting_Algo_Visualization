import pygame
import random

BAR_NUMBER = 100

pygame.font.init()
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sorting")

run = True

def draw_bars(surface, num_list):
    w = (WIDTH / (len(num_list) + 2))
    x = w
    for num in num_list:
        pygame.draw.rect(surface, (255,125,0), (x, HEIGHT - num, w, num))
        x += w

l = []
for i in range(BAR_NUMBER):
    l.append(random.randint(20, HEIGHT))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    draw_bars(screen, l)
    pygame.display.flip()
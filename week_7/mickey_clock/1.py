import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1500, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()


font = pygame.font.SysFont('Verdana', 60)
bg = pygame.image.load('mickeyclock.jpeg').convert()
bg_rect = bg.get_rect()

bg_rect.center = WIDTH / 2, HEIGHT / 2

radius_list = {
    'sec': RADIUS - 10, 
    'min': RADIUS - 55, 
    'hour': RADIUS - 100
}

clock60 = dict(zip(range(60), range(0, 360, 6))) 

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surface.blit(bg, bg_rect)
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('black'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)

    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('white'), pygame.Color('black'))
    surface.blit(time_render, (0, 0))

    pygame.display.flip()
    clock.tick(20)  
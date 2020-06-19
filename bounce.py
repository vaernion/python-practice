import sys

import pygame

pygame.init()
pygame.display.set_caption("bounce")

size = width, height = 640, 480
dx = 10
dy = 10
x = 0
y = 0
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)


def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("coral"))
    return fps_text


while 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:
        dx = -dx
    if y < 0 or y > height:
        dy = -dy

    screen.fill(black)
    screen.blit(update_fps(), (width - width // 15, height // 20))
    pygame.draw.circle(screen, white, (x, y), 8)

    pygame.display.flip()

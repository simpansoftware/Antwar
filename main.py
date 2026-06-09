import pygame
import random
import time

pygame.init()
xres = 640
yres = 480
screen = pygame.display.set_mode((xres, yres))
pygame.display.set_caption("Antwar")
clock = pygame.time.Clock()
size = 2

running = True
while running:
    # so i cant make it fully random without causing performance issues
    # thank you python for being slow
    for x in range(0, xres, size):
        for y in range(0, yres, size):
            thing = random.randrange(2)
            if thing == 1:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, (x, y, size, size))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()
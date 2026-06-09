import pygame
import numpy

pygame.init()
xres = 640
yres = 480
screen = pygame.display.set_mode((xres, yres))
pygame.display.set_caption("Antwar")
clock = pygame.time.Clock()
size = 2

running = True
while running:
    # update: we use numpy because thats way faster than python on its own
    width = xres // size
    height = yres // size
    noise = numpy.random.randint(0, 2, (xres // size, yres // size), dtype=numpy.uint8) * 255
    # i sincerely thank gpt5 for this function below for my optimization
    surface = pygame.surfarray.make_surface(numpy.repeat(numpy.repeat(numpy.repeat(noise[:, :, None], 3, axis=2),size, axis=0), size, axis=1))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()

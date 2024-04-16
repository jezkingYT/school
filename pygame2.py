import pygame

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("hra")

x1 = 50
r = 50
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))
    x1 += 0.5
    if x1 > width - r:
        x1 = 50
    pygame.draw.circle(window, (180, 0, 180), (x1, 200), 50)
    pygame.draw.circle(window, (0, 180, 180), (400, 200), 50)
    pygame.draw.circle(window, (250, 0, 180), (200, 400), 50)

    pygame.display.update() 

pygame.quit()
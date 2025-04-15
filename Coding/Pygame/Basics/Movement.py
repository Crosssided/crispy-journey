import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Basic window")
clock = pygame.time.Clock()

mover = pygame.Rect(100, 100, 50, 50)
mover_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        mover.y -= mover_speed
    if keys[pygame.K_DOWN]:
        mover.y += mover_speed
    if keys[pygame.K_LEFT]:
        mover.x -= mover_speed
    if keys[pygame.K_RIGHT]:
        mover.x += mover_speed

    
    screen.fill("white")
    pygame.draw.rect(screen, "red", mover)

    clock.tick(60)
    pygame.display.update()

pygame.quit()            

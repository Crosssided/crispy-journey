import pygame

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
PADDLE_SPEED = 6
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Ball and Paddle properties
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
paddle1 = pygame.Rect(20, HEIGHT // 2 - 40, 10, 80)
paddle2 = pygame.Rect(WIDTH - 30, HEIGHT // 2 - 40, 10, 80)

# Ball movement
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

# Game loop
running = True
while running:
    pygame.time.delay(16)  # 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED
    
    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy
    
    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    
    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1
    
    # Ball reset if out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
        ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
    
    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    pygame.display.flip()

pygame.quit()

import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing ball")
clock = pygame.time.Clock()

gravity = 0.3
ground_lvl = 500
ball_height = 100
# resistance = 1

class Ball:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity = 0
        # self.bounce_strength = 0.8
        # self.bounce_height = ball_height
    
    def apply_gravty(self):
        self.velocity += gravity
        # self.velocity = min(self.velocity, 10)
        self.rect.y += self.velocity
    
    def bounce(self):
        # self.bounce_height *= resistance

        if self.rect.bottom >= ground_lvl:
            self.rect.bottom = ground_lvl

            self.velocity -= 3
            self.velocity = -self.velocity
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

ball = Ball(225, ball_height, 50, 50, "red")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.apply_gravty()
    ball.bounce()

    screen.fill("black")
    ball.draw()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

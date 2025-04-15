import pygame
import random

pygame.init()
pygame.font.init()

w, h, = 360, 640
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Bird")

gravity = 0.5
jump_force = -10
score = 0

font = pygame.font.Font("Pygame/Projects/fonts/Mojang-Regular.ttf", 32)
small_font = pygame.font.Font("Pygame/Projects/fonts/Mojang-Regular.ttf", 24)

class Bird:
    def __init__(self, x, y, width, height, colour):
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.velocity = 0
    
    def do_gravity(self):
        
        self.velocity += gravity
        self.rect.y += self.velocity

        if self.rect.top <= 0:
            self.rect.y =0
        if self.rect.bottom >= h:
            self.rect.bottom = h

    def jump(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.MOUSEBUTTONDOWN or event.key == pygame.K_SPACE:
                self.velocity = 0
                self.velocity += jump_force
        
    def draw(self):
        pygame.draw.rect(screen, self.colour, self.rect)

class Pipe:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

        self.pipe = pygame.Rect(x, y, width, height)

    def move(self, speed):
        self.pipe.x -= speed

    def collision(self, run):
        self.run = run

    def draw(self):
        pygame.draw.rect(screen, self.colour, self.pipe)

bird = Bird(100, h/2, 50, 50, "#E3963E")

def generate_pipes():
    gap = 225
    top_height = random.randint(50, h-150)
    bottom_height = top_height + gap

    top_pipe = Pipe(w, 0, 50, top_height, "red")
    bottom_pipe = Pipe(w, bottom_height, 50, h, "red")

    return top_pipe, bottom_pipe

pipes = []
pipe_interval = 100
pipe_timer = 100

clock = pygame.time.Clock()

running = True
collided = False
show_score = True

game_over = font.render("GAME OVER", True, "black")
game_over_rect = game_over.get_rect(center=(w/2, h/2))

retry = small_font.render("Press 'R' to retry", True, "black")
retry_rect = retry.get_rect(center=(w/2, h/2+35))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            collided = False
            bird.rect.y = h // 2
            bird.velocity = 0
            pipes = []
            score = 0
            pipe_timer = 100

        bird.jump(event)
    
    bird.do_gravity()   

    if not collided:
        screen.fill("#87CEEB")
        bird.draw()

        pipe_timer += 1
        if pipe_timer >= pipe_interval:
            pipes.extend(generate_pipes())
            pipe_timer = 0
        
        if pipe_timer == 80:
            score += 1

        pipes = [p for p in pipes if p.x > -10]

        for p in pipes:
            p.move(3)
            p.draw()

            if bird.rect.colliderect(p.pipe):
                collided = True
        
        text = font.render(f"Score: {score}", True, "black")
        text_rect = text.get_rect()
        screen.blit(text, text_rect)

        if collided:
            screen.blit(game_over, game_over_rect)
            text_rect = text.get_rect(center=(w/2, h/2-40))
            screen.blit(text, text_rect)
            screen.blit(retry, retry_rect)

    pygame.display.flip()
    clock.tick(60)



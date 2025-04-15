import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Gravity")

clock = pygame.time.Clock()

# gravity
gravity = 0.5
jump_force = -10

# assets
ground = pygame.Rect(0, 375, 600, 25)
sky = "#87CEEB"

# player class
class Player:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed
        self.on_ground = False
        self.velocity = 0
    
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity += jump_force
            self.on_ground = False

    def gravity_apply(self):
        if not self.on_ground:
            self.velocity += gravity
            self.velocity == min(self.velocity, 10)
        
        self.rect.y += self.velocity
        
        if self.rect.bottom >= 375:
            self.rect.bottom = 375
            self.velocity = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 600:
            self.rect.right = 600

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

player = Player(100, 100, 25, 25, "red", 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # apply gravity
    player.gravity_apply()

    keys = pygame.key.get_pressed()
    player.move(keys)

    # draw assets
    screen.fill(sky)
    pygame.draw.rect(screen, "#6C8E68", ground)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

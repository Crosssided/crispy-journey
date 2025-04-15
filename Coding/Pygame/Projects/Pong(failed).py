import pygame
import random
import math

pygame.init()

w, h, = (600, 400)
aspect_ratio_w = h/w
aspect_ratio_h = w/h

screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("Pong")

# Classes
class Player:
    def __init__(self, x, y, width, height, colour, speed):
        self.Rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.speed = speed
        
    def movement(self, keys, k_up, k_down):
        if keys[k_up]:
            self.Rect.y -= self.speed
        if keys[k_down]:
            self.Rect.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.Rect)

    def inbounds(self):
        if self.Rect.top <= 0:
            self.Rect.top = 0
        if self.Rect.bottom >= 400:
            self.Rect.bottom = 400

class Pong():
    def __init__(self, x, y, width, height, colour, speed, mid_point, agnel):
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.speed = speed
        self.midpoint = mid_point
        self.angle = angle
        
    def movement(self, leftright):

        # self.dx = self.Rect.x - target_x
        # self.dy = self.Rect.y - target_y

        # self.distance = math.sqrt(self.dx**2 + self.dy**2) # Use pythagoras to calculate the hypotneus of the triangle
        # self.Rect.x += (self.dx/self.distance) * 3 # normalise the vectors
        # self.Rect.y += (self.dy/self.distance) * 3 # kinda like a circle

        self.radian = math.radians(self.angle)
        self.left_right = leftright
        # self.Rect.x += math.cos(radian) * self.left_right * self.speed
        # self.Rect.y += math.sin(radian) * self.left_right * self.speed
        self.rect.x += math.cos(self.radian) * self.left_right * self.speed
        self.rect.y += math.sin(self.radian) * self.left_right * self.speed

    def collision(self):

        if self.rect.x >= 600 or self.rect.x <= 0:
            self.rect.y = h/2
            self.rect.x = w/2

        if self.rect.colliderect(p1.Rect) or self.rect.colliderect(p2.Rect):
            self.angle *= random.choice([1, -1])
            
        if self.rect.top <= 0:
            self.angle *= -1
        if self.rect.bottom >= 400:
            self.angle *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)


# point_left = [0, random.randint(0, 400)]
# point_right = [600, random.randint(0,400)]
mid_point = (w/2, h/2)

# destination = random.choice([point_left, point_right])

angle = random.uniform(-30, 30)
LorR = random.choice([1, -1])

p1 = Player(w-w, int(h*0.375), 30, 120, "#eab7b7", 5)
p2 = Player(w-int(30/600*w), int(h*0.375), 30, 120, "#eab7b7", 5)
pong = Pong(275, 175, 25, 25, "#D18CAF", 5, mid_point, angle)


running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        elif event.type == pygame.VIDEORESIZE:
            new_w = event.w
            new_h = event.h

            if new_w-w > new_h-h:
                new_h = int(event.w*aspect_ratio_w)

            if new_h-h > new_w-w:
                new_w = int(event.h*aspect_ratio_h)

            screen = pygame.display.set_mode((new_w, new_h), pygame.RESIZABLE)

            p1 = Player(new_w-new_w, int(new_h*0.375), 30, 120, "#eab7b7", 5)
            p2 = Player(new_w-int(30/new_w*new_w), int(new_h*0.375), 30, 120, "#eab7b7", 5)

            new_w, new_h = w, h
    
    screen.fill("#f7e9d1")
    p1.draw(screen)
    p1.movement(pygame.key.get_pressed(), pygame.K_w, pygame.K_s)
    p1.inbounds()

    p2.draw(screen)
    p2.movement(pygame.key.get_pressed(), pygame.K_UP, pygame.K_DOWN)
    p2.inbounds()

    pong.draw(screen)
    pong.collision()
    pong.movement(LorR)
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

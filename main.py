import pygame
import random
import math
import time

WIDTH = 1200
HEIGHT = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Silly Pygame things")
clock = pygame.time.Clock()

player = pygame.image.load("scarameow.png").convert_alpha()
player = pygame.transform.scale(
    player,
    (100,100)
)

player_x = 0
player_y = 300

player_rect = pygame.Rect(
    player_x, 
    player_y,
    90,
    90
)

cupcakes = []

for i in range(10):
    cupcake_x = random.randint(0, WIDTH)
    cupcake_y = random.randint(0, HEIGHT)

    cupcake_rect = pygame.Rect(
        cupcake_x, 
        cupcake_y,
        35,
        35
    )
    cupcakes.append(cupcake_rect)

platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),
    pygame.Rect(100, 600, 180, 40),
    pygame.Rect(420, 550, 150, 30),
    pygame.Rect(550, 480, 200, 50),
    pygame.Rect(820, 380, 160, 70),
    pygame.Rect(1000, 260, 150, 30),
    pygame.Rect(650, 220, 180, 40),
    pygame.Rect(230, 200, 150, 20),
]

running = True

x_vel = 0
x_str = 5
jump_vel = 0
jump_str = -10
gravity = 0.5
on_ground = True      

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 24, 40))

    screen.blit(player, (player_x, player_y))

    for platform in platforms:
        pygame.draw.rect(
            screen,
            (100, 180, 100),
            platform
        )

    for cupcake in cupcakes:
        pygame.draw.rect(
            screen,
            (255, 192, 203),
            cupcake
        )

    keys = pygame.key.get_pressed()
    x_vel = 0
    if keys[pygame.K_LEFT]:
        x_vel = -x_str
        player_rect.x += x_vel
    if keys[pygame.K_RIGHT]:
        x_vel = x_str
        player_rect.x += x_vel
    if keys[pygame.K_UP] and on_ground:
        on_ground = False
        jump_vel = jump_str

    jump_vel += gravity
    player_rect.y += jump_vel

    on_ground = False

    for platform in platforms:
        if player_rect.colliderect(platform):
            if jump_vel > 0:
                player_rect.bottom = platform.top
                jump_vel = 0
                on_ground = True
            elif jump_vel < 0:
                player_rect.top = platform.bottom
                jump_vel = 0

    player_x = player_rect.x
    player_y = player_rect.y

    for cupcake in cupcakes[:]:
        if player_rect.colliderect(cupcake):
            cupcakes.remove(cupcake)
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            new_cupcake = pygame.Rect(
                x,
                y, 
                35, 
                35
            )
            cupcakes.append(new_cupcake)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
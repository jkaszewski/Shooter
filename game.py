import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shooter Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = display_width // 2 - player_size // 2
player_y = display_height - player_size - 10
player_speed = 5

# Bullet settings
bullet_size = 10
bullet_speed = 7

# Enemy settings
enemy_size = 50
enemy_speed = 3

# Create the player
player_img = pygame.Surface((player_size, player_size))
player_img.fill(GREEN)

# Create a list to hold bullets
bullets = []

# Create a list to hold enemies
enemies = []

# Create a list to hold players
players = []

# Clock for managing the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fire bullets when spacebar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_x + player_size // 2 - bullet_size // 2, player_y, bullet_size, bullet_size)
                bullets.append(bullet)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < display_width - player_size:
        player_x += player_speed

    # Move the bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Spawn enemies randomly
    if len(enemies) < 10 and random.randint(0, 100) < 3:
        enemy_x = random.randint(0, display_width - enemy_size)
        enemy_y = random.randint(-100, -enemy_size)
        enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        enemies.append(enemy)

    # Move and remove enemies that have reached the bottom
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > display_height:
            enemies.remove(enemy)

    # Check for collisions bullet
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
    
    # Check for collisions players
    for player in players:
        if enemies.colliderect(player):
            enemies.remove(player)
            enemies.remove(enemy)

    # Clear the display
    game_display.fill(WHITE)

    # Draw the player
    game_display.blit(player_img, (player_x, player_y))

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(game_display, BLUE, bullet)

    # Draw the enemies
    for enemy in enemies:
        pygame.draw.rect(game_display, RED, enemy)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

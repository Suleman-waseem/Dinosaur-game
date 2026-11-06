
import pygame
import random
import sys

pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREEN = (40, 160, 60)

# Ground
GROUND_Y = 320

# Dinosaur
dino = pygame.Rect(80, GROUND_Y - 50, 40, 50)
velocity_y = 0
gravity = 0.8
jump_power = -15
on_ground = True

# Cactus
cactus = pygame.Rect(800, GROUND_Y - 45, 25, 45)
cactus_speed = 7

score = 0
game_over = False


def reset_game():
    global velocity_y, on_ground, score, game_over
    global cactus_speed

    dino.x = 80
    dino.y = GROUND_Y - 50
    cactus.x = WIDTH + 100
    cactus.y = GROUND_Y - 45

    velocity_y = 0
    on_ground = True
    cactus_speed = 7
    score = 0
    game_over = False


# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    reset_game()
                elif on_ground:
                    velocity_y = jump_power
                    on_ground = False

    if not game_over:
        # Dinosaur jump and gravity
        velocity_y += gravity
        dino.y += int(velocity_y)

        if dino.bottom >= GROUND_Y:
            dino.bottom = GROUND_Y
            velocity_y = 0
            on_ground = True

        # Move cactus
        cactus.x -= cactus_speed

        if cactus.right < 0:
            cactus.x = WIDTH + random.randint(100, 300)
            score += 1
            cactus_speed = min(cactus_speed + 0.2, 14)

        # Collision detection
        if dino.colliderect(cactus):
            game_over = True

    # Draw screen
    screen.fill(WHITE)

    # Ground line
    pygame.draw.line(
        screen, BLACK,
        (0, GROUND_Y), (WIDTH, GROUND_Y), 3
    )

    # Draw dinosaur
    pygame.draw.rect(screen, GREEN, dino)

    # Draw dinosaur eye
    pygame.draw.circle(
        screen, WHITE,
        (dino.x + 29, dino.y + 10), 4
    )

    # Draw cactus
    pygame.draw.rect(screen, GREEN, cactus)
    pygame.draw.rect(
        screen, GREEN,
        (cactus.x - 10, cactus.y + 15, 10, 8)
    )
    pygame.draw.rect(
        screen, GREEN,
        (cactus.x + 25, cactus.y + 25, 10, 8)
    )

    # Show score
    score_text = font.render(
        f"Score: {score}", True, BLACK
    )
    screen.blit(score_text, (650, 20))

    if game_over:
        message = font.render(
            "GAME OVER! Press SPACE to restart",
            True, BLACK
        )
        screen.blit(
            message,
            (WIDTH // 2 - message.get_width() // 2, 150)
        )

    pygame.display.update()
    clock.tick(60)

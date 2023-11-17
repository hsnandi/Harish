import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Set up snake
snake_size = 20
snake_speed = 5
snake = [[100, 50], [90, 50], [80, 50]]
snake_direction = [1, 0]

# Set up food
food_size = 20
food = [random.randrange(1, (width // 20)) * 20, random.randrange(1, (height // 20)) * 20]

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction[1]:
                snake_direction = [0, -1]
            elif event.key == pygame.K_DOWN and not snake_direction[1]:
                snake_direction = [0, 1]
            elif event.key == pygame.K_LEFT and not snake_direction[0]:
                snake_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and not snake_direction[0]:
                snake_direction = [1, 0]

    # Move the snake
    new_head = [snake[0][0] + snake_direction[0] * snake_size, snake[0][1] + snake_direction[1] * snake_size]
    snake.insert(0, new_head)

    # Check for collisions
    if (
        new_head[0] < 0 or new_head[0] >= width
        or new_head[1] < 0 or new_head[1] >= height
        or new_head in snake[1:]
    ):
        pygame.quit()
        sys.exit()

    # Check if the snake eats the food
    if new_head == food:
        food = [random.randrange(1, (width // 20)) * 20, random.randrange(1, (height // 20)) * 20]
    else:
        snake.pop()

    # Draw everything
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, green, (segment[0], segment[1], snake_size, snake_size))
    pygame.draw.rect(screen, white, (food[0], food[1], food_size, food_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(snake_speed)

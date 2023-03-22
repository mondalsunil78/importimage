import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake
snake_size = 20
snake_speed = 5
snake_list = []
snake_length = 1
snake_head = [window_width/2, window_height/2]
snake_list.append(snake_head)

# Set up the food
food_size = 20
food_pos = [random.randrange(0, window_width-food_size), random.randrange(0, window_height-food_size)]

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_head[0] -= snake_size
    elif keys[pygame.K_RIGHT]:
        snake_head[0] += snake_size
    elif keys[pygame.K_UP]:
        snake_head[1] -= snake_size
    elif keys[pygame.K_DOWN]:
        snake_head[1] += snake_size

    # Move the snake
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with the food
    if abs(snake_head[0] - food_pos[0]) < food_size and abs(snake_head[1] - food_pos[1]) < food_size:
        food_pos = [random.randrange(0, window_width-food_size), random.randrange(0, window_height-food_size)]
        snake_length += 1

    # Check for collision with the walls
    if snake_head[0] < 0 or snake_head[0] > window_width-snake_size \
            or snake_head[1] < 0 \
            or snake_head[1] > window_height-snake_size:
        game_over = True

    # Check for collision with the snake's body
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Fill the screen with white
    game_window.fill((255, 255, 255))

    # Draw the snake
    for segment in snake_list:
        pygame.draw.rect(game_window, (0, 255, 0), [segment[0], segment[1], snake_size, snake_size])

    # Draw the food
    pygame.draw.rect(game_window, (255, 0, 0), [food_pos[0], food_pos[1], food_size, food_size])

    # Update the screen
    pygame.display.update()

    # Set the game clock tick rate
    clock.tick(snake_speed)

# Quit pygame
pygame.quit()

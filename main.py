import pygame
import sys
from enum import Enum
import random

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRICK_ROWS = 1
BRICK_COLS = 10
BRICK_HEIGHT = 20
X_SPEED_ADJUSTMENT_FACTOR = 4
FPS = 60

class Effect(Enum):
    ENLARGE_PADDLE = 1
    SHORTEN_PADDLE = 2

class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.speed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Ball:
    _MAX_SPEED_X = 5    # class level constant

    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.color = WHITE
        self.speed_x = 5
        self.speed_y = -5

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self, paddle, bricks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off the walls
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

        # Bounce off the paddle
        if self.rect.colliderect(paddle.rect):
            self.speed_y = -self.speed_y
            # Calculate the hit position on the paddle
            hit_pos = (self.rect.centerx - paddle.rect.left) / paddle.rect.width
            self.speed_x = (hit_pos - 0.5) * X_SPEED_ADJUSTMENT_FACTOR * Ball._MAX_SPEED_X  # Adjust x speed based on hit position

        # Bounce off a brick
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                # Apply the power-up effect
                self.apply_effect(paddle, brick.effect)
                # Remove the block and change ball speed
                bricks.remove(brick)
                self.speed_y = -self.speed_y
                break

    def apply_effect(self, paddle, effect):
        if effect == Effect.ENLARGE_PADDLE:
            paddle.rect.width = min(paddle.rect.width * 2, WIDTH)
        if effect == Effect.SHORTEN_PADDLE:
            paddle.rect.width /= 2

class Brick:
    def __init__(self, x, y, width, height, effect=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.effect = effect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

def check_game_over(bricks, ball):
    """Check if the game is over."""
    if not bricks:
        return True, "You Win!"
    if ball.rect.top >= HEIGHT:
        return True, "Game Over!"
    return False, ""

def init_bricks(width):
    """Initialize the bricks."""
    bricks = []
    brick_width = width // BRICK_COLS

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick = Brick(col * brick_width, row * BRICK_HEIGHT + 60, brick_width, BRICK_HEIGHT, random.choice(list(Effect)))
            bricks.append(brick)

    return bricks

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Breakout Clone")

    clock = pygame.time.Clock()

    paddle = Paddle(WIDTH // 2 - 100, HEIGHT - 30, 200, 20)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10)
    balls = []
    balls.append(ball)
    bricks = init_bricks(WIDTH)

    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        if not game_over:
            # Paddle movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move(-paddle.speed)
            if keys[pygame.K_RIGHT]:
                paddle.move(paddle.speed)

            # Ball movement
            ball.move(paddle, bricks)

            # Check if the game is over
            game_over, msg = check_game_over(bricks, ball)

        # Black background color
        window.fill(BLACK)

        # Draw everything needed
        ball.draw(window)
        for brick in bricks:
            brick.draw(window)
        paddle.draw(window)

        # Handle game over
        if game_over:
            font = pygame.font.Font(None, 74)
            text = font.render(msg, True, WHITE)
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
            window.blit(text, text_rect)

            # Restart or quit
            small_font = pygame.font.Font(None, 36)
            restart_text = small_font.render("Press R to Restart or Q to Quit", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
            window.blit(restart_text, restart_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset the game
                paddle = Paddle(WIDTH // 2 - 50, HEIGHT - 30, 100, 20)
                ball = Ball(WIDTH // 2, HEIGHT // 2, 10)
                bricks = init_bricks(WIDTH)
                game_over = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        # Update display
        pygame.display.flip()

        # Cap FPS
        clock.tick(FPS)

if __name__ == '__main__':
    main()


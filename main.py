from pywebio.output import *
from pywebio import start_server
import os

def main():
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
        }
        h1, h2 {
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
        }
        .social-button:hover {
            transform: translateY(-2px);
        }
        .facebook  { background-color: #1877F2; }
        .youtube   { background-color: #FF0000; }
        .instagram { background-color: #C13584; }
        .github    { background-color: #333333; }
        .render    { background-color: #00D3F7; }
        @media (max-width: 600px) {
            .social-button {
                padding: 8px 12px;
                font-size: 0.9rem;
            }
        }
    </style>

    <div class="container">
        <h1>موقع شركتنا</h1>
        <div class="social-buttons">
            <a href="https://www.facebook.com/fars.bla.frs.671146" class="social-button facebook" target="_blank">فيسبوك</a>
            <a href="https://www.youtube.com/@Programmer-s-Diary" class="social-button youtube" target="_blank">يوتيوب</a>
            <a href="https://www.instagram.com/frsbl_frs" class="social-button instagram" target="_blank">انستغرام</a>
        </div>
    </div>

    <div class="container">
        <h2>رافع الموقع</h2>
        <div class="social-buttons">
            <a href="https://github.com/your-username/your-repo" class="social-button github" target="_blank">GitHub</a>
            <a href="https://render.com/your-app-link" class="social-button render" target="_blank">Render</a>
        </div>
    </div>
    """)

# تشغيل التطبيق
PORT = int(os.getenv("PORT", 10000))
start_server(main, port=PORT, debug=True)
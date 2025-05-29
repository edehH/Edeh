from pywebio.output import put_html
from pywebio import start_server
import os

def web_main():
    put_html("""
    <style>
        body {
            font-family: "Segoe UI", Tahoma, sans-serif;
            background: url("https://www2.0zz0.com/2025/04/27/20/110982446.png") no-repeat center/cover fixed;
            color: #333;
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255,255,255,0.65);
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        h2, h3 {
            margin-bottom: 10px;
            color: #2c3e50;
        }
        .social-buttons {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 30px;
        }
        .social-box {
            text-align: center;
        }
        .social-image {
            width: 100px;
            height: 60px;
            border-radius: 8px;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
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
    </style>

    <div class="container">
        <h2>مواقعنا على منصات التواصل</h2>
        <div class="social-buttons">
            <div class="social-box">
                <a href="https://www.youtube.com/@%D9%8A%D9%8E%D9%88%D9%92%D9%85%D9%90%D9%8A%D9%8E%D8%A7%D8%AA%D9%92-%D9%85%D9%8F%D8%A8%D9%8E%D8%B1%D9%92%D9%85%D9%90%D8%AC%D9%92-%D9%85%D9%91%D9%8E%D8%B2%D9%8F%D8%AC%D9%92" target="_blank">
                    <img src="https://www2.0zz0.com/2025/04/29/06/582028911.png" class="social-image" alt="يوتيوب">
                </a>
                <h3>يوتيوب</h3>
            </div>
            <div class="social-box">
                <a href="https://www.instagram.com/frsbl_frs" target="_blank">
                    <img src="https://www2.0zz0.com/2025/04/29/06/276003792.png" class="social-image" alt="إنستغرام">
                </a>
                <h3>إنستغرام</h3>
            </div>
            <div class="social-box">
                <a href="https://www.facebook.com/fars.bla.frs.671146" target="_blank">
                    <img src="https://www2.0zz0.com/2025/04/29/06/721134643.png" class="social-image" alt="فيسبوك">
                </a>
                <h3>فيسبوك</h3>
            </div>
        </div>
    </div>

    <div class="container">
        <h3>نكات برمجية للمستوى الأول</h3>
        <div style="font-size:18px; line-height:1.8;">
            <div>1. 😂 ليش المبرمج يحب يستخدم الكومبيوتر؟ لأنه مكان ما فيهوش <b>bugs</b>... قصدي صراصير!</div>
            <div>2. 😄 كيف تعرف إن المبرمج مبسوط؟ لما يكون الكود تبعه <b>compile</b> من أول مرة!</div>
            <div>3. 🤔 وش الفرق بين المبرمج الكويس والمبرمج اللي مش كويس؟ الكويس بيكتب كود محد يفهمه، واللي مش كويس بيكتب كود حتى هو ما يفهمه!</div>
            <div>4. 😡 ليش المبرمج لما يعصب يروح يكتب كود؟ عشان يطلع اللي في قلبه على شكل <b>errors</b>!</div>
            <div>5. 😍 وش يقول المبرمج حق الـ <b>front-end</b> لما يشوف تصميم حلو؟ "يا له من <b>CSS</b> ساحر!"</div>
            <div>6. 😫 ليش المبرمج ما يحب الأفلام الطويلة؟ لأنه ما فيها <b>Ctrl + F</b> عشان يدور على الأحداث المهمة!</div>
            <div>7. 🤪 وش يسوي المبرمج لما يحس بالملل؟ يقعد يدور على <b>infinite loops</b> في الكود تبعه!</div>
            <div>8. 🛠 كيف المبرمج يصلح سيارته؟ يستخدم مفتاح <b>F12</b> عشان يشوف الـ <b>console</b>!</div>
            <div>9. 🤥 ليش المبرمج لما يتكلم عن مشكلة يقول "It's not a bug, it's a feature"? عشان يحس إنه مسوي شيء متعمد!</div>
            <div>10. 😎 وش أحلى شعور عند المبرمج؟ لما يلاقي حل لمشكلة قعد عليها أيام ويطلع سطر واحد!</div>
            <div>11. ☕ ليش المبرمج يحب الشاي والقهوة؟ عشان تساعده يسوي <b>debug</b> لعقله!</div>
            <div>12. 🥺 وش يقول المبرمج لما يعلق جهازه؟ "يا <b>Kernel</b> يا حبيبي!"</div>
            <div>13. ❤ كيف المبرمج يعبر عن حبه؟ يكتب كود فيه <b>comments</b> كلها قلوب!</div>
            <div>14. 🤓 ليش المبرمج لما يشتري شيء جديد ما يقرأ الـ <b>manual</b>؟ لأنه متعود يتعامل مع الـ <b>documentation</b>!</div>
            <div>15. ⏪ وش يسوي المبرمج لما يخرب الكود تبعه؟ يسوي <b>Ctrl + Z</b> ألف مرة!</div>
            <div>16. 📡 ليش المبرمج لما يروح مكان جديد يدور على الـ <b>Wi-Fi</b>؟ عشان يتأكد إنه متصل بالعالم!</div>
            <div>17. 🎉 وش يقول المبرمج لما ينجح مشروعه؟ "Finally, no more <b>segmentation fault</b>!"</div>
            <div>18. 😬 كيف المبرمج يحتفل بنهاية مشروع؟ يسوي <b>git push --force</b> على فرع الـ <b>main</b>! (طبعا هذا على مسؤوليته!)</div>
            <div>19. ✈ ليش المبرمج لما يسافر ياخذ معاه لاب توب؟ عشان يمكن يحتاج يسوي <b>hotfix</b> وهو في المطار!</div>
            <div>20. 👍 وش نصيحة المبرمج للمبتدئين؟ "لا تخافوا من الـ <b>errors</b>، تراها مجرد رسائل حب من الكومبيوتر!"</div>
        </div>
    </div>

    <div class="container">
        <h3>نكات برمجية للمستوى الثاني</h3>
        <div style="font-size:18px; line-height:1.8;">
            <div>21. ❄ ليش المبرمج دايمًا بارد؟ لأنه يتعامل مع الـ <b>cache</b>!</div>
            <div>22. 💤 مبرمج نام وهو يحل مشكلة... صحى لقاه <b>feature</b> مو <b>bug</b>!</div>
            <div>23. 🍳 مبرمج دخل مطعم، سألوه: كيف تفضل البيض؟ قال: <b>Boolean</b>... إما مسلوق أو لا.</div>
            <div>24. 🌊 لماذا يكره المبرمج البحر؟ لأنه مليان <b>crashes</b>.</div>
            <div>25. 🧠 مبرمج تقدم لوظيفة، سألوه عن خبرته؟ قال: عندي <b>Git commit history</b> أطول من حياتي!</div>
            <div>26. 🧘‍♂ كيف يعالج المبرمج الاكتئاب؟ يعمل <b>debug</b> لمشاعره.</div>
            <div>27. 🌙 ليش المبرمجين يحبون الليل؟ لأن الدنيا تصير <b>dark mode</b> طبيعي!</div>
            <div>28. 👶 لما المبرمج يتزوج، وش يسمي أولاده؟ <b>Array[0]</b>، <b>Array[1]</b>...</div>
            <div>29. 🥪 مبرمج فتح ثلاجة، كتب: <b>if (food == true) eat(); else sleep();</b></div>
        </div>
    </div>
    """)

if __name__ == '__main__':
    PORT = int(os.getenv("PORT", 10000))
    start_server(web_main, port=PORT, debug=True)

from pywebio import start_server
from pywebio.input import input, input_group, radio
from pywebio.output import put_text, put_html, put_table, toast, clear, put_buttons
from datetime import datetime
import sqlite3
import os

# الاتصال بقاعدة البيانات مع تفعيل check_same_thread=False
conn = sqlite3.connect("bookings.db", check_same_thread=False)
cursor = conn.cursor()

# إنشاء جدول للحجوزات إذا لم يكن موجودًا
cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    time TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )''')
conn.commit()

ADMIN_EMAIL = "edehwww@gmail.com"  # البريد الخاص بالمشرف

def delete_booking(index, is_admin):
    """يسمح بالحذف فقط إذا كان المستخدم مشرفًا"""
    if is_admin:
        cursor.execute("DELETE FROM bookings WHERE id = ?", (index,))
        conn.commit()
        toast("✅ تم حذف الحجز بنجاح!", color="warn")
    else:
        toast("❌ ليس لديك صلاحية لحذف الحجوزات!", color="error")
    clear()
    App()

def get_bookings():
    """جلب الحجوزات من قاعدة البيانات"""
    cursor.execute("SELECT id, user, phone, time FROM bookings")
    return cursor.fetchall()

def add_booking(user, phone, time):
    """إضافة حجز جديد إلى قاعدة البيانات"""
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO bookings (user, phone, time, created_at) VALUES (?, ?, ?, ?)",
                   (user, phone, time, created_at))
    conn.commit()

def App():
    """واجهة التطبيق الرئيسية"""
    put_html('''
    <meta name="google-adsense-account" content="ca-pub-7516051845423430">
    <meta name="description" content="هذا الموقع مخصص لحجز المباريات.">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7516051845423430"
         crossorigin="anonymous"></script>
    <style>
        html, body {
            background-image: url('https://www2.0zz0.com/2025/03/29/09/901974005.png');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            font-size: 18px;
            color: yellow;
        }
        *:not(html):not(body) {
            background: transparent !important;
            box-shadow: none !important;
            border: none !important;
            color: yellow;
        }
        .pywebio-container,
        .pywebio-content,
        .form-group,
        .input-group,
        .radio-group,
        .checkbox-group,
        .widget {
            background: transparent !important;
            box-shadow: none !important;
        }
        h3, p {
            font-size: 22px;
        }
        .radio-group label, .input-group label, .form-group label {
            font-size: 20px;
        }
        .pywebio-container {
            font-size: 20px;
        }

        /* نلغي أي خلفية مفروضة على الأزرار لتبقى خلفيتها الافتراضية */
        .pywebio-container button {
            background-color: initial !important;
        }
        
        /* استهداف أزرار النموذج باستخدام محددات nth-of-type */
        /* نفترض أن زر "التقدم" هو الأول في النموذج */
        .pywebio-form button:nth-of-type(1) {
            color: green !important;
        }
        /* وزر "إعادة ضبط" هو الثاني */
        .pywebio-form button:nth-of-type(2) {
            color: red !important;
        }
        
        .pywebio-container button:hover {
            opacity: 0.8;
        }
    </style>
    ''')

    put_html('''
        <div style="text-align:center;">
            <img src="https://i.postimg.cc/NMY7p2Jm/IMG-20250308-WA0003.jpg" 
                 style="width:100%; max-width: 800px; border-radius: 10px;" />
        </div>
    ''')

    # اختيار دور المستخدم
    role = radio("حدد نوع المستخدم", options=["أنا مشرف", "متابعة كزائر"])
    is_admin = False
    if role == "أنا مشرف":
        admin_email = input("📧 أدخل بريد المشرف للتحقق", required=True)
        if admin_email == ADMIN_EMAIL:
            is_admin = True
            toast("🎉 مرحباً مشرف الموقع!", color="success")
        else:
            toast("❌ بيانات المشرف غير صحيحة!", color="error")

    put_html('<center><h3>📅 المواعيد المحجوزة</h3></center>')
    bookings = get_bookings()
    if bookings:
        table_data = [['👤 الاسم', '📞 رقم الهاتف', '⏰ الوقت', '⚙ إجراء']]
        for booking in bookings:
            actions = put_buttons(["❌ حذف"], onclick=lambda x, idx=booking[0]: delete_booking(idx, is_admin)) if is_admin else "🚫"
            table_data.append([booking[1], booking[2], booking[3], actions])
        put_table(table_data)
    else:
        put_html('<center><p style="color:#3498db;">❌ لا يوجد حجوزات حتى الآن</p></center>')

    if is_admin:
        # هنا نموذج الحجز الجديد
        data = input_group("📝 حجز مباراة جديدة", [
            input('👤 ادخل اسم اللاعب', name='user', required=True),
            input('📞 ادخل رقم الهاتف', name='phone', required=True),
            input('⏰ ادخل الوقت الذي تريد الحجز فيه (مثال: 15:00)', name='time', required=True)
        ])
        cursor.execute("SELECT * FROM bookings WHERE time = ?", (data['time'],))
        existing_booking = cursor.fetchone()
        if existing_booking:
            toast("⚠ هذا الوقت محجوز بالفعل، يرجى اختيار وقت آخر!", color="error")
        else:
            add_booking(data['user'], data['phone'], data['time'])
            toast("✅ تمت إضافة الحجز بنجاح!", color="success")
        clear()
        App()
    else:
        put_html('<center><p>📲 للحجز اتواصل معنا ليتم عرضك في قائمة الحجوزات</p></center>')

# تشغيل التطبيق
PORT = int(os.getenv("PORT", 10000))
start_server(App, port=PORT, debug=True)
# رزومه ساز حرفه‌ای

<div dir="rtl">

> [🌐 English Version](README.md)

[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

یک رزومه‌ساز مدرن، ریسپانسیو و پر امکانات که به شما کمک می‌کند رزومه‌های حرفه‌ای به راحتی بسازید.

## ✨ ویژگی‌ها

- 🎨 طراحی مدرن و تمیز
- 🌓 حالت شب و روز
- 📱 کاملاً ریسپانسیو
- 🔍 بهینه‌سازی شده برای موتورهای جستجو
- 🎪 انیمیشن‌های روان
- 💼 نمایش نمونه کارها
- 🔗 یکپارچه‌سازی با شبکه‌های اجتماعی
- 📞 گزینه‌های سریع تماس

## 🚀 شروع به کار

### پیش‌نیازها

- پایتون 3.8 یا بالاتر
- مدیر بسته pip

### نصب و راه‌اندازی

1. کلون کردن مخزن:
```bash
git clone https://github.com/SeedHosein/resume.git
cd resume
```

2. ساخت محیط مجازی (توصیه شده):
```bash
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
```

3. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

4. اجرای برنامه:
```bash
python app.py
```

5. باز کردن http://localhost:5000 در مرورگر

## 🛠️ پیکربندی

### تنظیمات اولیه

1. فایل `app.py` را باز کنید
2. دیکشنری `data` را با اطلاعات خود تغییر دهید:

```python
data = {
    "firstname": "نام شما",
    "lastname": "نام خانوادگی شما",
    "title": "عنوان حرفه‌ای شما",
    "description": "توضیح مختصر درباره شما",
    "skills": ["مهارت 1", "مهارت 2"],
    # اضافه کردن جزئیات بیشتر...
}
```

### تنظیمات نمونه کارها

پروژه‌های خود را در بخش نمونه کارها اضافه کنید:

```python
"portfolio": {
    "دسته‌بندی": {
        "name": "نام دسته‌بندی",
        "projects": [
            {
                "title": "عنوان پروژه",
                "description": "توضیحات پروژه",
                "image": "آدرس_تصویر",
                "tags": ["برچسب1", "برچسب2"],
                "link": "لینک_پروژه"
            }
        ]
    }
}
```

### لینک‌های شبکه‌های اجتماعی

پروفایل‌های شبکه‌های اجتماعی خود را پیکربندی کنید:

```python
"contact": {
    "social": {
        "github": "آدرس_گیت‌هاب_شما",
        "linkedin": "آدرس_لینکدین_شما",
        "x": "آدرس_توییتر_شما",
        # اضافه کردن پلتفرم‌های بیشتر...
    }
}
```

## 🎨 شخصی‌سازی

### رنگ‌ها

برای تغییر طرح رنگی، فایل `static/css/style.css` را ویرایش کنید:

```css
:root {
    --primary: #6366f1;
    --primary-light: #a5b4fc;
    --primary-dark: #3730a3;
    /* اضافه/تغییر رنگ‌ها */
}
```

### تم‌ها

پروژه به صورت پیش‌فرض از تم‌های روشن/تاریک پشتیبانی می‌کند. تغییر تم به صورت خودکار مدیریت می‌شود.

## 📱 طراحی ریسپانسیو

رزومه کاملاً ریسپانسیو و بهینه‌شده برای:
- نمایشگرهای دسکتاپ
- تبلت‌ها
- دستگاه‌های موبایل
- جهت‌های مختلف نمایش

## 🤝 مشارکت

1. مخزن را fork کنید
2. شاخه ویژگی خود را بسازید (`git checkout -b feature/ویژگی_جدید`)
3. تغییرات خود را commit کنید (`git commit -m 'افزودن ویژگی جدید'`)
4. به شاخه push کنید (`git push origin feature/ویژگی_جدید`)
5. یک Pull Request باز کنید

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.

## 🌟 حمایت از پروژه

اگر این پروژه به شما کمک کرد، لطفاً یک ⭐️ به آن بدهید!

</div>

<!-- متاتگ‌های سئو -->
<meta name="description" content="رزومه‌ساز حرفه‌ای و مدرن با قابلیت‌های پیشرفته. دارای حالت شب/روز، نمایش نمونه کارها و یکپارچه‌سازی با شبکه‌های اجتماعی.">
<meta name="keywords" content="رزومه ساز, ساخت رزومه, رزومه آنلاین, رزومه حرفه‌ای, قالب رزومه, رزومه فارسی, cv ساز, رزومه ساز فارسی, رزومه انگلیسی">
<meta name="author" content="SeedHosein">
<meta name="robots" content="index, follow">
<meta property="og:title" content="رزومه ساز حرفه‌ای">
<meta property="og:description" content="رزومه‌ساز حرفه‌ای و مدرن با قابلیت‌های پیشرفته">
<meta property="og:url" content="https://github.com/SeedHosein/resume">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="رزومه ساز حرفه‌ای">
<meta name="twitter:description" content="رزومه‌ساز حرفه‌ای و مدرن با قابلیت‌های پیشرفته">"
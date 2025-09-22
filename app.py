from flask import Flask, request, redirect, url_for, render_template

data = {
    "firstname": "سیدحسین",
    "lastname": "موسوی دهاقانی",
    "age": "20",
    "title": "توسعه‌دهنده بک‌اند (Python & Django)",
    "description": "توسعه‌دهنده بک‌اند | متخصص API | عاشق یادگیری و خلاقیت",
    "about": "من یک توسعه‌دهنده بک‌اند با تمرکز بر Python و Django هستم. علاقه‌مند به یادگیری تکنولوژی‌های جدید و حل چالش‌های پیچیده.",
    "skills": [
        "Python",
        "Django",
        "Flask",
        "RESTful API",
        "Git",
        "PostgreSQL",
        "Linux",
        "Docker"
    ],
    "portfolio": {
        "backend": {
            "name": "بک‌اند",
            "projects": [
                {
                    "title": "پروژه مدیریت کاربران",
                    "description": "یک API برای مدیریت کاربران با Django REST Framework",
                    "image": "https://placehold.co/600x400/1f2937/a5b4fc?text=Backend",
                    "tags": ["Django", "REST", "API", "Backend"]
                },
                {
                    "title": "پروژه احراز هویت",
                    "description": "یک API برای احراز هویت کاربران با Django REST Framework",
                    "image": "https://placehold.co/600x400/1f2937/a5b4fc?text=Backend",
                    "tags": ["Django", "REST", "API"]
                }
            ]
        },
        "frontend": {
            "name": "فرانت‌اند",
            "projects": [
                {
                    "title": "وب‌سایت شرکتی",
                    "description": "یک وب‌سایت شرکتی با React",
                    "image": "https://placehold.co/600x400/38bdf8/1e3a8a?text=Frontend",
                    "tags": ["React", "Frontend"]
                },
                {
                    "title": "پروژه فروشگاه آنلاین",
                    "description": "یک فروشگاه آنلاین با React",
                    "image": "https://placehold.co/600x400/38bdf8/1e3a8a?text=Frontend",
                    "tags": ["React", "Frontend"]
                }
            ]
        },
        "fullstack": {
            "name": "فول‌استک",
            "projects": [
                {
                    "title": "فروشگاه آنلاین",
                    "description": "یک فروشگاه آنلاین با Django و React",
                    "image": "https://placehold.co/600x400/34d399/14532d?text=Fullstack",
                    "tags": ["Django", "React", "Fullstack"]
                },
                {
                    "title": "پروژه مدیریت محتوا",
                    "description": "یک پروژه فول‌استک با Django و React",
                    "image": "https://placehold.co/600x400/34d399/14532d?text=Fullstack",
                    "tags": ["Django", "React", "Fullstack"]
                }
            ]
        },
        "test": {
            "name": "تست",
            "projects": [
                {
                    "title": "پروژه تست",
                    "description": "یک پروژه تست با Django و React",
                    "image": "https://placehold.co/600x400/34d399/14532d?text=Test",
                    "tags": ["Django", "React", "Test"],
                    "link": "https://github.com/yourusername/test-project"
                }
            ]
        }
    },
    "contact": {
        "email": "SeedHosein0@email.com",
        "phone": "989966697895",
        "viewphone": "+98 996 669 7895",
        "telegram": "SeedHosein0",
        "location": "ایران، اصفهان",
        "social": {
            "github": "https://github.com/SeedHosein",
            "linkedin": "https://www.linkedin.com/in/SeedHosein",
            "instagram": "https://www.instagram.com/SeedHosein0",
            "whatsapp": "https://wa.me/989966697895",
        }
    }
}


app = Flask(
        __name__,
        static_folder='static',
        )
@app.route("/fa")
@app.route("/")
def index():
    return redirect(url_for('resume_fa'))

@app.route("/fa/resume")
def resume_fa():
    return render_template('resume.html', **data)


if __name__ == '__main__':
    app.run(debug=False)
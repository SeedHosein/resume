# Professional Resume Builder

> [🇮🇷 نسخه فارسی](README.fa.md)

[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A modern, responsive, and feature-rich resume builder that helps you create professional resumes with ease.

## ✨ Features

- 🎨 Modern and clean design
- 🌓 Dark/Light mode
- 📱 Fully responsive
- 🔍 SEO optimized
- 🎪 Smooth animations
- 💼 Portfolio showcase
- 🔗 Social media integration
- 📞 Quick contact options

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/SeedHosein/resume.git
cd resume
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open http://localhost:5000 in your browser

## 🛠️ Configuration

### Basic Setup

1. Open `app.py`
2. Modify the `data` dictionary with your information:

```python
data = {
    "firstname": "Your Name",
    "lastname": "Your Lastname",
    "title": "Your Professional Title",
    "description": "Brief description about you",
    "skills": ["Skill 1", "Skill 2"],
    # Add more details...
}
```

### Portfolio Setup

Add your projects in the portfolio section:

```python
"portfolio": {
    "category": {
        "name": "Category Name",
        "projects": [
            {
                "title": "Project Title",
                "description": "Project Description",
                "image": "image_url",
                "tags": ["tag1", "tag2"],
                "link": "project_url"
            }
        ]
    }
}
```

### Social Media Links

Configure your social media profiles:

```python
"contact": {
    "social": {
        "github": "your_github_url",
        "linkedin": "your_linkedin_url",
        "x": "your_twitter_url",
        # Add more platforms...
    }
}
```

## 🎨 Customization

### Colors

Edit `static/css/style.css` to modify the color scheme:

```css
:root {
    --primary: #6366f1;
    --primary-light: #a5b4fc;
    --primary-dark: #3730a3;
    /* Add/modify colors */
}
```

### Themes

The project supports dark/light themes out of the box. Theme switching is handled automatically.

## 📱 Responsive Design

The resume is fully responsive and optimized for:
- Desktop screens
- Tablets
- Mobile devices
- Different orientations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

<!-- SEO Meta Tags -->
<meta name="description" content="Create professional resumes easily with this modern, responsive resume builder. Features dark mode, portfolio showcase, and social media integration.">
<meta name="keywords" content="resume builder, cv maker, professional resume, online resume creator, portfolio builder, resume template, CV template, professional CV, resume generator">
<meta name="author" content="SeedHosein">
<meta name="robots" content="index, follow">
<meta property="og:title" content="Professional Resume Builder">
<meta property="og:description" content="Create professional resumes easily with this modern, responsive resume builder.">
<meta property="og:url" content="https://github.com/SeedHosein/resume">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Professional Resume Builder">
<meta name="twitter:description" content="Create professional resumes easily with this modern, responsive resume builder.">"
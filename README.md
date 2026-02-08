# Full Stack Developer Portfolio

A modern, animated single-page portfolio website built with Django, HTML, CSS, and JavaScript.

## Features

- Single-page design with smooth scrolling
- Animated sections and transitions
- Responsive layout
- Django admin panel for managing projects and skills
- Modern gradient design with glassmorphism effects

## Setup Instructions

1. Install Python (3.8 or higher)

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ to see your portfolio

9. Visit http://127.0.0.1:8000/admin to add projects and skills

## Customization

- Update personal information in `portfolio/templates/portfolio/index.html`
- Modify colors in `portfolio/static/css/style.css` (check the `:root` variables)
- Add your projects and skills through the Django admin panel
- Customize animations in `portfolio/static/js/script.js`

## Project Structure

```
portfolio_site/
├── portfolio/              # Main app
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── portfolio/
│   │       └── index.html
│   ├── models.py          # Project and Skill models
│   ├── views.py           # View logic
│   └── urls.py            # URL routing
├── portfolio_site/        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## Technologies Used

- Django 4.2
- HTML5
- CSS3 (with animations)
- JavaScript (Vanilla)
- SQLite

## License

MIT License

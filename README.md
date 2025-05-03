# TheNoteBlogs

A production-ready, modular Flask web application for www.thenoteblogs.store.

## Features
- Modular Blueprints for each section (Stories, Movies, etc.)
- Content managed via Markdown files
- Modern, responsive UI with semantic HTML
- SEO-friendly with meta tags and Google Adsense ad placeholders
- Ready for production deployment (WSGI entry point)

## Project Structure
```
thenoteblogs/
│   README.md
│   requirements.txt
│   wsgi.py
│
├── app/
│   ├── __init__.py
│   ├── main/           # Homepage, About, Terms, Privacy
│   ├── stories/        # Stories Blueprint
│   ├── movies/         # Movies Blueprint
│   ├── templates/
│   └── static/
│
├── content/
│   ├── stories/
│   └── movies/
└── static/
    ├── images/
    ├── css/
    └── js/
```

## Setup & Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app (development):
   ```bash
   flask run
   ```
3. Run in production (e.g., with gunicorn):
   ```bash
   gunicorn -w 4 wsgi:app
   ```
   ```bash
   gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app
   ```

## Content Management
- Add/edit Markdown files in `content/stories/` and `content/movies/`.
- Images go in `static/images/`.

## Google Adsense
- Replace ad placeholders in templates with your actual Adsense code.

## Contact
- Privacy Policy contact: random@gmail.com

---

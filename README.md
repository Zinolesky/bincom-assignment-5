# Bincom Python Assessment - Assignment 5: Multimedia Website Django Project

## Overview
A full-stack Django multimedia web platform enabling users to upload, stream, browse, and manage:
- **High-Definition Images** (with responsive lightbox zoom)
- **HTML5 Video Playback** (with custom controls and cover poster art)
- **Audio & Podcasts** (with interactive audio players)

---

## Key Features
1. **Multimedia Model Architecture (`MediaItem`, `Category`):**
   - Handles multi-format files with organized upload routing (`/media/multimedia/%Y/%m/`).
   - Categorization, views tracking, timestamps, and custom thumbnails.
2. **Dynamic Gallery UI:**
   - Real-time tab filtering across **All**, **Images**, **Videos**, and **Audio**.
   - Keyword search by title and description.
3. **Dedicated In-Browser Players:**
   - Embedded HTML5 `<video>` player.
   - Embedded `<audio>` player with album cover art display.
   - One-click asset download buttons.
4. **Interactive Upload Portal:**
   - Multi-part form handling with client & server-side validation.
5. **Django Admin Dashboard:**
   - Comprehensive administrative control over media approval, views, and categories.

---

## Project Structure
```text
bincom-assignment-5/
│
├── media/                      # Uploaded images, videos, audio & thumbnails
├── media_app/
│   ├── migrations/             # Database schema migrations
│   ├── templates/media_app/
│   │   ├── base.html           # Dark-themed modern layout & navbar
│   │   ├── gallery.html        # Filterable responsive multimedia grid
│   │   ├── detail.html         # In-browser multimedia player & metadata
│   │   └── upload.html         # File upload interface
│   ├── admin.py                # Admin panel registrations
│   ├── forms.py                # Multi-part file upload form
│   ├── models.py               # MediaItem and Category models
│   ├── tests.py                # Unit test suite
│   ├── urls.py                 # Media routing endpoints
│   └── views.py                # Gallery, detail & upload view controllers
│
├── multimedia_project/
│   ├── settings.py             # Django settings & MEDIA_URL / MEDIA_ROOT configs
│   ├── urls.py                 # Root URL routing
│   └── wsgi.py
│
├── .dockerignore
├── docker-compose.yml          # Containerized deployment orchestration
├── Dockerfile                  # Production container definition
├── manage.py
├── requirements.txt            # Django, Pillow, Gunicorn
├── seed_data.py                # Demo content seeder (Image, Audio, Video)
└── README.md
```

---

## How to Run

### Local Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run migrations
python manage.py migrate

# 3. Seed demo multimedia assets
python seed_data.py

# 4. Start the local development server
python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.

### Run Unit Tests
```bash
python manage.py test media_app
```

### Docker Setup
```bash
docker compose up --build
```

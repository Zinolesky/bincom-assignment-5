# The Road to Python — Full-Stack Multimedia Learning Platform
> **Bincom Python Assessment — Assignment 5: Multimedia Website Django Project**

[![Django](https://img.shields.io/badge/Django-5.1+-092e20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952b3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Overview

**The Road to Python** is a modern, responsive full-stack Django multimedia web platform built for developers navigating a comprehensive 9-phase learning roadmap. The application hosts, streams, and organizes **99 multimedia assets** spanning videos, audio stream lessons, podcasts, visual developer cheat sheets, and interactive PDF reference guides.

Every media card in the application features custom, high-resolution thumbnail previews—ensuring **zero blank placeholders** across all formats.

---

## The 9-Phase Learning Curriculum

The platform organizes content into an ordered 45-step sequential learning roadmap:

| Phase | Category | Roadmap Steps | Focus & Core Skills |
| :---: | :--- | :---: | :--- |
| **1** | **Python Core Mastery** | Step 1 | Syntax, OOP, data structures, exceptions, file I/O |
| **2** | **Database Design & SQL** | Steps 2–4 | Relational models, multi-table joins, transactions, constraints |
| **3** | **Web Frontend — HTML & CSS** | Steps 5–9 | Semantic layout, CSS Grid, Flexbox, responsive web design |
| **4** | **Web Frontend — JavaScript** | Steps 10–13 | DOM manipulation, async JavaScript, APIs, event handling |
| **5** | **Python Backend — Flask** | Steps 14–26 | Microservices, Jinja2 templating, REST endpoints, deployment |
| **6** | **Full-Stack Production — Django** | Steps 27–37 | ORM, MVT architecture, auth, migrations, admin customization |
| **7** | **Desktop GUI Development — Qt** | Step 38 | PySide/PyQt, event loops, desktop application architecture |
| **8** | **Mobile & Touch Interfaces — Kivy** | Steps 39–44 | Touch events, canvas rendering, geocoding, mobile packaging |
| **9** | **Low-Level Systems — C++ (Bonus)** | Step 45 | Memory management, pointers, compilation, systems interop |

---

## Key Features

### 1. Multi-Format Multimedia Streaming Engine
- **HTML5 Video Player:** Seamless playback of MP4 video lessons with custom poster frame art extracted using OpenCV.
- **Synchronized Audio Streams:** All 45 roadmap lessons are streamable via native HTML5 `<audio>` tags directly from video tracks—enabling on-the-go listening without requiring duplicate storage.
- **Interactive PDF Cheat Sheet Reader:** In-browser embedded PDF viewer with full scrolling, responsive toolbar, "Open in New Tab", and one-click download buttons.
- **Audio Podcasts:** Dedicated standalone technical discussion episodes with custom cover badges and soundwave graphics.
- **Visual Cheat Sheets:** High-resolution SVG architectural diagrams and syntax summaries with responsive lightbox view.

### 2. Smart Navigation & Real-Time Filtering
- Dynamic tab filtering across:
  - **Full Curriculum (99 assets)**
  - **Roadmap Videos (45 lessons)**
  - **PDF Cheat Sheets (4 guides)**
  - **Visual Cheat Sheets (2 diagrams)**
  - **Podcasts & Audio (48 audio streams & discussions)**
- Instant keyword search across titles and descriptions.
- Dynamic view counter tracking engagement on each media asset.

### 3. Automated Thumbnail Generation (Zero Blank Placeholders)
- **Video Previews:** Automated OpenCV frame capture at key instructional timestamps (~15–30s).
- **Audio / Podcast Art:** High-contrast navy podcast cards rendered with waveform visualizers and headphone badge icons.
- **PDF Documents:** Multi-page cover previews rendered at 144 DPI using `pypdfium2`.

### 4. Upload Portal & Administrative Control
- Client & server-side validated multi-part file upload portal (`/upload/`).
- Django Admin interface (`/admin/`) for categorization, content moderation, view metrics, and sequential step ordering.

---

## Project Structure

```text
bincom-assignment-5/
├── db.sqlite3                       # Pre-seeded database with 99 multimedia assets
├── docker-compose.yml               # Containerized deployment specification
├── Dockerfile                       # Production container build
├── manage.py                        # Django management command entrypoint
├── requirements.txt                 # Application dependencies
├── seed_data.py                     # 9-Phase curriculum seeder
├── README.md                        # Documentation
│
├── media/                           # Hosted media files
│   ├── documents/                   # PDF reference guides & cheat sheets
│   ├── multimedia/                  # Audio MP3s & SVG cheat sheets
│   │   ├── audio/                   # Technical discussion podcasts
│   │   └── images/                  # Visual cheat sheet graphics
│   └── thumbnails/                  # Generated cover preview art
│       ├── audio/                   # 48 podcast & audio stream cards
│       ├── documents/               # 4 high-res PDF cover thumbnails
│       └── videos/                  # 45 video frame captures
│
├── media_app/                       # Django core application
│   ├── migrations/                  # Schema migrations
│   ├── templates/media_app/         # Clean dark-mode UI templates
│   │   ├── base.html                # Navigation, footer, and styling
│   │   ├── gallery.html             # Filterable curriculum grid
│   │   ├── detail.html              # In-browser multimedia player
│   │   └── upload.html              # File upload interface
│   ├── admin.py                     # Admin customization
│   ├── forms.py                     # Multi-part file upload forms
│   ├── models.py                    # Category & MediaItem models
│   ├── tests.py                     # Automated unit test suite
│   ├── urls.py                      # App URL routing
│   └── views.py                     # View controllers & filtering logic
│
├── multimedia_project/              # Django project root configuration
│   ├── settings.py                  # Settings & media file routing
│   ├── urls.py                      # Root URL routing
│   ├── wsgi.py                      # WSGI configuration
│   └── asgi.py                      # ASGI configuration
│
└── static/                          # Static branding assets
    └── images/                      # Official logo, badge, and favicon
```

---

## Quickstart Guide

### 1. Prerequisites
- Python 3.11+
- Git

### 2. Local Setup
```bash
# Clone the repository
git clone https://github.com/Zinolesky/bincom-assignment-5.git
cd bincom-assignment-5

# Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# (Optional) Seed or re-seed the full 9-phase curriculum
python seed_data.py

# Launch development server
python manage.py runserver
```

Open **`http://127.0.0.1:8000/`** in your browser.

---

## Running Automated Tests

The test suite covers view responses, view counter increments, media type filtering, and PDF reader integration:

```bash
python manage.py test media_app
```

Expected output:
```text
Found 4 test(s).
Creating test database for alias 'default'...
....
----------------------------------------------------------------------
Ran 4 tests in 0.179s

OK
Destroying test database for alias 'default'...
```

---

## Docker Deployment

To launch the platform inside a containerized production environment:

```bash
# Build and run with Docker Compose
docker compose up --build -d

# Check running status
docker compose ps
```

Access the application at **`http://localhost:8000`**.

---

## Technology Stack

- **Framework:** [Django 5.1](https://www.djangoproject.com/)
- **Frontend:** Vanilla CSS, Bootstrap 5.3, Bootstrap Icons, Google Fonts (Inter)
- **Image & Document Processing:** [Pillow](https://python-pillow.org/), [pypdfium2](https://github.com/pypdfium2-team/pypdfium2), [OpenCV Headless](https://opencv.org/)
- **Audio Processing:** [gTTS](https://github.com/pndurette/gTTS)
- **WSGI Server:** [Gunicorn](https://gunicorn.org/)
- **Database:** SQLite (default) / PostgreSQL (production-ready)

---

## Author

**Efezino Prince Taigbenu**  
*Bincom Python Assessment 2026*

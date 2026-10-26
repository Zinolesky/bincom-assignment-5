"""
Comprehensive Seeder for 'The Road to Python' Multimedia Platform.

Ordered Learning Roadmap (Video + Audio Streams):
  Phase 1: Python Core Mastery (Step 1)
  Phase 2: Database Design & SQL (Steps 2-4)
  Phase 3: Web Frontend - HTML & CSS (Steps 5-9)
  Phase 4: Web Frontend - JavaScript (Steps 10-13)
  Phase 5: Python Backend - Flask (Steps 14-26)
  Phase 6: Production Full-Stack - Django (Steps 27-37)
  Phase 7: Desktop GUI Development - Qt (Step 38)
  Phase 8: Mobile & Touch Interfaces - Kivy (Steps 39-44)
  Phase 9: Low-Level Systems & C++ Bonus (Step 45)

All 45 roadmap lessons are available both as Full Videos and as Audio Streams (playable via HTML5 audio),
enabling listening on the go without requiring additional disk storage.
Plus:
  - Developer Cheat Sheets (Images)
  - Python Mastery Podcast Episodes (Audio MP3)
"""
import os
import glob
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_project.settings')
django.setup()

from django.conf import settings
from media_app.models import Category, MediaItem


def safe_print(text):
    try:
        print(text)
    except UnicodeEncodeError:
        print(str(text).encode('ascii', errors='replace').decode('ascii'))


def find_rel_file(subfolder, pattern):
    """
    Locates matching video file inside media/multimedia/videos/<subfolder>
    and returns its Django-relative media path (multimedia/videos/...).
    """
    media_root = str(settings.MEDIA_ROOT)
    folder = os.path.join(media_root, 'multimedia', 'videos', subfolder)
    matches = glob.glob(os.path.join(folder, pattern))
    if matches:
        return os.path.relpath(matches[0], media_root).replace('\\', '/')
    
    clean_pat = pattern.replace('*', '')
    return f"multimedia/videos/{subfolder}/{clean_pat}"


def seed():
    safe_print("=" * 75)
    safe_print("Seeding 'The Road to Python' Full-Stack Curriculum (Video + Audio Streams)...")
    safe_print("=" * 75)

    MediaItem.objects.all().delete()
    Category.objects.all().delete()

    # 1. Categories
    cat_phase1, _ = Category.objects.get_or_create(
        name="Phase 1: Python Core Mastery",
        slug="phase-1-core",
        description="Comprehensive foundations covering Python syntax, data structures, and functions before frameworks."
    )
    cat_phase2, _ = Category.objects.get_or_create(
        name="Phase 2: Database Design & SQL",
        slug="phase-2-sql",
        description="Master database queries, schema design, and table relationships before building persistent apps."
    )
    cat_phase3, _ = Category.objects.get_or_create(
        name="Phase 3: Web Frontend - HTML & CSS",
        slug="phase-3-html-css",
        description="Learn document structure, modern semantic markup, responsive CSS layout, and layout projects."
    )
    cat_phase4, _ = Category.objects.get_or_create(
        name="Phase 4: Web Frontend - JavaScript",
        slug="phase-4-javascript",
        description="Add frontend interactivity, DOM manipulation, asynchronous event handling, and client-server flow."
    )
    cat_phase5, _ = Category.objects.get_or_create(
        name="Phase 5: Python Backend - Flask",
        slug="phase-5-flask",
        description="Connect Python to the web: routing, Jinja2 templates, forms, sessions, SQLAlchemy, and Linux WSGI."
    )
    cat_phase6, _ = Category.objects.get_or_create(
        name="Phase 6: Production Full-Stack - Django",
        slug="phase-6-django",
        description="Master batteries-included Python web engineering: MVT architecture, Django ORM, authentication, admin panel, and REST APIs."
    )
    cat_phase7, _ = Category.objects.get_or_create(
        name="Phase 7: Desktop GUI Development - Qt",
        slug="phase-7-qt",
        description="Master standard event-driven desktop GUI applications, signal-slot architectures, and native widgets."
    )
    cat_phase8, _ = Category.objects.get_or_create(
        name="Phase 8: Mobile App Development - Kivy",
        slug="phase-8-kivy",
        description="Transition to custom touch and mobile interfaces: Kv design language, gestures, map views, and GPS."
    )
    cat_bonus, _ = Category.objects.get_or_create(
        name="Phase 9: Low-Level Systems & C++ (Bonus)",
        slug="phase-9-bonus-cpp",
        description="Wrap up your foundation: explore low-level memory pointers, static typing, and machine-level compilation."
    )
    cat_cheatsheet, _ = Category.objects.get_or_create(
        name="Developer Cheat Sheets",
        slug="developer-cheat-sheets",
        description="Quick-reference visual cards for syntax, collections, backend patterns, and Docker."
    )
    cat_podcasts, _ = Category.objects.get_or_create(
        name="Tech Podcasts",
        slug="tech-podcasts",
        description="Deep-dive audio episodes on roadmap milestones, microservices, and time complexity."
    )

    # 2. Roadmap Video & Audio Curriculum (45 Steps)
    roadmap_items = [
        # PHASE 1: Python Core Mastery
        {
            "step": 1,
            "title": "Roadmap Step 1: 12-Hour Python Full Course by Bro Code",
            "desc": "The ultimate starting point: master core variables, collections, loops, object-oriented programming (OOP), file I/O, and foundational Python concepts.",
            "sub": "01_Python_Core",
            "pat": "*Python Full Course*",
            "cat": cat_phase1,
            "views": 2450,
        },

        # PHASE 2: Database Design & SQL
        {
            "step": 2,
            "title": "Roadmap Step 2A: SQL Day 1 - Introduction to SQL & Basic Queries",
            "desc": "Learn relational database architecture, writing SELECT queries, column filtering with WHERE, ordering, and data types before building apps that store data.",
            "sub": "02_SQL",
            "pat": "*Day 1*",
            "cat": cat_phase2,
            "views": 1150,
        },
        {
            "step": 3,
            "title": "Roadmap Step 2B: SQL Day 2 - Manipulating Data & Multiple Tables",
            "desc": "Master INSERT, UPDATE, DELETE, Foreign Keys, table joins (INNER, LEFT, RIGHT), and multi-table relational integrity.",
            "sub": "02_SQL",
            "pat": "*Day 2*",
            "cat": cat_phase2,
            "views": 1020,
        },
        {
            "step": 4,
            "title": "Roadmap Step 2C: SQL Day 3 - Advanced Queries & Real-World Applications",
            "desc": "Aggregate functions (GROUP BY, HAVING), subqueries, index optimization, and real-world backend data analysis.",
            "sub": "02_SQL",
            "pat": "*Day 3*",
            "cat": cat_phase2,
            "views": 940,
        },

        # PHASE 3: Web Frontend - HTML & CSS
        {
            "step": 5,
            "title": "Roadmap Step 3A: HTML & CSS Full Course for Beginners",
            "desc": "Learn how web pages are structured and styled so you can build robust templates for your Python web apps.",
            "sub": "03_HTML_CSS",
            "pat": "*ssvid.app--HTML-CSS*",
            "cat": cat_phase3,
            "views": 1380,
        },
        {
            "step": 6,
            "title": "Roadmap Step 3B: HTML & CSS Day 1 - Introduction to HTML Structure",
            "desc": "Core semantic HTML tags, document structure, forms, inputs, and accessibility standards.",
            "sub": "03_HTML_CSS",
            "pat": "*Day 1 Introduction*",
            "cat": cat_phase3,
            "views": 890,
        },
        {
            "step": 7,
            "title": "Roadmap Step 3C: HTML & CSS Day 2 - Styling and Layout with CSS",
            "desc": "CSS Box Model, padding, margins, borders, typography, colors, and positioning.",
            "sub": "03_HTML_CSS",
            "pat": "*Day 2 Styling*",
            "cat": cat_phase3,
            "views": 820,
        },
        {
            "step": 8,
            "title": "Roadmap Step 3D: HTML & CSS Day 3 - Advanced Styling & Responsive Design",
            "desc": "Mastering Flexbox, media queries, mobile-responsive viewports, and modern UI styling.",
            "sub": "03_HTML_CSS",
            "pat": "*Day 3 Advanced*",
            "cat": cat_phase3,
            "views": 790,
        },
        {
            "step": 9,
            "title": "Roadmap Step 3E: Day 1 Netflix Clone - Building the Homepage Layout",
            "desc": "Apply what you just learned in HTML & CSS by building a real-world streaming service layout project before moving to scripting.",
            "sub": "03_HTML_CSS",
            "pat": "*Netflix Clone*",
            "cat": cat_phase3,
            "views": 1260,
        },

        # PHASE 4: Web Frontend - JavaScript
        {
            "step": 10,
            "title": "Roadmap Step 4A: Learn JavaScript - Full Course for Beginners",
            "desc": "Add frontend interactivity and learn how the browser communicates with backend Python servers.",
            "sub": "04_JavaScript",
            "pat": "*Learn JavaScript*",
            "cat": cat_phase4,
            "views": 1420,
        },
        {
            "step": 11,
            "title": "Roadmap Step 4B: JavaScript Day 1 - Variables, Data Types & Control Flow",
            "desc": "Core syntax, let vs const, conditionals, loops, functions, and fundamental program logic.",
            "sub": "04_JavaScript",
            "pat": "*Day 1*",
            "cat": cat_phase4,
            "views": 760,
        },
        {
            "step": 12,
            "title": "Roadmap Step 4C: JavaScript Day 2 - Advanced Data Handling and Functions",
            "desc": "Working with arrays, object literals, arrow functions, higher-order methods, and scope.",
            "sub": "04_JavaScript",
            "pat": "*Day 2*",
            "cat": cat_phase4,
            "views": 710,
        },
        {
            "step": 13,
            "title": "Roadmap Step 4D: JavaScript Day 3 - DOM Manipulation & Interactive Events",
            "desc": "Querying DOM nodes, event listeners, handling user clicks and keystrokes, and dynamic UI updates.",
            "sub": "04_JavaScript",
            "pat": "*Day 3*",
            "cat": cat_phase4,
            "views": 740,
        },

        # PHASE 5: Python Backend - Flask
        {
            "step": 14,
            "title": "Roadmap Step 5A: Learn Flask for Python - Full Tutorial (freeCodeCamp)",
            "desc": "Connect your Python skills with your HTML/CSS/JS frontend knowledge using a lightweight web microframework.",
            "sub": "05_Flask",
            "pat": "*Learn Flask*",
            "cat": cat_phase5,
            "views": 1540,
        },
        {
            "step": 15,
            "title": "Roadmap Step 5B: Flask Tutorial 1 - How to Make Websites with Python",
            "desc": "Creating your first Flask application, routing decorators, dynamic parameters, and running local servers.",
            "sub": "05_Flask",
            "pat": "*Tutorial 1 -*",
            "cat": cat_phase5,
            "views": 690,
        },
        {
            "step": 16,
            "title": "Roadmap Step 5C: Flask Tutorial 2 - HTML Templates & Jinja2",
            "desc": "Dynamic template rendering with Jinja2, expressions, loops, and conditional presentation logic.",
            "sub": "05_Flask",
            "pat": "*Tutorial 2 -*",
            "cat": cat_phase5,
            "views": 630,
        },
        {
            "step": 17,
            "title": "Roadmap Step 5D: Flask Tutorial 3 - Bootstrap Styling & Template Inheritance",
            "desc": "Inheriting base templates and styling responsive navigation bars with Bootstrap 5.",
            "sub": "05_Flask",
            "pat": "*Tutorial 3 -*",
            "cat": cat_phase5,
            "views": 590,
        },
        {
            "step": 18,
            "title": "Roadmap Step 5E: Flask Tutorial 4 - HTTP Methods (GET & POST) Form Data",
            "desc": "Safely capturing incoming user inputs, processing form submissions, and request handling.",
            "sub": "05_Flask",
            "pat": "*Tutorial 4 -*",
            "cat": cat_phase5,
            "views": 550,
        },
        {
            "step": 19,
            "title": "Roadmap Step 5F: Flask Tutorial 5 - User Sessions & State",
            "desc": "Managing user state across requests, signed cookies, and session-based authentication.",
            "sub": "05_Flask",
            "pat": "*Tutorial 5 -*",
            "cat": cat_phase5,
            "views": 510,
        },
        {
            "step": 20,
            "title": "Roadmap Step 5G: Flask Tutorial 6 - Message Flashing & Alerts",
            "desc": "Displaying feedback and notification banners across redirect responses.",
            "sub": "05_Flask",
            "pat": "*Tutorial 6 -*",
            "cat": cat_phase5,
            "views": 470,
        },
        {
            "step": 21,
            "title": "Roadmap Step 5H: Flask Tutorial 7 - Using SQLAlchemy Database",
            "desc": "Connecting Python backends to relational databases via ORM models, migrations, and automated record persistence.",
            "sub": "05_Flask",
            "pat": "*Tutorial 7 -*",
            "cat": cat_phase5,
            "views": 580,
        },
        {
            "step": 22,
            "title": "Roadmap Step 5I: Flask Tutorial 8 - Adding, Deleting & Updating Users",
            "desc": "Full database CRUD implementation with SQLAlchemy models and transactional commits.",
            "sub": "05_Flask",
            "pat": "*Tutorial 8 -*",
            "cat": cat_phase5,
            "views": 520,
        },
        {
            "step": 23,
            "title": "Roadmap Step 5J: Flask Tutorial 9 - Static Files (CSS, JS, Media)",
            "desc": "Serving custom CSS, JavaScript, and user-uploaded media assets effectively.",
            "sub": "05_Flask",
            "pat": "*Tutorial 9 -*",
            "cat": cat_phase5,
            "views": 480,
        },
        {
            "step": 24,
            "title": "Roadmap Step 5K: Flask Tutorial 10 - Blueprints & Modular Architecture",
            "desc": "Structuring large Python web apps using modular Blueprints across multiple packages.",
            "sub": "05_Flask",
            "pat": "*Tutorial 10 -*",
            "cat": cat_phase5,
            "views": 560,
        },
        {
            "step": 25,
            "title": "Roadmap Step 5L: Python Flask Tutorial - Blueprints and Configuration",
            "desc": "Modular application factories, config class separation, and enterprise project layout.",
            "sub": "05_Flask",
            "pat": "*Part 11*",
            "cat": cat_phase5,
            "views": 610,
        },
        {
            "step": 26,
            "title": "Roadmap Step 5M: How to Deploy a Flask App to a Linux Server",
            "desc": "Production engineering: configuring Gunicorn WSGI, Nginx reverse proxy, and systemd services.",
            "sub": "05_Flask",
            "pat": "*Deploy a Flask App*",
            "cat": cat_phase5,
            "views": 980,
        },

        # PHASE 6: Production Full-Stack - Django
        {
            "step": 27,
            "title": "Roadmap Step 6A: Django Introduction - What is Django & Architecture",
            "desc": "Introduction to Django's batteries-included philosophy, Model-View-Template (MVT) pattern, and request lifecycle.",
            "sub": "06_Django",
            "pat": "*01002*",
            "cat": cat_phase6,
            "views": 1650,
        },
        {
            "step": 28,
            "title": "Roadmap Step 6B: Django Setup - Installing & Creating Your Project",
            "desc": "Virtual environments, django-admin startproject, apps structure, and starting the local development server.",
            "sub": "06_Django",
            "pat": "*02003*",
            "cat": cat_phase6,
            "views": 1420,
        },
        {
            "step": 29,
            "title": "Roadmap Step 6C: Django URLs, Views & Dynamic Path Routing",
            "desc": "URL dispatching, view functions, path converters, capturing parameters, and reverse URL resolution.",
            "sub": "06_Django",
            "pat": "*03003*",
            "cat": cat_phase6,
            "views": 1310,
        },
        {
            "step": 30,
            "title": "Roadmap Step 6D: Django Templates & Dynamic Rendering",
            "desc": "Django template language (DTL), context dictionaries, filters, template inheritance, and base layouts.",
            "sub": "06_Django",
            "pat": "*04003*",
            "cat": cat_phase6,
            "views": 1250,
        },
        {
            "step": 31,
            "title": "Roadmap Step 6E: Data Models, Migrations & SQLite Setup",
            "desc": "Defining Django model fields, running makemigrations and migrate, and inspecting schema generation.",
            "sub": "06_Django",
            "pat": "*05002*",
            "cat": cat_phase6,
            "views": 1190,
        },
        {
            "step": 32,
            "title": "Roadmap Step 6F: The Django Admin Panel & Model Registration",
            "desc": "Creating superusers, registering models with admin.site.register, and configuring custom list displays.",
            "sub": "06_Django",
            "pat": "*07002*",
            "cat": cat_phase6,
            "views": 1130,
        },
        {
            "step": 33,
            "title": "Roadmap Step 6G: Django Model Relationships (One-to-Many & Many-to-Many)",
            "desc": "ForeignKeys, ManyToManyField, related_name, query filtering across relationships, and on_delete cascades.",
            "sub": "06_Django",
            "pat": "*08002*",
            "cat": cat_phase6,
            "views": 1070,
        },
        {
            "step": 34,
            "title": "Roadmap Step 6H: Django Forms & ModelForms",
            "desc": "Form validation, CSRF token security, cleaning user input, and automatic ModelForm persistence.",
            "sub": "06_Django",
            "pat": "*10015*",
            "cat": cat_phase6,
            "views": 990,
        },
        {
            "step": 35,
            "title": "Roadmap Step 6I: Class-Based Views (CBV) & Generic Views",
            "desc": "ListView, DetailView, CreateView, UpdateView, and DeleteView for standardized CRUD operations.",
            "sub": "06_Django",
            "pat": "*10018*",
            "cat": cat_phase6,
            "views": 950,
        },
        {
            "step": 36,
            "title": "Roadmap Step 6J: User Uploads, Media Files & File Handling",
            "desc": "Configuring MEDIA_URL and MEDIA_ROOT, FileField, ImageField, and serving user-uploaded content.",
            "sub": "06_Django",
            "pat": "*14002*",
            "cat": cat_phase6,
            "views": 910,
        },
        {
            "step": 37,
            "title": "Roadmap Step 6K: Deploying Django to Production",
            "desc": "Environment variables, ALLOWED_HOSTS, DEBUG=False, Whitenoise static file serving, and WSGI servers.",
            "sub": "06_Django",
            "pat": "*15002*",
            "cat": cat_phase6,
            "views": 1390,
        },

        # PHASE 7: Desktop GUI Development - Qt
        {
            "step": 38,
            "title": "Roadmap Step 7: Qt Crash Course for Beginners - Create Desktop GUI Apps",
            "desc": "Study the Qt folder first for standard event-driven desktop GUI widgets, window layouts, signal-slot event loops, and native dialogs.",
            "sub": "07_Qt",
            "pat": "*Qt Crash Course*",
            "cat": cat_phase7,
            "views": 840,
        },

        # PHASE 8: Mobile App Development - Kivy
        {
            "step": 39,
            "title": "Roadmap Step 8A: Kivy Full Course - Create Python Games & Mobile Apps",
            "desc": "Pivot from web and desktop to building cross-platform desktop and mobile touch interfaces in Python.",
            "sub": "08_Kivy",
            "pat": "*www.ssvid.net--Kivy*",
            "cat": cat_phase8,
            "views": 1180,
        },
        {
            "step": 40,
            "title": "Roadmap Step 8B: Kivy App Part 1 - Architecture & Setup",
            "desc": "Structuring a production-ready mobile application project with Kivy and KivyMD.",
            "sub": "08_Kivy",
            "pat": "*Part 1_*",
            "cat": cat_phase8,
            "views": 520,
        },
        {
            "step": 41,
            "title": "Roadmap Step 8C: Kivy App Part 2 - Map & Local Database",
            "desc": "Integrating SQLite and interactive map views inside Python mobile applications.",
            "sub": "08_Kivy",
            "pat": "*Part 2_*",
            "cat": cat_phase8,
            "views": 470,
        },
        {
            "step": 42,
            "title": "Roadmap Step 8D: Kivy App Part 3 - Markers & Dynamic Menus",
            "desc": "Rendering custom touch markers and popup navigation menus.",
            "sub": "08_Kivy",
            "pat": "*Part 3_*",
            "cat": cat_phase8,
            "views": 410,
        },
        {
            "step": 43,
            "title": "Roadmap Step 8E: Kivy App Part 4 - Search Menu & Geocoding",
            "desc": "Implementing search bars, geocoding coordinates, and real-time list filtering.",
            "sub": "08_Kivy",
            "pat": "*Part 4_*",
            "cat": cat_phase8,
            "views": 390,
        },
        {
            "step": 44,
            "title": "Roadmap Step 8F: Kivy App Part 6 - GPS Markers & Android Permissions",
            "desc": "Requesting Android runtime permissions and reading hardware GPS sensors directly from Python.",
            "sub": "08_Kivy",
            "pat": "*Part 6_*",
            "cat": cat_phase8,
            "views": 530,
        },

        # PHASE 9: Low-Level Systems & C++ (Bonus)
        {
            "step": 45,
            "title": "Roadmap Bonus (Optional): C++ Full Course for Free (Low-Level Systems)",
            "desc": "Tackle low-level memory management and static typing last as an advanced systems bonus to master low-level programming concepts.",
            "sub": "09_CPP_Bonus",
            "pat": "*C++ Full Course*",
            "cat": cat_bonus,
            "views": 1820,
        },
    ]

    safe_print("Inserting 45 Video Roadmap Steps + 45 Audio Stream Roadmap Lessons...")
    for item in roadmap_items:
        rel_file = find_rel_file(item["sub"], item["pat"])
        clean_topic = item["title"].split(": ", 1)[-1] if ": " in item["title"] else item["title"]

        # 1. Video Lesson
        m_video = MediaItem.objects.create(
            title=item["title"],
            description=item["desc"],
            media_type="video",
            category=item["cat"],
            media_file=rel_file,
            step_number=item["step"],
            views_count=item["views"],
        )
        safe_print(f"  [Video Step {m_video.step_number:02d}] {m_video.title}")

        # 2. Audio Stream Lesson (Option 1: Stream audio track directly from same MP4 container)
        audio_title = f"Audio Lesson {item['step']:02d}: {clean_topic} (Audio Stream)"
        audio_desc = f"Listen on the go: streaming the full audio lesson for Step {item['step']}. {item['desc']}"
        m_audio = MediaItem.objects.create(
            title=audio_title,
            description=audio_desc,
            media_type="audio",
            category=item["cat"],
            media_file=rel_file,
            step_number=item["step"],
            views_count=int(item["views"] * 0.45) + 30,
        )
        safe_print(f"  [Audio Step {m_audio.step_number:02d}] {m_audio.title}")

    # 3. Developer Cheat Sheets (Images)
    cheat_sheets = [
        {
            "title": "Cheat Sheet: Python 3 Core Syntax & Data Structures",
            "desc": "Quick visual reference covering primary data types, mutability (lists, tuples, dicts, sets), control flow, list comprehensions, lambda, and memory-efficient generators.",
            "file": "multimedia/images/python_basics_cheatsheet.svg",
            "cat": cat_cheatsheet,
            "views": 920,
        },
        {
            "title": "Cheat Sheet: Web Frameworks, SQL & Deployment Architecture",
            "desc": "Quick visual reference card comparing Flask microframework routes to Django MVT architecture, CRUD SQL operations, Gunicorn/Nginx setups, and Docker Compose configurations.",
            "file": "multimedia/images/web_backend_cheatsheet.svg",
            "cat": cat_cheatsheet,
            "views": 840,
        },
    ]

    for sheet in cheat_sheets:
        m = MediaItem.objects.create(
            title=sheet["title"],
            description=sheet["desc"],
            media_type="image",
            category=sheet["cat"],
            media_file=sheet["file"],
            step_number=0,
            views_count=sheet["views"],
        )
        safe_print(f"  [Resource - Image] {m.title}")

    # 4. Podcasts (Audio)
    podcasts = [
        {
            "title": "The Road to Python Podcast - Ep 1: The Modern Developer Roadmap",
            "desc": "Episode 1 breaks down the optimal learning roadmap: from syntax and SQL to building distributed backends and mobile apps.",
            "file": "multimedia/audio/podcast_ep1_roadmap.mp3",
            "cat": cat_podcasts,
            "views": 410,
        },
        {
            "title": "The Road to Python Podcast - Ep 2: Flask vs Django & Cloud Microservices",
            "desc": "Episode 2 compares minimalist microservices with batteries-included frameworks, exploring database connection pooling and containerized deployments.",
            "file": "multimedia/audio/podcast_ep2_backend.mp3",
            "cat": cat_podcasts,
            "views": 380,
        },
        {
            "title": "The Road to Python Podcast - Ep 3: Algorithmic Efficiency, Sorting & Generators",
            "desc": "Episode 3 delves into O(n log n) sorting, binary search, and the mechanics of Python's yield generator functions.",
            "file": "multimedia/audio/podcast_ep3_algorithms.mp3",
            "cat": cat_podcasts,
            "views": 330,
        },
    ]

    for pod in podcasts:
        m = MediaItem.objects.create(
            title=pod["title"],
            description=pod["desc"],
            media_type="audio",
            category=pod["cat"],
            media_file=pod["file"],
            step_number=0,
            views_count=pod["views"],
        )
        safe_print(f"  [Resource - Audio] {m.title}")

    total = MediaItem.objects.count()
    videos = MediaItem.objects.filter(media_type='video').count()
    audios = MediaItem.objects.filter(media_type='audio').count()
    safe_print("=" * 75)
    safe_print("Seeding completed successfully!")
    safe_print(f"  Total Roadmap Video Steps: {videos}")
    safe_print(f"  Total Roadmap Audio Steps: {audios}")
    safe_print(f"  Total Multimedia Items:    {total}")
    safe_print("=" * 75)


if __name__ == "__main__":
    seed()

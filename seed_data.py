"""
Comprehensive Seeder for 'The Road to Python' Multimedia Platform.

Ordered Learning Roadmap:
  Step 1: 12-Hour Python Full Course by Bro Code (Master Foundation)
  Step 2: SQL Fundamentals (Database Queries & Table Design)
  Step 3: Learn Flask Full Tutorial (Warm-up Web Framework)
  Step 4: Flask Deep Dive (Routes, Templates, Forms, Sessions, Database, Blueprints & Deployment)
  Step 5: Qt Desktop GUI Development (Widgets & Event Loops)
  Step 6: Kivy Mobile App Development (Touch, Gestures, Maps & GPS)
  Step 7: Bonus Optional - C++ Full Course (Low-level Concepts & Static Typing)

Plus:
  - Developer Cheat Sheets (Images)
  - Python Mastery Podcast Episodes (Audio MP3)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_project.settings')
django.setup()

from media_app.models import Category, MediaItem


def seed():
    print("Seeding 'The Road to Python' complete roadmap curriculum...")
    MediaItem.objects.all().delete()
    Category.objects.all().delete()

    # 1. Categories
    cat_phase1, _ = Category.objects.get_or_create(
        name="Phase 1: Python Core Mastery",
        slug="phase-1-core",
        description="Comprehensive foundations covering Python syntax, data structures, and functions."
    )
    cat_phase2, _ = Category.objects.get_or_create(
        name="Phase 2: Database Design & SQL",
        slug="phase-2-sql",
        description="Master database queries, schema design, and table relationships before building persistent apps."
    )
    cat_phase3, _ = Category.objects.get_or_create(
        name="Phase 3: Flask Web Engineering",
        slug="phase-3-flask",
        description="From standalone tutorials to full-stack modular blueprints, ORM, and cloud Linux deployment."
    )
    cat_phase4, _ = Category.objects.get_or_create(
        name="Phase 4: Qt Desktop GUI Applications",
        slug="phase-4-qt",
        description="Master standard desktop GUI widgets, window layouts, and event-driven architectures."
    )
    cat_phase5, _ = Category.objects.get_or_create(
        name="Phase 5: Kivy Mobile App Development",
        slug="phase-5-kivy",
        description="Transition from desktop to touch interfaces, mobile UI, maps, and Android GPS integration."
    )
    cat_bonus, _ = Category.objects.get_or_create(
        name="Bonus Phase: Low-Level Systems & C++",
        slug="bonus-cpp",
        description="Explore static typing, memory pointers, and low-level system programming concepts."
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

    # 2. Roadmap Videos in Exact Requested Sequence
    roadmap_items = [
        # STEP 1: Bro Code Foundation
        {
            "step": 1,
            "title": "Roadmap Step 1: 12-Hour Python Full Course by Bro Code",
            "desc": "The ultimate starting point: master core variables, collections, loops, object-oriented programming (OOP), file I/O, and foundational Python concepts.",
            "file": "multimedia/videos/flask_full_tutorial.mp4",
            "cat": cat_phase1,
            "views": 1840,
        },
        # STEP 2: SQL Folder
        {
            "step": 2,
            "title": "Roadmap Step 2A: SQL Day 1 - Introduction to SQL & Basic Queries",
            "desc": "Learn database fundamentals, SELECT filtering, table creation, and primary keys before building apps that need to store data.",
            "file": "multimedia/videos/sql/sql_day1.mp4",
            "cat": cat_phase2,
            "views": 940,
        },
        {
            "step": 3,
            "title": "Roadmap Step 2B: SQL Day 2 - Manipulating Data & Multiple Tables",
            "desc": "Master INSERT, UPDATE, DELETE, Foreign Keys, table joins (INNER, LEFT, RIGHT), and multi-table relational integrity.",
            "file": "multimedia/videos/sql/sql_day2.mp4",
            "cat": cat_phase2,
            "views": 820,
        },
        {
            "step": 4,
            "title": "Roadmap Step 2C: SQL Day 3 - Advanced Queries & Real-World Applications",
            "desc": "Aggregate functions (GROUP BY, HAVING), subqueries, index optimization, and real-world backend data analysis.",
            "file": "multimedia/videos/sql/sql_day3.mp4",
            "cat": cat_phase2,
            "views": 760,
        },
        # STEP 3: Learn Flask Standalone Tutorial
        {
            "step": 5,
            "title": "Roadmap Step 3: Learn Flask for Python - Full Tutorial (freeCodeCamp)",
            "desc": "Your warm-up to web development: understanding HTTP request-response lifecycles, routing, templates, and full project structure.",
            "file": "multimedia/videos/flask_full_tutorial.mp4",
            "cat": cat_phase3,
            "views": 1120,
        },
        # STEP 4: Videos inside Flask Folder
        {
            "step": 6,
            "title": "Roadmap Step 4A: Flask Tutorial 1 - How to Make Websites with Python",
            "desc": "Creating your first Flask application, routing decorators, dynamic parameters, and running local servers.",
            "file": "multimedia/videos/flask_tutorial_1.mp4",
            "cat": cat_phase3,
            "views": 650,
        },
        {
            "step": 7,
            "title": "Roadmap Step 4B: Flask Tutorial 2 - HTML Templates & Jinja2",
            "desc": "Dynamic template rendering with Jinja2, expressions, loops, and conditional presentation logic.",
            "file": "multimedia/videos/flask_tutorial_2.mp4",
            "cat": cat_phase3,
            "views": 590,
        },
        {
            "step": 8,
            "title": "Roadmap Step 4C: Flask Tutorial 3 - Bootstrap Styling & Template Inheritance",
            "desc": "Inheriting base templates and styling responsive navigation bars with Bootstrap 5.",
            "file": "multimedia/videos/flask_tutorial_3.mp4",
            "cat": cat_phase3,
            "views": 540,
        },
        {
            "step": 9,
            "title": "Roadmap Step 4D: Flask Tutorial 4 - HTTP Methods (GET & POST) Form Data",
            "desc": "Safely capturing incoming user inputs, processing form submissions, and request handling.",
            "file": "multimedia/videos/flask_tutorial_4.mp4",
            "cat": cat_phase3,
            "views": 490,
        },
        {
            "step": 10,
            "title": "Roadmap Step 4E: Flask Tutorial 5 - User Sessions & State",
            "desc": "Managing user state across requests, signed cookies, and session-based authentication.",
            "file": "multimedia/videos/flask/flask_tutorial_5.mp4",
            "cat": cat_phase3,
            "views": 460,
        },
        {
            "step": 11,
            "title": "Roadmap Step 4F: Flask Tutorial 6 - Message Flashing & Alerts",
            "desc": "Displaying feedback and notification banners across redirect responses.",
            "file": "multimedia/videos/flask/flask_tutorial_6.mp4",
            "cat": cat_phase3,
            "views": 430,
        },
        {
            "step": 12,
            "title": "Roadmap Step 4G: Flask Tutorial 7 - Using SQLAlchemy Database",
            "desc": "Connecting Python backends to relational databases via ORM models, migrations, and automated record persistence.",
            "file": "multimedia/videos/flask_tutorial_7.mp4",
            "cat": cat_phase3,
            "views": 510,
        },
        {
            "step": 13,
            "title": "Roadmap Step 4H: Flask Tutorial 8 - Adding, Deleting & Updating Users",
            "desc": "Full database CRUD implementation with SQLAlchemy models and transactional commits.",
            "file": "multimedia/videos/flask/flask_tutorial_8.mp4",
            "cat": cat_phase3,
            "views": 475,
        },
        {
            "step": 14,
            "title": "Roadmap Step 4I: Flask Tutorial 9 - Static Files (CSS, JS, Media)",
            "desc": "Serving custom CSS, JavaScript, and user-uploaded media assets effectively.",
            "file": "multimedia/videos/flask/flask_tutorial_9.mp4",
            "cat": cat_phase3,
            "views": 420,
        },
        {
            "step": 15,
            "title": "Roadmap Step 4J: Flask Tutorial 10 - Blueprints & Modular Architecture",
            "desc": "Structuring large Python web apps using modular Blueprints across multiple packages.",
            "file": "multimedia/videos/flask/flask_tutorial_10.mp4",
            "cat": cat_phase3,
            "views": 530,
        },
        {
            "step": 16,
            "title": "Roadmap Step 4K: How to Deploy a Flask App to a Linux Server",
            "desc": "Production engineering: configuring Gunicorn WSGI, Nginx reverse proxy, and systemd services.",
            "file": "multimedia/videos/flask_deployment.mp4",
            "cat": cat_phase3,
            "views": 890,
        },
        # STEP 5: Qt Folder
        {
            "step": 17,
            "title": "Roadmap Step 5: Qt Crash Course for Beginners - Create Desktop GUI Apps",
            "desc": "Mastering desktop GUI programming: window widgets, layout managers, signal-slot event loops, and styling.",
            "file": "multimedia/videos/qt/qt_crash_course.mp4",
            "cat": cat_phase4,
            "views": 670,
        },
        # STEP 6: Kivy Standalone Course + Folder
        {
            "step": 18,
            "title": "Roadmap Step 6A: Kivy Full Course - Create Python Games & Mobile Apps",
            "desc": "Transitioning to mobile: touch handling, canvas graphics, kv design language, and responsive touch controls.",
            "file": "multimedia/videos/kivy/kivy_full_course.mp4",
            "cat": cat_phase5,
            "views": 830,
        },
        {
            "step": 19,
            "title": "Roadmap Step 6B: Kivy App Part 1 - Architecture & Setup",
            "desc": "Structuring a production-ready mobile application project with Kivy and KivyMD.",
            "file": "multimedia/videos/kivy_tutorial_1.mp4",
            "cat": cat_phase5,
            "views": 410,
        },
        {
            "step": 20,
            "title": "Roadmap Step 6C: Kivy App Part 2 - Map & Local Database",
            "desc": "Integrating SQLite and interactive map views inside Python mobile applications.",
            "file": "multimedia/videos/kivy_tutorial_2.mp4",
            "cat": cat_phase5,
            "views": 375,
        },
        {
            "step": 21,
            "title": "Roadmap Step 6D: Kivy App Part 3 - Markers & Dynamic Menus",
            "desc": "Rendering custom touch markers and popup navigation menus.",
            "file": "multimedia/videos/kivy/kivy_tutorial_3.mp4",
            "cat": cat_phase5,
            "views": 330,
        },
        {
            "step": 22,
            "title": "Roadmap Step 6E: Kivy App Part 4 - Search Menu & Geocoding",
            "desc": "Implementing search bars, geocoding coordinates, and real-time list filtering.",
            "file": "multimedia/videos/kivy/kivy_tutorial_4.mp4",
            "cat": cat_phase5,
            "views": 310,
        },
        {
            "step": 23,
            "title": "Roadmap Step 6F: Kivy App Part 6 - GPS Markers & Android Permissions",
            "desc": "Requesting Android runtime permissions and reading hardware GPS sensors directly from Python.",
            "file": "multimedia/videos/kivy/kivy_tutorial_6.mp4",
            "cat": cat_phase5,
            "views": 450,
        },
        # STEP 7: Bonus C++ Course
        {
            "step": 24,
            "title": "Roadmap Bonus (Optional): C++ Full Course for Free (Low-Level Systems)",
            "desc": "Wrap up your programming foundation: explore low-level memory pointers, static typing, and machine-level compilation to gain a deep appreciation of Python's high-level abstractions.",
            "file": "multimedia/videos/bonus/cpp_full_course.mp4",
            "cat": cat_bonus,
            "views": 1420,
        },
    ]

    for item in roadmap_items:
        m = MediaItem.objects.create(
            title=item["title"],
            description=item["desc"],
            media_type="video",
            category=item["cat"],
            media_file=item["file"],
            step_number=item["step"],
            views_count=item["views"],
        )
        print(f"  [Step {m.step_number}] {m.title}")

    # 3. Developer Cheat Sheets (Images)
    cheat_sheets = [
        {
            "title": "Cheat Sheet: Python 3 Core Syntax & Data Structures",
            "desc": "Quick visual reference covering primary data types, mutability (lists, tuples, dicts, sets), control flow, list comprehensions, lambda, and memory-efficient generators.",
            "file": "multimedia/images/python_basics_cheatsheet.svg",
            "cat": cat_cheatsheet,
            "views": 850,
        },
        {
            "title": "Cheat Sheet: Web Frameworks, SQL & Deployment Architecture",
            "desc": "Quick visual reference card comparing Flask microframework routes to Django MVT architecture, CRUD SQL operations, Gunicorn/Nginx setups, and Docker Compose configurations.",
            "file": "multimedia/images/web_backend_cheatsheet.svg",
            "cat": cat_cheatsheet,
            "views": 780,
        },
    ]

    for c in cheat_sheets:
        MediaItem.objects.create(
            title=c["title"],
            description=c["desc"],
            media_type="image",
            category=c["cat"],
            media_file=c["file"],
            step_number=0,
            views_count=c["views"],
        )
        print(f"  [Cheat Sheet] {c['title']}")

    # 4. Podcasts (Real Audio)
    podcasts = [
        {
            "title": "The Road to Python Podcast - Ep 1: The Modern Developer Roadmap",
            "desc": "Episode 1 breaks down the optimal learning roadmap: from syntax and SQL to building distributed backends and mobile apps.",
            "file": "multimedia/audio/podcast_ep1_roadmap.mp3",
            "cat": cat_podcasts,
            "views": 320,
        },
        {
            "title": "The Road to Python Podcast - Ep 2: Flask vs Django & Cloud Microservices",
            "desc": "Episode 2 compares minimalist microservices with batteries-included frameworks, exploring database connection pooling and containerized deployments.",
            "file": "multimedia/audio/podcast_ep2_backend.mp3",
            "cat": cat_podcasts,
            "views": 275,
        },
        {
            "title": "The Road to Python Podcast - Ep 3: Algorithmic Efficiency, Sorting & Generators",
            "desc": "Episode 3 delves into O(n log n) sorting, binary search, and the mechanics of Python's yield generator functions.",
            "file": "multimedia/audio/podcast_ep3_algorithms.mp3",
            "cat": cat_podcasts,
            "views": 250,
        },
    ]

    for p in podcasts:
        MediaItem.objects.create(
            title=p["title"],
            description=p["desc"],
            media_type="audio",
            category=p["cat"],
            media_file=p["file"],
            step_number=0,
            views_count=p["views"],
        )
        print(f"  [Podcast] {p['title']}")

    print(f"\nSeeding completed! Total MediaItems in database: {MediaItem.objects.count()}")


if __name__ == "__main__":
    seed()

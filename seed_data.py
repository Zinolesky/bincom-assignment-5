"""
Seed database with:
1. Python Learning Roadmap Videos (ordered progressively).
2. Developer Cheat Sheets (Images).
3. Python Mastery Podcast Audio Tracks (Real Audio).
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_project.settings')
django.setup()

from media_app.models import Category, MediaItem


def seed():
    print("Clearing and re-seeding structured multimedia dataset...")
    MediaItem.objects.all().delete()
    Category.objects.all().delete()

    # 1. Categories
    cat_roadmap, _ = Category.objects.get_or_create(
        name="Python Developer Roadmap",
        slug="python-developer-roadmap",
        description="Structured step-by-step video curriculum from fundamentals to full-stack deployment."
    )
    cat_cheatsheet, _ = Category.objects.get_or_create(
        name="Developer Cheat Sheets",
        slug="developer-cheat-sheets",
        description="Visual quick-reference cards for Python syntax, collections, and backend design."
    )
    cat_podcasts, _ = Category.objects.get_or_create(
        name="Tech Podcasts",
        slug="tech-podcasts",
        description="Audio episodes discussing system architecture, algorithms, and web frameworks."
    )

    # 2. Roadmap Videos (Ordered by learning milestones)
    roadmap_videos = [
        {
            "title": "Roadmap Step 1: SQL Fundamentals & Database Queries",
            "description": "Milestone 1: Learn how relational databases work, writing basic queries, table schema design, and data normalization.",
            "file": "multimedia/videos/sql_day_1.mp4",
            "category": cat_roadmap,
            "views": 520,
        },
        {
            "title": "Roadmap Step 2: Flask Web Basics & Routing",
            "description": "Milestone 2: Creating your first Python web server, handling HTTP GET/POST methods, routing, and dynamic URL parameters.",
            "file": "multimedia/videos/flask_tutorial_1.mp4",
            "category": cat_roadmap,
            "views": 485,
        },
        {
            "title": "Roadmap Step 3: Dynamic Jinja2 Templates",
            "description": "Milestone 3: Rendering server-side HTML templates with Jinja2, loop directives, conditional displays, and variable contexts.",
            "file": "multimedia/videos/flask_tutorial_2.mp4",
            "category": cat_roadmap,
            "views": 412,
        },
        {
            "title": "Roadmap Step 4: UI Design with Bootstrap & Template Inheritance",
            "description": "Milestone 4: Modernizing web pages with Bootstrap 5, base layout templates, responsive navigation bars, and reusable components.",
            "file": "multimedia/videos/flask_tutorial_3.mp4",
            "category": cat_roadmap,
            "views": 380,
        },
        {
            "title": "Roadmap Step 5: Form Processing & Request Data",
            "description": "Milestone 5: Managing incoming user input, handling form submissions safely, and processing URL parameters.",
            "file": "multimedia/videos/flask_tutorial_4.mp4",
            "category": cat_roadmap,
            "views": 345,
        },
        {
            "title": "Roadmap Step 6: ORM Integration with SQLAlchemy & Databases",
            "description": "Milestone 6: Connecting Python backends to relational databases via ORM models, migrations, and automated record persistence.",
            "file": "multimedia/videos/flask_tutorial_7.mp4",
            "category": cat_roadmap,
            "views": 390,
        },
        {
            "title": "Roadmap Step 7: Mobile App Engineering with Python & Kivy",
            "description": "Milestone 7: Expanding Python beyond web servers into native mobile applications with Kivy, UI components, and local databases.",
            "file": "multimedia/videos/kivy_tutorial_2.mp4",
            "category": cat_roadmap,
            "views": 270,
        },
        {
            "title": "Roadmap Step 8: Linux Server Deployment & Cloud Hosting",
            "description": "Milestone 8: Production operations—configuring WSGI servers (Gunicorn), Nginx reverse proxy, and deploying Python web apps on Linux servers.",
            "file": "multimedia/videos/flask_deployment.mp4",
            "category": cat_roadmap,
            "views": 610,
        },
    ]

    for v in roadmap_videos:
        item = MediaItem.objects.create(
            title=v["title"],
            description=v["description"],
            media_type="video",
            category=v["category"],
            media_file=v["file"],
            views_count=v["views"],
        )
        print(f"  [Video] {item.title}")

    # 3. Developer Cheat Sheets (Images)
    cheat_sheets = [
        {
            "title": "Python 3 Syntax & Data Structures Cheat Sheet",
            "description": "Comprehensive reference covering primary data types, mutability (lists, tuples, dicts, sets), control flow, list comprehensions, lambda, and memory-efficient generators.",
            "file": "multimedia/images/python_basics_cheatsheet.svg",
            "category": cat_cheatsheet,
            "views": 750,
        },
        {
            "title": "Web Frameworks & Database Architecture Cheat Sheet",
            "description": "Quick reference comparing Flask microframework routes to Django MVT architecture, CRUD SQL operations, Gunicorn/Nginx, and Docker Compose configurations.",
            "file": "multimedia/images/web_backend_cheatsheet.svg",
            "category": cat_cheatsheet,
            "views": 680,
        },
    ]

    for c in cheat_sheets:
        item = MediaItem.objects.create(
            title=c["title"],
            description=c["description"],
            media_type="image",
            category=c["category"],
            media_file=c["file"],
            views_count=c["views"],
        )
        print(f"  [Image] {item.title}")

    # 4. Podcasts (Real Audio)
    podcasts = [
        {
            "title": "Python Mastery Podcast - Ep 1: The Modern Python Developer Roadmap",
            "description": "Episode 1 breaks down the optimal learning curve for modern Python developers: from core syntax to building distributed backends and database systems.",
            "file": "multimedia/audio/podcast_ep1_roadmap.mp3",
            "category": cat_podcasts,
            "views": 240,
        },
        {
            "title": "Python Mastery Podcast - Ep 2: Flask vs Django & Cloud Microservices",
            "description": "Episode 2 compares minimalist microservices with batteries-included frameworks, exploring database connection pooling and containerized deployments.",
            "file": "multimedia/audio/podcast_ep2_backend.mp3",
            "category": cat_podcasts,
            "views": 195,
        },
        {
            "title": "Python Mastery Podcast - Ep 3: Algorithmic Efficiency, Sorting & Generators",
            "description": "Episode 3 delves into O(n log n) sorting, binary search, and the mechanics of Python's yield generator functions.",
            "file": "multimedia/audio/podcast_ep3_algorithms.mp3",
            "category": cat_podcasts,
            "views": 180,
        },
    ]

    for p in podcasts:
        item = MediaItem.objects.create(
            title=p["title"],
            description=p["description"],
            media_type="audio",
            category=p["category"],
            media_file=p["file"],
            views_count=p["views"],
        )
        print(f"  [Audio] {item.title}")

    print(f"\nAll assets seeded! Total MediaItems in database: {MediaItem.objects.count()}")


if __name__ == "__main__":
    seed()

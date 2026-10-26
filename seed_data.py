import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_project.settings')
django.setup()

from django.core.files.base import ContentFile
from media_app.models import Category, MediaItem


def seed():
    print("Seeding multimedia data with real Tech videos...")

    # 1. Categories
    cat_python, _ = Category.objects.get_or_create(name="Python & Web Frameworks", slug="python-web-frameworks")
    cat_mobile, _ = Category.objects.get_or_create(name="Mobile App Development", slug="mobile-app-development")
    cat_nature, _ = Category.objects.get_or_create(name="Design & Photography", slug="design-photography")
    cat_podcast, _ = Category.objects.get_or_create(name="Tech Podcasts", slug="tech-podcasts")

    # 2. Real Tech Videos from D:\Users\Videos\Tech
    tech_videos = [
        {
            "title": "Flask Tutorial 1 - How to Make Websites with Python",
            "description": "Learn how to build websites from scratch using Python and Flask, covering setup, routing, and basic view handlers.",
            "file_rel_path": "multimedia/videos/flask_tutorial_1.mp4",
            "category": cat_python,
            "views": 412,
        },
        {
            "title": "Flask Tutorial 2 - HTML Templates & Jinja2",
            "description": "Deep-dive into dynamic HTML rendering, Jinja2 template tags, and passing contextual variables from Flask views.",
            "file_rel_path": "multimedia/videos/flask_tutorial_2.mp4",
            "category": cat_python,
            "views": 289,
        },
        {
            "title": "Flask Tutorial 3 - Bootstrap Styling & Template Inheritance",
            "description": "Modernizing user interfaces by integrating Bootstrap 5, base layout templates, and modular block inheritance.",
            "file_rel_path": "multimedia/videos/flask_tutorial_3.mp4",
            "category": cat_python,
            "views": 340,
        },
        {
            "title": "Kivy Python Mobile Tutorial - Architecture & App Setup",
            "description": "Architecting native mobile applications using Python, Kivy, and KivyMD for Android and cross-platform targets.",
            "file_rel_path": "multimedia/videos/kivy_tutorial_1.mp4",
            "category": cat_mobile,
            "views": 195,
        },
    ]

    for vid in tech_videos:
        item, created = MediaItem.objects.update_or_create(
            title=vid["title"],
            defaults={
                "description": vid["description"],
                "media_type": "video",
                "category": vid["category"],
                "media_file": vid["file_rel_path"],
                "views_count": vid["views"],
            }
        )
        status = "Created" if created else "Updated"
        print(f"  [{status}] Video: {item.title}")

    # Remove the mock placeholder video if present
    MediaItem.objects.filter(title="Django Full-Stack Walkthrough 2026").delete()

    # 3. Seed Image (Sample SVG image rendered as file)
    sample_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
      <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#9333ea;stop-opacity:1" />
        </linearGradient>
      </defs>
      <rect width="800" height="600" fill="url(#grad)"/>
      <circle cx="400" cy="300" r="140" fill="rgba(255,255,255,0.15)" />
      <text x="50%" y="48%" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="34" font-weight="bold">Bincom Python Assessment 5</text>
      <text x="50%" y="56%" text-anchor="middle" fill="#e2e8f0" font-family="sans-serif" font-size="20">Django Multimedia Showcase Asset</text>
    </svg>"""

    item1, created1 = MediaItem.objects.get_or_create(
        title="Sunset Panorama in Lagos",
        defaults={
            "description": "High resolution scenic graphic capturing vibrant gradient sky transitions across Lagos skyline.",
            "media_type": "image",
            "category": cat_nature,
            "views_count": 42,
        }
    )
    if created1:
        item1.media_file.save("lagos_sunset.svg", ContentFile(sample_svg.encode('utf-8')))

    # 4. Seed Audio
    item2, created2 = MediaItem.objects.get_or_create(
        title="Python Backend & Cloud Architecture Podcast",
        defaults={
            "description": "Episode 12 discussing scalable asynchronous APIs, PostgreSQL pooling, and containerized deployment patterns.",
            "media_type": "audio",
            "category": cat_podcast,
            "views_count": 128,
        }
    )
    if created2:
        item2.media_file.save("podcast_ep12.mp3", ContentFile(b"//ID3SampleEmptyMP3TrackBytes//"))

    print(f"\nSeeding completed successfully! Total MediaItems in database: {MediaItem.objects.count()}")


if __name__ == "__main__":
    seed()

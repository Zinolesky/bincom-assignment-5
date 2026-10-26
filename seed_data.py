import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multimedia_project.settings')
django.setup()

from django.core.files.base import ContentFile
from media_app.models import Category, MediaItem

def seed():
    print("Seeding multimedia data...")
    # 1. Categories
    cat_nature, _ = Category.objects.get_or_create(name="Nature & Wildlife", slug="nature-wildlife")
    cat_podcast, _ = Category.objects.get_or_create(name="Tech Podcasts", slug="tech-podcasts")
    cat_demo, _ = Category.objects.get_or_create(name="Product Showcases", slug="product-showcases")

    # 2. Seed Image (Sample SVG image rendered as file)
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

    # 3. Seed Audio
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

    # 4. Seed Video
    item3, created3 = MediaItem.objects.get_or_create(
        title="Django Full-Stack Walkthrough 2026",
        defaults={
            "description": "Hands-on video guide to architecting modular media portals with automated validation and responsive streaming.",
            "media_type": "video",
            "category": cat_demo,
            "views_count": 315,
        }
    )
    if created3:
        item3.media_file.save("django_walkthrough.mp4", ContentFile(b"//MP4ContainerHeaderBytes//"))

    print(f"Seeding completed. Total MediaItems in database: {MediaItem.objects.count()}")

if __name__ == "__main__":
    seed()

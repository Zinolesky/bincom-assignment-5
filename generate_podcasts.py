"""
Generates real audio podcast MP3 files using gTTS.
"""
import os
from gtts import gTTS

AUDIO_DIR = "d:/Users/Bincom Training/bincom-assignment-5/media/multimedia/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

podcasts = [
    {
        "filename": "podcast_ep1_roadmap.mp3",
        "text": (
            "Welcome to the Python Mastery Podcast, Episode 1: The Modern Python Developer Roadmap. "
            "Whether you are just getting started or building enterprise cloud services, Python offers an intuitive syntax "
            "paired with unmatched versatility. In this episode, we explore the core phases: mastering data structures, "
            "delving into object oriented design, transitioning to web frameworks like Flask and Django, and writing scalable "
            "PostgreSQL queries. Stay tuned as we break down every milestone of your software engineering journey."
        )
    },
    {
        "filename": "podcast_ep2_backend.mp3",
        "text": (
            "Hello engineers, welcome back to Episode 2: Microframeworks versus Batteries-Included Backends. "
            "Today we compare Flask and Django. Flask provides pure simplicity and minimal boilerplate, perfect for microservices. "
            "On the other hand, Django gives you the Model-View-Template pattern, a robust Object Relational Mapper, and an automatic admin panel. "
            "We also cover connection pooling with psycopg2, and how Docker Compose streamlines full-stack deployment. Enjoy the episode!"
        )
    },
    {
        "filename": "podcast_ep3_algorithms.mp3",
        "text": (
            "Welcome to Episode 3: Conquering Algorithms and Time Complexity in Python. "
            "In this session, we dissect algorithmic efficiency: why O of N log N sorting algorithms like Merge Sort outperform "
            "naive quadratic sorts, and how binary search achieves O of log N lookup times. We also discuss memory-efficient Python generators "
            "using the yield keyword to handle large datasets effortlessly. Keep building, and keep learning!"
        )
    }
]

for p in podcasts:
    filepath = os.path.join(AUDIO_DIR, p["filename"])
    print(f"Generating {p['filename']}...")
    tts = gTTS(text=p["text"], lang="en", tld="com")
    tts.save(filepath)

print("All podcast audio files generated successfully!")

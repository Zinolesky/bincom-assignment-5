"""
Creates high quality Python & Tech Cheat Sheet SVG graphics.
"""
import os

CHEAT_SHEET_DIR = "d:/Users/Bincom Training/bincom-assignment-5/media/multimedia/images"
os.makedirs(CHEAT_SHEET_DIR, exist_ok=True)

# 1. Python Basics & Data Structures Cheat Sheet
python_basics_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="1000" height="700">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f172a;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1e293b;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="1000" height="700" fill="url(#bg)"/>
  
  <!-- Header -->
  <rect x="30" y="30" width="940" height="70" rx="10" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="50" y="75" fill="#38bdf8" font-family="'Courier New', monospace" font-size="28" font-weight="bold">🐍 Python 3 Core Syntax &amp; Data Structures Cheat Sheet</text>

  <!-- Box 1: Data Types -->
  <g transform="translate(30, 120)">
    <rect width="450" height="260" rx="8" fill="#1e293b" stroke="#475569"/>
    <text x="20" y="35" fill="#f59e0b" font-family="sans-serif" font-size="18" font-weight="bold">1. Primary Data Types</text>
    <text x="20" y="70" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">x = 42                 # Integer</text>
    <text x="20" y="95" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">pi = 3.14159           # Float</text>
    <text x="20" y="120" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">name = "Bincom"        # String (str)</text>
    <text x="20" y="145" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">is_active = True       # Boolean</text>
    <text x="20" y="170" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">empty_val = None       # NoneType</text>
    <text x="20" y="205" fill="#38bdf8" font-family="'Courier New', monospace" font-size="13"># Type casting: int("10"), str(25), float(5)</text>
    <text x="20" y="230" fill="#38bdf8" font-family="'Courier New', monospace" font-size="13"># Formatting: f"Hello, {name}! Value: {x}"</text>
  </g>

  <!-- Box 2: Collections -->
  <g transform="translate(520, 120)">
    <rect width="450" height="260" rx="8" fill="#1e293b" stroke="#475569"/>
    <text x="20" y="35" fill="#10b981" font-family="sans-serif" font-size="18" font-weight="bold">2. Collections &amp; Mutability</text>
    <text x="20" y="70" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">nums = [1, 2, 3]       # List (Mutable, Ordered)</text>
    <text x="20" y="95" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">point = (10, 20)       # Tuple (Immutable, Ordered)</text>
    <text x="20" y="120" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">tags = {"py", "web"}   # Set (Unique, Unordered)</text>
    <text x="20" y="145" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14">user = {"id": 1}       # Dict (Key-Value, Fast O(1))</text>
    <text x="20" y="180" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">nums.append(4)         # Add to end</text>
    <text x="20" y="205" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">nums[1:3]              # Slicing: [2, 3]</text>
    <text x="20" y="230" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">user.get("role", "dev")# Safe key lookup</text>
  </g>

  <!-- Box 3: Control Flow & Comprehensions -->
  <g transform="translate(30, 410)">
    <rect width="450" height="260" rx="8" fill="#1e293b" stroke="#475569"/>
    <text x="20" y="35" fill="#ec4899" font-family="sans-serif" font-size="18" font-weight="bold">3. Control Flow &amp; Comprehensions</text>
    <text x="20" y="70" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14"># If / Elif / Else</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">if score &gt;= 90: grade = "A"</text>
    <text x="20" y="120" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">elif score &gt;= 80: grade = "B"</text>
    <text x="20" y="145" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">else: grade = "C"</text>
    <text x="20" y="185" fill="#94a3b8" font-family="'Courier New', monospace" font-size="14"># List Comprehension</text>
    <text x="20" y="210" fill="#a78bfa" font-family="'Courier New', monospace" font-size="13">evens = [x for x in range(10) if x % 2 == 0]</text>
    <text x="20" y="235" fill="#a78bfa" font-family="'Courier New', monospace" font-size="13">squared = {x: x**2 for x in nums}</text>
  </g>

  <!-- Box 4: Functions & Generators -->
  <g transform="translate(520, 410)">
    <rect width="450" height="260" rx="8" fill="#1e293b" stroke="#475569"/>
    <text x="20" y="35" fill="#818cf8" font-family="sans-serif" font-size="18" font-weight="bold">4. Functions, Lambda &amp; Generators</text>
    <text x="20" y="70" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">def greet(name: str = "World") -&gt; str:</text>
    <text x="40" y="95" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">return f"Hello {name}"</text>
    <text x="20" y="130" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13"># Lambda function</text>
    <text x="20" y="155" fill="#38bdf8" font-family="'Courier New', monospace" font-size="13">square = lambda x: x * x</text>
    <text x="20" y="190" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13"># Generator with yield (Memory O(1))</text>
    <text x="20" y="215" fill="#10b981" font-family="'Courier New', monospace" font-size="13">def count(): yield 1; yield 2</text>
    <text x="20" y="240" fill="#a78bfa" font-family="'Courier New', monospace" font-size="13">gen = count(); next(gen) # yields 1</text>
  </g>
</svg>"""

with open(f"{CHEAT_SHEET_DIR}/python_basics_cheatsheet.svg", "w", encoding="utf-8") as f:
    f.write(python_basics_svg)

# 2. Flask & Django Backend Architecture Cheat Sheet
backend_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="1000" height="700">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#022c22;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="1000" height="700" fill="url(#bg2)"/>
  
  <rect x="30" y="30" width="940" height="70" rx="10" fill="#059669" fill-opacity="0.2" stroke="#10b981" stroke-width="1.5"/>
  <text x="50" y="75" fill="#34d399" font-family="'Courier New', monospace" font-size="28" font-weight="bold">🌐 Python Web Frameworks: Flask vs Django Cheat Sheet</text>

  <!-- Box 1: Flask Minimal Pattern -->
  <g transform="translate(30, 120)">
    <rect width="450" height="260" rx="8" fill="#132a22" stroke="#047857"/>
    <text x="20" y="35" fill="#34d399" font-family="sans-serif" font-size="18" font-weight="bold">1. Flask Microframework</text>
    <text x="20" y="70" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">from flask import Flask, render_template, request</text>
    <text x="20" y="95" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">app = Flask(__name__)</text>
    <text x="20" y="130" fill="#6ee7b7" font-family="'Courier New', monospace" font-size="13">@app.route('/api/items', methods=['GET', 'POST'])</text>
    <text x="20" y="155" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">def get_items():</text>
    <text x="40" y="180" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">if request.method == 'POST':</text>
    <text x="60" y="205" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">data = request.json</text>
    <text x="40" y="230" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">return {"status": "success"}, 200</text>
  </g>

  <!-- Box 2: Django MVT Pattern -->
  <g transform="translate(520, 120)">
    <rect width="450" height="260" rx="8" fill="#132a22" stroke="#047857"/>
    <text x="20" y="35" fill="#60a5fa" font-family="sans-serif" font-size="18" font-weight="bold">2. Django MVT Structure</text>
    <text x="20" y="70" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">• Model: models.Model (Database ORM schema)</text>
    <text x="20" y="95" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">• View: Business logic &amp; query handling</text>
    <text x="20" y="120" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">• Template: Dynamic HTML presentation layer</text>
    <text x="20" y="160" fill="#93c5fd" font-family="'Courier New', monospace" font-size="13"># Common Commands:</text>
    <text x="20" y="185" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">python manage.py makemigrations</text>
    <text x="20" y="210" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">python manage.py migrate</text>
    <text x="20" y="235" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">python manage.py runserver</text>
  </g>

  <!-- Box 3: Database & ORM -->
  <g transform="translate(30, 410)">
    <rect width="450" height="260" rx="8" fill="#132a22" stroke="#047857"/>
    <text x="20" y="35" fill="#facc15" font-family="sans-serif" font-size="18" font-weight="bold">3. Database &amp; SQL Querying</text>
    <text x="20" y="70" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13"># SQL Operations (CRUD)</text>
    <text x="20" y="95" fill="#fde047" font-family="'Courier New', monospace" font-size="13">CREATE TABLE students (id SERIAL PRIMARY KEY);</text>
    <text x="20" y="120" fill="#fde047" font-family="'Courier New', monospace" font-size="13">INSERT INTO students (name) VALUES ('Zino');</text>
    <text x="20" y="145" fill="#fde047" font-family="'Courier New', monospace" font-size="13">SELECT * FROM students WHERE score &gt; 80;</text>
    <text x="20" y="170" fill="#fde047" font-family="'Courier New', monospace" font-size="13">UPDATE students SET score=95 WHERE id=1;</text>
    <text x="20" y="195" fill="#fde047" font-family="'Courier New', monospace" font-size="13">DELETE FROM students WHERE id=1;</text>
    <text x="20" y="230" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13"># Parameterized queries prevent SQL Injection</text>
  </g>

  <!-- Box 4: Production Deployment -->
  <g transform="translate(520, 410)">
    <rect width="450" height="260" rx="8" fill="#132a22" stroke="#047857"/>
    <text x="20" y="35" fill="#c084fc" font-family="sans-serif" font-size="18" font-weight="bold">4. Production &amp; Containerization</text>
    <text x="20" y="70" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">WSGI / ASGI Servers: Gunicorn, Uvicorn</text>
    <text x="20" y="100" fill="#cbd5e1" font-family="'Courier New', monospace" font-size="13">Reverse Proxy: Nginx (SSL, Static Caching)</text>
    <text x="20" y="130" fill="#a855f7" font-family="'Courier New', monospace" font-size="13"># Docker Compose Multi-Container Workflow</text>
    <text x="20" y="160" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">services:</text>
    <text x="40" y="185" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">db:  image: postgres:16-alpine</text>
    <text x="40" y="210" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">web: build: .</text>
    <text x="40" y="235" fill="#94a3b8" font-family="'Courier New', monospace" font-size="13">     ports: ["8000:8000"]</text>
  </g>
</svg>"""

with open(f"{CHEAT_SHEET_DIR}/web_backend_cheatsheet.svg", "w", encoding="utf-8") as f:
    f.write(backend_svg)

print("Cheat sheets generated successfully!")

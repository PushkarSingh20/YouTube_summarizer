┌───────────────────────────────────────────────┐  
# 🎬 YouTube Summarizer with Gemini AI  

- paste a youtube link → get a neat summary.  
- built to save your time, cuz videos are long.  
- not a phd paper, just Flask + Gemini + transcripts.  
- not a “hello world” project, this one actually works (sometimes).  
- inspired by laziness & too many long tutorials.  

└───────────────────────────────────────────────┘  

---

## ⚙️ tech stack  
- [![Python](https://skillicons.dev/icons?i=python)](https://www.python.org/) → python (backbone of this thing)  
- [![Flask](https://skillicons.dev/icons?i=flask)](https://flask.palletsprojects.com/) → flask (lightweight backend, still does the job)  
- [![HTML](https://skillicons.dev/icons?i=html)]() [![CSS](https://skillicons.dev/icons?i=css)]() [![JS](https://skillicons.dev/icons?i=js)]() → the frontend trio (basic but enough)  
- [![Google](https://skillicons.dev/icons?i=googlecloud)](https://ai.google/) → gemini-pro (brain behind summaries)  
- [![YouTube](https://skillicons.dev/icons?i=youtube)](https://github.com/jdepoix/youtube-transcript-api) → youtube-transcript-api (grabs video subtitles, when available)  


---

## 🧩 how it works  
- u paste a youtube url  
- backend extracts video id (regex magic 🪄)  
- tries to pull transcript (if youtube allows it, else cry 😭)  
- feeds transcript into Gemini → gets a summary back  
- spits out a 250 words “too long didn’t watch” version  

---

## 😮‍💨 logs (dev pain points)  
- transcripts don’t exist for all videos → instant 💀 error  
- Gemini sometimes acts like a poet instead of summarizer  
- spent hours debugging only to realize → wrong folder path  
- .env quotes issue wasted half a day (yup, never put quotes there)  
- overall: fun project, 50% coding, 50% swearing at errors  

---

## 🐛 known bugs  
- “Transcript not available” → still breaks vibe  
- if YouTube changes their API tomorrow → rip project  
- not production ready, just localhost hero  
- error handling is… let’s say “optimistic”  

---

## 🚀 setup (run at ur own risk)  

### 1️⃣ clone repo  
```bash
git clone https://github.com/YOUR_USERNAME/youtube-summarizer.git
cd youtube-summarizer

### 2️⃣ create venv
python -m venv venv

### 3️⃣ activate venv 
# windows
venv\Scripts\activate  

### 4️⃣ install deps
pip install -r requirements.txt


### 5️⃣ add API key 
GOOGLE_API_KEY=your_api_key_here


### 6️⃣ run it
python yt_summarizer.py

## why this shit?  
- youtube videos are too damn long
- chatgpt can summarize but → copying transcripts is pain
- so yeah, flask + gemini + transcripts = problem kinda solved 

## LICENSE📜
fork it, star it, deploy it, even break it.
But give me some money, I'm a broke programmer 🥲😭

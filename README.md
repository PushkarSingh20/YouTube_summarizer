# 🎬 YouTube Summarizer with Gemini AI  

AI-powered web app that generates concise summaries of YouTube videos using **Flask**, **Google Gemini**, and the **YouTube Transcript API**.  

---

## ✨ Features
- 🎯 **Summarize any YouTube video** into key points (under 250 words)  
- ⚡ **Fast & simple UI** built with HTML, CSS, and JavaScript  
- 🤖 Powered by **Google Gemini Pro** for natural language understanding  
- 🔒 Uses `.env` for secure API key management  
- 🌍 Cross-platform — run locally with Python & Flask  

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)  
- **Frontend**: HTML, CSS, JavaScript  
- **AI Model**: Google Gemini Pro  
- **Transcript API**: youtube-transcript-api (fallback planned for YouTube Data API)  

---

## 🚀 Setup & Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/YOUR_USERNAME/youtube-summarizer.git
cd youtube-summarizer

### 2️⃣ Create a virtual environment 
```bash
python -m venv venv


### 3️⃣ Activate the environment
```bash
venv\Scripts\activate


### 4️⃣ Install dependencies  
```bash
pip install -r requirements.txt


### 5️⃣ Add your API Key 
```bash
GOOGLE_API_KEY=your_api_key_here

### 6️⃣ Run the app 
```bash
python yt_summarizer.py

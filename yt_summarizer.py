from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import re
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here: """

def extract_video_id(youtube_url):
    """Extract video ID from various YouTube URL formats"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\n?#]+)',
        r'youtube\.com\/watch\?.*v=([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)
    
    return None

def extract_transcript_details(youtube_video_url):
    """Extract transcript from YouTube video"""
    try:
        video_id = extract_video_id(youtube_video_url)
        if not video_id:
            raise Exception("Invalid YouTube URL")
        
        # Try to fetch transcript in English, fallback to auto
        try:
            transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        except NoTranscriptFound:
            # fallback: fetch any available transcript
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript = transcript_list.find_transcript(transcript_list._langs)
            transcript_text = transcript.fetch()
        
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript, video_id
    except TranscriptsDisabled:
        raise Exception("Transcripts are disabled for this video")
    except NoTranscriptFound:
        raise Exception("No transcript available in requested languages")
    except Exception as e:
        raise Exception(f"Transcript error: {str(e)}")


def generate_gemini_content(transcript_text, prompt):
    """Generate summary using Gemini AI"""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        raise e

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/summarize', methods=['POST'])
def summarize_video():
    """API endpoint to summarize YouTube video"""
    try:
        data = request.get_json()
        video_url = data.get('url')
        print("DEBUG: Got video_url =", video_url)  

        if not video_url:
            return jsonify({'error': 'No URL provided'}), 400
        
        # Extract transcript
        transcript, video_id = extract_transcript_details(video_url)
        print("DEBUG: Transcript length =", len(transcript.split()))  
        
        if not transcript:
            return jsonify({'error': 'Transcript not available for this video'}), 400
        
        # Generate summary
        summary = generate_gemini_content(transcript, prompt)
        print("DEBUG: Gemini summary preview =", summary[:200]) 
        
        if not summary or summary.startswith("❌"):
            return jsonify({'error': summary}), 500
        
        return jsonify({
            'success': True,
            'video_id': video_id,
            'summary': summary,
            'transcript_length': len(transcript.split())
        })
    
    except Exception as e:
        print("DEBUG: Exception in summarize_video:", str(e))  
        return jsonify({'error': f"Server error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
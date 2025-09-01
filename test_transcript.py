from youtube_transcript_api import YouTubeTranscriptApi

video_id = "5MgBikgcWnY"  # TED talk

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    print("Transcript fetched! First lines:")
    for line in transcript[:5]:
        print(line)
except Exception as e:
    print("Transcript error:", e)

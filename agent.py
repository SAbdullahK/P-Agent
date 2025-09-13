import os
import time
import streamlit as st
from google.genai import Client
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from dataclasses import dataclass

# Load .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("❌ Google API key not found in .env file.")
    st.stop()

client = Client(api_key=GOOGLE_API_KEY)

@dataclass
class Post:
    platform: str
    content: str


def get_transcript(video_id: str):
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)
        transcript_text = " ".join(
            snippet["text"] if isinstance(snippet, dict) else snippet.text
            for snippet in fetched_transcript
        )
        return transcript_text
    
    except Exception as e:
        return f"❌Failed to fetch transcript : {str(e)}"


def generate_content(video_transcript: str, social_media_platform: str, user_query: str, retries=3, delay=5) -> Post:
    for attempt in range(1, retries + 1):
        try:
            prompt = (
                f"Here is a user query: {user_query}\n\n"
                f"Here is the YouTube video transcript: {video_transcript}\n\n"
                f"Generate a social media post for {social_media_platform}."
            )

            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=[prompt],
            )

            return Post(platform=social_media_platform, content=response.text.strip())
        except Exception as e:
            if attempt == retries:
                return Post(platform=social_media_platform, content=f"❌ Failed after {retries} attempts: {str(e)}")
            time.sleep(delay)


def run_agent(video_id: str, platform: str, user_query: str) -> Post:
    transcript = get_transcript(video_id)
    if transcript.startswith("❌"):
        return Post(platform=platform, content=transcript)
    return generate_content(transcript, platform, user_query)


# ----------------- STREAMLIT APP -----------------
st.set_page_config(page_title="🎯 Social Media Post Generator", layout="centered")

st.title("🎯 Social Media Post Generator")
st.write("Generate posts for LinkedIn, Instagram, Facebook, or Twitter(X) from a YouTube video.")

with st.form("input_form"):
    video_id = st.text_input("Enter YouTube Video ID", placeholder="e.g., VJgdOMXhEj0")
    platform = st.selectbox("Choose Platform", ["LinkedIn", "Instagram", "Facebook", "Twitter(X)"])
    user_query = st.text_area("Enter your query", placeholder="Generate a LinkedIn post about this video")

    submitted = st.form_submit_button("🚀 Generate Post")

if submitted:
    if not video_id or not user_query:
        st.warning("⚠️ Please enter both a video ID and query.")
    else:
        with st.spinner("⏳ Generating your post..."):
            result = run_agent(video_id, platform, user_query)

        if result.content.startswith("❌"):
            st.error(result.content)
        else:
            st.success(f"✅ Generated Post for {platform}")
            st.write(result.content)
            st.download_button("💾 Download Post", result.content, file_name=f"{platform}_post.txt")

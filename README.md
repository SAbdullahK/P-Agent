# 🎥 Social Media Post Generator

This project is an **AI-powered social media assistant** that takes a YouTube video, extracts its transcript, and generates a **ready-to-post caption** for platforms like **LinkedIn, Instagram, Facebook, and Twitter(X)** using **Google Gemini**.

Built with:

* 🐍 Python
* 🌐 Streamlit (for the web UI)
* 🤖 Google Gemini API
* 🎬 YouTube Transcript API

---

## ✨ Features

* 🔍 Fetch YouTube transcripts automatically by **video ID**.
* 📝 Generate platform-specific posts (LinkedIn, Instagram, Facebook, Twitter).
* 🔄 Retry mechanism for stable AI responses.
* 🌙 Simple, clean **Streamlit web interface**.

---

## ⚙️ Installation

1. Clone this repo:

```bash
git clone https://github.com/your-username/social-media-post-generator.git
cd social-media-post-generator
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # on Linux/Mac
.venv\Scripts\activate      # on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your **Google API key** in a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### CLI Mode

Run the script directly:

```bash
python agent.py
```

### Web App Mode

Launch the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📦 Requirements

* Python 3.10+
* Streamlit
* google-genai
* python-dotenv
* youtube-transcript-api

---

## 🚀 Future Improvements

* Embed YouTube video player in Streamlit UI.
* Add support for TikTok/Threads captions.
* Option to generate multiple variations of the post.

---

## 📝 License

MIT License – feel free to use and improve this project!

---

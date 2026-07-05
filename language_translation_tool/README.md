# 🌐 Language Translation Tool

**CodeAlpha Artificial Intelligence Internship — Task 1**

A simple, clean web app that lets a user type text, pick a source and target
language, and instantly get a translated result — with an optional
text-to-speech playback of the translation.

## ✨ Features
- Text input box for the source text
- Dropdowns to select source language (or auto-detect) and target language
- Uses Google Translate (via the free `deep-translator` library) for translation
- One-click copy of the translated text (via the built-in copy icon on the result box)
- Optional 🔊 text-to-speech playback of the translated text (via `gTTS`)

## 🛠️ Tech Stack
- Python
- [Streamlit](https://streamlit.io/) — for the user interface
- [deep-translator](https://github.com/nidhaloff/deep-translator) — translation API wrapper
- [gTTS](https://github.com/pndurang/gTTS) — Google Text-to-Speech

## ▶️ How to Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/<your-username>/codealpha_tasks.git
   cd codealpha_tasks/language_translation_tool
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Your browser will open automatically at `http://localhost:8501` — start translating!

## 📸 Demo Flow
1. Type or paste text into the input box.
2. Select source language (or leave as "Auto Detect").
3. Select the target language.
4. Click **Translate 🔁**.
5. View the translated text, copy it, or click the 🔊 expander to hear it spoken aloud.

## 📂 Project Structure
```
language_translation_tool/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🙋 Author
Built as part of the CodeAlpha Artificial Intelligence Internship (June Batch).

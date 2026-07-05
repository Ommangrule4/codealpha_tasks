"""
CodeAlpha - Artificial Intelligence Internship
Task 1: Language Translation Tool

A simple web-based translation tool built with Streamlit.
- Enter text
- Choose source & target language
- Get translated text instantly
- Optional: listen to the translation (text-to-speech)

Run locally with:
    streamlit run app.py
"""

import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io

# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------
st.set_page_config(page_title="AI Language Translator", page_icon="🌐", layout="centered")

st.title("🌐 AI Language Translation Tool")
st.caption("CodeAlpha Artificial Intelligence Internship — Task 1")

# ---------------------------------------------------------
# Language list (supported by Google Translate via deep-translator)
# ---------------------------------------------------------
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
# LANGUAGES = {"english": "en", "hindi": "hi", ...}

# Build a nice display list: "English (en)"
lang_display = [f"{name.title()} ({code})" for name, code in LANGUAGES.items()]
code_from_display = {f"{name.title()} ({code})": code for name, code in LANGUAGES.items()}

col1, col2 = st.columns(2)

with col1:
    source_display = st.selectbox(
        "Source language",
        options=["Auto Detect"] + lang_display,
        index=0,
    )

with col2:
    # default target = English
    default_target_index = lang_display.index("English (en)") + 1 if "English (en)" in lang_display else 0
    target_display = st.selectbox(
        "Target language",
        options=lang_display,
        index=lang_display.index("English (en)") if "English (en)" in lang_display else 0,
    )

source_lang = "auto" if source_display == "Auto Detect" else code_from_display[source_display]
target_lang = code_from_display[target_display]

# ---------------------------------------------------------
# Text input
# ---------------------------------------------------------
input_text = st.text_area("Enter text to translate", height=150, placeholder="Type or paste text here...")

translate_clicked = st.button("Translate 🔁", type="primary", use_container_width=True)

# ---------------------------------------------------------
# Translation logic
# ---------------------------------------------------------
if translate_clicked:
    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            with st.spinner("Translating..."):
                translated = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)

            st.subheader("Translated Text")
            # st.code gives the user a built-in copy icon in the top-right corner
            st.code(translated, language=None)

            # ---------------------------------------------------------
            # Optional: Text-to-Speech
            # ---------------------------------------------------------
            with st.expander("🔊 Listen to translation (Text-to-Speech)"):
                try:
                    tts = gTTS(text=translated, lang=target_lang)
                    audio_bytes = io.BytesIO()
                    tts.write_to_fp(audio_bytes)
                    audio_bytes.seek(0)
                    st.audio(audio_bytes, format="audio/mp3")
                except Exception as tts_error:
                    st.info(
                        "Text-to-speech isn't available for this language, "
                        f"or an error occurred: {tts_error}"
                    )

        except Exception as e:
            st.error(f"Something went wrong while translating: {e}")

st.divider()
st.caption("Built with Streamlit + deep-translator + gTTS · CodeAlpha AI Internship")

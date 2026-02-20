import streamlit as st
from faster_whisper import WhisperModel
import tempfile
import os
import json
import streamlit.components.v1 as components

# Set page config
st.set_page_config(
    page_title="Writers Whisper",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a cleaner, high-end look
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp {
            background-color: #00000;
            color: #333333;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        h1 {
            font-weight: 300;
            color: #fffff;
            margin-bottom: 0.5rem;
        }
        div[data-testid="stAudioInput"] {
             margin-top: 2rem;
             margin-bottom: 2rem;
        }
        .stCode {
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.title("Writers Whisper")
st.markdown("### Simplicity for your thoughts.")

# Load Model
@st.cache_resource
def load_model():
    # Run on CPU with INT8
    model_size = "base"
    return WhisperModel(model_size, device="cpu", compute_type="int8")

with st.spinner("Loading AI Model..."):
    try:
        model = load_model()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

# Audio Input
audio_value = st.audio_input("Record your voice")

if audio_value:
    with st.spinner("Transcribing..."):
        try:
            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio_value.getvalue())
                tmp_file_path = tmp_file.name

            # Transcribe
            segments, info = model.transcribe(tmp_file_path, beam_size=5)

            # Collect text
            transcribed_text = ""
            for segment in segments:
                transcribed_text += segment.text + " "

            transcribed_text = transcribed_text.strip()

            # Display
            st.success("Transcription Complete")

            st.text_area(
                label="Transcription",
                value=transcribed_text,
                height=400
            )

            components.html(f"""
            <div id="transcription-text" style="display:none;">{transcribed_text}</div>
            <button onclick="copyToClipboard()" style="margin-top:10px; padding:8px 16px; border-radius:8px; border:none; background-color:#2c3e50; color:white; cursor:pointer;">Copy to Clipboard</button>
            <script>
            function copyToClipboard() {{
                const text = document.getElementById('transcription-text').innerText;
                navigator.clipboard.writeText(text).then(function() {{
                    console.log('Copy successful');
                }}, function(err) {{
                    console.error('Could not copy text: ', err);
                }});
            }}
            </script>
            """, height=50)

        except Exception as e:
            st.error(f"An error occurred during transcription: {e}")
        finally:
            # Cleanup
            if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)
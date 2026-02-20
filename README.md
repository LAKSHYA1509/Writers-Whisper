# Writers Whisper ✍️

**Simplicity for your thoughts.**

Writers Whisper is a minimal Streamlit app that converts your voice into text using OpenAI’s Whisper model (via `faster-whisper`). Record your thoughts and get instant transcription in a clean, distraction-free interface.

---

## Features

* 🎙️ Record audio directly in the browser
* ⚡ Fast transcription using `faster-whisper`
* 🧠 Runs locally on CPU (INT8 optimized)
* 📋 Copy-to-clipboard support
* 🎨 Minimal, elegant UI

---

## Tech Stack

* [Streamlit](https://streamlit.io/)
* [faster-whisper](https://github.com/guillaumekln/faster-whisper)
* Python 3.9+

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/writers-whisper.git
cd writers-whisper
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install streamlit faster-whisper
```

---

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal.

---

## How It Works

* Loads the **Whisper base model**
* Runs on **CPU with INT8 quantization**
* Temporarily saves recorded audio
* Transcribes using beam search
* Displays formatted text in a resizable text area

---

## Model Details

* Model size: `base`
* Device: `cpu`
* Compute type: `int8`

You can change the model size inside the app:

```python
model_size = "base"  # try: tiny, small, medium
```

---

## Notes

* First run may take time (model download).
* Works fully offline after model is downloaded.
* Performance depends on CPU speed.

---

## Future Ideas

* Multiple language support
* Auto punctuation toggle
* Export as Markdown
* Dark mode

---

## License

MIT License

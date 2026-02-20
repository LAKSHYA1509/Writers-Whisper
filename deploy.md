# Writers Whisper Deployment Guide

This guide describes how to deploy the Writers Whisper application.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Local Deployment

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd writers-whisper
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

5.  **Access the app:**
    Open your browser and navigate to `http://localhost:8501`.

## Deploying to Streamlit Community Cloud

Streamlit Community Cloud is the easiest way to deploy Streamlit apps for free.

1.  **Push your code to GitHub:**
    Ensure your project is in a public GitHub repository.

2.  **Sign up/Login to Streamlit Cloud:**
    Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.

3.  **Deploy the app:**
    - Click "New app".
    - Select your repository, branch (e.g., `main`), and the main file path (`app.py`).
    - Click "Deploy!".

4.  **Wait for build:**
    Streamlit Cloud will install the dependencies from `requirements.txt` and start your app. This might take a few minutes initially as it downloads the Whisper model.

## Note on Performance

This application uses the `base` model of `faster-whisper` running on CPU.
- **First Run:** The model will be downloaded automatically on the first run, which may take some time.
- **Transcription Speed:** Transcription speed depends on the CPU power. The `int8` quantization is used to speed up inference on CPUs.

## Troubleshooting

- **Audio Input:** Ensure your browser has permission to access your microphone.
- **Dependencies:** If you encounter errors related to libraries, ensure all dependencies in `requirements.txt` are installed.
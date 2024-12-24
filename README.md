
# Text2Talk 
## Text-to-Speech App

A simple and interactive web application that converts text to speech in over 85 languages, with multiple accent and playback speed options. This app uses **Google Text-to-Speech (gTTS)** and **Pydub** for audio manipulation.

The app is deployed on **Streamlit Cloud**. You can try it out here:

[Text2Talk](https://text2talk.streamlit.app/)

## Features

- Convert text to speech in **85+ languages**.
- Select from various **voice accents** (e.g., US, UK, Australian, Indian).
- **Adjust playback speed** for the generated speech.
- **Download the generated audio** in MP3 format.

## Tech Stack

- **Backend**: Python 3.x
- **Libraries**:
  - `streamlit`: for creating the web app interface
  - `gTTS`: Google Text-to-Speech for converting text to speech
  - `pydub`: for manipulating and adjusting the audio (playback speed, etc.)
- **Deployment**: Streamlit Cloud


> Replace the above link with the actual URL of your deployed app on Streamlit Cloud.

## Setup

### Prerequisites

Make sure you have Python 3.x installed. You will also need `pip` to install dependencies.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/weirdo-147/Text2Talk.git
   cd Text2Talk
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv tts
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     tts\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source tts/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the App Locally**:
   ```bash
   streamlit run tts_app.py
   ```

### Requirements

The following libraries are required for this app to run:

- `streamlit`
- `gTTS`
- `pydub`

### Dependencies Installation

You can install them with the following:

```bash
pip install streamlit gTTS pydub
```

### Optional: FFmpeg for Pydub

If you're using `pydub`, you might need **FFmpeg** to handle audio file conversion. [Install FFmpeg](https://www.ffmpeg.org/download.html) and add it to your system's PATH.

## Deployment

This app is deployed on **Streamlit Cloud**. 

## Usage

1. **Enter Text**: Type any text you want to convert into speech in the text area.
2. **Select Language**: Choose the language of the text from the dropdown (over 85 languages available).
3. **Select Voice**: Choose the accent or voice type.
4. **Playback Speed**: Adjust the speed of the speech with the slider.
5. **Convert and Listen**: Click **Convert to Speech** to generate and play the speech.
6. **Download Audio**: Click the download button to save the speech as an MP3 file.

## Contributing

Feel free to fork this repository, create a branch, and submit pull requests for bug fixes, features, or improvements. Please ensure all tests pass before submitting changes.

### Steps for Contribution:
1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch for your changes.
4. Commit your changes with a meaningful message.
5. Push your changes and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# 🤖 LiveKit AI Voice Assistant – Internship Task

This project implements a **real-time AI voice assistant** using [LiveKit Agents](https://docs.livekit.io/agents/), combining **STT**, **LLM**, and **TTS** in a seamless pipeline. The assistant supports multilingual speech, logs performance metrics, handles conversation interruptions, and responds with natural-sounding speech.

---

## 🚀 Features

- 🎙️ Real-time **Speech-to-Text (STT)** via Deepgram
- 🧠 **LLM inference** via Groq using `llama3-8b-8192`
- 🗣️ High-quality **Text-to-Speech (TTS)** using Cartesia
- 🌐 Multilingual voice input support
- 🔁 **Turn detection** and robust VAD
- 🔇 Noise cancellation with LiveKit BVC
- 📊 **Metric logging**: EOU delay, TTFT, TTFB, Total Latency
- 📄 Exports call performance logs to Excel
- ✅ Supports live & local run modes
- ☁️ LiveKit Cloud support for real-time streaming

---

## 📁 Project Structure

```
AI-VOICE-AGENT/
├── src/
│ ├── agent.py # Main assistant logic
│ ├── metrics.py # Excel logging for performance metrics
│ └── pycache/
├── .env # API keys and credentials
├── .gitignore
├── metrics.xlxs # contains log details
├── requirements.txt # Project dependencies

```

---

## ⚙️ Requirements

- Python 3.10+
- Virtual environment (`venv` recommended)
- [LiveKit SDK for Python](https://docs.livekit.io)
- API Keys:
  - Deepgram (STT)
  - Groq (LLM)
  - ElevenLabs or Cartesia (TTS)
  - LiveKit Cloud (RTC + Agent)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
  - git clone https://github.com/yourusername/ai-voice-assistant.git
  - cd ai-voice-assistant
```

### 2. Setup Virtual Environment
```
 - python -m venv venv

  # On Unix/macOS
  - source venv/bin/activate

  # On Windows
  -venv\Scripts\activate

```

### 3. Install Dependencies

```
  - pip install "livekit-agents[deepgram,groq,elevenlabs,openai ,cartesia,silero,turn-detector]~=1.0" "livekit-plugins-noise-cancellation~=0.2" python-dotenv openpyxl

```

### 4. Then Run this

```
  # To save current installed packages to a file:
  - pip freeze > requirements.txt

```

### 4. Configure .env
Create a .env file in the root directory with your credentials:

```
  - LIVEKIT_URL=wss://your-project.livekit.cloud
  - LIVEKIT_API_KEY=your_livekit_api_key
  - LIVEKIT_API_SECRET=your_livekit_api_secret

  - DEEPGRAM_API_KEY=your_deepgram_api_key
  - CARTESIA_API_KEY=your_cartesia_api_key
  - GROQ_API_KEY=your_groq_api_key
  - ELEVENLABS_API_KEY=your_elevenlabs_api_key

```

## ▶️ Run the Assistant
### 🖥️ Run Locally (Console Mode)

```
  # This runs the assistant locally for development or testing purposes using console mode.
  - python src/agent.py console

```

### ☁️ Run on LiveKit Cloud (Playground)

```
  # This runs the assistant on LiveKit Cloud using the LiveKit Agents Playground.
  - python src/agent.py dev


```

--> ⚠️ Note: Ensure your .env file is configured correctly with valid API keys and URLs before launching.

---

## 📊 Metrics Logging
- The metrics.py file collects and logs important real-time performance statistics:

- EOU Delay – Time taken to detect the end of the user's utterance.

- TTFT (Time To First Token) – Time taken by the LLM to generate the first token.

- TTFB (Time To First Byte) – Time taken by the TTS engine to begin audio output.

- Total Latency – Combined system response time from input to voice reply.

📝 Metrics are saved as Excel sheets in the local directory for later evaluation.

--- 
## 🧪 Example Prompt

The assistant automatically greets the user on joining:
```
  --> "Hello! How can I assist you today?"
```

---
## 🙌 Acknowledgements
  - LiveKit
  - Groq
  - Deepgram
  - Cartesia
  - ElevenLabs



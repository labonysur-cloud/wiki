# Wiki AI Project Folder Structure

wiki/
│── app.py                  # Main loop: wake word → STT → Brain → Tools → TTS
│── requirements.txt        # All Python dependencies
│── config.yaml             # Personality, wake prompts, TTS voice, timer defaults
│── README.md               # Instructions, usage guide
│
├── core/                   # Core engine (voice, brain, tools)
│   ├── init.py
│   ├── wakeword.py         # Detect “Hey Wiki” offline
│   ├── stt.py              # Speech-to-text (Faster-Whisper tiny/small)
│   ├── tts.py              # Text-to-speech (Edge-TTS / Piper)
│   ├── brain.py            # LLM brain (offline mini LLM)
│   ├── tools.py            # Timers, app automation, web search
│   ├── memory.py           # Local memory (SQLite or JSON)
│   └── utils.py            # Helper functions (logging, audio processing)
│
├── skills/                 # Extendable feature modules
│   ├── init.py
│   ├── cooking.py          # Pasta, egg, rice, curry timers
│   ├── study.py            # Study / Pomodoro timers
│   ├── media.py            # Music / video control
│   └── documents.py        # PDF summarizer, OCR (optional)
│
├── ui/                     # GUI / Tray interface (optional)
│   ├── init.py
│   ├── tray.py             # Windows tray app (PySide6)
│   └── overlay.py          # Popup for live transcript & response
│
├── data/                   # Persistent storage
│   ├── memory.db           # SQLite memory database
│   ├── logs/               # Debug logs
│   └── audio/              # Temporary audio files (mic input / TTS output)
│
└── tests/                  # Unit tests
    ├── test_timers.py
    ├── test_stt.py
    ├── test_tools.py
    └── test_brain.py



# Wiki AI Project

## Project Overview
Wiki is an offline, CPU-friendly AI assistant for Windows with timers, memory, and voice commands.

## Daily Progress

### Day 1
- Created all files and folder structure.
- Set up MySQL database with tables: memory, timers, preferences, logs.
- Connected backend Python code to MySQL.
- Ran all SQL scripts successfully in MySQL Workbench.
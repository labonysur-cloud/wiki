# Wiki — Desktop Voice Assistant

Wiki is a desktop voice assistant built in Python, focused on reliable local execution and practical daily productivity workflows. The project is designed to run on Windows and combines wake-word detection, speech recognition, natural-language response generation, text-to-speech, automation tools, and persistent memory.

## Repository

- **Name:** `labonysur-cloud/wiki`
- **Description:** Wiki is a desktop voice assistant.
- **Primary Goal:** Provide a personal, extensible assistant that can run with low latency and minimal cloud dependency.

## Core Capabilities

- Wake-word activation ("Hey Wiki")
- Speech-to-text (offline-friendly transcription pipeline)
- Text-to-speech response generation
- Assistant reasoning/response layer (LLM-powered brain module)
- Timer and productivity task orchestration
- Local memory for conversation and preferences
- Optional desktop UI/tray integration

## Technical Architecture

The project follows a modular structure so each capability can be developed and tested independently.

### Entry and Runtime

- `app.py`: Main application runtime and event loop.
- `config.yaml`: Runtime configuration for assistant behavior, prompts, voices, timers, and feature toggles.

### Core Layer (`core/`)

- `wakeword.py`: Wake-word detection pipeline.
- `stt.py`: Speech-to-text handling and transcription integration.
- `tts.py`: Text-to-speech generation pipeline.
- `brain.py`: Response and decision layer for conversational logic.
- `tools.py`: System tools (timers, helper actions, command execution pathways).
- `memory.py`: Persistence adapter for storing user context and assistant memory.
- `utils.py`: Shared helper utilities (logging, parsing, audio helpers).

### Skill Layer (`skills/`)

Task-oriented modules for specialized domains:

- `cooking.py`
- `study.py`
- `media.py`
- `documents.py`

### UI Layer (`ui/`)

Optional user interface components:

- `tray.py`: Tray-based desktop interaction surface.
- `overlay.py`: Overlay for live assistant feedback/transcript interaction.

### Data and Persistence (`data/`)

- `memory.db`: Local persistent memory store.
- `logs/`: Runtime and debug logs.
- `audio/`: Temporary audio artifacts for recording and playback pipelines.

### Tests (`tests/`)

- `test_timers.py`
- `test_stt.py`
- `test_tools.py`
- `test_brain.py`

## Suggested Runtime Flow

1. Application starts through `app.py`.
2. Wake-word listener waits for activation phrase.
3. User speech is captured and transcribed in `core/stt.py`.
4. Intent/response generation is handled in `core/brain.py`.
5. If required, actions are delegated through `core/tools.py` or skill modules.
6. Response text is synthesized by `core/tts.py` and played to the user.
7. Key context is stored through `core/memory.py` into local persistence.

## Installation

### Prerequisites

- Python 3.10+
- Windows environment (primary target)
- Audio input/output devices configured correctly

### Setup

```bash
git clone https://github.com/labonysur-cloud/wiki.git
cd wiki
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Assistant

```bash
python app.py
```

## Configuration

Use `config.yaml` to control runtime behavior, including:

- Wake-word and activation parameters
- STT/TTS model or provider settings
- Voice profile and response style
- Default timer/task behavior
- Logging verbosity and debug flags

## Testing

Run tests with:

```bash
pytest -q
```

## Engineering Priorities

This repository is structured for:

- **Modularity:** Clear boundaries between core engine, skills, UI, and storage.
- **Extensibility:** New skills can be added with minimal core coupling.
- **Local-first reliability:** Persistent memory and local execution paths where possible.
- **Maintainability:** Dedicated test modules for critical assistant subsystems.

## Current Development Notes

- The repository currently includes foundational components for wake-word, voice interaction, memory, tools, and domain skills.
- Desktop assistant behavior is centered on productivity and personal workflow support.
- The architecture supports iterative upgrades to STT/TTS backends and intelligence layers without breaking overall flow.

## Contributing

Contributions are welcome. For changes affecting architecture or feature behavior, include:

- A clear problem statement
- Implementation notes
- Test coverage updates

## License

No license is currently defined in this repository. Add a license file before production or public distribution.
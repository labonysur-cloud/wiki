# Wiki — Desktop Voice Assistant

Wiki is a Python-based desktop voice assistant for Windows. It is currently implemented as a modular assistant runtime with wake-word activation, speech pipeline hooks, command/response intelligence powered by CSV datasets, and built-in desktop automation tools.

This README reflects the current repository implementation on the `master` branch.

## Repository Information

- **Repository:** `labonysur-cloud/wiki`
- **Description:** Wiki is a desktop voice assistant.
- **Default Branch:** `master`

## Current Implementation Status

The codebase is in an active foundational stage.

Implemented and populated modules currently include:

- `app.py` — main assistant runtime loop
- `core/brain.py` — command matching and response engine
- `core/tools.py` — timers, app launching, and website opening
- `core/db.py` — MySQL connection helper

Several planned modules and tests exist as placeholders (empty files) and are ready for incremental implementation.

## Technical Stack (Based on Real Code)

### Language and Runtime

- **Python 3.x**

### Libraries Used in Current Code

From implemented files:

- `pandas` (dataset ingestion and table operations)
- `numpy` (similarity score array operations)
- `mysql-connector-python` via `mysql.connector` (database connectivity)
- Python standard library: `time`, `threading`, `subprocess`, `webbrowser`, `re`, `os`

> Note: The repository currently uses `requirements.text` (empty) instead of `requirements.txt`. Dependency pinning is not yet defined in the repo.

## Project Structure

```text
wiki/
├── app.py
├── config.yaml
├── requirements.text
├── README.md
├── core/
│   ├── __init__.py
│   ├── brain.py
│   ├── db.py
│   ├── memory.py
│   ├── stt.py
│   ├── tools.py
│   ├── tts.py
│   ├── utils.py
│   └── wakeword.py
├── skills/
│   ├── __init__.py
│   ├── cooking.py
│   ├── documents.py
│   ├── media.py
│   └── study.py
├── ui/
│   ├── __init__.py
│   ├── overlay.py
│   └── tray.py
├── data/
└── tests/
    ├── test_brain.py
    ├── test_stt.py
    ├── test_timers.py
    └── test_tools.py
```

## Runtime Architecture

### 1) Application Orchestration (`app.py`)

The assistant loop follows this flow:

1. Initialize `Brain` with dataset paths:
   - `datasets/commands.csv`
   - `datasets/cooking.csv`
   - `datasets/study.csv`
2. Wait for wake-word detection via `core.wakeword.detect_wakeword()`.
3. Capture transcribed user input via `core.stt.listen()`.
4. Route request to `Brain.respond()`.
5. Speak output through `core.tts.speak()`.
6. Continue loop with a CPU-friendly sleep interval.

### 2) Command Intelligence (`core/brain.py`)

`Brain` currently provides:

- Multi-CSV dataset loading and merge using `pandas.concat`
- Required schema validation (`command`, `response` columns)
- Optional command `category` handling
- Keyword-overlap similarity scoring
- Best-match selection with threshold-based fallback response
- Tool routing when matched category is `tools`
- Dynamic command insertion through `add_command(...)`

#### Matching Strategy

Similarity is computed using token overlap:

- Convert both input and command to lowercase token sets
- Score = overlap size / max(command token count, 1)
- Select highest score (`numpy.argmax`)
- If score < `0.1`, return fallback response

### 3) Tool Execution Layer (`core/tools.py`)

Current tool features:

- **Timers:** named timers using background threads
- **App launchers:** configured for Windows `calc.exe` and `notepad.exe`
- **Website openers:** auto-prefixes non-HTTP input with `https://www.`

### 4) Data Connectivity (`core/db.py`)

`create_connection()` connects to local MySQL:

- Host: `localhost`
- Database: `wiki_db`
- Connector: `mysql.connector`

This module establishes the base for persistent storage and structured assistant state.

## Existing Integration Points (Declared, Not Yet Implemented)

The following imports/interfaces are already wired in runtime but module implementations are currently placeholders:

- `core.stt.listen`
- `core.tts.speak`
- `core.wakeword.detect_wakeword`
- `core.memory.Memory`

This means the architecture is already defined for full voice interaction; implementation can be completed module-by-module without changing high-level app flow.

## Setup Instructions (Current State)

### Prerequisites

- Python 3.10+
- Windows (for current app-launch integrations)
- MySQL server (if using `core/db.py`)

### Environment Setup

```bash
git clone https://github.com/labonysur-cloud/wiki.git
cd wiki
python -m venv .venv
.venv\Scripts\activate
pip install pandas numpy mysql-connector-python
```

> Because `requirements.text` is currently empty, dependencies are listed manually above.

## Run

```bash
python app.py
```

## Important Implementation Notes

- `config.yaml` currently exists but is empty.
- `data/` directory exists for persistent assets/storage.
- `tests/` files are present as scaffolding but currently empty.
- Dataset CSVs referenced by `app.py` must exist under a `datasets/` directory for runtime execution.

## Recommended Next Engineering Steps

1. Implement `core/stt.py`, `core/tts.py`, and `core/wakeword.py` concrete pipelines.
2. Implement `core/memory.py` and integrate it with MySQL or SQLite persistence.
3. Add `requirements.txt` with pinned versions.
4. Create and validate dataset files under `datasets/`.
5. Populate tests for `Brain`, tool routing, and end-to-end loop behavior.
6. Move sensitive DB credentials to environment variables.

## Security and Configuration Guidance

The current `core/db.py` includes hardcoded connection credentials. For production-grade practice:

- Store credentials in environment variables.
- Load config from `.env` or secure secret manager.
- Never commit real passwords to source control.

## License

No license file is currently present in the repository. Add one before public distribution or external contributions.

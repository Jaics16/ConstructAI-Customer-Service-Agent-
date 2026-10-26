# ConstructAI — Construction Customer-Service Agent (Local AI Edition)

A Gradio chat application for a construction company in Kerala, India. It demonstrates an AI agent that calls tools backed by a SQLite database. This assignment-ready version uses a local model through Ollama, so it does **not** require OpenAI API credits or an OpenAI API key.

> **Demo data warning:** This project contains fictional company information and rates. Replace them with verified, company-approved data before real-world use. The estimate tool does not calculate GST.

## Features

- Gradio chat interface and conversation history.
- SQLite database rebuilt from the supplied CSV files at startup.
- Four agent tools: `get_company_info`, `get_service_record`, `calculate_construction_estimate`, and `transfer_to_human`.
- Bounded agent loop (`MAX_STEPS`) and unknown-tool refusal.
- Visible tool trace for assignment demonstration and evaluation.
- Local model inference through Ollama's OpenAI-compatible API.
- No OpenAI API key, subscription, or API credits required. Internet is needed to download Ollama and the model; chat inference runs locally afterward.

## Requirements

- Windows 10/11
- Python 3.10 or newer
- Ollama for Windows
- Several GB of free disk space for the model

## Setup in Windows / VS Code

### 1. Install Ollama

Download and install Ollama from: https://ollama.com/download/windows

Open a **new** VS Code terminal and verify it is installed:

```powershell
ollama --version
```

### 2. Download the local model

```powershell
ollama pull qwen2.5:3b
```

Test the model (type `/bye` to exit):

```powershell
ollama run qwen2.5:3b
```

Qwen 2.5 3B is a small starting point. Tool selection quality can vary by hardware/model; test all assignment scenarios and document results.

### 3. Create and activate a Python virtual environment

Open this project folder in VS Code, then run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 4. Configure the project

Copy `.env.example` to `.env` in the same folder as `app.py`. The default configuration is ready for a local Ollama server; no API key should be added. The relevant settings are:

```env
MODEL=qwen2.5:3b
OLLAMA_BASE_URL=http://localhost:11434/v1
COMPANY_NAME=Kerala BuildCare (Demo)
COMPANY_LOCATION=Kerala, India
```

Keep `.env` private and do not commit it to GitHub.

### 5. Start the application

Make sure Ollama is running and the model is downloaded. In the activated VS Code terminal, run:

```powershell
python -m py_compile app.py
python app.py
```

Open the local Gradio URL printed in the terminal (usually http://127.0.0.1:7860).

## Database files

The application rebuilds `constructai.db` from these files every time it starts:

- `data/shop_info.csv` — company FAQ topics and content.
- `data/services.csv` — service names, categories, units, rates, availability, and descriptions.

The generated `.db` file is local and should not be uploaded to GitHub.

## Tools

| Tool | Purpose | Example question |
|---|---|---|
| `get_company_info(topic)` | FAQ lookup | “What are your working hours?” |
| `get_service_record(name)` | Service/rate lookup | “Tell me about site assessment.” |
| `calculate_construction_estimate(items)` | Calculates using Python and SQLite rates | “Calculate two Basic Design Consultation visits.” |
| `transfer_to_human(customer_question, reason)` | Stores a handover record in SQLite | “I want to speak to a person.” |

The estimate tool performs arithmetic in Python; the model is not trusted to calculate prices. Tax is deliberately not calculated. Handover records are stored locally; this demo does not send email or notify staff.

## Assignment testing checklist

Test the following and record whether the expected tool was called in the visible trace:

1. “What are your working hours?” — expect `get_company_info`.
2. “Tell me about the site assessment service.” — expect `get_service_record`.
3. “Calculate two Basic Design Consultation visits.” — expect `calculate_construction_estimate`.
4. “What is my project's current progress?” — may require `transfer_to_human` because live tracking is not in the demo database.
5. “I want to complain and speak to someone.” — expect `transfer_to_human`.
6. “Write a poem about space.” — expect a polite out-of-scope response without an unrelated tool call.

For a tool-choice evaluation, prepare at least 10 questions, record expected tools, observed tools, correctness, and any errors. Local models can be less reliable at structured tool calling than larger hosted models, so include those limitations in the assignment report.

## Troubleshooting

- **`ollama` is not recognized:** restart the terminal after installing Ollama, or verify the installation.
- **Connection refused at `localhost:11434`:** open/start the Ollama app and retry.
- **Model not found:** run `ollama pull qwen2.5:3b`.
- **Slow responses or memory errors:** use a smaller model if available and supported, or close other applications.
- **No tool calls / wrong tool calls:** test with clear prompts, inspect the visible trace, and record limitations. Tool-call behavior varies across model versions.

## Security and production notes

- This is an educational prototype, not a production customer-support system.
- Demo facts and rates must be replaced with verified information.
- Add authentication, rate limiting, data retention controls, privacy protections, backups, and staff handover workflows before public deployment.
- Never expose internal prompts or database data beyond the intended scope.

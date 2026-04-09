
# NEXUS-PULSE
### Autonomous Multi-Agent Intelligence Pipeline

> **Powered by uv (Astral) · LangGraph · Groq · Streamlit**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nexus-pulse.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Table of Contents
- [Overview](#overview)
- [Live Links](#live-links)
- [Key Features](#key-features)
- [Agent Architecture](#agent-architecture)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Development Phases](#development-phases)
- [Live Demo](#live-demo)
- [Join Our Telegram](#join-our-telegram)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**NEXUS-PULSE** is an autonomous, multi-agent intelligence pipeline engineered to ingest, verify, synthesize, and disseminate actionable intelligence with zero manual intervention—unless you choose to intercept.

Built for speed, security, and scalability, NEXUS-PULSE leverages:
- Tavily API for real-time web reconnaissance
- Groq-powered LLMs (`llama-3.3-70b-versatile` & `llama-3.1-8b-instant`) for high-throughput reasoning
- ChromaDB for local, persistent vector memory
- LangGraph for stateful, conditional multi-agent orchestration
- Human-in-the-loop checkpoints for critical approval gates
- Telegram Bot API for instant intelligence delivery
- Streamlit Dashboard for remote command & control

> **Use Case**: Ideal for automated research briefings, threat intelligence aggregation, market analysis pipelines, or portfolio demonstration of agentic AI engineering.

---

## Live Links

**Application**: https://nexus-pulse.streamlit.app/

**Telegram Channel**: https://t.me/NexusPulseNews

---

## Key Features

| Feature | Description |
|---------|-------------|
| Multi-Agent Personas | Four specialized LLM nodes: Triage, Authentication, Synthesis, Formatting |
| Stateful Orchestration | LangGraph-powered cyclic state machine with conditional routing |
| Semantic Memory | Local ChromaDB vector store with HuggingFace embeddings for context retrieval |
| Human-in-the-Loop | Pause execution at critical checkpoints for manual approval/denial |
| Telegram Dissemination | Auto-deliver finalized briefs to your Telegram channel via bot |
| Streamlit Command UI | Visual dashboard to trigger pipelines, monitor state, and authorize releases |
| uv-Powered Workflow | Blazing-fast dependency resolution and virtual environment management |
| Security-First Design | `.env` isolation, `.gitignore` hygiene, and credential-free codebase |

---

## Agent Architecture

```
┌─────────────────────────────────────────┐
│            INPUT: Search Topic           │
└────────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│  TRIAGE NODE (llama-3.1-8b-instant)     │
│  • Filters irrelevant/noisy data         │
│  • Extracts core intelligence signals    │
└────────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│ AUTH NODE (llama-3.3-70b-versatile)     │
│  • Cross-references against vector DB   │
│  • Sets verification_status boolean      │
└────────────────────────────────────────┘
                 ▼
        ┌────────────────
        │ verification?  │
        └───────┬────────┘
       false    │    true
          ▼     ▼
   ┌─────────┐  ┌─────────────────────────┐
   │ TERMINATE│  │ SYNTHESIS NODE          │
   │  Node   │  │ (llama-3.3-70b-versatile)│
   └─────────  │ • Rewrites & compresses │
                │ • Maintains factual integrity│
                └────────┬────────────────
                         ▼
─────────────────────────────────────────┐
│ FORMATTING NODE (llama-3.1-8b-instant)  │
│ • Enforces rigid output structure        │
│ • Prepares payload for dissemination     │
└────────────────┬────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│ HUMAN CHECKPOINT (Optional Pause)       │
│ • Review draft in Streamlit UI          │
│ • Approve/Reject before transmission    │
└────────────────────────────────────────┘
                 ▼
┌─────────────────────────────────────────┐
│ TELEGRAM DELIVERY NODE                  │
│ • Secure HTTP POST to Telegram Bot API  │
│ • Logs to nexus_ops.log                 │
└─────────────────────────────────────────┘
```

---

## Tech Stack

| Category | Technologies |
|----------|-------------|
| Runtime | Python 3.10+, uv (Astral) |
| Orchestration | LangGraph, LangChain Core |
| LLM Inference | Groq API (`llama-3.3-70b-versatile`, `llama-3.1-8b-instant`) |
| Search & Retrieval | Tavily API, HuggingFace Embeddings |
| Vector Memory | ChromaDB (Local SQLite) |
| Frontend | Streamlit, Streamlit Community Cloud |
| Messaging | Telegram Bot API |
| DevOps | Git, GitHub, Windows PowerShell, VS Code |
| Logging | Python `logging` module → `nexus_ops.log` |

---

## Quick Start

### Prerequisites
- Windows 11 (PowerShell as Administrator)
- uv installed
- Git configured with SSH/HTTPS access to GitHub
- API Keys: Tavily, Groq, Telegram Bot

### 1. Clone & Initialize
```powershell
# Navigate to projects directory
cd C:\Projects\Nexus Pulse
mkdir nexus && cd nexus

# Initialize uv project + virtual environment
uv init
uv venv
.venv\Scripts\activate

# Launch VS Code with environment inherited
code .
```

### 2. Install Dependencies
```powershell
# Add core dependencies via uv (resolves in milliseconds)
uv add langgraph langchain-core streamlit chromadb \
       tavily-python python-telegram-bot \
       groq sentence-transformers python-dotenv
```

### 3. Configure Environment
```powershell
# Create .env file at project root (NEVER commit this)
notepad .env
```

Paste your credentials:
```env
TAVILY_API_KEY=your_tavily_key_here
GROQ_API_KEY=your_groq_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=@NexusPulseNews
```

### 4. Run Locally
```powershell
# Launch the Streamlit command dashboard
uv run streamlit run app.py
```
→ Opens at `http://localhost:8501`

### 5. Deploy to Streamlit Cloud
1. Push code to GitHub: `git push origin main`
2. Visit Streamlit Community Cloud
3. Connect your `Nexus-Pulse` repository
4. Add the 4 environment secrets in the dashboard
5. Deploy → Live at: **https://nexus-pulse.streamlit.app/**

---

## Configuration

### Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `TAVILY_API_KEY` | Tavily search API authentication | Yes |
| `GROQ_API_KEY` | Groq LLM inference access | Yes |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Father token | Yes |
| `TELEGRAM_CHAT_ID` | Target channel/user ID (e.g., `@NexusPulseNews`) | Yes |

### Model Configuration
```python
# src/agents/nodes.py - Model assignments
FAST_MODEL = "llama-3.1-8b-instant"      # Triage + Formatting nodes
HEAVY_MODEL = "llama-3.3-70b-versatile"  # Authentication + Synthesis nodes
```

### Local Storage Paths
```
nexus/
├── local_db/          # ChromaDB persistent vector store (git-ignored)
├── nexus_ops.log      # Execution telemetry & transmission logs
├── .checkpoints/      # LangGraph state snapshots for HITL
└── .env               # Secrets (NEVER commit)
```

---

## Project Structure

```
nexus/
│
├── app.py                     # Streamlit command dashboard (entry point)
├── pyproject.toml            # uv dependency manifest
├── uv.lock                   # Locked dependency versions
├── .gitignore                # Security exclusions
├── .env.example              # Credential template
│
├── src/
│   ├── state.py              # Typed state schema for graph payload
│   ├── graph_engine.py       # LangGraph orchestration + checkpointer
│   │
│   ├── reconnaissance/
│   │   └── search.py         # Tavily API integration + text parsing
│   │
│   ├── memory/
│   │   ├── vector_store.py   # ChromaDB + HuggingFace embeddings
│   │   └── ingest.py         # Chunking + embedding pipeline
│   │
│   ├── agents/
│   │   └── nodes.py          # 4 LLM personas + system prompts
│   │
│   └── delivery/
│       └── transmission.py   # Telegram Bot API HTTP client
│
├── tests/                    # Local validation scripts
│   ├── test_env.py
│   ├── test_memory.py
│   ├── test_agents.py
│   └── test_graph.py
│
└── nexus_ops.log             # Runtime telemetry (auto-generated)
```

---

## Development Phases

| Version | Tag | Scope | Commit Convention |
|---------|-----|-------|------------------|
| v0.1 | `v0.1-command-center` | Workspace init, uv setup, remote sync | `chore: initialize windows workspace...` |
| v0.2 | `v0.2-intel-acquisition` | Tavily + ChromaDB ingestion pipeline | `feat(data): configure search tools...` |
| v0.3 | `v0.3-cognitive-nodes` | LLM persona definitions + Groq binding | `feat(agents): define llm intelligence...` |
| v0.4 | `v0.4-state-routing` | LangGraph state machine + conditional edges | `feat(graph): orchestrate state machine...` |
| v0.5 | `v0.5-manual-override` | Human-in-the-loop checkpoint integration | `feat(auth): integrate human-in-the-loop...` |
| v0.6 | `v0.6-dissemination` | Telegram delivery + telemetry logging | `feat(delivery): integrate telegram...` |
| v1.0 | `v1.0-nexus-live` | Streamlit UI + Cloud deployment | `feat(ui): deploy autonomous command...` |

> Best Practice: Do not proceed to the next phase until all checklist items in the current phase are verified.

---

## Live Demo

### Command Dashboard
**https://nexus-pulse.streamlit.app/**

**Features**:
- Input target research topics
- Real-time visualization of agent state transitions
- Manual approval interface for HITL checkpoint
- One-click authorization for Telegram dissemination
- Live log streaming from `nexus_ops.log`

> Tip: For portfolio reviewers—trigger a demo run with topic "AI regulation updates Q4 2024" to showcase end-to-end pipeline execution.

---

## Join Our Telegram

Stay updated with intelligence briefs, project announcements, and community discussions:

### Channel Invite: https://t.me/NexusPulseNews

> The bot `@NexusPulseBot` auto-posts finalized briefs. Enable notifications to receive real-time intelligence.

---

## Contributing

Contributions are welcome! Please follow this workflow:

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit using Conventional Commits: `git commit -m "feat(scope): description"`
4. Push and open a Pull Request
5. Ensure all tests pass via `uv run pytest tests/`

### Local Development Tips
```powershell
# Activate environment
.venv\Scripts\activate

# Run tests
uv run pytest tests/ -v

# Format code
uv run ruff check src/ --fix
uv run black src/

# Monitor logs in real-time
Get-Content nexus_ops.log -Wait
```

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

```
MIT License

Copyright (c) 2024 Dhiraj

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---



```

# 🚀 NEXUS PULSE

<div align="center">

![Nexus Pulse Logo](https://img.shields.io/badge/NEXUS-PULSE-blue?style=for-the-badge&logo=rocket)
![Version](https://img.shields.io/badge/version-1.0.0-green?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.10+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-orange?style=for-the-badge)

### **Autonomous Multi-Agent Intelligence & Decision Engine**

[![Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Streamlit-red?style=for-the-badge&logo=streamlit)](https://nexus-pulse.streamlit.app/)
[![Telegram](https://img.shields.io/badge/📢_Telegram-Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/NexusPulseNews)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/dhiraj-malwade-6a8385399/)

**Autonomous • Stateful • Verifiable • Production-Grade • Human-Governed**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Architecture](#-architecture)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [System Capabilities](#-system-capabilities)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Development Phases](#-development-phases)
- [API Reference](#-api-reference)
- [Security](#-security)
- [Performance](#-performance)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact & Links](#-contact--links)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Overview

**NEXUS PULSE** is a cutting-edge, production-ready autonomous intelligence pipeline that orchestrates multiple AI agents to collect, verify, synthesize, and disseminate intelligence with human-in-the-loop governance. Built with modern Python tooling and enterprise-grade architecture, it represents the next generation of automated decision-support systems.

### Core Principles
- ✅ **Autonomous Operation** - Multi-agent orchestration with minimal human intervention
- ✅ **Stateful Processing** - Persistent state management with checkpoint recovery
- ✅ **Verifiable Intelligence** - Cross-referenced, authenticated data validation
- ✅ **Production-Grade** - Enterprise-ready with comprehensive logging and monitoring
- ✅ **Human-Governed** - Critical decision points require human authorization

---

## 🌐 Live Demo

Experience NEXUS PULSE in action:

🔗 **[Launch Live Demo](https://nexus-pulse.streamlit.app/)**

The live deployment showcases the full autonomous pipeline with real-time intelligence processing, human authorization checkpoints, and seamless Telegram delivery.

---

## 🏗 Architecture

<img width="1536" height="1024" alt="Nexus Pulse Architectural Diagram" src="https://github.com/user-attachments/assets/cb5265fd-dd13-4671-84cc-890c9c54ea24" />


*Figure 1: Complete NEXUS PULSE System Architecture - 7-Phase Autonomous Pipeline*


### Architecture Highlights

The system follows a sophisticated 7-phase pipeline architecture:

1. **Command Center** - Environment initialization and secure workspace provisioning
2. **Intel Acquisition** - Autonomous web reconnaissance and vector storage
3. **Cognitive Nodes** - Multi-agent LLM system with specialized personas
4. **State Routing** - LangGraph-based autonomous state machine with conditional logic
5. **Human Authorization** - Manual override checkpoints for governance
6. **Delivery & Interface** - Telegram dissemination and Streamlit dashboard
7. **Deployment & Operations** - Cloud deployment with operational telemetry

---

## ✨ Key Features

### 🤖 Autonomous Intelligence Processing
- **Multi-Agent Orchestration** - Four specialized AI nodes (Triage, Authentication, Synthesis, Formatting)
- **Conditional Routing** - Intelligent decision trees with automatic fail-safes
- **State Persistence** - SQLite-based checkpointing for crash recovery
- **Human-in-the-Loop** - Mandatory approval gates before external dissemination

### 🔍 Advanced Data Acquisition
- **Tavily Search Integration** - Real-time web intelligence gathering
- **Semantic Vector Search** - ChromaDB-powered local knowledge base
- **HuggingFace Embeddings** - State-of-the-art text vectorization
- **Sanitized Payloads** - Automatic content parsing and cleaning

### 🛡 Enterprise-Grade Security
- **Isolated Virtual Environment** - uv (Astral) for blazing-fast dependency management
- **Credential Isolation** - `.env`-based secret management with Git ignore
- **Local-Only Execution** - Sensitive data never leaves your infrastructure
- **Audit-Ready Logging** - Comprehensive `nexus_ops.log` with thread tracking

### 📊 Production Observability
- **Real-Time Status Dashboard** - Streamlit-based command interface
- **Execution Telemetry** - Timestamp, thread ID, and success code tracking
- **Visual State Progression** - Live node-by-node execution visualization
- **Error Recovery** - Automatic state restoration from checkpoints

---

## 💻 Technology Stack

### Core Framework
- **Python 3.10+** - Modern Python with type hints and async support
- **uv (Astral)** - Next-generation Python package manager (10-100x faster than pip)
- **LangGraph** - Cyclic graph orchestration for multi-agent workflows
- **LangChain Core** - LLM abstraction and tool integration

### AI & Machine Learning
- **Groq API** - High-speed LLM inference (Llama 3, Mixtral)
- **HuggingFace Transformers** - Embedding generation
- **ChromaDB** - Local vector database with SQLite backend

### Infrastructure
- **Windows PowerShell** - Native Windows development environment
- **Visual Studio Code** - IDE with Python extension
- **Git + GitHub** - Version control with semantic tagging
- **Streamlit Community Cloud** - Zero-config cloud deployment

### External Services
- **Tavily Search API** - AI-optimized web search
- **Telegram Bot API** - Secure message delivery
- **GitHub Remote** - Centralized code repository

---

## 🎪 System Capabilities

### Intelligence Pipeline
```
Reconnaissance → Authentication → Synthesis → Formatting → [Human Approval] → Delivery
```

### Agent Personas

| Node | Model Type | Responsibility |
|------|-----------|----------------|
| **Triage Node** | High-Speed LLM | Filters irrelevant data, noise suppression |
| **Authentication Node** | Heavy-Lifter LLM | Cross-verifies with vector memory, prevents hallucinations |
| **Synthesis Node** | Heavy-Lifter LLM | Compresses verified intelligence, analytical reasoning |
| **Formatting Node** | High-Speed LLM | Structured Markdown generation, delivery-safe formatting |

### State Machine Features
- ✅ **Cyclic Execution** - Supports iterative refinement loops
- ✅ **Conditional Branching** - Verified/Not-Verified routing
- ✅ **Termination Guards** - Prevents infinite loops
- ✅ **Checkpoint Recovery** - Resume from any approved state

---

## 📦 Installation

### Prerequisites
- Windows 11 (PowerShell)
- Python 3.10 or higher
- Git for Windows
- Visual Studio Code (recommended)

### Step-by-Step Setup

#### 1. Clone the Repository
```powershell
cd C:\Projects
git clone https://github.com/nemestron/Nexus-Pulse.git
cd Nexus-Pulse\nexus
```

#### 2. Initialize uv Environment
```powershell
# Initialize project with uv (Astral)
uv init

# Create virtual environment
uv venv

# Activate environment
.\.venv\Scripts\activate
```

#### 3. Install Dependencies
```powershell
# Install all dependencies with uv (10x faster than pip)
uv add langgraph langchain-core streamlit chromadb tavily-python python-telegram-bot
uv add groq huggingface-hub python-dotenv
```

#### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```env
# API Keys
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_target_chat_id_here

# Database Configuration
CHROMA_DB_PATH=./local_db

# Application Settings
DEBUG=false
LOG_LEVEL=INFO
```

Create `.env.example` (for version control):
```env
TAVILY_API_KEY=
GROQ_API_KEY=
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
CHROMA_DB_PATH=./local_db
DEBUG=false
LOG_LEVEL=INFO
```

#### 5. Verify Installation
```powershell
# Test environment setup
uv run python src/test_env.py

# Expected output: "✓ All credentials loaded successfully"
```

---

## ⚙️ Configuration

### Database Setup
The system uses a local ChromaDB instance for vector storage:

```python
# Default configuration in src/memory/vector_store.py
CHROMA_DB_PATH = "nexus/local_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "nexus_intelligence"
```

### Agent Configuration
Customize LLM models in `src/agents/nodes.py`:

```python
# High-speed model (Triage, Formatting)
FAST_MODEL = "llama-3.1-8b-instant"

# Heavy-lifter model (Authentication, Synthesis)
POWER_MODEL = "mixtral-8x7b-32768"
```

### Graph Compilation
The LangGraph engine compiles with checkpointing:

```python
# src/graph_engine.py
graph = StateGraph(StateSchema)
graph.compile(checkpointer=SQLiteSaver())
```

---

## 🚀 Usage

### Local Development

#### 1. Run the Streamlit Dashboard
```powershell
uv run streamlit run app.py
```
Access at: `http://localhost:8501`

#### 2. Execute Test Scripts
```powershell
# Test memory system
uv run python src/test_memory.py

# Test agent nodes
uv run python src/test_agents.py

# Test full graph execution
uv run python src/test_graph.py
```

### Production Deployment

#### Deploy to Streamlit Cloud
1. Push code to GitHub repository
2. Navigate to [Streamlit Community Cloud](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Add environment secrets in Streamlit dashboard
5. Deploy!

**Live URL:** https://nexus-pulse.streamlit.app/

### Telegram Integration

1. Create a Telegram Bot via [@BotFather](https://t.me/botfather)
2. Obtain your bot token
3. Add bot to your target channel/group
4. Configure `TELEGRAM_CHAT_ID` in `.env`
5. Test delivery:
```powershell
uv run python src/delivery/test_transmission.py
```

---

## 📂 Project Structure

```
nexus/
├── .venv/                          # uv virtual environment (gitignored)
├── local_db/                       # ChromaDB vector storage (gitignored)
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── nodes.py                # Multi-agent persona definitions
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── vector_store.py         # ChromaDB configuration
│   │   └── embeddings.py           # HuggingFace embedding utilities
│   ├── reconnaissance/
│   │   ├── __init__.py
│   │   └── search.py               # Tavily API integration
│   ├── delivery/
│   │   ├── __init__.py
│   │   └── transmission.py         # Telegram Bot API
│   ├── state.py                    # Typed state schema
│   ├── graph_engine.py             # LangGraph orchestration
│   ├── test_env.py                 # Environment validation
│   ├── test_memory.py              # Memory system tests
│   ├── test_agents.py              # Agent node tests
│   └── test_graph.py               # Graph execution tests
├── .env                            # Secrets (gitignored)
├── .env.example                    # Environment template
├── .gitignore                      # Git ignore rules
├── app.py                          # Streamlit dashboard
├── pyproject.toml                  # uv/Python project metadata
├── uv.lock                         # Dependency lock file
├── nexus_ops.log                   # Operational logs (gitignored)
├── README.md                       # This file
└── architecture-diagram.png        # System architecture visualization
```

---

## 🔄 Development Phases

### Phase 1: Command Center (v0.1)
**Objective:** Secure workspace provisioning and environment initialization
- Windows PowerShell setup
- uv (Astral) virtual environment
- Git remote synchronization
- Security boundary establishment

**Tag:** `v0.1-command-center`

### Phase 2: Intel Acquisition (v0.2)
**Objective:** Autonomous reconnaissance and vector storage
- Tavily Search API integration
- ChromaDB local vector database
- HuggingFace embeddings
- Ingestion pipeline with chunking

**Tag:** `v0.2-intel-acquisition`

### Phase 3: Cognitive Nodes (v0.3)
**Objective:** Multi-agent LLM system with specialized personas
- Triage Node (filtering)
- Authentication Node (verification)
- Synthesis Node (compression)
- Formatting Node (delivery prep)

**Tag:** `v0.3-cognitive-nodes`

### Phase 4: State Routing (v0.4)
**Objective:** LangGraph state machine with conditional logic
- Graph compilation
- Conditional routing (verified/not-verified)
- Termination guards
- Cyclic execution support

**Tag:** `v0.4-state-routing`

### Phase 5: Manual Override (v0.5)
**Objective:** Human-in-the-loop checkpoint mechanisms
- SQLite checkpointer
- Execution suspension
- Resume protocol
- State persistence

**Tag:** `v0.5-manual-override`

### Phase 6: Dissemination (v0.6)
**Objective:** External delivery via Telegram
- Telegram Bot API integration
- Markdown-safe formatting
- Operational telemetry
- Logging infrastructure

**Tag:** `v0.6-dissemination`

### Phase 7: Deployment (v1.0)
**Objective:** Production deployment with Streamlit dashboard
- Command interface
- Real-time status visualization
- Cloud deployment
- End-to-end testing

**Tag:** `v1.0-nexus-live`

---

## 📚 API Reference

### Core Classes

#### `StateSchema` (src/state.py)
```python
class StateSchema(TypedDict):
    """Strictly typed state payload for graph traversal"""
    raw_text: str
    filtered_topics: List[str]
    verification_status: bool
    synthesized_brief: str
    formatted_output: str
    authorization_approved: bool
```

#### `SearchClient` (src/reconnaissance/search.py)
```python
class SearchClient:
    def __init__(self, api_key: str)
    def search(self, query: str, max_results: int = 5) -> List[str]
```

#### `VectorMemory` (src/memory/vector_store.py)
```python
class VectorMemory:
    def __init__(self, db_path: str)
    def store(self, documents: List[str], metadata: dict)
    def retrieve(self, query: str, k: int = 3) -> List[Document]
```

### Graph Nodes

| Node | Function | Input | Output |
|------|----------|-------|--------|
| `triage_node` | Filters irrelevant data | `raw_text` | `filtered_topics` |
| `auth_node` | Verifies against memory | `filtered_topics` | `verification_status` |
| `synthesis_node` | Compresses intelligence | `verified_data` | `synthesized_brief` |
| `format_node` | Structures for delivery | `synthesized_brief` | `formatted_output` |
| `transmit_node` | Sends to Telegram | `formatted_output` | HTTP response |

---

## 🔒 Security

### Best Practices Implemented

1. **Credential Isolation**
   - All secrets stored in `.env` (gitignored)
   - `.env.example` provided for collaboration
   - No hardcoded credentials

2. **Local-Only Execution**
   - Vector database stored locally (`./local_db`)
   - Sensitive intelligence never leaves infrastructure
   - No external data exfiltration

3. **Dependency Security**
   - `uv.lock` ensures reproducible builds
   - Regular dependency audits
   - Semantic versioning with Git tags

4. **Access Control**
   - Human-in-the-loop approval required
   - Authorization flags prevent unauthorized transmission
   - Audit-ready logging

### Security Checklist
- ✅ `.venv/` excluded from Git
- ✅ `.env` excluded from Git
- ✅ `local_db/` excluded from Git
- ✅ API keys validated at runtime
- ✅ HTTPS-only external communications
- ✅ Input sanitization on all user inputs

---

## ⚡ Performance

### uv (Astral) Speed Benefits
- **10-100x faster** dependency resolution vs. pip
- **Instant** virtual environment creation
- **Millisecond** dependency locking

### Groq LLM Inference
- **Sub-second** response times for high-speed models
- **Parallel** agent execution support
- **Optimized** token usage

### ChromaDB Vector Search
- **Sub-millisecond** semantic retrieval
- **Persistent** SQLite backend
- **Efficient** embedding storage

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/nemestron/Nexus-Pulse
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Your Changes**
   - Follow PEP 8 style guidelines
   - Add type hints to all functions
   - Write unit tests for new features
   - Update documentation

4. **Commit with Conventional Commits**
   ```bash
   git commit -m "feat: add amazing feature"
   # or
   git commit -m "fix: resolve bug in auth node"
   # or
   git commit -m "docs: update README installation section"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/amazing-feature
   ```

### Development Guidelines
- Use `uv` for all dependency management
- Maintain semantic versioning with Git tags
- Ensure all tests pass before submitting
- Update `pyproject.toml` for new dependencies

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Dhiraj Malwade

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

## 📬 Contact & Links

### Project Links
- **🌐 Live Demo:** [https://nexus-pulse.streamlit.app/](https://nexus-pulse.streamlit.app/)
- **📢 Telegram Channel:** [https://t.me/NexusPulseNews](https://t.me/NexusPulseNews)
- **💼 LinkedIn:** [Dhiraj Malwade](https://www.linkedin.com/in/dhiraj-malwade-6a8385399/)
- ** GitHub Repository:** [Nexus-Pulse](https://github.com/nemestron/Nexus-Pulse)

### Support & Questions
For questions, feature requests, or bug reports:
- Open an issue on GitHub
- Join our [Telegram Channel](https://t.me/NexusPulseNews) for updates
- Connect on [LinkedIn](https://www.linkedin.com/in/dhiraj-malwade-6a8385399/) for professional inquiries

---

## 🙏 Acknowledgments

### Technologies & Frameworks
- **[uv (Astral)](https://github.com/astral-sh/uv)** - Blazing-fast Python package manager
- **[LangGraph](https://github.com/langchain-ai/langgraph)** - Cyclic graph orchestration
- **[LangChain](https://github.com/langchain-ai/langchain)** - LLM application framework
- **[Groq](https://groq.com/)** - High-speed LLM inference
- **[ChromaDB](https://www.trychroma.com/)** - Vector database
- **[Streamlit](https://streamlit.io/)** - Data app framework
- **[Tavily](https://tavily.com/)** - AI-optimized search API
- **[HuggingFace](https://huggingface.co/)** - Transformers and embeddings

### Inspiration
This project represents the convergence of autonomous AI agents, stateful orchestration, and human-governed decision-making. Built for the next generation of intelligent automation systems.

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

---

**NEXUS PULSE** • Autonomous Multi-Agent Intelligence & Decision Engine

*Stateful • Verifiable • Human-Governed • Production Ready*

[![Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Streamlit-red?style=for-the-badge&logo=streamlit)](https://nexus-pulse.streamlit.app/)
[![Telegram](https://img.shields.io/badge/📢_Telegram-Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/NexusPulseNews)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/dhiraj-malwade-6a8385399/)

---

Built with ❤️ by **Dhiraj Malwade** • 2026

</div>
